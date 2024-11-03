from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def take_screenshot(url, output_file):
    # Set up the Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--window-size=1920,1080')  # Set the window size

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Wait for the page to load (adjust the sleep time as needed)
        time.sleep(5)

        # Take a screenshot and save it to the specified file
        driver.save_screenshot(output_file)
        print(f"Screenshot saved to {output_file}")
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    url = "https://www.instagram.com/"
    output_file = "screenshot.png"
    take_screenshot(url, output_file)