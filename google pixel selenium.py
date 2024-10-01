from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the eBay website
driver.get('https://www.ebay.com/')

try:
    # Wait until the search box is present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.gh-tb.ui-autocomplete-input'))
    )
    
    # Send the search query
    search_box.send_keys("google pixel 7" + Keys.ENTER)

    while True:
        # Wait until the search results are loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 's-item__title'))
        )

        # Find all titles of the search results
        titles = driver.find_elements(By.CLASS_NAME, 's-item__title')
        
        # Print the titles
        for title in titles:
            print(title.text)
            
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 's-item__price'))
        )

        # Find all prices of the search results
        prices = driver.find_elements(By.CLASS_NAME, 's-item__price')

        # Print the prices
        for price in prices:
            print(price.text)

        # Try to find the "Next" button and click it
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.pagination__next'))
            )
            next_button.click()
        except TimeoutException:
            print("No more pages to load.")
            break

except TimeoutException:
    print("Timed out waiting for an element to load.")
except NoSuchElementException:
    print("Element not found.")
finally:
    # Close the driver
    driver.quit()
 

