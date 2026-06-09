import time
import data
import helpers
from selenium import webdriver
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # Locators
    from_locator = (By.ID, 'from')  # From
    to_locator = (By.ID, 'to')  # To

    open_route = (By.XPATH, "//div[contains(@class,'type-picker')]")

    personal_option_locator = (By.XPATH, '//div[text()="Personal"]')
    icon_taxi_locator = (By.XPATH, "//img[contains(@src, 'taxi')]")
    call_taxi_button = (By.XPATH, "//button[@class='button round' and contains(text(),'Chamar um táxi')]")
    comfort_mode = (By.XPATH, "//img[contains(@src, 'kids')]")

    number_locator = (By.XPATH, "//div[text()='Número de telefone']")
    phone_input = (By.ID,'phone')
    code_phone_input = (By.ID,'code')
    submit_phone = (By.XPATH, "//button[@type='submit' and text()='Próximo']")
    confirm_phone_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")

    payment_button = (By.XPATH, "//div[contains(@class,'pp-text') and contains(.,'Método de pagamento')]")
    add_card_button = (By.XPATH, "//div[contains(@class,'pp-plus-container')]")
    card_number = (By.XPATH, "//input[@placeholder='1234 0000 4321']")
    card_code = (By.XPATH, "//input[@placeholder='12']")
    add_button = (By.XPATH, "//button[text()='Adicionar']")
    outside_area = (By.CSS_SELECTOR, "body")
    close_flow_card_button = (By.CSS_SELECTOR, ".payment-picker .section.active button.close-button.section-close")


    comment_input = (By.ID, "comment")

    blanket_toggle = (By.CSS_SELECTOR, "div.switch")

    order_ice_cream = (By.XPATH, "//div[@class='counter-plus']")
    counter_value = (By.XPATH, "//div[@class='counter-value']")


# essencials actions

    def _find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def _click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def _type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def _wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))





#1


    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_locator))
        self.driver.find_element(*self.from_locator).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_locator))
        self.driver.find_element(*self.to_locator).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_locator)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_locator)
        ).get_attribute('value')

    def get_from_locator(self):
        return self.get_value(self.from_locator)

    def get_to_locator(self):
        return self.get_value(self.to_locator)

#2

    def select_personal_mode(self):
        self.driver.find_element(*self.personal_option_locator).click()

    def select_taxi_icon(self):
        self.driver.find_element(*self.icon_taxi_locator).click()

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_method(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_mode)).click()

    def is_comfort_selected(self):
        element = self.driver.find_element(*self.comfort_mode)
        return element.get_attribute("alt") == "Comfort"

    def is_comfort_active(self):
        element = self.wait.until(EC.presence_of_element_located(self.comfort_mode))
        classes = element.get_attribute("class") or ""
        return "active" in classes

    def select_comfort(self):
        element = self._wait(self.comfort_mode)



#3

    def fill_phone_number_complete(page, driver):
        self.fill_phone_flow(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.fill_code(code)
        self.confirm_code()

        return page.is_phone_confirmed()

    def fill_phone_flow(self, phone):
        self._click(self.number_locator)
        self._type(self.phone_input, phone)
        self._click(self.submit_phone)


    def fill_code(self, code):
        self._type(self.code_phone_input, code)

    def is_phone_confirmed(self):
        return len(self.driver.find_elements(*self.confirm_phone_button)) > 0

    def confirm_code(self):
        self._click(self.confirm_phone_button)

#4
    def click_payment_method(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.payment_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_add_card(self):
        self._click(self.add_card_button)

    def fill_card_number_and_code(self, number, code):
        self._type(self.card_number, number)
        self._type(self.card_code, code)

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def click_outside_area(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.outside_area)
    ).click()

    def flow_card_fished(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.close_flow_card_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def is_card_added(self):
        return WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Cartão')]"))
        )

#5
    def add_comment(self, text):
        self._type(self.comment_input, text)

    def is_comment_added(self, expected_text):
        element = self.driver.find_element(By.ID, "comment")
        value = element.get_attribute("value")
        return value == expected_text

#6
    def toggle_blanket_and_tissues(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.switch"))
        )

        self.driver.execute_script("arguments[0].click();", element)

    def is_blanket_selected(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input.switch-input")
        return element.is_selected()


#7
    def add_ice_cream(self, quantity):
        for count in range(quantity):
            self._click(self.order_ice_cream)
            time.sleep(1)

    def get_ice_cream_count(self):
        element = self.driver.find_element(*self.counter_value)
        return int(element.text)



#8
    def open_comfort_flow(self):
        self._click(self.personal_option_locator)
        self._click(self.icon_taxi_locator)
        self._click(self.call_taxi_button)
        self._click(self.comfort_mode)


    def complete_phone_flow(self, phone):
        self._click(self.phone_input)
        self._type(self.phone_input, phone)
        self._click(self.submit_phone)

        code = helpers.retrieve_phone_code(self.driver)
        self._type(self.code_phone_input, code)
        self._click(self.confirm_phone_button)


    def complete_payment_flow(self, number, code):
        self.click_payment_method()
        self.click_add_card()
        self.fill_card_number_and_code(data.CARD_NUMBER, data.CARD_CODE)
        self.click_outside_area()
        self.click_add_button()
        time.sleep(2)
        self.flow_card_fished()




    def complete_order_flow(self, phone, card_number, card_code, comment):
        self.complete_phone_flow(phone)
        self.add_comment(comment)
        self.add_ice_creams(2)
        self.toggle_blanket()
        self.complete_payment_flow(card_number, card_code)
        time.sleep(3)


    def click_order_button(self):
        self.driver.find_element(
            By.XPATH,
            "//button[.//span[text()='Pedir']]"
        ).click()

    def is_search_car_visible(self):
        return self.driver.find_element(
            By.XPATH,
            "//div[@class='order-header-title']"
        ).is_displayed()
