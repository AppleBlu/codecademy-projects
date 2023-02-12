#loveseat description
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.';
#loveseat price
loverly_loveseat_price = 254.00;
#settee description
stylish_setee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.';
#settee price
stylish_setee_price = 180.50;
#lamp description
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.';
#lamp price
luxurious_lamp_price = 52.15 ;
#tax (8.8%)
sales_tax = .088;
#total price of items
customer_one_total = (loverly_loveseat_price + luxurious_lamp_price);
#all the descriptions of the items
custermer_one_itemization = (lovely_loveseat_description + luxurious_lamp_description);
#the total is being x by 0.08 to get 8.8% of the toatal (this is the tax) 
customer_one_tax = customer_one_total * sales_tax;
#the tax is being added to the total and permantly changing the total vairible
customer_one_total += customer_one_tax;
#prints descriptions and price. (recipit)
print('Customer one items:');
print(custermer_one_itemization);
print('Customer one total:');
print(customer_one_total)