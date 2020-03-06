#Desafio1

salBruto = float(input("Entre com o seu salário bruto: "))

perg1 = input("Possui algum dependente?(S/N) ")
if perg1 == 'S' or perg1 == 's':
    nDependentes = int(input("Insira quantos dependentes possui: "))
else:
    nDependentes = 0

perg2 = input("Possui alguma pensão diretamente descontada da fonte?(S/N)")
if perg1 == 'S' or perg1 == 's':
    valorPensao = float(input("Qual o valor da pensão(R$): "))
else:
    valorPensao = 0.00

PAT = float(input("Insira o valor do seu PAT(R$): "))

perg3 = input("Possui algum plano de saúde diretamente descontado?(S/N)")
if perg1 == 'S' or perg1 == 's':
    plnSaude = float(input("Insira quantos dependentes possui: "))
else:
    plnSaude = 0.00

perg4 = input("Possui algum desconto adicional?(S/N)")
if perg1 == 'S' or perg1 == 's':
    descontos = float(input("Qual o valor da pensão(R$): "))
else:
    descontos = 0.00

if salBruto <= 1045.00:
	INSS = salBruto * 7.5/100
elif salBruto > 1045.01 and salBruto <= 2089.60:
	INSS = salBruto * 9/100
elif salBruto >= 2089.61 and salBruto <= 3134.40:
	INSS = salBruto * 12/100
elif salBruto >= 3134.41 and salBruto <= 6101.06:
	INSS = salBruto * 14/100
elif salBruto > 6101.06:
    INSS = 671.12 

baseCalc = salBruto - INSS - valorPensao - nDependentes * 189.59

if baseCalc <= 1903.98:
    aliquota = 0.00
    deducao = 0.00
elif baseCalc >= 1903.99 and baseCalc <= 2826.65:
	aliquota = 7.5/100
	deducao = 142.80
elif baseCalc >= 2826.66 and baseCalc <= 3751.05:
	aliquota = 15/100
	deducao = 354.80
elif baseCalc > 3751.06 and baseCalc <= 4664.68:
	aliquota = 22.5/100
	deducao = 636.13
elif baseCalc > 4664.68:
    aliquota = 27.5/100
    deducao = 869.36

IRRF = baseCalc * aliquota - deducao

salLiq = salBruto - ((valorPensao * nDependentes) + plnSaude + PAT + descontos + INSS + IRRF)

print("Seu salário líquido é: R$ ", salLiq)
print("Valor pago ao INSS: R$ ", INSS)
print("Valor pago ao IRRF: R$ ", IRRF)