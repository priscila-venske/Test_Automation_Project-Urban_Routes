import time
import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def _start_comfort_flow(self):
        self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_order_taxi_button()
        self.page.select_comfort()

    def test_set_route(self):
        self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO
        print("Teste de rota: Endereços validados com sucesso.")

    def test_select_plan(self):
        self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_order_taxi_button()
        self.page.select_comfort()
        assert self.page.is_comfort_selected() == True

    def test_fill_phone_number(self):
        self._start_comfort_flow()
        self.page.set_phone(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.page.set_code(code)

    def test_fill_card(self):
        self._start_comfort_flow()
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        self._start_comfort_flow()
        self.page.add_comment(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self._start_comfort_flow()
        self.page.select_extras()

    def test_order_2_ice_creams(self):
        self._start_comfort_flow()
        number_of_ice_creams = 2
        self.page.add_ice_cream(number_of_ice_creams)

    def test_car_search_model_appears(self):
        self._start_comfort_flow()
        self.page.order_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()