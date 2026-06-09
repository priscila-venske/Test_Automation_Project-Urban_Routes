import time

from selenium.webdriver.common.devtools.v129 import page

import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)



# 1.Definir o endereço:
    def test_set_route(self):

        assert self.page.get_from_location_value() == data.ADDRESS_FROM
        assert self.page.get_to_location_value() == data.ADDRESS_TO



# 2.Selecionar o plano Comfort
    def test_select_plan(self):
        self.page.open_comfort_flow()

        assert self.page.is_comfort_selected()



# 3.Preencher o número de telefone
    def test_fill_phone_number(self):
        self.page.open_comfort_flow()
        self.page.fill_phone_flow(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.page.fill_code(code)
        self.page.confirm_code()

        assert self.page.is_phone_confirmed()


# 4.Adicionar um cartão de crédito
    def test_fill_card(self):
        self.page.open_comfort_flow()
        self.page.complete_payment_flow(data.CARD_NUMBER,data.CARD_CODE)

        assert self.page.is_card_added()


# 5.Escrever um comentário para o motorista;
    def test_comment_for_driver(self):
        self.page.open_comfort_flow()
        self.page.add_comment(data.MESSAGE_FOR_DRIVER)

        assert self.page.is_comment_added(data.MESSAGE_FOR_DRIVER)


# 6.Pedir um cobertor e lenços
    def test_order_toggle_blanket_and_tissues(self):
        self.page.open_comfort_flow()
        self.page.toggle_blanket_and_tissues()

        assert self.page.is_blanket_selected()



# 7.Pedir 2 sorvetes;
    def test_order_2_ice_creams(self):
        self.page.open_comfort_flow()
        self.page.add_ice_cream(2)

        assert self.page.get_ice_cream_count() == 2



# 8.Pedir um táxi com a tarifa "Comfort".
    def test_car_search_model_appears(self):
        self.page.open_comfort_flow()
        self.page.fill_phone_flow(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.page.fill_code(code)
        self.page.confirm_code()
        time.sleep(1)
        self.page.complete_payment_flow(data.CARD_NUMBER,data.CARD_CODE)
        self.page.add_comment(data.MESSAGE_FOR_DRIVER)
        self.page.add_ice_cream(2)
        self.page.toggle_blanket_and_tissues()
        self.page.click_order_button()

        assert self.page.is_search_car_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
