from selenium import webdriver
from time import sleep
import random

class BuscaMinasBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        self.driver.get("http://minesweeperonline.com/")
        sleep(2)
        i = 1
        j = 1
        while True:
            try:
                self.driver.find_element_by_id(str(i) + '_' + str(j))
                i += 1
            except:
                break

        while True:
            try:
                self.driver.find_element_by_id(str(i-1) + '_' + str(j))
                j += 1
            except:
                break

        i = random.randint(1,i-1)
        j = random.randint(1,j-1)
        self.driver.find_element_by_id(str(i) + '_' + str(j)).click()
        sleep(1)

        ## Case 1
        list = self.driver.find_elements_by_class_name('square.open1')
        for element in list:
            id = element.get_attribute('id')
            coordinates = id.split("_")
            name1 = self.driver.find_element_by_id(str(int(coordinates[0]) - 1) + "_" + coordinates[1]).get_attribute(
                'class')
            name2 = self.driver.find_element_by_id(coordinates[0] + "_" + str(int(coordinates[1]) + 1)).get_attribute(
                'class')

            if name1 == "square blank" and name2 == "square blank":
                self.driver.find_element_by_id(str(int(coordinates[0]) - 1) + "_" + str(int(coordinates[1])+1))\
                    .click()
        sleep(2)

BuscaMinasBot()