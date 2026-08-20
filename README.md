<p align="center">
  <img src="assets/hero.svg" alt="🧪 Laboratory Research Blog & Portal Hero Banner" width="100%" />
</p>

<h1 align="center">🧪 Laboratory Research Blog & Portal</h1>

<p align="center">
  <strong>Full-Stack Scientific Laboratory Knowledge Portal & Research Blog Built with Flask & SQLAlchemy.</strong>
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-code-architecture">Code Architecture</a> •
  <a href="#-system-flow">System Flow</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" /> <img src="https://img.shields.io/badge/SQLAlchemy-2.0+-d71f00?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLAlchemy" /> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" />
</p>

---

## 📌 Overview

A full-featured Flask web application serving as an academic laboratory portal and scientific research blog. Provides secure user authentication, role-based member management, rich article publishing with image uploads, author-specific profile pages, and administrative dashboard management.

---

## ✨ Features (Key Outcomes & Capabilities)

| Icon | Feature | Outcome & Real Proof |
| :---: | :--- | :--- |
| 📝 | **Research Article Publishing** | Create, edit, and delete research posts with image attachments |
| 🔐 | **Secure User Authentication** | Password hashing via Werkzeug with session protection |
| 👥 | **Member & Author Portals** | Author-specific article listings (`/user/<username>`) and member profiles |
| 📊 | **Lab Management Dashboard** | Centralized administrative overview for all laboratory posts |

---

## 🔬 Code Architecture & Implementation

### 🔬 Code Implementation (`app.py`)
- **Database Models (`SQLAlchemy`)**:
  - `User`: `id`, `username`, `password_hash` (Werkzeug secure hashing), `role` (Admin/Member).
  - `Post`: `id`, `title`, `content`, `image_filename`, `created_at`, `user_id` (foreign key).
- **Authentication & Security**: Session management with `os.urandom(24)` secret key, password hashing via `generate_password_hash` / `check_password_hash`, and secure filename sanitization (`secure_filename`).
- **File Upload Engine**: Image uploads restricted to `ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}` and served via `static/uploads/`.
- **Templates**: Jinja2 inheritance with `base.html`, `dashboard.html`, `post.html`, and `user_posts.html`.

---

## 📊 System Flow

```mermaid
graph TD
  Visitor([👤 Visitor / Member]) --> Routes[🚪 Flask App Router]
  Routes --> Auth[🔐 Auth: Login / Register / Sessions]
  Routes --> Posts[📝 Post Management: CRUD & Uploads]
  Routes --> UserPage[👥 Author Profiles: /user/username]
  Auth & Posts --> DB[(🗄️ SQLite blog.db via SQLAlchemy)]
  Posts --> Storage[(📁 static/uploads/ Images)]

  classDef primary fill:#06b6d4,stroke:#0891b2,stroke-width:2px,color:#fff;
  classDef accent fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff;
  class Routes,Auth primary;
  class DB,Storage accent;
```

---

## 📁 Project Structure

```bash
laboratory-blog-flask/
├── 📁 assets/                 # High-resolution SVG banners
│   └── 🎨 hero.svg
├── 📁 templates/              # Jinja2 templates (base, dashboard, post, user_posts)
├── 📁 static/                 # CSS stylesheets, JS scripts & uploads
├── 📄 app.py                  # Flask routes, SQLAlchemy models & auth logic
├── 📄 reset_database.py       # Database initialization & reset utility
├── 📄 requirements.txt        # Flask, Flask-SQLAlchemy, Werkzeug
└── 📄 README.md               # Documentation
```

---

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/LoNebula/Laboratory-blog-flask.git
cd Laboratory-blog-flask

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize database
python reset_database.py

# 4. Launch application (http://127.0.0.1:5000)
python app.py
```

---

<p align="center">
  Released under the <a href="LICENSE">MIT License</a>. Crafted with precision by <a href="https://github.com/LoNebula">LoNebula</a>
</p>
