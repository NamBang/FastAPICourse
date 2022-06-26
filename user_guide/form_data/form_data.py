from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(default=None), password: str = Form(default=None)):
    return {"username": username, "password": password}