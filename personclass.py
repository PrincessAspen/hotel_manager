class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people = []

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greeting_count += 1
        if not other_person in self.unique_people:
            self.unique_people.append(other_person)
      
    def print_contact_info(self):
        print("%s's contact information is %s, %s" % (self.name, self.email, self.phone))
        
    def add_friend(self, other_person):
        self.friends.append(other_person)
        
    def num_friends(self):
        print(len(self.friends))
        
    def num_unique_people_greeted(self):
        print(len(self.unique_people))
        
    def __str__(self):
        return "Person: %s, %s, %s" % (self.name, self.email, self.phone)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan= Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.add_friend(jordan)
jordan.add_friend(sonny)

jordan.num_friends()

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.num_unique_people_greeted()
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

sonny.print_contact_info()
print(sonny)