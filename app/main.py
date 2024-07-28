from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import RedirectResponse

load_dotenv()
app = FastAPI()

#Move it to env
WALLET_ADRESS = "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"
API_KEY = "cqt_wFDJ6q9g4BRGdjGBqjdgjy7D4BtF"

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.post("/assets/")
def get_assets():
    try:
        ...
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/total_usd_value/")
def get_usd_value():
    try:
        ...
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/transactions/")
def get_wallet_transactions():
    try:
        ...
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))