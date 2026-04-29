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

### Option A: Standard Run (Development)
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server using SQLite:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Option B: Dockerized Setup with MySQL (Production-grade)
Our project is container-ready. We use **Docker Compose** to orchestrate the FastAPI backend and a MySQL database container, ensuring isolated and consistent environments.

1. Ensure Docker and Docker Compose are installed on your machine.
2. Build and start the containers in the background:
   ```bash
   docker-compose up -d --build
   ```
3. The API will be accessible at `http://localhost:8000`, connected seamlessly to the dedicated MySQL container.
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
