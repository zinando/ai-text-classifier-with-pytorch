from fastapi import FastAPI, HTTPException, Request
from app.schemas import PredictionOutput, TextInput
from app.model import predict_text, load_model
from contextlib import asynccontextmanager
from fastapi.concurrency import run_in_threadpool
import os
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.h5')

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = load_model(MODEL_PATH)
    yield

app = FastAPI(
    title="AI Text Classifier App With PyTorch",
    lifespan=lifespan
    )

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post(
    "/predicy",
    response_model=PredictionOutput,
    summary="Predicts the state of a text string"
)
async def predict(data: TextInput, request: Request):
    try:
        label, confidence = await run_in_threadpool(
            predict_text,
            request.app.state.model,
            data.text
        )
        return PredictionOutput(
            label = label,
            confidence = confidence
        )
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Model inference failed: {e}")

