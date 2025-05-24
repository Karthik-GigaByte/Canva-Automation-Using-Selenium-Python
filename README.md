# Canva-Automation-Using-Selenium-Python![Badge](https://img.shields.io/badge/Selenium-Testing-1FDD0A)

## Introduction

This repository contains a suite of automated tests for the Glassdoor website, implemented using Selenium and Python. The purpose of these tests is to validate the functionality of key features on the Glassdoor website, including user login, password changes, job postings, company searches, and job searches. This project aims to ensure that these features work as expected and to catch any regressions or failures early in the development cycle.

## Technologies Used


- **Programming Language:**    [![Python](https://img.shields.io/badge/Python-100000?style=plastic&logo=Python&logoColor=white&labelColor=0F0312&color=black)](https://github.com/Karthik-GigaByte/Glassdoor-Automation)
  
- **Automation Tool:**    [![Selenium](https://img.shields.io/badge/Selenium-100000?style=plastic&logo=Selenium&logoColor=white&labelColor=43DD0F&color=black)](https://github.com/Karthik-GigaByte/Glassdoor-Automation)
  
- **Environment Management:** dotenv (.env)

## Test Cases

Below is the table of test cases covered in this Selenium automation suite:

| Test Case ID | Description          | Method                     | Status (Active/Deprecated) |Status                     |
|--------------|----------------------|----------------------------|----------------------------|---------------------------|
| TC01         | Login functionality  | `test_login()`             | Active                     | Pass                      |
| TC02         | Change Password      | `test_change_password()`   | Active                     | Pass                      |
| TC03         | Posting a test       | `test_posting()`           | Active                     | Pass                      |
| TC04         | Search for templates | `test_search_templates()`  | Active                     | Pass                      |
| TC05         | download_template    | `download_template`        | Active                     | Pass                      |

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Karthik-GigaByte/Canva-Automation-Using-Selenium-Python
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup the dotenv**:
    ```bash
     pip install dotenv
    ```
    
## Demonstration

Here are some animated GIFs showing the tests in action:

### Login Test

![Login Test GIF](path_to_your_gif/login_test.gif)

### Change Password Test

![Change Password GIF](path_to_your_gif/change_password_test.gif)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
  
