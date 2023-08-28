from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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




def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    msdata = {
        "chat_id": chat_id,
        "text": "chromedriver started sucessfully"
    }

    response = requests.get(url, params=msdata)
    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")