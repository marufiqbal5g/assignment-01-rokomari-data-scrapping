from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://www.rokomari.com/book/authors?ref=sm_p0')

driver.maximize_window()

writter_name_list = []

for page in range(1,61):
    driver.get(f'https://www.rokomari.com/book/authors?ref=sm_p0&page={page}')
    for i in range(1,49):
        j = str(i)
        w_name = driver.find_element(By.XPATH,'//*[@id="author-list"]/div[3]/section/div[2]/div['+j+']/a/h2').text 
        writter_name_list.append(w_name)



print(writter_name_list)
print('Total Lengts of the writter names:',len(writter_name_list))

file='C:\\D DRIVE\\ML_WITH_NLP_B_7\\ASSIGNMENT-01_DATA_SCRAPPING\\writters_name.txt'

with open(file, 'w', encoding="utf-8") as f:
    for item in writter_name_list:
        f.write(f"{item}\n")