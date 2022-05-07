# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/health")
# def health():
#     return "Service is online."


from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    query_string: str
  

sentiment_model = pipeline("sentiment-analysis")
print('Starting a Fast API App:')
app = FastAPI()

@app.post("/my-endpoint")
def my_endpoint(request: PredictionRequest):
    print(type(request.query_string))
    sentiment = sentiment_model(request.query_string)
    return(f"Sentiment test: {request} == {sentiment}")