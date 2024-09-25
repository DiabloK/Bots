import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from SQL import BancoM
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager  # Firefox
from selenium.webdriver.firefox.service import Service  # Serviço para o Firefox

from urllib.parse import urlparse, parse_qs
def HostColequetor(navegador): 
    service_firefox = Service(GeckoDriverManager().install())

    # Inicializando o navegador Firefox

    navegador = webdriver.Firefox(service=service_firefox)
    navegador.get("http://zabbix.acessoline.net.br/")

    # Localizando os campos de login e senha e o botão de login
    campo_usuario = navegador.find_element(By.XPATH, '//*[@id="name"]')
    campo_senha = navegador.find_element(By.XPATH, '//*[@id="password"]')

    # Inserindo o usuário e a senha
    campo_usuario.send_keys("vinicius.signorelli")
    campo_senha.send_keys("Vs2021GG")

    # Submetendo o formulário
    campo_senha.send_keys(Keys.ENTER)

    time.sleep(3) # timer para deixar ele logar
    
    listaID=[]
    pagina = 1
    loop=False
    #funcinal para mais de 10 paginas tem funcinar para mesmo 
    
    while loop!=True:
        # Atualizar a URL para a página atual
        url = f"http://zabbix.acessoline.net.br/zabbix/zabbix.php?name=&ip=&dns=&port=&status=-1&evaltype=0&tags%5B0%5D%5Btag%5D=&tags%5B0%5D%5Boperator%5D=0&tags%5B0%5D%5Bvalue%5D=&maintenance_status=1&filter_name=&filter_show_counter=0&filter_custom_time=0&sort=name&sortorder=ASC&show_suppressed=0&page={pagina}&action=host.view&groupids%5B%5D=77"
        navegador.get(url)
        time.sleep(3)  # Aguarda o carregamento da página

        # Captura o link da URL atual
        link_atual = navegador.current_url

        # Condição para sair do loop
        elemento = navegador.find_element(By.XPATH, '/html/body/div/main/form/div/nav/a[13]')
        # Captura o valor do atributo href (link)
        link_destino = elemento.get_attribute('href')

        # Parseando a URL
        parsed_url = urlparse(link_destino)
        query_params = parse_qs(parsed_url.query)

        # Extraindo o valor de "page"
        page_value = query_params.get('page', [None])[0]

        if int(pagina) == int(page_value): 
            print("Condição atendida. Saindo do loop.")
            loop=True

        # Loop para buscar elementos na página
        for i in range(1, 51):  # Se houver 50 elementos por página
            try:
                # Tentar encontrar o elemento
                elemento = navegador.find_element(By.XPATH, f'/html/body/div/main/form/table/tbody/tr[{i}]/td[1]/a')

                # Capturar o valor do atributo data-menu-popup
                data_menu_popup = elemento.get_attribute('data-menu-popup')

                # Analisar o JSON para extrair o hostid
                data_json = json.loads(data_menu_popup)
                hostid = data_json['data']['hostid']

                # Adicionar o hostid à lista
                listaID.append(hostid)
                BancoM.inserir_dados_Brutos(hostid)

            except Exception as e:
                print(f"Elemento não encontrado na posição {i}: {e}")
                break  # Sai do loop se não houver mais elementos na tabela

        pagina += 1  # Incrementa a página para o próximo loop