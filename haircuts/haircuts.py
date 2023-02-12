hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#creating an empty varible
total_price = 0
#making a loop to set 'total_price' to all the prices from [prices] list added together
for p in prices:
  total_price += p
#setting 'averge_price' to 'total_price' divided by how many elements are in the [price list]
average_price = total_price / len(prices)
#testing if the 'average_price' vairble works
print('Average Haircut Price: ' + str(average_price))
#cutting all prices by 5
new_prices = [p - 5 for p in prices]
#tetsing new_prices 
print(new_prices)
#creating an empty vairible
total_revenue = 0
#creating a for loop to see how much money was made last week
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
#testing 'total_revenue'
print('Total Revenue: ' + str(total_revenue))
#finding out the daily revenue
average_daily_revenue = total_revenue / 7