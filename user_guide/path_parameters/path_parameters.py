from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    hoda = "wavea"
    yamaha = "serius"
    taobao = "bisa"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.hoda:
        return {"model_name": model_name, "model_type": "wavea"}
    
    if model_name.value == "serius":
        return {"model_name": model_name, "model_type": "serius"}
    return {"model_name": model_name, "message": "Have some residuals"}