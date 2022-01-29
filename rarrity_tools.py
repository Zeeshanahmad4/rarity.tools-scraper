import eel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url=input("Enter Your URL:")
tokens=input("Enter No of Tokens:")
list = []
tokens = int(tokens)
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(url)
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//a[contains(@href,'https://opensea.io/assets') and @class='link']")))
button = driver.find_element(By.XPATH, "//div[contains(text(),'Next')]")

token_count = 0
flag = 0
# https://rarity.tools/cryptopunks
for i in range(209):

    if flag == 3:
        break
    else:
        crypto = driver.find_elements(
            By.XPATH, "//a[contains(@href,'https://opensea.io/assets') and @class='link']")
        for crypto1 in range(48):
            if token_count == tokens:
                flag = 3
                break
            else:
                list.append(crypto[crypto1].get_attribute('href')[0:77])
                token_count += 1
        button.click()

print(list)
with open('crypto.txt', 'w', newline="") as crypto_file:
    # csv_writer = writelines(crypto_file)

    for line in list:
         # csv_writer.writerow([line])
         crypto_file.write(line+"\n")
    crypto_file.close()

driver.close()
