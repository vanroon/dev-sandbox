class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## PErson has-a name
		self.name = name
		## Person has-a pet
		self.pet = pet

## Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
	
		super(Employee, self).__init__(name)

		## Employee is-a person and Person has-a name

		self.salary = salary


