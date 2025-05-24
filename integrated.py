import os
import time
import random
from login_test import CanvaLoginTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

screenshots_directory = 'Screenshots'
# Create the directory if it does not exist
if not os.path.exists(screenshots_directory):
    os.makedirs(screenshots_directory)
    print(f'Directory created: {screenshots_directory}')
else:
    print(f'Directory already exists: {screenshots_directory}')
    
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
            # Define the path for the screenshot file
            screenshot_file_path = os.path.join(screenshots_directory, f'search_input.png')
            self.driver.save_screenshot(screenshot_file_path)
            search_bar.send_keys(Keys.RETURN)
            print("Search success")
            time.sleep(10)
            screenshot_file_path = os.path.join(screenshots_directory, f'templates.png')
            self.driver.save_screenshot(screenshot_file_path)
        except Exception as e:
            print(f"Search failed: {e}")
            return
            
        print(f" Current url : {driver.current_url}" )

        driver.implicitly_wait(10)

        # Find all elements with the given class name (assuming this class name is consistent for all templates)
        templates = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"][aria-label]')
        condition = True
        while condition:
            random_template = random.choice(templates)
            template_name = random_template.get_attribute('aria-label')
            print(f"Randomly selected template: {template_name}")
            random_template.click()
            time.sleep(10)  # Adjust sleep time as needed
            screenshot_file_path = os.path.join(screenshots_directory, f'Customize_template_button.png')
            self.driver.save_screenshot(screenshot_file_path)

            try:
                use_template_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[text()='Use this template']"))
                )
                print("Use this template button found,\nclosing and selecting another template.")
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
                )
                close_button.click()
                # condition = False
                time.sleep(10)  # Adjust sleep time as needed
            except:
                print("Use this template button not findable")
            try:
                time.sleep(5)
                customize_template_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Customise this template']"))
                )
                customize_template_button.click()
                condition = False
                print("Customise template found")
            except:
                print("Customize template Not found...")
                
        print("Finally found the template and Testing the buttons.")
        print(driver.current_url)
        window_handles = driver.window_handles

        # Loop through all window handles and switch to the latest one
        for handle in window_handles:
            driver.switch_to.window(handle)
            
        print(driver.current_url)
        try:
            screenshot_file_path = os.path.join(screenshots_directory, f'Customize_tab.png')
            self.driver.save_screenshot(screenshot_file_path)
            time.sleep(20)
            # Click file button
            file_button = WebDriverWait(driver, 10).until( 
                EC.element_to_be_clickable((By.XPATH, "//span[text()='File']"))
                )
            file_button.click()
            print("Clicked the file option")
        except:
            print("cannot find the file_button" )
        try:
            # Click for remane button 
            edit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Design title']"))
            )
            edit.click()
            edit.clear()
            edit.click()
            
            time.sleep(4)
            
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
                # EC.element_to_be_clickable((By.XPATH, '//button[@class="_1QoxDw o4TrkA CA2Rbg fgQwew zQlusQ uRvRjQ oGPTlw YPTJew Qkd66A tYI0Vw vCeYsQ"]'))
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Download']"))
            )
            download_button.click()
            time.sleep(5)
            print("Clicked the download button successfully")
        except:
            print("Cannot click the downoad button" )
        try:
            screenshot_file_path = os.path.join(screenshots_directory, f'download.png')
            self.driver.save_screenshot(screenshot_file_path)
            # Click download button
            download_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Download']"))
            )
            download_button.click()
            time.sleep(20)
            print("Clicked the download button successfully")
        except:
            print("Cannot click the downoad button" )
            
        driver.get("https://canva.com/")
                
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