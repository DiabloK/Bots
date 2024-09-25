import sqlite3

def criar_banco():
    # Conectando ao banco de dados (ou criando um novo se não existir)
    conn = sqlite3.connect('SQL/banco.sql')
    cursor = conn.cursor()

    # Criando a tabela IDS se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS IDS  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostid INTEGER NOT NULL,
        data_coleta DATETIME DEFAULT CURRENT_TIMESTAMP, -- Coluna para Data de Coleta
        status BOOLEAN DEFAULT 0 -- Coluna para Status com valor padrão
    )
    ''')

    # Criando a tabela DadosBrutos se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DadosBrutos  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostid INTEGER NOT NULL,
        data_coleta DATETIME DEFAULT CURRENT_TIMESTAMP, -- Coluna para Data de Coleta
        status BOOLEAN DEFAULT 0 -- Coluna para Status com valor padrão
    )
    ''')

    # Confirmando as alterações no banco de dados
    conn.commit()
    # Fechando a conexão
    conn.close()


def inserir_dados_Brutos(hostid):
    # Conectando ao banco de dados
    conn = sqlite3.connect('SQL/banco.sql')
    cursor = conn.cursor()

    # Inserindo dados na tabela (somente hostid, status usa valor padrão)
    cursor.execute('''
    INSERT INTO DadosBrutos (hostid) VALUES (?)
    ''', (hostid,))
    
    conn.commit()
    conn.close()
    #mexer aqui 
def inserir_dados_finais(hostid): 
    conn = sqlite3.connect('SQL/banco.sql')
    cursor = conn.cursor()

    # Inserindo dados na tabela (somente hostid, status usa valor padrão)
    cursor.execute('''
    INSERT INTO IDS (hostid) VALUES (?)
    ''', (hostid,))
    
    conn.commit()
    conn.close()

def ler_dados():
    # Conectando ao banco de dados
    conn = sqlite3.connect('SQL/banco.sql')
    cursor = conn.cursor()

    # Lendo os dados da tabela
    cursor.execute('SELECT * FROM DadosBrutos')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
# Commitando as alterações e fechando a conexão
