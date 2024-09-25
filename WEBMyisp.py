from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.firefox import GeckoDriverManager  # Firefox
from selenium.webdriver.firefox.service import Service  # Serviço para o Firefox

def Myispbusca(texto_desejado): 
    
    service_firefox = Service(GeckoDriverManager().install())
    navegador = webdriver.Firefox(service=service_firefox)
    navegador.get("http://myisp.acessoline.net.br/MyIspWeb/admin.jsp")
    campo_usuario = navegador.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/fieldset/div[1]/input')
    campo_senha = navegador.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/fieldset/div[2]/input')

    # Inserindo o usuário e a senha
    campo_usuario.send_keys("vinicius.signorelli")
    campo_senha.send_keys("Vs2021GG")

    # Submetendo o formulário
    campo_senha.send_keys(Keys.ENTER)
    time.sleep(2)
    navegador.get("http://myisp.acessoline.net.br/MyIspWeb/admin/directory/search.jsp?filter=&section=")

    opcao_dropdown = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div/div/a[6]/span')
    opcao_dropdown.click()  # Clica na opção do menu dropdown

    # Preencher o campo de busca
    campo_de_busca = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/input[1]')
    campo_de_busca.send_keys('CIASC')

    # Clicar no botão de pesquisa
    botao_pesquisa = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div/form/button')
    botao_pesquisa.click()
    time.sleep(1)
    Primeiro= navegador.find_element(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/a')
    Primeiro.click()
    
    Primeiro= navegador.find_element(By.XPATH, '/html/body/div/nav/div/div[2]/ul/li[4]/a')
    Primeiro.click()
    texto_desejado=str(texto_desejado)
    try:
    # Espera até que os <td> estejam presentes
        WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td"))
        )

        # Obtém todos os elementos <td>
        tds = navegador.find_elements(By.XPATH, "//td")
        encontrado = False

        for i, td in enumerate(tds):
            if texto_desejado.strip() in td.text:
                encontrado = True
                # Acesse o container (elemento pai, que pode ser <tr>)
                container = td.find_element(By.XPATH, "..")  # O ".." refere-se ao elemento pai
                texto_container = container.text
                return (texto_container)
                break

        if not encontrado:
            print(f"Elemento com o texto '{texto_desejado}' não encontrado.")

    except Exception as e:
        return f"Erro: {e}"