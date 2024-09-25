from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager  # Firefox
from selenium.webdriver.firefox.service import Service  # Serviço para o Firefox
from SQL import BancoM
import Zabbix
import WEBMyisp
import re



BancoM.criar_banco()

# Configurando o serviço para Firefox
#service_firefox = Service(GeckoDriverManager().install())

# Inicializando o navegador Firefox

#navegador = webdriver.Firefox(service=service_firefox)
#Zabbix.HostColequetor(navegador)
'''print("digite o circuito:")
texto = input("")  
texto_original=WEBMyisp.Myispbusca(texto)'''

# Exibir o texto ajustado
#Para verificar as configs 
#navegador.get(f"http://zabbix.acessoline.net.br/zabbix/hosts.php?form=update&hostid={hostid}")


