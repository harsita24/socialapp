from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.contrib.auth.views import LogoutView
from .views import (
    CustomPasswordChangeView,
    CustomLoginView,
)
from .views import SignUpView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # ✅ Use your custom view
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # add next_page
    path('signup/', SignUpView.as_view(), name='signup'),  # ✅ add this
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
