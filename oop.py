class person:
    def __init__(self,name,age,country,feet,inches):
        self.name = name
        self.age = age
        self.country = country
        self.feet = feet
        self.inches = inches

    def details(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I am from", self.country)
        print("I am", self.feet, "feet and", self.inches, "inches tall")

    def modify(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        country = input("Enter where you are from: ")
        feet = input("Enter the feet:")
        inches = input("Enter the inches")
        self.name = name
        self.age = age
        self.country = country
        self.feet = feet
        self.inches = inches

p1 = person("Angel", 15, "United Kingdom", 5, 5)
p2 = person("Danstan", 27, "Kenya", 6, 0)
#p1.details()
#print(p1.details)
p1.modify()
