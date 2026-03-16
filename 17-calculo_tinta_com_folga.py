import math

area = float(input("Digite o tamanho da área em m²: "))

# adiciona 10% de folga
area = area * 1.1

# litros necessários
litros = area / 6

# apenas latas
latas = math.ceil(litros / 18)
preco_latas = latas * 80

# apenas galões
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25

print("Usando apenas latas:")
print("Quantidade:", latas)
print("Preço: R$", preco_latas)

print("\nUsando apenas galões:")
print("Quantidade:", galoes)
print("Preço: R$", preco_galoes)
