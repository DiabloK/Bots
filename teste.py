import os
from seleniumwire import webdriver

usuario = os.getenv('vinicius.signorelli')
senha = os.getenv('Vs2021GG')
ip_do_vpn = '187.87.152.42'


proxy_options = {
    'proxy': {
        'http': f'http://{usuario}:{senha}@{ip_do_vpn}',
        'https': f'https://{usuario}:{senha}@{ip_do_vpn}'
    }
}

driver = webdriver.Chrome(seleniumwire_options=proxy_options)
driver.get("http://zabbix.acessoline.net.br/zabbix/zabbix.php?name=&ip=&dns=&port=&status=-1&evaltype=0&tags%5B0%5D%5Btag%5D=&tags%5B0%5D%5Boperator%5D=0&tags%5B0%5D%5Bvalue%5D=&maintenance_status=1&filter_name=&filter_show_counter=0&filter_custom_time=0&sort=name&sortorder=ASC&show_suppressed=0&action=host.view&groupids%5B%5D=77")