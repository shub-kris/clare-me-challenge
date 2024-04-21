from typing import List, Union
import json

import torch
import uvicorn
from fastapi import FastAPI
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

app = FastAPI(title="Claire Text Classification API")

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def load_model():
    trained_model_path = "model-weights"
    tokenizer = AutoTokenizer.from_pretrained(trained_model_path)
    model = AutoModelForSequenceClassification.from_pretrained(trained_model_path)
    global classifier
    classifier = pipeline(
        "text-classification", model=model, tokenizer=tokenizer, device=device
    )

@app.post("/predict")
def predict(text: Union[str, List[str]]):
    prediction = classifier(text)
    prediction_dict = {"prediction": prediction}
    return json.dumps(prediction_dict)


if __name__ == "__main__":
    uvicorn.run(app="app.main:app", host="127.0.0.1", port=8000)
