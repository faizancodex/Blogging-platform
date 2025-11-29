# 📝 Wefyx — Blogging Platform

Wefyx is a full-featured blogging platform built using **Django**, designed for seamless content discovery and interaction.  
Users can read and explore blogs, follow creators, manage profiles, filter posts by category, and create their own blogs.

---

## 🚀 Features

### 👥 User Management
- User login and signup
- Forgot password / password reset
- Profile creation and updates (name, bio, profile picture)
- View other bloggers' profiles
- Follow / unfollow bloggers

### 📰 Blog Features
- Create, edit, and delete blog posts
- Categorize posts (Technology, Travel, Adventure, Lifestyle, etc.)
- Explore Recent Posts and trending blogs
- Filter blogs by category
- Search blogs by title or keywords
- View a blogger’s complete post history

### ❤️ Social Features
- Follow / unfollow creator profiles
- Personalized feed based on users you follow
- See follower and following count

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django, Django ORM |
| Frontend | HTML, CSS, JavaScript|
| Database | SQLite|
| Authentication | Django Auth System |
| Additional | Django Messages Framework, Slug URLs |

---

## 🔧 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/faizancodex/wefyx.git
cd wefyx
```

2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the server
```bash
python manage.py runserver
```

---

## 📸 Screenshots

### 🏠 Home Page  
![Home Page](screenshots/homepage.png)

---

### 🔍 Filter Blogs  
![Filter](screenshots/filter.png)

---

### 📖 Read Post  
![Read Post](screenshots/readpost.png)

---

### 👤 Creator Profile  
![Creator Profile](screenshots/createrself.png)

---

### ⚙️ Edit Profile  
![Edit Profile](screenshots/editprofile.png)

---

### ✍️ Upload Post  
![Upload Post](screenshots/uploadpost.png)

---

### 🚀 Explore Latest & Trending Posts  
![Explore](screenshots/explore.png)

---

### 📚 Bookstore  
![Bookstore](screenshots/bookstore.png)

---

### 📘 Guides  
![Guides](screenshots/guides.png)

---

### 🆕 Signup Page  
![Signup](screenshots/signin.png)

---

### 🔐 Login Page  
![Login Page](screenshots/loginpage.png)

---

### ❓ Forgot Password  
![Forgot Password](screenshots/forgotpassword.png)

---

### 🔁 Reset Password  
![Reset Password](screenshots/resetpassword.png)

---
