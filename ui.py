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

