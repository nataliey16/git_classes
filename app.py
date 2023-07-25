# add your name to the print statement below
name = "Natalie Y"
print(f"Hello, my name is {name}")

adding_change = "Adding a new comment"
adding_change2 = "Adding another comment"

#Adding a class

class Person:
    def __init__(self, s_personId, s_firstName, s_lastName, s_favouriteColour, s_age, s_isWorking):
        self.personId = s_personId
        self.firstName = s_firstName
        self.lastName = s_lastName
        self.favouriteColour = s_favouriteColour
        self.age = s_age
        self.isWorking = s_isWorking
    def print_person_char(self):
        self.currentFavouriteColour = input("Is your favourite colour still Olive Green?  ")
        if (self.currentFavouriteColour == "no"):
                    self.favouriteColour = input("What is your favourite colour? ")
        else:
              self.currentFavouriteColour == self.favouriteColour
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Favourite colour: {self.favouriteColour}")
        print(f"Age: {self.age}")
        print(f"Working status: {self.isWorking}")

        self.get_age_in_ten_years = self.age + 10
        print(f"The person's age in 10 years is {self.get_age_in_ten_years}")



person_char= Person("NYE", "Natalie", "Yeung", "Olive Green", 26, "Yes")
person_char.print_person_char()