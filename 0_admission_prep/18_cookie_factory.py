

# cookie factory----------------------------------------------------------------------
doses = int(input())

for batch in range(1, doses + 1):
    flour = False
    sugar = False
    eggs = False
    has_all_ingredients = False
    ingredient = ''

    while True:
        ingredient = input()

        if ingredient == 'flour':
            flour = True

        elif ingredient == 'sugar':
            sugar = True

        elif ingredient == 'eggs':
            eggs = True

        has_all_ingredients = flour and sugar and eggs
        if ingredient == 'Bake!':
            if not has_all_ingredients:
                print('The batter should contain flour, eggs and sugar!')
            else:
                print(f'Baking batch number {batch}...')
                break
