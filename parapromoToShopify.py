import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from unidecode import unidecode


def get_filtered_product_name_from_csv(filename):
    products = [[], []]
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Skip empty rows
                row[0] = row[0].split('] ', 1)[-1]
                products[0].append(row[0])
                products[1].append(row[2])
    products[0].pop(0)
    products[1].pop(0)
    return products

def accept_cookie(driver):
    wait = WebDriverWait(driver, 50)
    try:
        cookie_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'didomi-continue-without-agreeing')))
        cookie_button.click()
#         ad_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'cross')))
#         print(ad_button)
#         ad_button.click()
    except NoSuchElementException:
        print("Element not found.")

def check_brand_match(driver, index):
    wait = WebDriverWait(driver, 50)
    product_brand = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fmd_div_nom_marque')))
    print(unidecode(product_brand.text.lower()),
    unidecode(products[1][index].lower()),
    unidecode(product_brand.text.lower()) == unidecode(products[1][index].lower()))
    return False

def retrieve_product_data(driver):
    wait = WebDriverWait(driver, 50)


def select_first_product(driver):
    wait = WebDriverWait(driver, 50)
    product = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'article')))
    product.click()

def start_search(driver, index):
    wait = WebDriverWait(driver, 50)
    try:
        searchbar = wait.until(EC.element_to_be_clickable((By.ID,'input_search')))
        searchbar.click()
        input_searchbar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'ais-SearchBox-input')))
        input_searchbar.send_keys(products[0][index])
        input_searchbar.send_keys(Keys.ENTER)
        if (check_brand_match(driver, index)):
            select_first_product(driver)
    except NoSuchElementException:
        print("Element not found.")

def search_product_cocooncenter(product):
    # Set the path to the chromedriver executable
    driver_service = Service(ChromeDriverManager().install())

    # Set the options for the Chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Maximize the browser window

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.set_page_load_timeout(30)

    # Open Cocooncenter website
    driver.get('https://www.cocooncenter.com/')
    accept_cookie(driver)
    for x in range(len(products[0])):
        start_search(driver, x)

    # ... Perform further actions on the website ...

    # Close the browser window
    driver.quit()


# Replace 'example.csv' with the actual filename of your CSV file
products = get_filtered_product_name_from_csv('Parapromo_DB.csv')
search_product_cocooncenter(products)
# print(products)
