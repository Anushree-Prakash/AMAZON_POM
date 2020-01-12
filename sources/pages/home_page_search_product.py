'''
@author : anushree
@email : anu@gmail.com
@date : 18/12/2019
'''

import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from sources.generic_utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cl
import logging

class HomePageSearchProduct(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver(driver) using super() -->parameterized constructor
        super().__init__(driver)
        self.driver = driver
        self.search_Product_Name="twotabsearchtextbox"

    def SearchBox(self,productName):
        # using self keyword we can access the methods in generic_methods
        self.sendKeys(productName,self.search_Product_Name)
        # self.elementClick("//span[@id='nav-search-submit-text']/../input",locatorType='xpath')
        self.elementClick("//input[@value='Go']", "xpath")
        time.sleep(3)

    def click_on_product(self):
        # self.switch_to_child_window(self.driver)
        self.elementClick("(//span[text()='Apple iPhone XR (64GB) - Black'])[2]","xpath")
        self.timeSleep()

