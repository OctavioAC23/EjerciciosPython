from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura las opciones del navegador Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Indica que estamos utilizando el nuevo navegador Edge basado en Chromium
edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Ruta a la aplicación de Edge

# Inicia el controlador de Edge con las opciones especificadas
controlador = webdriver.Edge(options=edge_options)

controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&response_type=html&skip_suggest=1")

# Espera implícita para asegurar que la página se cargue completamente
controlador.implicitly_wait(10)

time.sleep(1)

enlace_forgot_password = controlador.find_element(By.LINK_TEXT, 'He olvidado la contraseña')
enlace_forgot_password.click()

time.sleep(5)
