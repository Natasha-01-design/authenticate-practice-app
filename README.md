# Flask Authentication App

A simple **Flask authentication system** with **user registration, login, logout, and protected dashboard** functionality.
It uses **Flask**, **Flask-SQLAlchemy**, and **Werkzeug security** to handle user accounts securely with hashed passwords.

---

##  Features

* Register a new account with a unique username.
* Secure password storage using hashing (no plain text passwords).
* Login with existing credentials.
* Session-based authentication (users stay logged in until they log out).
* Logout functionality.
* Basic error handling (invalid login, duplicate username, etc.).
* Custom error pages (404, 500).

---

## Technologies Used

* [Flask](https://flask.palletsprojects.com/) – Web framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) – Database ORM
* [Werkzeug](https://werkzeug.palletsprojects.com/) – Password hashing & verification
* [SQLite](https://www.sqlite.org/) – Lightweight database
* \[HTML, Jinja2 Templates, Sass/CSS] – Frontend styling

---

##  Project Structure

```
flask-auth-app/
│
├── app.py                # Main Flask application
├── users.db              # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
│
├── static/
│   └── styles.css        # Compiled CSS (from styles.scss if using Sass)
│
├── templates/
│   ├── base.html         # Base layout
│   ├── index.html        # Home (login/register form)
│   ├── dashboard.html    # User dashboard (protected)
│   ├── 404.html          # Custom "Not Found" page
│   └── 500.html          # Custom "Server Error" page
│
└── README.md             # Project documentation
```

---

## ⚙ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask-auth-app.git
   cd flask-auth-app
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:

   ```
   Flask
   Flask-SQLAlchemy
   Werkzeug
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. **Visit in your browser**

   ```
   http://127.0.0.1:5000/
   ```

---

##  Usage

1. Open the home page (`/`).
2. Register a new account using the **Register** button.
3. Log in with your username and password.
4. After login, you’ll be redirected to your **Dashboard**.
5. Use the **Logout** link to end your session.

---

##  Security Notes

* Passwords are **hashed** using Werkzeug before storage.
* Sessions are protected with a secret key (`app.secret_key`).
* Never store plain text passwords in the database.
* For production:

  * Replace `your_secret_key` with a strong random key.
  * Use a proper database (PostgreSQL, MySQL) instead of SQLite.
  * Disable `debug=True`.

---

##  Next Steps / Improvements

* Add email verification.
* Add password reset functionality.
* Improve error messages and validation (e.g., password length).
* Style with Bootstrap or Tailwind for better UI.

---

##  Author

Developed by **Natasha Karwitha**
Built as part of a Flask learning project.
