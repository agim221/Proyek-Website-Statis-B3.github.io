from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://rateyourmusic.com/charts/top/album/all-time/")
time.sleep(5)

now =datetime.now()
music_list = []
i = 1

while i <= 80:
    for music in driver.find_elements(By.CLASS_NAME, "page_section_charts_item_wrapper"):
        driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(0.8)
        for img in music.find_elements(By.TAG_NAME, "img"):
            
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            
            music_list.append(
                {"No": i ,
                 "Judul":music.text.split("\n")[0],
                 "Penyanyi": music.text.split("\n")[1],
                 "Rating": music.text.split("\n")[2],
                 "Genre": music.text.split("\n")[6].split()[0],
                 "Tanggal_Rilis": music.text.split("\n")[5],
                 "Img": img.get_attribute("src"), 
                 "waktu_scraping": now.strftime("%Y-%m-%d %H:%M:%S")
                 }
                )
            i = i + 1
            
            break
    try:
        pagination_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ui_pagination_page_charts_navigation_bottom"]/a'))
        )
        pagination_btn.click()

        time.sleep(5)
    except NoSuchElementException as e:
        break
    
hasil_scraping = open("hasilscraping.json", "w")
json.dump(music_list, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()
