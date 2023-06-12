name="Python"
print("I know "+name)

myLang="I know {}".format("Python")
print(myLang)

name="Python"
myLang="I know {}".format(name)
print(myLang)

myLang="I know {} {} {}".format("Python","Java","JS")
print(myLang)

myLang="I know {0} {1} {2}".format("Python","Java","JS")
print(myLang)

myLang="I know {2} {1} {0}".format("Python","Java","JS")
print(myLang)

myLang="I know {p} {j} {js}".format(p="Python",j="Java",js="JS")
print(myLang)

