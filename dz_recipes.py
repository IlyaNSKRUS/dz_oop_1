cook_book = {}

with open('recipes.txt', encoding='utf') as file:
    for line in file:
        ingredients_list = []
        dish_name = line.strip()
        quantity_ingr = int(file.readline())
        for ingredient_line in range(quantity_ingr):
            quantity_ingr -= 1
            ingredient_dict = {}
            item1, item2, item3 = file.readline().split("|")
            ingredient_dict['ingredient_name'] = item1.strip(' ')
            ingredient_dict['quantity'] = item2.strip(' ')
            ingredient_dict['measure'] = item3.strip(' \n')
            ingredients_list.append(ingredient_dict)
            cook_book[dish_name] = ingredients_list
        pusto = file.readline()

def func(dishes, person_count):
    ing_list = {}
    for item, item2 in cook_book.items():
        if item in dishes:
            for ing in item2:
                quantity = int(ing.get('quantity')) * person_count
                if ing.get('ingredient_name') not in ing_list:
                    ing_list[ing.get('ingredient_name')] = {'measure': ing.get('measure'), 'quantity': quantity}
                else:
                    ing_list[ing.get('ingredient_name')] = {'measure': ing.get('measure'), 'quantity': ing_list[ing.get('ingredient_name')]['quantity'] + quantity}
    print(ing_list)

func(['Запеченный картофель','Омлет','Фахитос'],3)

