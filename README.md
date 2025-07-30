# 🎓 Student Feedback System (Django)

The **Student Feedback System** is a Django-based web application that allows students to submit feedback with details such as name, email, course, rating, and message. Submitted feedback is stored securely in the database, and users are shown a thank-you confirmation page. This project is ideal for learning Django fundamentals, including models, views, templates, and form handling.

---

## 📂 Project Details
- **Project Name:** `student_feedback`  
- **App Name:** `feedback`  
- **Framework:** Django (Python)  
- **Database:** SQLite (Default)  

---

## 🚀 Features
- Collects student details: **Name, Email, Course, Rating, Feedback Message**
- Auto-generated **timestamp** for each feedback submission
- Displays a **thank-you confirmation page** after form submission  
- Uses Django’s MVT (Model-View-Template) architecture  
- Beginner-friendly and lightweight  

---

Create Virtual Environment & Install Dependencies:
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On Mac/Linux

pip install django

Run Migrations:
python manage.py makemigrations
python manage.py migrate

Start the Development Server:
python manage.py runserver

📂 Project Structure:
student_feedback/
│
├── feedback/
│   ├── migrations/
│   ├── templates/
│   │   ├── feedback_form.html
│   │   └── thank_you.html
│   ├── models.py
│   ├── views.py
│
├── student_feedback/
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md


🔑 Admin Access:
python manage.py createsuperuser

📝 Description:
This project demonstrates Django’s core features such as model creation, form handling using POST requests, URL routing, template rendering, and database operations. It is designed as a beginner-friendly application that can be easily extended with features like feedback listing, filtering, or email notifications.


