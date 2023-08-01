
from generic.utilities import Utils
from selenium.webdriver.common.by import By

from generic.base_class import BaseClass


class SearchFlightsResults(BaseClass):
    log=Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    # locators
    filter_by_non_stop = (By.XPATH, "//p[text()='0']")
    filter_by_one_stop = (By.XPATH, "//p[text()='1']")
    filter_by_two_stop = (By.XPATH, "//p[text()='2']")
    search_flight_results = (By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)')]")

    def get_flights_by_one_stop(self):
        return self.driver.find_element(*self.filter_by_one_stop)

    def get_flights_by_two_stop(self):
        return self.driver.find_element(*self.filter_by_two_stop)

    def get_flights_by_non_stop(self):
        return self.driver.find_element(*self.filter_by_non_stop)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(*self.search_flight_results)

    def filter_flights_by_stop(self, bystop):
        if bystop == '1 Stop':
            self.get_flights_by_one_stop().click()
            self.log.info("Selected flights with 1 stop")
        elif bystop == '2 Stop(s)':
            self.get_flights_by_two_stop().click()
            self.log.info("Selected flights with 2 stop")
        elif bystop == 'Non Stop':
            self.get_flights_by_non_stop().click()
            self.log.info("Selected flights with non stop")
        else:
            self.log.info("Please provide valid filter option")
