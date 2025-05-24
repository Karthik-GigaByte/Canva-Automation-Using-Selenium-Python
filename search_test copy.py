import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test import CanvaLoginTest
import random

class CanvaSearchTest():
    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def logging(self):
        self.loggs= CanvaLoginTest(self.email, self.password, self.phone_number)
        self.loggs.login()
        self.driver = self.loggs.driver
        
    def search_test(self):
        if self.driver is None:
            print("Login failed. Unable to proceed with search.")
            return
        print("After returning driver inside search_test.py.")
        
        try:
            driver = self.driver
            # Finding the search bar and accessing it
            search_bar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="search" and contains(@class, "s_JGcg fFOiLQ eoXdOg CmLV0g yW_5QA tMP70Q")]'))
            )
            time.sleep(3)
            search_bar.click()
            search_bar.send_keys('Presentation slides')
            search_bar.send_keys(Keys.RETURN)
            print("Search success")
            time.sleep(10)
        except Exception as e:
            print(f"Search failed: {e}")
            return
            
        print(f" Current url : {driver.current_url}" )

        driver.implicitly_wait(10)

        # Find all elements with the given class name (assuming this class name is consistent for all templates)
        templates = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"][aria-label]')

        while True:
            random_template = random.choice(templates)
            template_name = random_template.get_attribute('aria-label')
            print(f"Randomly selected template: {template_name}")
            random_template.click()
            time.sleep(10)  # Adjust sleep time as needed

            try:
                use_template_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[text()='Use this template']"))
                )
                print("Use this template button found, closing and selecting another template.")
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
                )
                close_button.click()
                time.sleep(3)  # Adjust sleep time as needed
            except:
                print("Use this template button not findable")
            try:
                customize_template_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Customize this template']"))
                )
                print("Customize template found")
            except:
                print("Not found...")
            
            try:
                #Trying to click the Starred button
                starred = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_7BKwSA']/button"))
                )
                time.sleep(2)
                starred.click()
                print("Starred button clicked successfully")
            except:
                print("Not found starred button")
            try:
                #Trying to Share by Copying
                options= WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='uLt0uw']/button"))
                )
                options.click()
                time.sleep(5)
                Copy_Share= WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ZjEpig']"))
                )
                Copy_Share.click()
                print("Copied the link successfully")
            except:
                print("Not found Share button")
            try:
                # customize_template_button.click()
                customize_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Customise this template'))
                )
            except:
                print("not able to find the customize_button" )
            try:
                customize_button.click()
                time.sleep(30)  
                print("Customise this template button clicked.")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("No appropriate button found, retrying.")
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
                )
                close_button.click()
                time.sleep(3)  # Adjust sleep time as needed    
            try:
                # Click file button
                file_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='VOvjeA']"))
                )
                file_button.click()
                print("i get any file")
            except:
                print("cannot find the file_button" )
            try:
                # Click for remane button 
                edit = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Design title']"))
                )
                edit.click()
                time.sleep(4)
                # Define a list of names starting with "Design"
                design = [
                    "Design A",
                    "Design B",
                    "Design C",
                    "Design D",
                    "Design E",
                    "Design F",
                    "Design G",
                    "Design H",
                    "Design I",
                    "Design J",
                    "Design K",
                    "Design L",
                    "Design M",
                    "Design N",
                    "Design O"
                ]
                random_name = random.choice(design)
                edit.send_keys(random_name)
                print("Edited the name successfully")
            except:
                print("cannot edit the name" )
            try:
                # Click download button
                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//li[@class='k__oiw _9Mb__A']//button[contains(@class, 'oGPTlw')]"))
                )
                download_button.click()
                time.sleep(10)
                print("Clicked the download button successfully")
            except:
                print("Cannot click the downoad button" )
    def run_test(self):
        self.logging()
        self.search_test()

# Uncomment the below lines to test the search independently
if __name__ == "__main__":
    email = 'canva.at.automation@gmail.com'
    password = 'Canva@123'
    phone_number = '9886327627'
    canva = CanvaSearchTest(email, password, phone_number)
    canva.run_test()