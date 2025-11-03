<h1 align="center">
  Bloome &nbsp;·&nbsp; Production-Ready Django Social Network
</h1>

<p align="center">
  <strong>🚀 Full-Stack Social Media Platform | Real-time Chat | Smart News Feed | Open Source</strong>
</p>

<p align="center">
  <a href="https://img.shields.io/badge/version-2.0.0-red">
    <img src="https://img.shields.io/badge/version-2.0.0-red" alt="version" />
  </a>
  <a href="https://img.shields.io/badge/Django-4.2+-green?logo=django">
    <img src="https://img.shields.io/badge/Django-4.2+-green?logo=django" alt="django badge" />
  </a>
  <a href="https://img.shields.io/badge/Python-3.8+-blue?logo=python">
    <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="python badge" />
  </a>
  <a href="https://img.shields.io/badge/Bootstrap-5.0+-purple?logo=bootstrap">
    <img src="https://img.shields.io/badge/Bootstrap-5.0+-purple?logo=bootstrap" alt="bootstrap badge" />
  </a>
  <a href="https://img.shields.io/badge/HTMX-1.8+-orange?logo=htmx">
    <img src="https://img.shields.io/badge/HTMX-1.8+-orange?logo=htmx" alt="htmx badge" />
  </a>
  <a href="https://img.shields.io/badge/hosted%20on-render-purple?logo=render">
    <img src="https://img.shields.io/badge/hosted%20on-render-purple?logo=render" alt="render badge" />
  </a>
  <a href="https://img.shields.io/badge/websockets-enabled-brightgreen?logo=fastapi">
    <img src="https://img.shields.io/badge/websockets-enabled-brightgreen?logo=fastapi" alt="ws badge" />
  </a>
  <a href="https://img.shields.io/badge/License-MIT-yellow.svg">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license badge" />
  </a>
</p>

---

## ✨ Feature tour

- **News-feed** with likes, comments, and friend requests  
- **Real-time chat** (WebSockets) with online presence  
- **Async tasks** (Celery) powering welcome-email flow  
- **Object storage** on Backblaze B2 (S3-compatible)  
- **Zero-downtime deploys** on Render using Gunicorn + UvicornWorker  
- **Responsive UI** built with Bootstrap 5 & HTMX  
- **Modular settings** (`development.py`, `production.py`, `local.py`) ready for 12-factor apps  

---

## 🛠️ Tech Stack

<div align="center">

| **Layer** | **Technologies** | **Purpose** |
|-----------|------------------|-------------|
| **🎨 Frontend** | Bootstrap 5, HTMX, JavaScript, CSS3 | Responsive UI, Real-time interactions |
| **⚙️ Backend** | Django 4.2+, Django Channels, Python 3.8+ | Web framework, WebSocket support |
| **🔄 Real-time** | Daphne ASGI, Redis, WebSockets | Async processing, Chat, Notifications |
| **💾 Database** | SQLite (dev), MySQL/PostgreSQL (prod) | Data persistence, Relationships |
| **☁️ Storage** | Backblaze B2 (S3-compatible) | Media files, Static assets |
| **🚀 Deployment** | Render, Gunicorn, UvicornWorker | Production hosting, Load balancing |
| **📧 Tasks** | Celery, Redis Broker | Background jobs, Email sending |

</div>

---

## 📋 Quick Start(Local Setup)

Note: You can add both MySQL or SQLite database. The configuration is added in the settings.py so you just have to uncomment the code and set database host, user, password and port. 

Warning: If you face any database related error then you have to add the information by using python-dot-env or directly in the code of MySQL setup.

Clone the repository & Navigate to the project directory:

```bash
  git clone https://github.com/emhash/Bloome

  cd Bloome
```

Create a virtual envoirnment:

```bash 
python -m venv myenv
```
Active virtual envoirnment with Bash terminal:
```bash 
source myenv/Scripts/activate
```
(You can activate the virtual envoirnment using any terminal. Based on the terminal the activation process of virtual envoirnment might be different)

Now install the necessary module & start the server:
```bash 
pip install -r requirements.txt
python manage.py runserver

```
**In case of migration problem migrate and then run the server**
```bash 
python manage.py makemigrations
python manage.py migrate

```




---

| Pillar | What’s new | Why it matters |
|--------|------------|----------------|
| **Architecture & DX** | Re-organised project into a layered folder structure. Added `.gitignore`, sample `.env`, and commented S3 settings. | Accelerates onboarding and prevents secrets leakage. |
| **Real-time features** | One-to-one chat via **Django Channels** + **Daphne** (ASGI). | Demonstrates WebSocket and async proficiency. |
| **Cloud storage** | Integrated Backblaze **B2 S3** bucket for media uploads. | Shows cost-efficient object-storage skills. |
| **Modern hosting** | Migrated PythonAnywhere → **Render** native-ASGI. | Hands-on container/cloud deployment experience. |
| **Email & tasks** | Automated welcome email + full **Celery + Redis** setup ready for future jobs. | Production-ready background-job architecture. |
| **Security** | Fixed CSRF issues; secrets/hosts now env-driven. | Secure-by-default mindset. |
