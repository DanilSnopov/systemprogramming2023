from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import lxml
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.binary_location = '/usr/bin/firefox'
driver = webdriver.Firefox(options=options)

driver.get("https://www.invokergame.com/")
driver.find_element(By.XPATH, '//*[@value="SURVIVAL"]').click()
driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div/table/tbody/tr/td[3]/a').click()
driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[1]/nobr/table/tbody/tr/td/input').click()
q = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[2]/div[1]')
w = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[2]/div[2]')
e = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[2]/div[3]')
r = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[2]/div[6]')
c = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[6]/div[2]/div[3]/div[2]/div[4]')
combinations = [[q, q, q], [q, q, w], [q, q, e], [w, w, w], [w, w, q], [w, w, e], [e, e, e], [e, e, q], [e, e, w], [q, w, e]]
while True:
    page = driver.page_source
    container = BeautifulSoup(page, 'lxml').find('tr', class_='speechboxTR')
    ids = [int(spell['id'][6:]) for spell in container.find_all('td', class_="ActiveSpell")]
    for id in ids:
        for press in combinations[id]:
            press.click()
        r.click()
        c.click()

#178
#194
#180
#197
#191
#197