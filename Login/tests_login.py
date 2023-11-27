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

    def test_exitoso(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.llena_formulario("usuario@usuario.com", "12345678")

    def test_campos_vacios(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)

        # Espera a que aparezca el botón para iniciar sesión
        login_button = self.espera_elemento("a > button")
        assert login_button.is_displayed() and login_button.is_enabled(), "El botón de iniciar sesión no está presente o no es clickeable"

        # Hace clic en el botón para iniciar sesión
        login_button.click()

        # Ingresa al formulario sin completar campos
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

        # Espera a que aparezca el mensaje de error en el campo de correo electrónico
        email_error_message = self.espera_elemento("#loginForm_email_help > .ant-form-item-explain-error")
        assert "Por favor ingresa tu correo electrónico" in email_error_message.text

        # Espera a que aparezca el mensaje de error en el campo de contraseña
        password_error_message = self.espera_elemento("#loginForm_password_help > .ant-form-item-explain-error")
        assert "Por favor ingresa tu contraseña" in password_error_message.text


    @pytest.mark.parametrize("username, password", [
        ("usuario_invalido@example.com", "contraseña_invalida"),
        ("prueba@outlook.com", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'"),
        ("random_user@gmail.com", "invalid_password")
    ])
    def test_credenciales_invalidas(self, username, password):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)

        # Realiza un intento de inicio de sesión con credenciales no válidas
        self.llena_formulario(username, password)

        # Espera a que aparezca la notificación de error
        error_notification = self.espera_elemento(".ant-notification-notice-message")
        assert "Error en autenticación" in error_notification.text

    def test_formato_correo(self):
        # Navegar a la página de inicio
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)

        # Utilizar la función llena_formulario
        self.llena_formulario("qwerty", "password")

        # Realizar acciones adicionales (doble clic, etc.) si es necesario
        element = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error").click()

    def llena_formulario(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.ID, "loginForm_email").click()
        self.driver.find_element(By.ID, "loginForm_email").send_keys(username)
        self.driver.find_element(By.ID, "loginForm_password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

    def espera_elemento(self, selector):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
