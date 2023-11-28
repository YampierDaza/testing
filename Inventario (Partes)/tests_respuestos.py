import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestRepuestos:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(945, 1060)

    def teardown_method(self, method):
        self.driver.quit()

    def login_exitoso(self):
        self.driver.find_element(By.CSS_SELECTOR, "header").click()
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.ID, "loginForm_email").send_keys("usuario@usuario.com")
        self.driver.find_element(By.ID, "loginForm_password").send_keys("12345678")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn > span").click()

    def test_registro_exitoso(self):
        # Iniciar sesión
        self.login_exitoso()

        # Esperar a que el menú esté presente
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-menu-submenu-title"))
        ).click()

        # Esperar a que el submenú esté presente y hacer clic
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-menu-submenu-title > .ant-menu-title-content"))
        ).click()

        # Esperar a que el siguiente elemento esté presente y hacer clic
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-menu-item-active > .ant-menu-title-content"))
        ).click()

        # Esperar a que el botón esté presente y sea cliclable
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn > span:nth-child(2)"))
        ).click()

        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Filtro de aire")
        self.driver.find_element(By.ID, "code").click()
        self.driver.find_element(By.ID, "code").send_keys("FA12345")
        self.driver.find_element(By.ID, "quantity").send_keys("50")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "price").click()
        self.driver.find_element(By.ID, "price").send_keys("58000")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Filtro de aire de alta calidad para mejorar el rendimiento del motor y reducir el consumo de combustible.")
        ##self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-default > span:nth-child(2)").click()

        # Usar la ruta absoluta proporcionada
        directorio_actual = os.path.dirname(os.path.realpath(__file__))

        # Construye la ruta relativa al archivo deseado
        nombre_archivo = "filtro de aire.png"
        ruta_relativa = os.path.join(directorio_actual, nombre_archivo)

        self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(ruta_relativa)

        ##self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-default > span:nth-child(2)").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()

        #se queda esperando a que aparezca la notificacion
        notification_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))
        ).text

        #verifica el mensaje es "Operacion exitosa"
        assert notification_message == "Operacion exitosa", f"El mensaje actual es: {notification_message}"

if __name__ == "__main__":
    pytest.main()