# Ashrita Kantamneni
# CS - UY 1114
# 24 May 2024 - Lab 1

import random 
import math 

length_beam = random.uniform(2.5,5.0) #in meters
width_beam = random.uniform(0.1,0.3) #in meters
height_beam = random.uniform(0.1,0.3) #in meters
applied_load = random.randint(1000,5000) #in newtons
yield_strength = 200 * math.pow(10,6)

moment_of_inertia = (width_beam * math.pow(height_beam,3))/12
distance_from_axis = height_beam/2
max_stress = (applied_load * distance_from_axis) / moment_of_inertia

if max_stress <= yield_strength:
  print('The beam is safe')
else:
  print('The beam will fail')




