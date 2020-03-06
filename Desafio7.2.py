altura = float(input("Diga sua altura(em metros): "))
peso = float(input("Diga seu peso(em Kg): "))

IMC = peso/(altura * altura)

if IMC < 15:
    avaliacao = "Extremamente abaixo do peso"
elif IMC >= 15 and IMC < 16:
    avaliacao = "Gravemente abaixo do peso"
elif IMC >= 16 and IMC < 18.5:
    avaliacao = "Abaixo do peso ideal"
elif IMC >= 18.5 and IMC < 25:
    avaliacao = "Faixa de peso ideal"
elif IMC >= 25 and IMC < 30:
    avaliacao = "Em sobrepeso"
elif IMC >= 30 and IMC < 35:
    avaliacao = "Obesidade em Grau I"
elif IMC >= 35 and IMC < 40:
    avaliacao = "Obesidade em Grau II (grave)"
elif IMC > 40:
    avaliacao = "Obesidade em Grau III (mórbida)"

idealMin = (18.5 * (altura * altura))
idealMax = (25.0 * (altura * altura))

print(f"\n\nSeu IMC é: {IMC:.2f}")
print("Sua avaliação:", avaliacao)
print(f"O peso ideal para você é entre {idealMin:.2f}Kg e {idealMax:.2f}Kg\n\n")