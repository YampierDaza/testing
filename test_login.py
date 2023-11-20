from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def realizar_prueba(usuario, contrasena):
    driver = webdriver.Chrome()
    driver.get("https://www.auto-haus.link")

    user = driver.find_element(By.ID, "loginForm_email")
    user.send_keys(usuario)

    password = driver.find_element(By.ID, "loginForm_password")
    password.send_keys(contrasena)
    password.submit()

    # Espera 2 segundos para dar tiempo a que se procese la acción
    time.sleep(2)
import pytest
import time
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
        # Prueba 1: Login o password vacíos
        self.realizar_prueba("", "")

        # Prueba 2: Login o password incorrecto
        self.realizar_prueba("123456789", "123456789")

        # Prueba 3: Login exitoso
        self.realizar_prueba("usuario@usuario.com", "12345678")

        # Prueba 4: Inyección de SQL
        self.realizar_prueba("prueba", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'")

    def realizar_prueba(self, usuario, contrasena):
        self.driver.get("https://www.auto-haus.link/")
        self.driver.set_window_size(1376, 1080)

        user_input = self.driver.find_element(By.ID, "loginForm_email")
        user_input.clear()
        user_input.send_keys(usuario)

        password_input = self.driver.find_element(By.ID, "loginForm_password")
        password_input.clear()
        password_input.send_keys(contrasena)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".ant-btn")
        submit_button.click()

        try:
            # Espera hasta 10 segundos a que aparezca algún elemento en la página principal
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='clase-de-elemento-en-la-pagina-principal']"))
            )
            print(f"Prueba exitosa para Usuario: {usuario}, Contraseña: {contrasena}")
        except:
            print(f"Prueba fallida para Usuario: {usuario}, Contraseña: {contrasena}")

# Si ejecutas este script, debería realizar todas las pruebas que has definido.
if __name__ == "__main__":
    pytest.main([__file__])

    # Verifica la URL después del inicio de sesión
    if driver.current_url == "https://www.auto-haus.link":
        print("Inicio de sesión exitoso")
    else:
        print("Inicio de sesión fallido")

    driver.quit()

# Realiza las pruebas
realizar_prueba("", "")  # Prueba 1: Login o password vacíos
realizar_prueba("123456789", "123456789")  # Prueba 2: Login o password incorrecto
realizar_prueba("usuario@example2.com", "contraseña123")  # Prueba 3: Login exitoso
realizar_prueba("prueba", "SELECT * FROM Users WHERE Username='1' OR '1' = '1' AND Password='1' OR '1' = '1'")  # Prueba 4: Inyección de SQL
