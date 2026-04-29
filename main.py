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
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        self.page._enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO
        time.sleep(10)





    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para adicionar comentário para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para pedir coberta e lenços")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Adicionar em S8
            print("função criada para adicionar sorvetes")

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para verificar se o modelo do carro aparece na busca")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
