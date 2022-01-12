################################
# Piikani Nation Restaurant lanuage Converter
# A program used to order food, 
#   and convert the language from engish to piikani. 
#
# Programmer: Colton Blackwell
# Date: September 30th, 2021 

food = {'fish': 'mamii', 'fries': 'paataakistsi', 'burger': 'pikkiaaksin'}

drink = {'coffee': 'iitapsiksikimmii', 'tea': 'siksikimmii', 'water': 'aohkii'}

people = int(input("Oki! Welcome to the restaurant. How many do we have today? => "))

print("Ok! I'll go around one by one and take your order!\n \n")

orderFood = {'fish': 0, 'fries': 0, 'burger': 0}

orderDrink = {'coffee': 0, 'tea': 0, 'water': 0}

productCost = {'fish': 5.00, 'fries' : 3.00, 'burger' : 4.50, 'coffee' : 1.50, 'tea': 1.00, 'water': 0.00 }

userPayment = 0.00 

for i in range(1, people + 1):
    
  print("Customer #", i)

  userFood = input(": What would you like to eat? (fish/fries/burger) => ").lower()

  if (userFood != 'fish' and userFood != 'fries' and userFood != 'burger'):
    print("Sorry, we don't serve", userFood, "here...")
  else:
    print("So that's one", food[userFood], "(", userFood, ")")
    print("...The waiter adds one", userFood, "to the list...")
    orderFood[userFood] += 1
    print("The list now has", orderFood[userFood], userFood, "\n")
    userPayment += productCost.get(userFood)
    print("The cost of", userFood, "is: ${:.2f}".format(productCost.get(userFood)))
    print("The new cost of the meal is: ${:.2f}".format(userPayment), "\n")
    
  userDrink = input("What would you like to drink? (coffee/tea/water) => ").lower()

  if (userDrink != 'coffee' and userDrink != 'tea' and userDrink != 'water'):
    print("Sorry, we don't serve", userDrink, "here...")
  else:
    
    print("So that's one", drink[userDrink], "(", userDrink, ")")
    print("...The waiter adds one", userDrink, "to the list...")
    orderDrink[userDrink] += 1
    print("The list now has", orderDrink[userDrink], userDrink, "\n")
    userPayment += productCost.get(userDrink)
    print("The cost of", userDrink, "is: ${:.2f}".format(productCost.get(userDrink)))
    print("The new cost of the meal is: ${:.2f}".format(userPayment), "\n")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")


print("***************************************\n")
print("Ok, here are the order that I have...")

print(orderFood.get('fish'), food.get('fish'), "(fish)")
print(orderFood.get('fries'), food.get('fries'), "(fries)")
print(orderFood.get('burger'), food.get('burger'), "(burger)")
print(orderDrink.get('coffee'), drink.get('coffee'), "(coffee)")
print(orderDrink.get('tea'), drink.get('tea'), "(tea)")
print(orderDrink.get('water'), drink.get('water'), "(water)\n")

print("Your final payment comes out to... ${:.2f}".format(userPayment))