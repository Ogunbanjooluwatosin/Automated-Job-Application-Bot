# ------------------------------------imports----------------------
import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ------------------------------------when page crashes----------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ------------------------------------driver----------------------
chrome_driver_path = Service(executable_path="C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3586571061&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
driver.get(url)


# ----------------------------to cancel------------------------------
def cancel():
    x = driver.find_element(by=By.XPATH, value="//*[@id='ember694']/li-icon/svg")
    x.click()
    discard = driver.find_element(by=By.XPATH, value="//*[@id='ember719']/span")
    discard.click()


# ----------------------------to sign in------------------------------

EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]
PHONE_NO = os.environ["number"]
sign_in = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

email_entry = driver.find_element(by=By.XPATH, value="//*[@id='username']")
email_entry.send_keys(EMAIL)

password_entry = driver.find_element(by=By.XPATH, value="//*[@id='password']")
password_entry.send_keys(PASSWORD)

login = driver.find_element(by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
login.click()
# ----------------------------for all jobs------------------------------
all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for job in all_jobs:
    print("clicked")
    job.click()
    try:
        apply = driver.find_element(by=By.XPATH, value="//*[@id='ember320']/span")
        apply.click()
        # number_entry = driver.find_element(by=By.XPATH,
        #                                    value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3586571061-87714189-phoneNumber-nationalNumber']")
        # number_entry.send_keys(PHONE_NO)
        next_button = driver.find_element(by=By.XPATH, value="//*[@id='ember366']/span")
        next_button.click()
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            cancel()
            print("skipped.")
            continue
        else:
            print("click")
            submit_button.click()
            x = driver.find_element(by=By.XPATH, value="//*[@id='ember694']/li-icon/svg")
            x.click()
    except NoSuchElementException:
        print("cancel")
        cancel()
        continue
driver.quit()
