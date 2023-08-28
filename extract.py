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
# In[2]:

from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
uri = os.environ.get('URI')
chat_id = "6125234965"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"



# bot = telebot.TeleBot(BOT_TOKEN)
mongo_client = pymongo.MongoClient(uri)
db = mongo_client["real_quiz"]


# In[6]:





import os
import requests
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
uri = os.environ.get('URI')
chat_id = "6125234965"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def collection_exists(collection_name):
    return collection_name in db.list_collection_names()


# In[7]:


def save_data_to_mongodb(collection_name, data):
    collection = db[collection_name]

    # Insert the data into the collection
    inserted_data = collection.insert_one(data)


# In[8]:

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.service import Service
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--desable-dev-shm-usage")
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# In[9]:
def drivelogin(driver):
    url = "https://quiz.directory/"
    driver.get(url)
    time.sleep(5)
    login_button = driver.find_element(By.CLASS_NAME, 'bq-header-login-btn')
    login_button.click()
    driver.switch_to.window(driver.window_handles[-1])
    nump = driver.find_element(By.ID, 'login-phone')
    nump.send_keys(7410823899)
    sub = driver.find_elements(By.CLASS_NAME, 'button-item-label')[1]
    sub.click()
    msdata = {
        "chat_id": chat_id,
        "text": "plzz click on confirm"
    }

    response = requests.get(url, params=msdata)
    driver.switch_to.window(driver.window_handles[0])
    msdata = {
        "chat_id": chat_id,
        "text": "successfully logged in"
    }

    response = requests.get(url, params=msdata)
    return True

# In[16]:


def que(driver):
    dic = {
    }
    nom = driver.find_element(By.CLASS_NAME, 'bq-question-header').text
    nob = nom.split(' ')[1]
    try:
        msg = driver.find_element(By.CLASS_NAME, 'bq-question-message').text
        desc = True
        desc_text = msg
    except:
        desc = False
        desc_text = ""
    que = driver.find_element(By.CLASS_NAME, 'bq-question-title').text
    options = []
    optionsE = driver.find_elements(By.CLASS_NAME, 'bq-question-answer')
    for option in optionsE:
        opt = option.find_element(By.CLASS_NAME, 'bq-answer-label-text').text
        options.append(opt)
    element = driver.find_element(By.CLASS_NAME, 'bq-question-answer.correct')
    attribute_value = int(element.get_attribute('data-value'))
    dic = {
        "message": desc,
        "message_text": desc_text,
        "question": que,
        "options": options,
        "correct_option": options[attribute_value],
        "correct_option_id": attribute_value,
        "question_no": nob
    }
    msdata = {
        "chat_id": chat_id,
        "text": f"Q.{nob} {que} "
    }

    response = requests.get(url, params=msdata)
    return dic


# In[17]:


def clko(driver):
    actions = ActionChains(driver)
    element_class = "bq-answer-label"  # Replace with the actual class name of the elements
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, element_class)))

    # Choose the index of the element you want to click (e.g., index 1)
    desired_element_index = 0

    element_to_click = elements[desired_element_index]

    # Click the desired element
    #     element_to_click.click()
    try:
        actions.click(element_to_click).perform()
    except:

        actions.click(driver.find_element(By.CLASS_NAME, 'bq-answer-label')).perform()


# In[18]:


def clkb(driver):
    actions = ActionChains(driver)
    element_class = "js-next-button"  # Replace with the actual class name of the elements

    elements = driver.find_element(By.CLASS_NAME, element_class)
    # Click the desired element
    actions.click(elements).perform()


# In[19]:





# In[20]:


def drive(ids,driver):
    url = f"https://quiz.directory/quiz/{ids}/"
    driver.get(url)


def clkbtn(driver):
    bth = driver.find_element(By.CLASS_NAME, 'bq-quiz-play-button')
    bth.click()


def strtlp(lim, ids,driver):
    i = 1
    while i < (lim + 5):
        nom = driver.find_element(By.CLASS_NAME, 'bq-question-header').text
        nomr = nom.split(' ')
        if nomr[1] == nomr[-1]:
            break
        else:
            try:
                clko(driver)
                dts = que(driver)
                save_data_to_mongodb(ids, dts)
            except:
                clko(driver)
                try:
                    dts = que(driver)
                    save_data_to_mongodb(ids, dts)
                except:
                    dts = que(driver)
                    save_data_to_mongodb(ids, dts)

        try:

            clkb(driver)
        except:
            clkb(driver)
        i += 1


def startB(ids,driver):
    if collection_exists(ids):
        o=1+1
        msdata = {
            "chat_id": chat_id,
            "text": f"this quiz is already scraped"
        }

        response = requests.get(url, params=msdata)
    else:

        drive(ids,driver)
        counters = driver.find_elements(By.CLASS_NAME, 'bq-quiz-counter')
        counter = counters[0]
        lim = int(counter.find_element(By.CLASS_NAME, 'bq-info-main').text)
        msdata = {
            "chat_id": chat_id,
            "text": f"this quiz has {lim} questions"
        }

        response = requests.get(url, params=msdata)
        # bot.reply_to(ctx, f'quiz has {lim} questions')
        clkbtn(driver)
        msdata = {
            "chat_id": chat_id,
            "text": "quiz extraction has been started plz wait"
        }

        response = requests.get(url, params=msdata)
        # bot.reply_to(ctx, "quiz extraction has been started plz wait")
        strtlp(lim, ids,driver)



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
    jg=drivelogin(myDriver)
    response = requests.get(url, params=msdata)
    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")

