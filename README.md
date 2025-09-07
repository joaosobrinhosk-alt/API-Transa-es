# 💱 API-Transições - Conversor de Moedas e Monitor de Cotações

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![GitHub](https://img.shields.io/badge/GitHub-API%20Project-green)

---

## 🔹 Descrição
API-Transições é um projeto em **Python** que permite converter valores entre **Euro, Dólar e Bitcoin** e acompanhar suas cotações em tempo real usando a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).  
O programa mantém um **histórico de transações** e exibe os resultados no terminal, garantindo praticidade e confiabilidade.

---

## 🚀 Funcionalidades
- Converter **Euro para Real** e **Dólar para Real**.  
- Consultar o valor do **Bitcoin** em tempo real.  
- Registrar todas as transações realizadas.  
- Menu interativo para facilitar o uso.  
- Tratamento de erros automático para entradas inválidas.  

---

## 🛠 Tecnologias
- **Python 3.10+**  
- **Requests** para integração com APIs externas  
- **Listas e dicionários** para armazenar histórico  
- **Funções modulares** para organizar o código  

---

## ⚡ Como usar
1. Clone o repositório:  
```bash
git clone https://github.com/joaosobrinhosk-alt/API-Transicoes.git
cd API-Transicoes
Instale a biblioteca Requests:

bash
Copiar código
pip install requests
Execute o programa:

bash
Copiar código
python main.py
Siga o menu para realizar conversões e consultar o histórico de transações.

📊 Exemplo de uso
nginx
Copiar código
Escolha uma opção: 1
Euro pra Real: 10
✅ 10 EUR equivalem a R$63,41

Escolha uma opção: 4
📜 Histórico de transações:
- 10 Euros → R$63,41
- 20 Dólares → R$108,20
- 1 Bitcoin → R$605,495.00
📂 Estrutura do projeto
bash
Copiar código
API-Transicoes/
├── main.py       # Menu interativo e execução principal
├── function.py   # Funções de conversão e consulta de moedas
├── README.md     # Documentação do projeto
└── requirements.txt # Dependências (opcional)
