#code to determine the price of ground shipping with the weight of the package
def ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.50) + 20.00
  elif (weight > 2) and (weight <= 6):
    return (weight * 3.00) + 20.00
  elif (weight > 6) and (weight <= 10):
    return (weight * 4.00) + 20.00
  elif (weight > 10):
    return (weight * 4.75) + 20.00

#prints how much it will cost for ground shipping
print('For ground shipping it will cost $' + str(ground_shipping(8.4)))

#vairible for how much premuim ground shipping is
premium_ground_shipping = 120.00

#code to determine how much it will cost for drone shipping your packege. depends on the weight 
def drone_shipping(weight):
  if weight <= 2:
    return (weight * 1.50) * 3
  elif (weight > 2) and (weight <= 6):
    return (weight * 3.00) * 3
  elif (weight > 6) and (weight <= 10):
    return (weight * 4.00) * 3
  elif (weight > 10):
    return (weight * 4.75) * 3

print('For drone shipping it will cost $' + str(drone_shipping(1.5)))


def cheapest_shipping(weight):

  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)

  if (ground < premium) and (ground < drone):
    method = 'Standard ground'
    cost = ground
  elif (premium < ground) and (premium < drone):
    method = 'Premium ground'
    cost = premium 
  else:
    method = 'Drone'
    cost = drone
  print(
    'The cheepest option to ship you item will cost $%.2f with %s shipping'
  % (cost, method)
  )

 
cheapest_shipping(4.8)
cheapest_shipping(41.5)