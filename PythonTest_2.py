x = "Guilty The Plug"

print(type(x))  # Show data type, determines what it might be in this case a 'string'
print(x[11:15])  # Show a sequence of numbers from number space : to ending space (Basically specify number position)

# Specify data type between integer, float and a complex number/s.
num1 = 5  # Integer
num2 = 5.8  # Float
num3 = 67j  # Complex

print(type(num1))
print(type(num2))
print(type(num3))

# Specify data type of a 'List'
myList = [23, 82, 42, "Andrew"]
myList2 = [24, 65, 45, 90]
myList3 = [98, 65, 26, 12]

print(type(myList))
print(type(myList2))

# Inserts a number into the list (number of placeholder, and number value)
myList2.insert(3, 21)
print(myList2)

# Reverses the list backwards
myList.reverse()
print(myList)

Cars = {"Aston Martin", "VW", "Ford", "B.M.W", "Nissan"}
print(type(Cars))

Cars1 = ("Aston Martin", "VW", "Ford", "B.M.W", "Nissan")
print(Cars1)
print(type(Cars1))

late = True
early = False
print(type(late))

myDict = {"1": "Oslin", "2": "Kayleen", "3": "Nazneen", "4": "AK", "5": "The Plug!"}
