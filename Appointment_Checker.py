import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

while True:
    driver = webdriver.Firefox()  # Initialize the Firefox driver

    try:
        # Step 1: Open the website
        driver.get('https://termine.staedteregion-aachen.de/auslaenderamt/')
        time.sleep(1)

        # Step 2: Set the window size
        driver.set_window_size(1400, 781)
        time.sleep(1)

        # Step 3: Click on the 'Accept Cookies' button if it appears
        try:
            cookies_button = driver.find_element(By.ID, 'cookie_msg_btn_yes')
            cookies_button.click()
            time.sleep(1)
        except:
            print("Cookie button not found, continuing...")
            pass  # If there's no cookie message or any issues, ignore and proceed

        # Step 4: Click on the element with id 'buttonfunktionseinheit-1'
        driver.find_element(By.ID, 'buttonfunktionseinheit-1').click()
        time.sleep(1)

        # Step 5: Click on the element with id 'header_concerns_accordion-117'
        driver.find_element(By.ID, 'header_concerns_accordion-117').click()
        time.sleep(1)

        # Step 6: Click on the glyphicon inside the element with id 'button-plus-193'
        driver.find_element(By.CSS_SELECTOR, '#button-plus-193 > .glyphicon').click()
        time.sleep(1)

        # Step 7: Click on the element with id 'WeiterButton'
        driver.find_element(By.ID, 'WeiterButton').click()
        time.sleep(1)

        # Step 8: Try to find and click the 'OKButton' if it exists
        try:
            ok_button = driver.find_element(By.ID, 'OKButton')
            ok_button.click()
            time.sleep(1)
        except:
            print("OKButton not found or not clickable")

        # Step 9 and subsequent steps: Perform additional actions such as scrolling
        driver.execute_script("window.scrollTo(0, 268)")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 518)")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, '.onehundred').click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 68)")
        time.sleep(1)

        # Final Step: Check if "Keine Zeiten verfügbar" is displayed on the page
        page_source = driver.page_source
        if "Keine Zeiten verfügbar" in page_source:
            print("No appointment")
        else:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Appointments may be available at {current_time}")
            # Make the Mac continuously say "Appointment available" until you stop the script
            while True:
                # Set the volume to maximum
                os.system("osascript -e 'set volume output volume 100'")
                # Make the announcement
                os.system('say "Appointment available"')
                time.sleep(10)  # Wait for 10 seconds



    finally:
        # Close the browser
        driver.quit()

    print("No appointments were available. Waiting for 10 minutes before trying again...")
    time.sleep(600)  # Wait for 10 minutes before running the script again
