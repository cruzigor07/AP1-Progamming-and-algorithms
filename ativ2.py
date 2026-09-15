titulo = "Calculo da compra"
preco_Produto = 35.00
quantidade = 2

subtotal = preco_Produto * quantidade  
desconto = subtotal * 0.1  
valor_final = subtotal - desconto     

print(f"""
{titulo}
O cliente comprou {quantidade} itens, valor de R$ {preco_Produto:.2f} unidade
Desconto: R$ {desconto}
Valor final: R$ {valor_final:.2f}
""")