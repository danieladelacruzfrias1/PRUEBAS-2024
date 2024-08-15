from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://kuula.co/post/n1/collection/7Kgqj'

# Configurar el navegador (asegúrate de tener el driver adecuado instalado)
driver = webdriver.Chrome()  # o webdriver.Firefox() si usas Firefox
driver.get(url)

# Esperar a que los comentarios se carguen
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "comments"))
    )
finally:
    # Obtener el contenido HTML
    html_contents = driver.page_source
    driver.quit()

# Analizar el HTML con BeautifulSoup
html_soup = BeautifulSoup(html_contents, 'html.parser')

# Extraer comentarios
extraer_comentarios = html_soup.find_all('li', class_='comments')

# Verificar si se extrajeron comentarios y imprimirlos
if extraer_comentarios:
    print("Comentarios extraídos exitosamente:")
    for comentario in extraer_comentarios:
        # Imprimir el contenido de comentario para depuración
        print(comentario.prettify())
        
        # Buscar el texto dentro de las etiquetas <div> o <span>
        div_tag = comentario.find('div')
        if div_tag:
            texto_comentario = div_tag.get_text(strip=True)
            print(texto_comentario)
        else:
            print("No se encontró una etiqueta <div> en este comentario.")
else:
    print("No se encontraron comentarios.")
