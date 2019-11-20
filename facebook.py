users = []
posts = []
comments = []

class User ():
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friend_list = []

	def add_friend(self,email):
		self.friend_list.append(email)
		print(self.name + " has added " + self.email + " as a friend")

	def remove_friend(self, email):
		self.friend_list.remove(email)

	def post(self, post, date, likes):
		post1 = Post(comment, date, likes, self.email)
		posts.append(post1)
		print(self.name + " has posted: " + post)
		post1.the_date(post1.date)

	def get_useInfo(self):
		print("Name: " + self.name + "\nEmail: " + self.email + "\nPassword: " + self.password)
		print("Friends: " + str(self.friend_list) + "\nPosts: " + str(posts))




class Post():
	def __init__ (self, comment, date, likes, author):
		self.comment = comment
		self.date = date
		self.likes = likes
		self.author = author

	def add_comment(self,comment, date, likes, author):
		comment1 = comment(comment, date, likes, self)
		comments.append(comment)
		print("your comment is " + self.comment)
		print("the other comments are: " + str(self.list_comments))

	def remove_comment(self):
		self.list_comments.remove(comment)

	def the_date(self,date):
		print("posted on " + self.date)

	def add_like(self,likes):
		likes = likes + 1
		print("likes: " + str(likes) + "M")


class comment(Post):
	def __init__ (self):
		Post.__init__(self)
		self.c_text = c_text



user1 = User("shoba", "shoba2004@meet.mit.sho", "shoba_the_king")
user2 = User("doba", "doba334@meet.mit.sym", "doba55512")

user2.add_friend(user1.email)
user1.add_friend(user2.email)
user1.post("hey", "21.10", 32)
user2.post("you", "3.2", 4)
user1.get_useInfo()
user2.remove_friend(user1.email)




