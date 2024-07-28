from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from starlette.responses import RedirectResponse
import requests
from requests.auth import HTTPBasicAuth

load_dotenv()
app = FastAPI()

#Move it to env
WALLET_ADRESS = "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"
API_KEY = "cqt_wFDJ6q9g4BRGdjGBqjdgjy7D4BtF"


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.post("/assets/")
def get_assets(chain_name:str, wallet_address:str):
    try:
        if not chain_name:
            raise Exception("chain_name was not provided")
        if not wallet_address:
            raise Exception("wallet_adress is empty or incorrect")
        auth_data = HTTPBasicAuth(API_KEY, '')
        endpoint_url = f"https://api.covalenthq.com/v1/{chain_name}/address/{wallet_address}/balances_v2/"
        response = requests.get(endpoint_url,auth=auth_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching assets")
        return  response.json().get('data', {}).get('items', [])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/total_usd_value/")
def get_native_token_balance(chain_name:str, wallet_address:str):
    try:
        if not chain_name:
            raise Exception("chain_name was not provided")
        if not wallet_address:
            raise Exception("wallet_adress is empty or incorrect")

        auth_data = HTTPBasicAuth(API_KEY, '')
        endpoint_url = f"https://api.covalenthq.com/v1/{chain_name}/address/{wallet_address}/balances_v2/"
        response = requests.get(endpoint_url,auth=auth_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching wallet data")
        wallet_data = response.json().get('data', {}).get('items', [])

        # Calculate the total USD value
        total_usd_value = 0
        for asset in wallet_data:
            if 'pretty_quote_24h' in asset and asset['pretty_quote_24h'] is not None:
                total_usd_value += float(asset['pretty_quote_24h'].replace('$', '')) 

        return {"wallet_address": wallet_address, "total_usd_value": total_usd_value}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/transactions/")
def get_wallet_transactions(chain_name:str, wallet_adress:str, page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    try:
        if not chain_name:
            raise Exception("chain_name was not provided")
        if not wallet_adress:
            raise Exception("wallet_adress is empty or incorrect")

        endpoint_url = f"https://api.covalenthq.com/v1/{chain_name}/address/{wallet_adress}/transactions_v2/"
        auth_data = HTTPBasicAuth(API_KEY, '')
        params = {
            "page-size": page_size,
            "page-number": page
        }
        response = requests.get(endpoint_url, params=params, auth=auth_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching transactions")

        return response.json().get('data', {}).get('items', [])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))