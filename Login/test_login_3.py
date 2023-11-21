from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.ID, "loginForm_email").click()
        self.driver.find_element(By.ID, "loginForm_email").send_keys("usuario@usuario.com")
        self.driver.find_element(By.ID, "loginForm_password").send_keys("12345678")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

    def test_login2(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()

        # Ingresa al formulario sin completar campos
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

        # Espera a que aparezca el mensaje de error en el campo de correo electrónico
        email_error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm_email_help > .ant-form-item-explain-error"))
        )

        # Verifica que el mensaje de error contiene el texto esperado
        assert "Por favor ingresa tu correo electrónico" in email_error_message.text

        # Espera a que aparezca el mensaje de error en el campo de contraseña
        password_error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm_password_help > .ant-form-item-explain-error"))
        )

        # Verifica que el mensaje de error contiene el texto esperado
        assert "Por favor ingresa tu contraseña" in password_error_message.text
