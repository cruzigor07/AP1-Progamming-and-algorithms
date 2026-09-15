def verificar_frete():
    valor = float(input("Valor do pedido: "))
    pagamento = input("Forma de pagamento (pix/cartao): ")
    if valor >= 50:
        print("FRETE GRATIS + DESCONTO" if pagamento.lower() == "pix" else "FRETE GRATIS")
    else:
        print("FRETE COBRADO - valor abaixo de 50")


def avaliar_pedido():
    cliente = input("Nome do cliente: ")
    valor = float(input("Valor do pedido: "))
    pago = input("Pagamento aprovado? (s/n): ").lower() == "s"
    match (valor, pago):
        case (v, True) if v >= 20:
            print(f"{cliente}: PEDIDO CONFIRMADO")
        case (v, False) if v >= 20:
            print(f"{cliente}: AGUARDANDO PAGAMENTO")
        case _:
            print(f"{cliente}: PEDIDO CANCELADO")


def main():
    opcao = ""
    while opcao != "3":
        print("\n1-Frete 2-Avaliar 3-Sair")
        opcao = input("Escolha uma opcao: ")
        match opcao:
            case "1": verificar_frete()
            case "2": avaliar_pedido()
            case "3": print("Saindo...")
            case _: print("Opcao invalida")


main()
