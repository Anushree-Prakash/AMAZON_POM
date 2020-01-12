from sources.pages.home_page_search_product import HomePageSearchProduct as searchProd
from sources.pages.add_to_cart import AddToCart
from sources.generic_utilities.webdriver_factory import WebDriverFactory
# Searching the product in search box
class Amazon(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver

    def searchProduct(self,name):
        searchProd(self.driver).SearchBox(name)

        searchProd(self.driver).click_on_product()
        AddToCart(self.driver).click_on_add_to_cart()

    # def add_to_cart(self):
    #     AddToCart







