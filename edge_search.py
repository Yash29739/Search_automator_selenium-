from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, os, random

words = [
    "python", "selenium", "automation", "edge browser", "chatgpt",
    "openai", "virtual environment", "git", "docker", "github",
    "AI", "machine learning", "deep learning", "cloud", "database",
    "javascript", "flutter", "firebase", "blockchain", "ganache",
    "react", "tailwind", "linux", "windows", "kubernetes", "nginx",
    "fastapi", "django", "flask", "data science"
]

driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
driver = webdriver.Edge(service=Service(driver_path))
driver.get("https://www.bing.com")

actions = ActionChains(driver)

try:

    search_box = driver.find_element(By.NAME, 'q')
    # search_button = driver.find_element(By.ID, 'search_icon')
    driver.implicitly_wait(10)

    actions.move_to_element(search_box).click().send_keys("Start the search").perform()
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        
        for i in range(20):
            word = random.choice(words) 
            
            search_box = driver.find_element(By.NAME, 'q')
            # search_button = driver.find_element(By.ID, 'sb_search')

            search_box.clear()
            search_box.send_keys(word)
            time.sleep(2)

            search_box.send_keys(Keys.RETURN);
            # search_button.click()
            time.sleep(4)
            print(f"Completed the serch for '{word}' with count {i+1}")
    except Exception as e:
        print("Error occured in the search of '{word}' with count {i+1} \n\n Error: {e}");
except  KeyboardInterrupt :
    print(f"ctrl+c ha been clicked, closing.... ")   
except Exception as e :
    print(f"Fatal errr: {e}")   
finally:
    print("Finally closing the browser....") 
    driver.quit()