SocialApp

SocialApp is a lightweight social networking platform built using Django.
It enables users to sign in, create public or private posts, and manage passwords securely.


Features
  ● User Authentication
  ● Signup,Login and Logout  
  ● Secure password change with validation  
  ● Post Management
  ● Create, view, and manage posts  
  ● Posts can be marked as Public (visible to all) or Private (visible only to the author)  
  ● Access Control
  ● Only authenticated users can access the post feed  
  ● Private posts are restricted to the original user  
  
  
Tech Stack

● Python 3.13  
● Django 5.2.4  
● SQLite (default Django database)  
● HTML & CSS (Django templates)  


Installation
Clone the repository:

git clone https://github.com/harsita24/socialapp.git
cd socialapp

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser (for admin access):
python manage.py createsuperuser

Run the development server:
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Result


<img width="1900" height="1004" alt="Screenshot 2025-07-28 130659" src="https://github.com/user-attachments/assets/3d8a04bc-07f7-4290-b825-7a9c778c9121" />
<img width="1903" height="996" alt="Screenshot 2025-07-28 130717" src="https://github.com/user-attachments/assets/154eca29-37d8-4921-a992-92b5115c4f45" />
<img width="1909" height="994" alt="Screenshot 2025-07-28 130818" src="https://github.com/user-attachments/assets/64cad17c-2a4a-4c80-883d-9730f76e383e" />
<img width="1912" height="993" alt="Screenshot 2025-07-28 130833" src="https://github.com/user-attachments/assets/fa6cc376-f458-4a39-9242-3aaf86ff3801" />
<img width="1887" height="1002" alt="Screenshot 2025-07-28 130853" src="https://github.com/user-attachments/assets/a7572af7-8a3d-40f0-aeb8-d5ec86c5a5a3" />
