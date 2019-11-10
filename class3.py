class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self):
		print("Yummy!" + self.name + " is eating" + food)
	def description(self):
		print (self.name + " is " + self.age + "years old and loves the color" + self.favorite_color)
	def make_sound(self):
		print (self.sound + self.sound + self.sound)

class person(object):
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self):
		print(self.name + " is eating his favorite food = trash")
	def sport(self):
		print(self.name + " is playing his favorite sport = sleeping")

person1 = person("shoba doba", 72, "Jer", "other")
person1.eat()
person1.sport()

class bird(object):
	def __init__ (self,name,color,speed):
		self.name = name
		self.color = color 
		self.speed = speed
	def get_speed(self):
		return self.speed