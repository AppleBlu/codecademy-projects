#list of all the different toppings in a pizza shop
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives','anchovies', 'mushrooms']
#prices for all the toppings
prices = [2, 6, 1, 3, 2, 7, 2]
#using 'len()' to work out how many diffent topping there are
num_of_pizzas = len(toppings)
#printing a string
print('We sell ' + str(num_of_pizzas) + ' different kinds of pizza!')
#combing to lists using 'zip'. also using 'list' to make the return a list
pizzas = list(zip(prices, toppings))
#sorting pizzas by price
pizzas.sort()
#tetsing the line of code above
print(pizzas)
#storeing the cheapest pizza from the list [pizzas] to the varible 'cheapest_pizza'
cheapest_pizza = pizzas[1]
#storeing the priciest pizza from the list [pizzas] to the varible 'priciest_pizza'
priciest_pizza = pizzas[-1]
#storeing the 3 cheapest pizzas from the list [pizzas] to the varible 'three_cheapest'
three_cheapest = pizzas[0:3]
#testing the line of code above
print(three_cheapest)
#using '.count()' to find out how many £2 pizzas there are on the menu and storing it to 'num_of_two_pound_pizzas'
num_of_two_pound_pizzas = prices.count(2)
#testing the line of code above
print(num_of_two_pound_pizzas)