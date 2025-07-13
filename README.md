# 🧪 Inventory Simulation API

A cloud-ready Python FastAPI application that simulates a warehouse inventory system with customer ordering and probabilistic restocking behavior.

> **Live Demo**: [http://34.239.108.187/stock](http://34.239.108.187/stock)  
> **Infra**: Deployed to AWS EC2 with Docker + modular Terraform (infra repo available on request)

---

## 📦 Features

- 🔁 **Inventory Tracking** for multiple items
- 📥 **Order Simulation** with stock validation
- 🔄 **Probabilistic Refill** engine to simulate supplier delays
- 🌐 RESTful API via FastAPI
- 🐳 Dockerized and deployed on AWS EC2
- 🧱 Infrastructure as Code using modular Terraform
- 🔐 Secure IAM-based EC2 access with SSM (no SSH)

---

## 🚀 API Endpoints

| Method | Endpoint  | Description                     |
| ------ | --------- | ------------------------------- |
| GET    | `/stock`  | View current stock levels       |
| POST   | `/order`  | Place a customer order          |
| POST   | `/refill` | Attempt a random refill attempt |

Example request:

```json
POST /order
{
  "item": "item-A",
  "quantity": 3
}
```

---

## 🧠 Simulation Logic

- Each item starts with a stock level
- Customer orders reduce stock if available
- Refill simulates supplier variability:
  - 50% chance to refill each item
  - Refill quantity: random between 10–30 units

---

## 🛠️ Local Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Or run with Docker:

```bash
docker build -t inventory-sim-api .
docker run -d -p 8000:80 inventory-sim-api
```

Visit: http://localhost:8000/stock

---

## ☁️ Infrastructure Deployment (Terraform + EC2)

The app is deployed using:

- AWS EC2 (Amazon Linux 2)
- Docker for containerization
- Terraform for infrastructure-as-code
- IAM roles + SSM for secure access (no SSH keys)
- GitHub-based bootstrapping

Full deployment is managed from a separate private repo (fastapi-ec2-tf).

---

## 📁 Project Structure

```
inventory-sim-api/
├── main.py            # FastAPI app
├── Dockerfile         # Container definition
├── requirements.txt   # Python dependencies
└── README.md          # Project overview
```

---

## 🧱 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)
- [Terraform](https://www.terraform.io/)
- [AWS EC2 + IAM + SSM](https://aws.amazon.com/ec2/)

---

## 🧑‍💻 Author

Smart T

---

## 📌 Status

🟢 Live and running
🛠️ Actively expanding to include logging, analytics, and multi-service architecture

---
