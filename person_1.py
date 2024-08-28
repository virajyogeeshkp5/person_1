class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello,My name is:", self.name, "and I am", self.age,"years old")


person1 = person("viraj", 30)
print("person name:", person1.name)
print("person age:", person1.age)
person1.greet()
