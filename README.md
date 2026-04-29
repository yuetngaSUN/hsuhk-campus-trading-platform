# 🎓 HSUHK Campus Trading Platform

![Status](https://img.shields.io/badge/Status-Beta-brightgreen)
![Course](https://img.shields.io/badge/Course-COM6102%20Distributed%20Systems-blue)
![Tech Stack](https://img.shields.io/badge/Tech_Stack-FastAPI%20%7C%20SQLite%20%7C%20AWS-orange)

Welcome to the **HSUHK Campus Trading Platform**! This is the backend repository for a modern, eco-friendly, and cloud-native e-commerce platform designed exclusively for students at The Hang Seng University of Hong Kong (HSUHK). 

The platform aims to facilitate a secure, sustainable, and convenient P2P marketplace for students to buy, sell, and exchange second-hand items (e.g., textbooks, electronics, furniture) within the campus community.

---

## 🌟 Key Features
- **Item Management:** Users can post items for sale with detailed descriptions, prices, and image URLs.
- **Dynamic Marketplace Display:** Real-time retrieval of all listed second-hand goods on the platform.
- **RESTful API Architecture:** Seamless communication between the Frontend UI and Backend server.
- **Eco-Friendly Community:** Promotes the reuse of products, saving money for students while reducing the campus's carbon footprint.

---

## 🛠️ Technology Stack & Cloud Architecture
This project is built based on modern cloud computing and distributed system principles (COM6102):

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12) - Chosen for its high performance and asynchronous capabilities.
- **Database:** **SQLite** (Currently used for rapid prototyping and live demo) / **MySQL** (Ready for Docker containerization).
- **Cloud Hosting:** Deployed and running on an **AWS EC2** instance (Ubuntu Server).
- **Frontend Hosting:** Hosted via **AWS S3** static website hosting (CORS enabled).
- **Containerization (Optional):** Pre-configured `Dockerfile` and `docker-compose.yml` for isolated environment deployment.

---

## 🚀 How to Run Locally

If you want to run this backend API on your local machine, please follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/yuetngaSUN/hsuhk-campus-trading-platform.git
cd hsuhk-campus-trading-platform
```

### 2. Install dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The server will start at `http://127.0.0.1:8000`. You can test the APIs interactively by visiting the auto-generated Swagger UI at `http://127.0.0.1:8000/docs`.

---

## ☁️ Deployment on AWS (Production)
For the final presentation demo, this backend is successfully hosted live on an AWS EC2 instance. The server is kept running continuously in the background.

```bash
# How we deployed it on the EC2 server:
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
```

---

## 👥 Course Information
- **Course:** COM6102 Distributed Systems and Cloud Computing
- **Institution:** The Hang Seng University of Hong Kong (HSUHK)
- **Status:** Final Project Presentation Version (Completed)
