# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService

# # Replace with your actual path if needed
# browser = webdriver.Chrome(service=ChromeService(executable_path='D:\\chromedriver-win64\\chromedriver.exe'))

# browser.get('http://www.google.com')
# print("Chrome launched successfully!")
# browser.quit()
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.options import Options

# # Specify the path to the Firefox binary
# firefox_options = Options()
# firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'  # Update this path if different

# # Initialize the Firefox WebDriver with the specified options
# browser = webdriver.Firefox(service=FirefoxService(executable_path='D:/geckodriver.exe'), options=firefox_options)
# browser.get('http://www.google.com')
# print("Firefox launched successfully!")
# browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time

devices = {
    "Desktop": [
        (1920, 1080),
        (1366, 768),
        (1536, 864)
    ],
    "Mobile": [
        (360, 640),
        (414, 896),
        (375, 667)
    ]
}

browsers = {
    "Chrome": webdriver.Chrome(),
    "Firefox": webdriver.Firefox(),
    "Safari": webdriver.Safari()
}


url = 'https://www.getcalley.com/page-sitemap.xml'


for browser_name, browser in browsers.items():
    for device, resolutions in devices.items():
        for resolution in resolutions:
            width, height = resolution
            browser.set_window_size(width, height)
            for i in range(1,6):
                browser.get(url)
                browser.find_element(By.XPATH, f'(//a[contains(text(), "https://www.getcalley.com/")])[{i}]').click()
                time.sleep(3)  
                               
                folder_path = f"{device}/{width}x{height}"
                os.makedirs(folder_path, exist_ok=True)

                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                screenshot_path = f"{folder_path}/Screenshot-{timestamp}.png"
                browser.save_screenshot(screenshot_path)

                print(f"Screenshot saved to {screenshot_path}")

    browser.quit()

