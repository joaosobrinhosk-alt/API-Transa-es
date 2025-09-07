import function

lista = []

while True:

    # Função para o analize e conversões
    function.analize()

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if escolha == 1:
        while True:
            try:
                valor = float(input("Euro pra Real: "))
                Euro = function.euroreal(valor)
                dic = {
                    "tipo": "Euro",
                    "valor": valor,
                    "resultado": Euro
                }
                lista.append(dic)
                break
            except:
                print("- Tente novamente!")
                function.linha()

    elif escolha == 2:
        while True:
            try:
                valor = float(input("Dólar pra Real: "))
                Dollar = function.dollarreal(valor)
                dic = {
                    "tipo": "Dollar",
                    "valor": valor,
                    "resultado": Dollar
                }
                lista.append(dic)
                break
            except:
                print("- Tente novamente!")
                function.linha()

    elif escolha == 3:
        Bitcoin = function.bitcoin()
        dic = {
            "tipo": "Bitcoin",
            "valor": 1,
            "resultado": Bitcoin
        }
        lista.append(dic)

    elif escolha == 4:
        if not lista:
            print("Nenhuma transação registrada ainda.")
        else:
            for transacao in lista:
                if transacao["tipo"] == "Euro":
                    print(f"A transação feita com {transacao['valor']} Euros resultou em R${transacao['resultado']:.2f} Reais")
                elif transacao["tipo"] == "Dollar":
                    print(f"A transação feita com {transacao['valor']} Dólares resultou em R${transacao['resultado']:.2f} Reais")
                elif transacao["tipo"] == "Bitcoin":
                    print(f"O Bitcoin estava avaliado em R${transacao['resultado']:.2f}")

    else:
        print("Fechando programa...")
        break
