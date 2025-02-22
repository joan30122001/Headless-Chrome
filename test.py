# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Set up Chrome options for headless mode
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run Chrome in headless mode
# options.add_argument("--disable-gpu")  # Disable GPU (useful for headless mode)
# options.add_argument("--no-sandbox")  # Bypass OS security model (needed for some environments)
# options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues

# # Initialize the WebDriver with options
# driver = webdriver.Chrome(options=options)

# try:
#     # Step 1: Open the login page
#     driver.get("http://52.91.120.52:8080/")  # Replace with the actual login page URL
#     time.sleep(2)  # Allow time for the page to load

#     # Step 2: Find the username and password fields and enter credentials
#     username_input = driver.find_element(By.NAME, "username")  # Update selector based on site
#     password_input = driver.find_element(By.NAME, "admin@12345")  # Update selector based on site

#     username_input.send_keys("admin")  # Replace with your actual username
#     password_input.send_keys("YOUR_PASSWORD")  # Replace with your actual password

#     # Step 3: Click the login button
#     login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust if needed
#     login_button.click()

#     # Step 4: Wait for login to process
#     time.sleep(3)

#     # Step 5: Verify if login is successful
#     if "dashboard" in driver.current_url.lower():  # Adjust based on expected redirect URL
#         print("Login successful!")
#     else:
#         print("Login failed!")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()  # Close the headless browser





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Use Selenium's built-in driver manager (No need for manual ChromeDriver)
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--ignore-certificate-errors")

# # Initialize WebDriver (Selenium Manager automatically manages the driver)
# driver = webdriver.Chrome(options=options)

# try:
#     driver.get("http://52.91.120.52:8080/")  # Replace with actual login page
#     time.sleep(2)

#     username_input = driver.find_element(By.NAME, "j_username")  # Adjust selector if needed
#     password_input = driver.find_element(By.NAME, "j_password")  # Adjust selector if needed

#     username_input.send_keys("admin")  # Replace with actual username
#     password_input.send_keys("admin@12345")  # Replace with actual password

#     login_button = driver.find_element(By.XPATH, "/html/body/main/div/form/button")  # Adjust if needed
#     login_button.click()

#     time.sleep(3)

#     if "http://52.91.120.52:8080/" in driver.current_url.lower():  # Adjust expected redirect URL
#         print("Login successful!")
#     else:
#         print("Login failed!")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Use Selenium's built-in driver manager (No need for manual ChromeDriver)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--ignore-certificate-errors")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open Jenkins login page
    driver.get("http://52.91.120.52:8080/")
    time.sleep(2)

    # Step 2: Locate and fill in the login fields
    username_input = driver.find_element(By.NAME, "j_username")
    password_input = driver.find_element(By.NAME, "j_password")

    username_input.send_keys("admin")  # Update with actual credentials
    password_input.send_keys("admin@12345")  # Update with actual credentials

    # Step 3: Click login button
    login_button = driver.find_element(By.XPATH, "/html/body/main/div/form/button")
    login_button.click()
    time.sleep(3)

    # Step 4: Verify login
    if "http://52.91.120.52:8080/" in driver.current_url.lower() or "jenkins" in driver.current_url.lower():
        print("Login successful!")
    else:
        print("Login failed!")
        driver.quit()
        exit()

    # Step 5: Navigate to "New Item" to create a project
    driver.get("http://52.91.120.52:8080/view/All/newJob")  # Direct URL to create new project
    time.sleep(2)

    # Step 6: Enter project name
    project_name = "Jenkins_Project"  # Change the project name if needed
    project_name_input = driver.find_element(By.ID, "name")
    project_name_input.send_keys(project_name)

    # Step 7: Select "Freestyle Project"
    freestyle_project_option = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[2]/div[2]/div[1]/ul/li[2]")
    freestyle_project_option.click()
    time.sleep(1)

    # Step 8: Click "OK" button to create the project
    ok_button = driver.find_element(By.ID, "ok-button")
    ok_button.click()
    time.sleep(3)

    # Step 9: Verify if project creation was successful
    if project_name.lower() in driver.current_url.lower():
        print(f"Project '{project_name}' created successfully!")
    else:
        print("Project creation failed!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Close browser
