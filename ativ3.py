nome_cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
preco = float(input("Preco unitario (R$): "))
quantidade = int(input("Quantidade: "))
percentual_desconto = float(input("Percentual de desconto (%): "))

subtotal = preco * quantidade
valor_desconto = subtotal * (percentual_desconto / 100)
total_final = subtotal - valor_desconto
valor_medio = total_final / quantidade

print(f"\nCliente: {nome_cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_final:.2f}")
print(f"Valor medio por unidade: R$ {valor_medio:.2f}")