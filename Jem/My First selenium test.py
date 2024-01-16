import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def open_webpage(url):
    chrome_driver_path = "C:\\Users\\adeol\\PycharmProjects\\Seleniumproject\\pythonProject\\Jem\\chromedriver-win64\\chromedriver.exe"

    # Create a Chrome service
    service = ChromeService(chrome_driver_path)

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to the desired webpage
        driver.get(url)

        # Optional: Add some delay to see the opened page (you may need to adjust this based on your internet speed)
        driver.implicitly_wait(5)

    finally:
        # Close the browser window
        time.sleep(20)
        driver.quit()


# Example usage
if __name__ == "__main__":
    # Replace '/path/to/chromedriver' with the actual path to your ChromeDriver executable


    # Replace 'https://www.example.com' with the URL of the webpage you want to open
    webpage_url = 'https://paypal.co.uk'

    # Open the webpage using the provided function
    open_webpage(webpage_url)
    time.sleep(10)
