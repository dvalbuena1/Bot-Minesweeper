from selenium import webdriver
from time import sleep

class BuscaMinasBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://buscaminas.eu/")
        sleep(2)
BuscaMinasBot()