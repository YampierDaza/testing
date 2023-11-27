import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PruebasInicioSesion():
    def configuracion_inicial(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def limpieza_final(self):
        self.driver.quit()

    def inicio_sesion(self, usuario, contrasena):
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.ID, "loginForm_email").send_keys(usuario)
        self.driver.find_element(By.ID, "loginForm_password").send_keys(contrasena)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()

    def prueba_inicio_sesion_exitoso(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.inicio_sesion("usuario@usuario.com", "12345678")
        # Agregar aserciones para inicio de sesión exitoso

    def prueba_inicio_sesion_campos_vacios(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()
        mensaje_error_email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm_email_help > .ant-form-item-explain-error"))
        )
        # Agregar aserciones para mensaje de error por campos vacíos

        mensaje_error_contrasena = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm_password_help > .ant-form-item-explain-error"))
        )
        # Agregar aserciones para mensaje de error por contraseña vacía

    @pytest.mark.parametrize("usuario, contrasena", [
        ("usuario_invalido@example.com", "contraseña_invalida"),
        ("prueba@outlook.com", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'"),
        ("random_user@gmail.com", "invalid_password")
    ])
    def prueba_inicio_sesion_credenciales_invalidas(self, usuario, contrasena):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.inicio_sesion(usuario, contrasena)

        notificacion_error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))
        )
        assert "Error en autenticación" in notificacion_error.text

    def prueba_correo(self):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)
        self.inicio_sesion("qwerty", "password")

        # Presionar Enter para enviar el formulario
        self.driver.find_element(By.ID, "loginForm_password").send_keys(Keys.ENTER)

        # Hacer clic en el botón (posiblemente de confirmación)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn > span").click()

        # Realizar acciones adicionales (doble clic, etc.) si es necesario
        elemento_error = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
        acciones = ActionChains(self.driver)
        acciones.double_click(elemento_error).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error").click()
