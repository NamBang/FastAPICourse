from email.policy import default
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_files(file: bytes =File(default=None), fileb: UploadFile=File(default=None), token: str = Form(default=None)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }