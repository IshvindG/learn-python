weight = 41.5


flat_charge_premium = 125
flat_charge_ground = 20
price_per_pound = 0
cost_ground = 0
#Ground Shipping 
if weight <= 2:
  price_per_pound += 1.5*weight
  cost_ground = flat_charge_ground+price_per_pound
elif 2 < weight <= 6:
  price_per_pound += 3*weight
  cost_ground = flat_charge_ground + price_per_pound
elif 6 < weight <= 10:
  price_per_pound += 4*weight
  cost_ground = flat_charge_ground + price_per_pound
elif weight > 10:
  price_per_pound += 4.75*weight
  cost_ground = flat_charge_ground + price_per_pound

print('Flat charge for ground shipping premium is {}'.format(flat_charge_premium))
print('Flat charge for standard ground shipping is {}'.format(flat_charge_ground))


#Drone Shipping

if weight <= 2:
  cost_drone = 4.50 * weight
elif 2 < weight <= 6:
  cost_drone = 9 * weight
elif 6 < weight <= 10:
  cost_drone = 12 * weight
elif weight > 10:
  cost_drone = 14.25 * weight 
print('')
print('Your total is for standard ground shipping is ' + str(cost_ground))
print('Your total is drone shipping is ' + str(cost_drone))
print('Your total is ' + str(flat_charge_premium))
