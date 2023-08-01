import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generic.base_class import BaseClass
from generic.utilities import Utils
from pages.search_flights_result_page import SearchFlightsResults


class LaunchPage(BaseClass):
    log = Utils.custom_logger()
    def __init__(self, driver):
        self.driver = driver

    # locators
    dept_from = (By.XPATH, "//input[@id='BE_flight_origin_city']")
    all_elements1 = (By.XPATH, "//input[@id='BE_flight_origin_city']")
    search_results = (By.XPATH, "//div[@class='viewport']//li")
    going_to = (By.XPATH, "//input[@id='BE_flight_arrival_city']")
    all_elements2 = (By.XPATH, "//input[@id='BE_flight_arrival_city']")
    select_date_filed = (By.XPATH, "//input[@id='BE_flight_origin_date']")
    all_dates = (By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
    search_button = (By.XPATH, "//input[@value='Search Flights']")

    def get_dept_from_field(self):
        return self.wait_until_element_is_clickable(*self.dept_from)

    def enter_dept_from_location(self, departlocation):
        self.get_dept_from_field().click()
        self.get_dept_from_field().send_keys(departlocation)
        self.wait_for_presence_of_all_elements(*self.all_elements1)
        search_results = self.driver.find_elements(*self.search_results)
        for result in search_results:
            self.log.info(result.text)
            if departlocation in result.text:
                result.click()
                break
        self.get_dept_from_field().send_keys(Keys.ENTER)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(*self.going_to)

    def enter_going_to_location(self, goingtolocation):
        self.get_going_to_field().click()
        self.get_going_to_field().send_keys(goingtolocation)
        self.wait_for_presence_of_all_elements(*self.all_elements2)
        search_results = self.driver.find_elements(*self.search_results)
        for result in search_results:
            self.log.info(result.text)
            if goingtolocation in result.text:
                result.click()
                break


    def get_dept_date_field(self):
        return self.wait_until_element_is_clickable(*self.select_date_filed)

    def enter_dept_date(self, deptdate):
        self.get_dept_date_field().click()
        self.wait_until_element_is_clickable(*self.all_dates)
        all_dates = self.wait_until_element_is_clickable(*self.all_dates).find_elements(*self.all_dates)
        for date in all_dates:
            if date.get_attribute("data-date") == deptdate:
                date.click()
                break

    def click_on_search(self):
        self.driver.find_element(*self.search_button).click()

    def search_flights(self, departlocation, goingtolocation, deptdate):
        self.enter_dept_from_location(departlocation)
        self.enter_going_to_location(goingtolocation)
        self.enter_dept_date(deptdate)
        self.click_on_search()
        search_flights = SearchFlightsResults(self.driver)
        return search_flights
