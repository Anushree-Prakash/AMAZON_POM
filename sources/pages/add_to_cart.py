'''
@author : anushree
@email : anu@gmail.com
@date : 18/12/2019
'''

from sources.generic_utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cl
import logging
from sources.pages.home_page_search_product import HomePageSearchProduct

class AddToCart(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)
    __add_to_cart_button = "add-to-cart-button"

    # def __add_to_cart(self):
    #     return self.getElement("add-to-cart-button",locatorType="id")

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver(driver) using super() -->parameterized constructor
        super().__init__(driver)
        self.driver = driver
        HomePageSearchProduct(driver)

    def click_on_add_to_cart(self):
        self.switch_to_child_window(self.driver)
        self.elementClick(self.__add_to_cart_button)
        self.timeSleep()




