from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    query_string: str
  

sentiment_model = pipeline("sentiment-analysis")
app = FastAPI()

@app.post("my-endpoint")
def my_endpoint(request: PredictionRequest):
    sentiment = sentiment_model(request)
    return(f"Sentiment test: {request} == {sentiment}")