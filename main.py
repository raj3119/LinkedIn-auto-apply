from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

try:
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/feed/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
except Exception as e:
    print("❌ Error launching browser:", e)
    exit()

def login(driver, wait):
    try:
        print("🔐 Attempting login...")

        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username.send_keys(os.getenv("Linkedin_Username"))

        password = driver.find_element(By.ID, "password")
        password.send_keys(os.getenv("Linkedin_Password")) 

        sign_in = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
        sign_in.click()

        wait.until(EC.presence_of_element_located((By.ID, "global-nav-search")))
        print("✅ Logged in successfully.")
        time.sleep(3)
    except Exception as e:
        print("❌ Login failed:", e)
        driver.quit()
        exit()

def search_jobs(driver, wait):
    try:
        search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        search.send_keys(os.getenv("Job"))
        search.send_keys(Keys.RETURN)
    except Exception as e:
        print("❌ Searching failed:", e)
        driver.quit()
        exit()

def apply_to_job(driver, wait):
    jobs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Jobs']")))
    jobs_tab.click()
    time.sleep(3)

    job_cards = driver.find_elements(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
    
    for button in job_cards[:5]:  # Apply to top 5 jobs
        try:
            button.click()
            print("👉 Clicked apply button")
            time.sleep(2)

            try:
                phone_field = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'phoneNumber')]"))
                )
                phone_field.clear()
                phone_field.send_keys(os.getenv("Phone"))
                print("📱 Filled phone")

                location_field = driver.find_element(By.XPATH, "//input[contains(@id,'city')]")
                location_field.clear()
                location_field.send_keys(os.getenv("City"))
                print("📍 Filled city")

                try:
                    submit_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Submit application')]")
                    submit_btn.click()
                    print("✅ Submitted simple application")

                except:
                    try:
                        next_btn = driver.find_element(By.XPATH, "//button/span[text()='Next']")
                        next_btn.click()
                        print("➡️ Clicked Next (multi-step form, skipped)")

                        # Handle Save/Discard popup
                        try:
                            discard_btn = WebDriverWait(driver, 5).until(
                                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Discard']"))
                            )
                            discard_btn.click()
                            print("❌ Discarded application due to complexity")
                        except:
                            print("ℹ️ No Save/Discard popup appeared")

                        # Close modal
                        close_btn = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss']"))
                        )
                        close_btn.click()
                        continue

                    except:
                        print("⚠️ No submit or next button found. Skipping...")
                        continue

            except Exception as e:
                print("⚠️ Simple form not found or not applicable:", e)
                try:
                    close_btn = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss']"))
                    )
                    close_btn.click()
                    print("❎ Closed complex job modal")
                except:
                    print("❌ Could not close modal, continuing")
                continue

        except Exception as e:
            print("❌ Could not click apply button:", e)
            continue

# ✅ Run the automation
login(driver, wait)
search_jobs(driver, wait)
apply_to_job(driver, wait)

time.sleep(4)
driver.quit()