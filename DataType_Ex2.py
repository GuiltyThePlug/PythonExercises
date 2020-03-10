Cars = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
Cars.sort()
print(Cars, "In Ascending Order ;-)")

print(sum((56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56)), "A sum of the total numbers in the 'Cars' List")

temp = []
[temp.append(x) for x in Cars if x not in temp]
print(temp)


