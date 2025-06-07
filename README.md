<h4 align='center'>
  
![Logo](https://github.com/user-attachments/assets/8e784d01-0977-410a-ae11-7ebc30a08061)

</h4>


<h1 align="center">
  Bloome &nbsp;·&nbsp; Full-Stack Social Network
</h1>

<p align="center">
  <a href="https://img.shields.io/badge/version-2.0.0-red">
    <img src="https://img.shields.io/badge/version-2.0.0-red" alt="version" />
  </a>
  <a href="https://img.shields.io/badge/bloome-fullstack_social_network-blue">
    <img src="https://img.shields.io/badge/bloome-fullstack_social_network-blue" alt="title badge" />
  </a>
  <a href="https://img.shields.io/badge/python-django-green">
    <img src="https://img.shields.io/badge/python-django-green" alt="django badge" />
  </a>
  <a href="https://img.shields.io/badge/hosted%20on-render-purple?logo=render">
    <img src="https://img.shields.io/badge/hosted%20on-render-purple?logo=render" alt="render badge" />
  </a>
  <a href="https://img.shields.io/badge/websockets-enabled-brightgreen?logo=fastapi">
    <img src="https://img.shields.io/badge/websockets-enabled-brightgreen?logo=fastapi" alt="ws badge" />
  </a>
  <a href="https://img.shields.io/badge/free%20plan-auto--sleep-yellow">
    <img src="https://img.shields.io/badge/free%20plan-auto--sleep-yellow" alt="sleep badge" />
  </a>
</p>

---

> **Bloome** is a production-grade Django social-media platform featuring a news-feed, real-time one-to-one chat, friend requests, likes, comments, and media uploads.

<details>
<summary><strong>Table of contents</strong></summary>

- [Live demo](#live-demo)
- [June 2025 New Update](#-june-2025-new-update)
- [Feature tour](#feature-tour)
- [Tech stack](#tech-stack)
- [Screenshots](#screenshots)
- [Quick Start(Local Setup)](#quick-startlocal-setup)
</details>

---

## Live demo

🌐 **URL:** <https://bloome.onrender.com>  
🪄 **Demo account:** `demo@gmail.com` **Password:** `demo1234`  

⚠️ *Free tier sleeps after 15 min idle; first hit may take ~30 s to spin up.*

---

## 🚀 June 2025 New Update

| Pillar | What’s new | Why it matters |
|--------|------------|----------------|
| **Architecture & DX** | Re-organised project into a layered folder structure. Added `.gitignore`, sample `.env`, and commented S3 settings. | Accelerates onboarding and prevents secrets leakage. |
| **Real-time features** | One-to-one chat via **Django Channels** + **Daphne** (ASGI). | Demonstrates WebSocket and async proficiency. |
| **Cloud storage** | Integrated Backblaze **B2 S3** bucket for media uploads. | Shows cost-efficient object-storage skills. |
| **Modern hosting** | Migrated PythonAnywhere → **Render** native-ASGI. | Hands-on container/cloud deployment experience. |
| **Email & tasks** | Automated welcome email + full **Celery + Redis** setup ready for future jobs. | Production-ready background-job architecture. |
| **Security** | Fixed CSRF issues; secrets/hosts now env-driven. | Secure-by-default mindset. |

---

## Feature tour

- **News-feed** with likes, comments, and friend requests  
- **Real-time chat** (WebSockets) with online presence  
- **Async tasks** (Celery) powering welcome-email flow  
- **Object storage** on Backblaze B2 (S3-compatible)  
- **Zero-downtime deploys** on Render using Gunicorn + UvicornWorker  
- **Responsive UI** built with Bootstrap 5 & HTMX  
- **Modular settings** (`development.py`, `production.py`, `local.py`) ready for 12-factor apps  

---

## Tech stack

| Layer        | Tools & Libraries                          |
|--------------|--------------------------------------------|
| **Frontend** | HTML / Bootstrap 5 · HTMX · CSS            |
| **Backend**  | Django >= 4.x · Django Channels · Celery   |
| **Async/WS** | Daphne · Redis broker                      |
| **Database** | SQLite (dev) · MySQL (prod-ready)          |
| **Storage**  | Backblaze B2 S3 bucket                     |
| **CI/CD**    | GitHub Actions · Render deployment         |

---

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/680567a2-9bf2-4f3b-93a3-3b68ff28293e" width="420" alt="newsfeed">
  <img src="https://github.com/user-attachments/assets/e98c0639-400c-4f8b-ac9c-d63a18c712fb" width="320" alt="chat list"><br><br>
  <img src="https://github.com/user-attachments/assets/cf7435d6-3848-481e-b390-b1680fc608a3" width="420" alt="profile">
  <img src="https://github.com/user-attachments/assets/3f79e369-b11e-40ac-bbd9-6820a803eff7" width="420" alt="admin dashboard">
</p>

---

## Quick Start(Local Setup)

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

## Author

- [@emhash](https://www.github.com/emhash)


![App Screenshot]()

