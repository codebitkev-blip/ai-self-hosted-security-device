# 🔐 AI Self-Hosted Security Device (AISSD)

A **self-hosted, offline-capable AI security device** that monitors local network traffic, detects anomalous behavior using machine learning, and exposes a **clean, local-only API** for visibility — without sending any data to the cloud.

This project focuses on **practical security engineering**, not buzzwords.

---

## 🎯 Project Goals

- Monitor local network traffic in real time
- Detect anomalous behavior using lightweight AI
- Store alerts locally (no external services)
- Expose security insights via a clean API
- Demonstrate secure, self-hosted system design

---

## 🧠 What This Device Does

1. Captures live network packets  
2. Extracts simple but meaningful features  
3. Uses an **Isolation Forest** model for anomaly detection  
4. Logs suspicious events locally  
5. Exposes alerts and statistics through a local API  

This functions like a **mini SIEM + AI anomaly detector** for lab or personal environments.

---

## 🏗️ High-Level Architecture

Network Interface
↓
Packet Sniffer (Scapy)
↓
Feature Extraction
↓
AI Anomaly Detection
↓
Local SQLite Storage
↓
Local FastAPI Dashboard


✔ Fully self-hosted  
✔ No cloud dependency  
✔ No telemetry  
✔ Offline-capable  

---

## 📁 Repository Structure

ai-self-hosted-security-device/

├── core/ # Packet capture & detection logic

├── api/ # FastAPI dashboard

├── storage/ # SQLite database & ML model

├── scripts/ # Training and helper scripts

├── security/ # Threat model & hardening notes

├── requirements.txt

├── docker-compose.yml

---

## 🧪 Technologies Used

- **Python 3**
- **Scapy** – packet capture
- **scikit-learn** – anomaly detection (Isolation Forest)
- **FastAPI** – local API dashboard
- **SQLite** – lightweight local storage
- **Uvicorn** – ASGI server

---

## 🚀 Getting Started

1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-self-hosted-security-device.git
cd ai-self-hosted-security-device

2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

4️⃣ Train the AI Model
python -m scripts.train_model

Model trained successfully

5️⃣ Start Packet Monitoring

Requires elevated privileges for packet capture.

sudo venv/bin/python -m core.packet_sniffer

└── README.md

6️⃣ Start the API Dashboard

In a new terminal (with venv active):

uvicorn api.main:app --host 127.0.0.1 --port 8000

🌐 API Usage

Open interactive API documentation:

http://127.0.0.1:8000/docs
