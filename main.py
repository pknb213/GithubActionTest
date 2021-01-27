from fastapi import FastAPI
import uvicorn
import requests
from requests.auth import HTTPBasicAuth

app = FastAPI()


@app.get("/")
def index():
    print("Hello, FastaAPI Template~")
    return {"RES": "Happy"}


# Please, if Product Env used to execution the 'run.sh'!
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)