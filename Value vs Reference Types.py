# This is Python code about reference and value types

value1 = 5
value2 = value1
value2 = 10
value1 = 8
print(value1, value2)
# Prints 8, 10
# Values are independent

ref1 = [0,1,2,3,4,5]
ref2 = ref1
ref2[0] = 999
ref1[5] = 5555
print(ref1, ref2)
# Prints [999,1,2,3,4,5555], [999,1,2,3,4,5555]
# References are kinda connected

# You can forget about all this, This just for learning
