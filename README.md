# AI Text Classifier With Pytorch

A lightweight FastAPI backend that demonstrates how AI models (e.g. PyTorch, or external inference services) can be cleanly integrated into a modern API service.

This project focuses on **API design, validation, and model abstraction**, rather than model training, making it suitable for production-oriented backend systems.

---

## 🚀 Features

- FastAPI-powered REST API
- Automatic request validation using Pydantic
- Clean separation between API and model inference logic
- Abstracted AI inference layer (easily swappable with PyTorch models)
- Auto-generated Swagger documentation
- Lightweight and environment-agnostic

---

## 🧠 Architecture Overview

The system follows a clean separation of concerns:

Client
↓
FastAPI (Routing & Validation)
↓
Model Abstraction Layer
↓
Inference Response


The model layer is intentionally abstracted to allow:
- Easy replacement with PyTorch models
- External AI services (e.g. hosted inference APIs)
- Simplified testing and faster startup times

---

## 🗂 Project Structure

ai-text-classifier-with-pytorch/
│
├── app/
│ ├── myapp.py # API routes
│ ├── schemas.py # Request & response models
│ └── model.py # AI inference abstraction
│
|__ models/
|   |__ model.h5
|
├── requirements.txt
└── README.md


---

## 🛠 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

> The model layer is designed to support PyTorch or other AI engines without changing the API layer.

---

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/zinando/ai-text-classifier-with-pytorch.git
cd ai-text-classifier-with-pytorch

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
uvicorn app.myapp:app --host 0.0.0.0 --port 8000 --reload

📄 API Documentation

FastAPI automatically generates interactive API documentation:

Swagger UI:
http://127.0.0.1:8000/docs

🔌 API Endpoints
Health Check
GET /
Response:
{
  "status": "ok"
}

Text Classification
POST /predict


Request Body:

{
  "text": "This is a good product"
}


Response:

{
  "label": "positive",
  "confidence": 0.91
}

🤖 AI Model Integration

For demonstration purposes, this project uses a placeholder inference function that simulates AI predictions.

In a production environment, this layer would:

Load a TensorFlow model at application startup

Perform preprocessing and inference

Return structured prediction results

Example (production-ready approach):

model = tf.keras.models.load_model("model.h5")

def predict_text(text):
    processed = preprocess(text)
    prediction = model(processed)
    return postprocess(prediction)


No changes are required in the API layer when upgrading the model.

🔐 Production Considerations

Load models once at startup to improve performance

Use worker processes (Gunicorn + Uvicorn)

Add request throttling and authentication

Move heavy inference to background tasks or external services

Add database-backed logging if needed

📌 Use Cases

AI-powered microservices

Text classification APIs

Model inference gateways

Backend services integrating ML models

👤 Author

Samuel Ndubumma Nnadozie
Backend Engineer | API & Workflow Automation

