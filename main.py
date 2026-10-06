def add_binary(a,b):
    return bin(a+b).split("b")[1]

print(add_binary(4,5))