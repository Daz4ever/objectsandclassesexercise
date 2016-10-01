class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def __repr__(self):
         return "%r %r %r" % (self.name, self.email, self.phone)




sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")


jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


sonny.greet(jordan)

jordan.greet(sonny)

print sonny.email
print sonny.phone

print jordan.email
print jordan.phone


class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "%s, %s, %s" % (self.year, self.make, self.model)


car = Vehicle('Nissan', 'Leaf', '2015')

print car.make
print car.model
print car.year

carinfo = car.print_info()


contactinfo = sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)

print len(jordan.friends)

jordan.add_friend(sonny)

print jordan.friends

print sonny.greeting_count
sonny.greet(jordan)
print sonny.greeting_count

print sonny
