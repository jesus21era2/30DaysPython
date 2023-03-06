#Exercise 1 https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md

def exercise1():
    brothers = ('Mathias', 'Gabriel', 'Juan')
    sisters = ('Carla', 'Anto', 'Valentina')
    siblings = brothers + sisters
    total = len(siblings)
    print(total, siblings)

def exercise2():
    fruits = ('banana', 'orange', 'mango', 'lemon')
    vegetables = ('Tomato', 'Potato','Onion', 'Carrot')
    animalp = ('Meat', 'Milk', 'Fish')
    food_stuff = fruits + vegetables + animalp
    if len(food_stuff) % 2 == 0: #par
        middle = food_stuff[round(len(food_stuff) / 2)]
    else: #impar
        middle = food_stuff[round(len(food_stuff) / 2) - 1]

#Slice out the first three items and the last three items from food_staff_lt list
    print(f'Last 3: {food_stuff[-3:]}, Middle:, {middle}, First three:, food_stuff[0:3]')

    del food_stuff

#Check if an item exists in tuple:
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    if 'Estonia' in nordic_countries: print('Estonia is a nordic country')
    else: print("Estonia isn't a nordic country")

    if 'Iceland' in nordic_countries: print('Iceland is a nordic country')
    else: print("Iceland isn't a nordic country")
exercise2()
