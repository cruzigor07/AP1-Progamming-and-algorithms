nota = float(input("Digite sua nota final (0 a 10): "))
frequencia = float(input("Digite sua frequência (%): "))
resposta = input("Fez a prova de recuperação? (sim/nao): ").strip().lower()
 
fez_recuperacao = resposta == "sim"
 
if frequencia < 75:
    resultado = "Reprovado por falta"
elif nota >= 7:
    resultado = "Aprovado direto"
elif fez_recuperacao:
    resultado = "Aprovado na recuperação"
else:
    resultado = "Reprovado por nota"
 
print()
print("Nota final:", nota)
print("Frequência:", frequencia, "%")
 
if fez_recuperacao:
    print("Fez recuperação: Sim")
else:
    print("Fez recuperação: Não")
 
print("Status:", resultado)
