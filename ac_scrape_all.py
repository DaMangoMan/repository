from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the webpage
driver.get("https://my.americorps.gov/mp/listing/publicRequestSearch.do")

# Find the submit button and click it
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr[8]/td/img")))
submit_button.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='2']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='3']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='4']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='5']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='6']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='7']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='8']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='9']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='10']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='11']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='12']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='13']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='14']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='15']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='16']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='17']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='18']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='19']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='20']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='21']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='22']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='23']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='24']")

# Click on the link
link.click()

try:
    # Wait for the page to load and find the link by XPath 1/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 2/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 3/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 4/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 5/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 6/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[9]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 7/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[10]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 8/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[11]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 9/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[12]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

try:
    # Wait for the page to load and find the link by XPath 10/10
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/table[2]/tbody/tr[13]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img")))
    
    # Click on the link
    link.click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the HTML source of the current page
    page_source = driver.page_source
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific section using the provided CSS selector
    target_section = soup.select('body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(4) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3)')
    
    # Check if the target section exists and if 'housing' is found within it
    if target_section:
        # Extract the text content of the section
        section_text = target_section[0].get_text()

        # Search for the keyword 'housing' within the section
        if 'housing' in section_text.lower():
            # Output the current webpage's URL
            print("Page URL:", driver.current_url)

    # Click the 'back' button in the web browser to go to the previous page
    driver.back()
except TimeoutException:
    pass

# Next page 2
link = driver.find_element(By.XPATH, "//a[@title='25']")

# Click on the link
link.click()