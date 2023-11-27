import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
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

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("usuario_invalido@example.com", "contraseña_invalida"),
    ("prueba@outlook.com", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'"),
    ("random_user@gmail.com", "invalid_password")
])



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("prueba@outlook.com", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'"),
    ("random_user@gmail.com", "invalid_password")
])
def test_login_with_invalid_credentials(driver, username, password):
    driver.get("https://www.auto-haus.link/")
    driver.set_window_size(1376, 1080)

    # Realiza un intento de inicio de sesión con credenciales no válidas
    driver.find_element(By.CSS_SELECTOR, "a > button").click()
    driver.find_element(By.ID, "loginForm_email").send_keys(username)
    driver.find_element(By.ID, "loginForm_password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

    # Espera a que aparezca la notificación de error
    error_notification = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))
    )

    # Verifica que la notificación de error contiene el texto esperado
    assert "Error en autenticación" in error_notification.text

def test_login4(self):
    # Navegar a la página de inicio
    self.driver.get("https://www.auto-haus.link/")
    self.driver.set_window_size(1376, 1080)

    # Hacer clic en el botón para iniciar sesión
    self.driver.find_element(By.CSS_SELECTOR, "a > button").click()

    # Ingresar el nombre de usuario y contraseña
    self.driver.find_element(By.ID, "loginForm_email").click()
    self.driver.find_element(By.ID, "loginForm_email").send_keys("qwerty")
    self.driver.find_element(By.ID, "loginForm_password").send_keys("password")

    # Presionar Enter para enviar el formulario
    self.driver.find_element(By.ID, "loginForm_password").send_keys(Keys.ENTER)

    # Hacer clic en el botón (posiblemente de confirmación)
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn > span").click()

    # Realizar acciones adicionales (doble clic, etc.) si es necesario
    element = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error").click()
