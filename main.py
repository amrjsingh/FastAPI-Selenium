from fastapi import FastAPI,Request, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
from selenium.webdriver.common.keys import Keys
import os
import requests

import pymongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
import time
# import telebot
from selenium.webdriver.chrome.options import Options
import os

import requests
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
uri = os.environ.get('URI')
chat_id = "6125234965"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


msdata = {
    "chat_id": chat_id,
    "text": "some text"
}

response = requests.get(url, params=msdata)


from appt import *
SECRET = os.getenv("SECRET")
driver=createDriver()
logi=drivelogin(driver)

app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    msdata = {
        "chat_id": chat_id,
        "text": "bot started"
    }

    response = requests.get(url, params=msdata)
    return {"message": "Hello World. Welcome to FastAPI!"}




@app.get("/quiz/{param}")
async def path_params(param: str):
    id=param
    msdata = {
        "chat_id": chat_id,
        "text": f"quiz **{id}** scraping started"
    }

    response = requests.get(url, params=msdata)
    hj=startB(id,driver)

    return "started plz wait"

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


