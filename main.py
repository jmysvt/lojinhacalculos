pco = float(input("Digite o preço da peça:"))
quant = int(input("Qual a quantidade de peças compradas? "))
desconto = float(input("Qual o desconto aplicado? "))

total = pco * quant

if desconto > 0:
  valordesconto = total * (desconto / 100)
  total = valordesconto

print("O preço final da compra é R$ {:.2f}".format(total))