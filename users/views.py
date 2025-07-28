from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm, SignUpForm
from .models import PasswordHistory
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password_change.html' 
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        user = self.request.user
        PasswordHistory.objects.create(user=user, hashed_password=user.password)
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Provide both login and signup forms to the template
        return render(request, self.template_name, {
            'login_form': self.get_form(),
            'signup_form': SignUpForm()
        })

    def post(self, request, *args, **kwargs):
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            login_form = self.get_form()
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('post_list')
            else:
                return render(request, self.template_name, {
                    'login_form': login_form,
                    'signup_form': signup_form
                })
        else:
            # Handle login
            self.form_class = self.get_form_class()
            login_form = self.get_form()
            signup_form = SignUpForm()
            if login_form.is_valid():
                return self.form_valid(login_form)
            else:
                return render(request, self.template_name, {
                    'login_form': login_form,
                    'signup_form': signup_form
                })

    def get_success_url(self):
        return reverse_lazy('post_list')
    
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')