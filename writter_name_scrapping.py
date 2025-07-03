from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# driver.get('https://www.rokomari.com/book/authors?ref=sm_p0')
driver.get('https://www.rokomari.com/book/')

driver.maximize_window()

time.sleep(3)

pop_up=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/button')
time.sleep(2)
pop_up.click()
time.sleep(3)

writter_subcatagory=driver.find_element(By.XPATH,'//*[@id="js--authors"]')
action=ActionChains(driver)
action.move_to_element(writter_subcatagory).click().perform()
time.sleep(5)

writter_name_list = []

for page in range(1,3):
    driver.get(f'https://www.rokomari.com/book/authors?ref=sm_p0&page={page}')
    for i in range(1,49):
        j = str(i)
        w_name = driver.find_element(By.XPATH,'//*[@id="author-list"]/div[3]/section/div[2]/div['+j+']/a/h2').text 
        writter_name_list.append(w_name)



print(writter_name_list)
print('Total Lengts of the writter names:',len(writter_name_list))



# # Save writters name in txt file
# file='C:\\D DRIVE\\ML_WITH_NLP_B_7\\ASSIGNMENT-01_DATA_SCRAPPING\\writters_name.txt'

# with open(file, 'w', encoding="utf-8") as f:
#     for item in writter_name_list:
#         f.write(f"{item}\n")



# Save writters name in excel file
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

# my_list = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

for index, item in enumerate(writter_name_list):
    ws.cell(row=index + 1, column=1, value=item)

wb.save("C:\\D DRIVE\\ML_WITH_NLP_B_7\\ASSIGNMENT-01_DATA_SCRAPPING\\Writters_Name.xlsx")
