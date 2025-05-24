import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test import CanvaLoginTest
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
class CanvaEditTest:
    def __init__(self):    
        email = 'canva.at.automation@gmail.com'
        password = 'Canva@123'
        phone_no = '9886327627'
        self.login_instance = CanvaLoginTest(email, password, phone_no)
        self.driver = self.login_instance.login()
        print("Driver returned succesffuly ")
        
    def edit_test(self):
        if self.driver is None:
            print("Login failed. Unable to proceed with search.")
            return
        # self.driver.get("https://canva.com/en_in")
        # time.sleep(10)
        print("After returning driver inside edit_test.py.")
        try:
            print("current url  : ", self.driver.current_url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="uLt0uw"]//span[contains(@class, "_8M3E3w")]'))
            )
            button = self.driver.find_element(By.XPATH, '//div[@class="uLt0uw"]//span[contains(@class, "_8M3E3w")]')
            button.click()
            
            time.sleep(5)
        except:
            print("profile Button not clickable")
            
        try:
            #Accessing the Settings button
            print("current url  : ", self.driver.current_url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//li[@class="k__oiw _9Mb__A"]/a[@class="_1QoxDw DNpAZA o4TrkA CA2Rbg fgQwew zQlusQ uRvRjQ oGPTlw YPTJew Qkd66A tYI0Vw vCeYsQ"]/span[text()="Settings"]'))
            )
            button = self.driver.find_element(By.XPATH, '//li[@class="k__oiw _9Mb__A"]/a[@class="_1QoxDw DNpAZA o4TrkA CA2Rbg fgQwew zQlusQ uRvRjQ oGPTlw YPTJew Qkd66A tYI0Vw vCeYsQ"]/span[text()="Settings"]')
            button.click()
            print("Setting Button clicked Successfully")
            time.sleep(5)
        except:
            print("Setting Button not Clickable")
        try:
            #Clicking the Edit button
            print("current url  : ", self.driver.current_url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="PUclIA"]/button[@type="button"]/span[text()="Edit"]'))
            )
            button = self.driver.find_element(By.XPATH, '//div[@class="PUclIA"]/button[@type="button"]/span[text()="Edit"]')
            button.click()
            print("Edit Button clicked Successfully")
            time.sleep(5)
        except:
            print("Edit Button not Clickable")
        try:
            # Wait for the input box to be present and focused
            input_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="yYw_FA"]//input[@type="text"]'))
            )
            input_box.send_keys(Keys.SHIFT, Keys.ARROW_UP)
            input_box.send_keys(Keys.DELETE)
            print("Name cleared")
            time.sleep(3)
            input_box.send_keys('Marvel design')
            time.sleep(3)
        except:
            print("Not Edit able")
            
        try:
            time.sleep(3)
            wait = WebDriverWait(self.driver, 10)
            # Wait for the "Save" button to be clickable and click it
            save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="r7sYbA"]/button[@type="submit"]/span[text()="Save"]')))
            save_button.click()
            print("Saved the new name successfully")
            time.sleep(10)
        except:
            print("New name is not getting saved")
        try:
            # Navigate back to the homepage
            # self.driver.get("https://www.canva.com")
            self.driver.back()
            print("Navigated back to the Canva homepage")
            time.sleep(10)
        except:
            print("Unable to navigate back to the Canva homepage")
            
        finally:
            self.driver.quit()

        time.sleep(20)
if __name__ == "__main__":
    search = CanvaEditTest()
    search.edit_test()