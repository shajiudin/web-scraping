from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Set up the webdriver
driver = webdriver.Chrome()

try:
    # Open the Daraz website
    driver.get('https://www.daraz.pk/#?')

    # Wait for the search box to be available and enter the search query
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-box__input--O34g'))
    )
    search_box.send_keys("iphone 14 cover" + Keys.ENTER)

    # Wait for the search results to load and display the titles
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RfADt'))
    )

    # Find all titles and click the first one
    titles = driver.find_elements(By.CLASS_NAME, 'RfADt')

    if titles:
        titles[0].click()

    # Wait for the "Add to Cart" button to be available and click it
    add_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-to-cart-buy-now-btn.pdp-button.pdp-button_type_text.pdp-button_theme_orange.pdp-button_size_xl'))
    )
    add_cart_button.click()

except TimeoutException:
    print("Element not found within the time limit.")
except NoSuchElementException:
    print("Element not found.")
finally:
    # Close the browser
    driver.quit()


