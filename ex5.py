my_name = 'Anton'
my_age = 28
my_height = 183 # cm
my_weight = 81 # kg
height = 73 # inch
cm_height = round(height * 2.54)
weight = 178.57 # in lb
kg_weight = round(0.45 * weight)
my_eyes = 'Grey'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {cm_height} cm's tall.")
print(f"He's {kg_weight} kg's heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this will be 292, a little bit of calculation
total = my_age + cm_height + kg_weight
print(f"If add {my_age}, {cm_height}, and {kg_weight} I get {total}.")

