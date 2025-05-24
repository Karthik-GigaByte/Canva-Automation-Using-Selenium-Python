import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
screenshots_directory = 'Screenshots'
# Create the directory if it does not exist

if not os.path.exists(screenshots_directory):
    os.makedirs(screenshots_directory)
    print(f'Directory created: {screenshots_directory}')
else:
    print(f'Directory already exists: {screenshots_directory}')
class CanvaLoginTest():
    def __init__(self, email, password, phone_number):
        options = uc.ChromeOptions()
        self.driver = uc.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def login(self):
        driver = self.driver
        canva = 'https://www.canva.com/'

        try:
            driver.get(canva)
            time.sleep(5)
            print("Canva Homepage Appeared..!!")

            print("Searching for Log In button ...")
            log_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Log in']"))
            )
            log_in_button.click()
            print("Login Button is clicked.")
            time.sleep(5)
            # Define the path for the screenshot file
            screenshot_file_path = os.path.join(screenshots_directory, f'login_button.png')
            self.driver.save_screenshot(screenshot_file_path)

            print("Searching for Google Account Login button ...")
            google_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Continue with Google']"))
            )
            google_button.click()
            print("Continue with Google button Button is clicked.")
            time.sleep(5)

            WebDriverWait(driver, 10).until(EC.new_window_is_opened)
            original_window = driver.current_window_handle
            print("Original URL: ", driver.current_url)
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)
            # Get the URL of the new window
            new_window_url = driver.current_url
            print("New window URL:", new_window_url)

            if "https://accounts.google.com/" in driver.current_url:
                print("Continuing with Google login")
                try:
                    email_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//input[@name='identifier' and @class='whsOnd zHQkBf']"))
                    )
                    email_input.send_keys(self.email)
                    # Define the path for the screenshot file
                    screenshot_file_path = os.path.join(screenshots_directory, f'email_input.png')
                    self.driver.save_screenshot(screenshot_file_path)
                    time.sleep(2)  # Reduced sleep time for demonstration
                    print("Email input is proceeded.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Google page not appeared.")

            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']"))
            )
            next_button.click()
            print("Next button is clicked.")

            password_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='Passwd' and @class='whsOnd zHQkBf']"))
            )
            password_input.send_keys(self.password)
            # Define the path for the screenshot file
            screenshot_file_path = os.path.join(screenshots_directory, f'password_input.png')
            self.driver.save_screenshot(screenshot_file_path)
            print("Password input is proceeded.")
            time.sleep(3)

            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']"))
            )
            next_button.click()
            print("Next button is clicked.")
            time.sleep(5)

            try:
                print("Trying to continue...")
                continue_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue') and @class='VfPpkd-vQzf8d']"))
                )
                continue_button.click()
                print("Continued successfully")
                time.sleep(5)
                screenshot_file_path = os.path.join(screenshots_directory, f'Home_page.png')
                self.driver.save_screenshot(screenshot_file_path)
            except:
                print("No continue button found.")
            time.sleep(10)
            
            # Wait for the new window to close
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
            # Ensure the original window still exists before switching back
            if original_window in driver.window_handles:
                driver.switch_to.window(original_window)
                print("Switched back to the original window.")
            else:
                print("Original window is no longer available.")

            print("Current URL: ", driver.current_url)

        except Exception as e:
            print(f"Error: {e}")
            print("Unable to open Canva")
        finally:
            return driver

# Uncomment the below lines to test the login independently
if __name__ == "__main__":
    email = 'canva.at.automation@gmail.com'
    password = 'Canva@123'
    phone_number = '9886327627'
    login = CanvaLoginTest(email, password, phone_number)
    login.login()
    
    
    
    