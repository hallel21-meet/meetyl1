class User ():
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friend_list = []
		self.posts = []
	def add_friend(self,email):
		self.friend_list.append(email)
		print(self.name + " has added " + self.email + " as a friend")
	def remove_friend(self, email):
		remove_friend.remove(email)
	def post(self,text):
		self.posts.append(text)
		print(self.name + " has posted: " + text)
	def get_useInfo(self):
		print("Name: " + self.name + "\nEmail: " + self.email + "\nPassword: " + self.password + "\nFriends: " + self.friend_list + "\nPosts: " + self.posts)

user1 = User("shoba", "shoba2004@meet.mit.sho", "shoba_the_king")
user2 = User("doba", "doba334@meet.mit.sym", "doba55512")

user2.add_friend(user1.email)
user1.add_friend(user2.email)
user1.post("hey")
user2.post("you")
user1.get_useInfo()