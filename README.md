API-Transições - Conversor de Moedas e Monitor de Cotações

Descrição:
API-Transições é um projeto em Python desenvolvido para converter valores entre Euro, Dólar e Bitcoin, além de acompanhar suas cotações em tempo real utilizando a API da AwesomeAPI. O programa mantém um histórico das transações realizadas, exibindo os resultados no terminal e permitindo salvar os dados conforme necessário.

Funcionalidades:
O sistema permite converter Euros e Dólares para Reais, consultar o valor do Bitcoin em tempo real e registrar todas as transações em um histórico que pode ser consultado a qualquer momento. Possui um menu interativo que guia o usuário pela seleção da operação desejada e inclui tratamento de erros para entradas inválidas, evitando que o programa feche inesperadamente.

Tecnologias Utilizadas:
O projeto foi desenvolvido em Python 3.10+, utilizando a biblioteca Requests para integrar a API externa. Estruturas de dados como listas e dicionários armazenam informações do histórico, enquanto funções modulares organizam a lógica do programa.

Como usar:
Para executar o projeto, é necessário clonar o repositório para sua máquina e instalar a biblioteca Requests caso ainda não a possua. Após iniciar o programa com python main.py, o usuário pode escolher a operação desejada diretamente pelo menu. Todas as entradas inválidas são tratadas e solicitam nova tentativa sem interromper a execução.

Exemplo de uso:
Ao escolher a opção de conversão de Euro para Real e inserir um valor, o programa retorna o equivalente em Reais. É possível consultar o histórico de transações para visualizar todas as conversões realizadas, incluindo valores de Dólar e Bitcoin.

Estrutura do projeto:
O arquivo main.py contém o menu interativo, enquanto function.py reúne as funções de conversão e consulta de moedas. O README documenta o projeto e um arquivo requirements.txt pode listar dependências adicionais.

Próximos melhoramentos:
O projeto pode ser expandido para salvar o histórico em JSON, incluir suporte a outras moedas, adicionar uma interface gráfica com Tkinter ou PyQt e criar alertas de variação de preço para o Bitcoin.
