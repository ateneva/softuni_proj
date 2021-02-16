
# logistics---------------------------------------------------------------------

cargos = int(input())
bus = 0
shuttle = 0
train = 0
cargo_volume = 0
total_price = 0

for cargo in range(cargos):
    cargo_weight = int(input())

    if cargo_weight <= 3:
        bus += cargo_weight
        price = 200
        cargo_price = cargo_weight * price

    elif cargo_weight >= 4 and cargo_weight <= 11:
        shuttle += cargo_weight
        price = 175
        cargo_price = cargo_weight * price

    elif cargo_weight >= 12:
        train += cargo_weight
        price = 120
        cargo_price = cargo_weight * price

    cargo_volume += cargo_weight
    total_price += cargo_price

# print(cargo_volume)
# print(bus)
# print(shuttle)
# print(train)
print(f'{total_price/cargo_volume:.2f}')
print(f'{bus/cargo_volume * 100:.2f}%')
print(f'{shuttle/cargo_volume * 100:.2f}%')
print(f'{train/cargo_volume * 100:.2f}%')
