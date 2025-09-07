# Função responsavel em buscar os valores em tempo real
import requests

def linha():
    print("-=" * 15)

# Função para o analize e conversões
def analize():
    linha()
    print("    analize e Conversões")
    linha()
    print("1. Euro pra real")
    print("2. Dollar pra real")
    print("3. Bitcoin")
    print("4. Conversões feitas")
    print("4. Sair")

# Função para transações do Euro pro Real
def euroreal(valor):
    api = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
    dados = api.json()
    euro = float(dados["EURBRL"]["bid"])
    moeda = valor * euro
    print(f"{valor} EUR equivalem a R${moeda:.2f}")
    return moeda  # <<<<<< AGORA RETORNA O VALOR

# Função para transações do Dollar para o Real
def dollarreal(valor):
    api = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    dados = api.json()
    usd = float(dados["USDBRL"]["bid"])
    moeda = valor * usd
    print(f"{valor} USD equivalem a R${moeda:.2f}")
    return moeda  # <<<<<< RETORNA O VALOR

# Função que ira apresentar o valor do Bitcoin
def bitcoin():
    api = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    dados = api.json()
    btc = float(dados["BTCBRL"]["bid"])
    print(f"1 BTC equivale a R${btc:,.2f}")
    return btc
