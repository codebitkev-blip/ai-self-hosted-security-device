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

