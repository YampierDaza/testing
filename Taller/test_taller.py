import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCrearOrdenTrabajo:
    def __init__(self):
        # Configuración inicial del navegador
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(945, 1060)

    def cerrar_navegador(self):
        # Cerrar el navegador al finalizar las pruebas
        self.driver.quit()

    def iniciar_sesion(self):
        # Método para realizar el inicio de sesión
        self.driver.find_element(By.CSS_SELECTOR, "header").click()
        self.driver.find_element(By.CSS_SELECTOR, "a > button").click()
        self.driver.find_element(By.ID, "loginForm_email").send_keys("usuario@usuario.com")
        self.driver.find_element(By.ID, "loginForm_password").send_keys("12345678")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn > span").click()

    def test_creacion_orden_trabajo_exitosa(self):
        # Iniciar sesión
        self.iniciar_sesion()

        # Esperar a que el menú esté presente y hacer clic
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

        # Rellenar el formulario de creación de orden de trabajo
        self.driver.find_element(By.ID, "vehicle").click()
        self.driver.find_element(By.ID, "vehicle").send_keys("Toyota Camry")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Reparación del sistema de frenos")
        self.driver.find_element(By.ID, "mechanic").click()
        self.driver.find_element(By.ID, "mechanic").send_keys("Juan Mecánico")

        # Enviar el formulario
        time.sleep(3)  # Esperar un tiempo para asegurar que se complete
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()

        # Esperar a que aparezca la notificación
        notification_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))
        ).text

        # Verificar que el mensaje sea "Operación exitosa"
        assert notification_message == "Operación exitosa", f"El mensaje actual es: {notification_message}"

# Crear una instancia de la clase y ejecutar las pruebas
pruebas_orden_trabajo = TestCrearOrdenTrabajo()
pruebas_orden_trabajo.test_creacion_orden_trabajo_exitosa()
pruebas_orden_trabajo.cerrar_navegador()
