def speak(self):
    print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

animals = [Cat()]
for animal in animals:
    animal.speak()
 #ISM