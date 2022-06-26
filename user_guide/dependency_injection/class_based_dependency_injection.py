from fastapi import FastAPI, Depends

app = FastAPI()

dummy_db = {
    '1': "SDE1 at Google Cloud",
    '2': "SDE2 at Google Cloud",
    '3': "SDE3 at Google Cloud",
    '4': "SDE4 at abc",
    '5': "SDE5 at efght"
}

def get_object_or_featured(id:str, feature_job:str):
    value = dummy_db.get(id)
    if not value:
        value = dummy_db.get(f"{feature_job}")
    return value

@app.get("/job/{id}")
def get_job_by_id(job_title: str = Depends(get_object_or_featured('2'))):
    return job_title