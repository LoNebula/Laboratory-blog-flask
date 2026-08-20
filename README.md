<p align="center">
  <img src="assets/hero.svg" alt="🧪 Laboratory Research Blog & Knowledge Portal Hero Banner" width="100%" />
</p>

<h1 align="center">🧪 Laboratory Research Blog & Knowledge Portal</h1>

<p align="center">
  <strong>Full-featured scientific laboratory portal, research blog, and member management system built with Flask and SQLAlchemy.</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" /> <img src="https://img.shields.io/badge/SQLAlchemy-2.0+-d71f00?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLAlchemy" /> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" />
</p>

---

## ✨ Features (Key Outcomes & Capabilities)

| Icon | Feature | Outcome & Real Proof |
| :---: | :--- | :--- |
| 📝 | **Research Article Publishing** | Rich Markdown scientific publishing with code syntax highlighting and math support |
| 👥 | **Lab Member Directory** | Manage professor, researcher, and student profiles, alumni histories, and publications |
| 🔒 | **Role-Based Authentication** | Secure session authentication, password hashing, and administrative dashboard |
| 🗄️ | **Lightweight SQLite / SQLAlchemy** | Zero-setup relational database architecture with automated migration scripts |

---

## 📊 Architecture & Flow

```mermaid
graph TD
  User([👤 Member / Visitor]) --> Router[🚪 Flask Application Router]
  Router --> Auth[🔐 Authentication & Session Manager]
  Router --> Blog[📝 Research Post Engine]
  Router --> Members[👥 Member Directory Service]
  Auth & Blog & Members --> DB[(🗄️ SQLite / SQLAlchemy Database)]
  
  classDef primary fill:#06b6d4,stroke:#0891b2,stroke-width:2px,color:#fff;
  classDef accent fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff;
  class Router,Auth primary;
  class Blog,Members,DB accent;
```

---

## 📁 Project Structure

```bash
laboratory-blog-flask/
├── 📁 templates/              # Jinja2 HTML templates
├── 📁 static/                 # CSS stylesheets & scripts
├── 📄 app.py                  # Flask application entry point
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md               # Documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Check language runtimes (Python / Node.js) and system dependencies.

```bash
# 1. Clone repository
git clone https://github.com/LoNebula/Laboratory-blog-flask.git
cd Laboratory-blog-flask

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch application
python app.py
```

---

## 💡 Usage Notes & Tips

> [!TIP]
> Ensure all required environment variables and dependencies are properly configured before execution.

---

<p align="center">
  Released under the <a href="LICENSE">MIT License</a>. Made with ❤️ by <a href="https://github.com/LoNebula">LoNebula</a>
</p>
