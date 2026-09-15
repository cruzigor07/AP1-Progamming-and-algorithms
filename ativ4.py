idade = int(input("Qual sua idade: "))
tem_ingresso = input("Você possui ingresso? (sim/nao): ").strip().lower() == "sim"

if idade < 16:
    mensagem = "Acesso não permitido"
elif tem_ingresso:
    mensagem = "Entrada liberada"
else:
    mensagem = "Compre um ingresso"

print(f"\nIdade informada: {idade} anos")
print(f"Possui ingresso: {'Sim' if tem_ingresso else 'Não'}")
print(f"Status: {mensagem}")