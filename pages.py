from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    # LOCALIZADORES
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    COMFORT_TARIF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Comfort']]")
    ORDER_TAXI_MAIN_BUTTON = (By.CSS_SELECTOR, "button.button.round")
    PHONE_INPUT = (By.ID, "phone")
    PHONE_BUTTON = (By.CLASS_NAME, "np-button")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Próximo')]")
    CODE_INPUT = (By.ID, "code")
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-text")
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, '.pp-plus-container')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, '//input[@id="code" and contains(@class,"card-input")]')
    LINK_CARD_BUTTON = (By.XPATH, '//button[text()="Link" or text()="Adicionar"]')
    COMMENT_INPUT = (By.ID, "comment")
    BLANKET_CHECKBOX = (By.XPATH, "//*[contains(@class, 'switch')]")
    ICE_CREAM_BUTTON = (By.XPATH, '//div[text()="Sorvete" or text()="Ice cream"]/..//div[@class="counter-plus"]')
    ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')

    def __init__(self, driver):
        self.driver = driver

    # MÉTODOS
    def set_route(self, from_text, to_text):
        self.driver.find_element(*self.FROM_INPUT).send_keys(from_text)
        self.driver.find_element(*self.TO_INPUT).send_keys(to_text + Keys.ENTER)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_INPUT).get_property('value')

    def get_to_location(self):
        return self.driver.find_element(*self.TO_INPUT).get_property('value')

    def click_order_taxi_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ORDER_TAXI_MAIN_BUTTON)
        )
        element.click()

    def select_comfort(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMFORT_TARIF)
        )
        element.click()

    def is_comfort_selected(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMFORT_TARIF)
        )
        classes = element.get_attribute("class")
        print(f"DEBUG: Classes do CARD selecionado: {classes}")
        return "active" in classes

    def set_phone(self, phone):
        self.driver.find_element(By.CLASS_NAME, "np-text").click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        element.click()

    def set_code(self, code):
        self.driver.find_element(*self.CODE_INPUT).send_keys(code)

    def add_card(self, number, cvv):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, '.pp-plus-container').click()
        card_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CARD_NUMBER_INPUT)
        )
        card_field.send_keys(number)

        cvv_field = self.driver.find_element(*self.CARD_CODE_INPUT)
        cvv_field.send_keys(cvv)
        cvv_field.send_keys(Keys.TAB)
        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_CARD_BUTTON)
        )
        confirm_btn.click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

    def add_comment(self, text):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(text)

    def select_extras(self):
        self.driver.find_element(*self.BLANKET_CHECKBOX).click()

    def add_ice_cream(self, quantity):
        plus_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ICE_CREAM_BUTTON)
        )
        for _ in range(quantity):
            plus_button.click()

    def order_taxi(self):
        # 1. Espera o botão existir no HTML
        order_btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", order_btn)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        )

        order_btn.click()