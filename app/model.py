import torch
import torch.nn as nn
import os
from dotenv import load_dotenv
from pathlib import Path

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        if isinstance(x, str):
            x = torch.tensor([[1.0]]) if "good" in x else torch.tensor([[0.0]])
        return torch.sigmoid(self.fc(x))
    
load_dotenv(override=True)
ENV = os.getenv("ENV", "development").lower()

def model_placeholder(input):
    result = 0.95 if 'good' in input else 0.45
    return result

def load_model(model_path: str | Path, device: str | None = None):
    """loads AI model from model_path"""
        
    if ENV == 'production':
        model_path = Path(model_path)

        device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")

        try:
            model = MyModel()  # same architecture as training
            model.load_state_dict(
                torch.load(model_path, map_location=device)
            )
            model.to(device)
            model.eval()
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load PyTorch model: {e}")
    return model_placeholder
    
def process_input(data:str):
    """Processes request data defore feeding AI model"""
    return data

def process_output(prediction:float):
    """Process output based on prediction result"""
    return "positive" if prediction > 0.5 else "negative"

def predict_text(model, text: str):
    pre_processed = process_input(text)
    confidence = model(pre_processed)
    return process_output(confidence), confidence
