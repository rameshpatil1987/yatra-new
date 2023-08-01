import time

from ddt import data, ddt, unpack
import pytest
from pages.yatra_launch_page import LaunchPage
import softest
from generic.utilities import Utils


@pytest.mark.usefixtures("setup", "log_on_failure")
# @ddt
class TestSearchFlights(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # @data(*Utils.read_data_from_excel("../data/input.xlsx", "Sheet1"))
    # @unpack
    def test_search_flights_one_stop(self):
        search_flight_result = self.lp.search_flights("New","Mum","15/08/2023")
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop("1 Stop")
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.ut.assertlistitemtext(all_stops, "1 Stop")

