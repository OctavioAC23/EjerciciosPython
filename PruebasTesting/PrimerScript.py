from selenium import webdriver

# Configura las opciones del navegador Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Indica que estamos utilizando el nuevo navegador Edge basado en Chromium
edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Ruta a la aplicación de Edge

# Inicia el controlador de Edge con las opciones especificadas
driver = webdriver.Edge(options=edge_options)

# Maximiza la ventana del navegador
driver.maximize_window()

# Abre la página de Udemy
driver.get("https://www.udemy.com/")

# Cierra el navegador al finalizar
driver.quit()
