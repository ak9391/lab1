# Ashrita Kantamneni
# CS - UY 1114
# 24 May 2024 - Lab 1

import math 

print('Fuel Efficiency Calculation')
distance_traveled = float(input('What is the distance traveled in kilometers?'))
fuel_consumed = float(input('How much fuel was consumed in liters?'))

fuel_efficiency = round(distance_traveled / fuel_consumed, 2)

fuel_efficiency_liters_per_km = round(100 / fuel_efficiency, 2)

print("Distance Traveled:", distance_traveled, "kilometers" )
print("Fuel Consumed:", fuel_consumed, "liters" )
print("Fuel Efficiency:", fuel_efficiency, "kilometers per liter")

print('Fuel Efficiency (liters per 100 kilometers):', fuel_efficiency_liters_per_km, "liters per 100 kilometers")
