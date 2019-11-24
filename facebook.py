users = []
posts = []
comments = []

class User():
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

	def post(self, post, date, likes, title):
		post1 = Post(post, date, likes, self.email, title)
		posts.append(post1)
		print(self.name + " has posted: " + post)
		post1.the_date(post1.date)

	def add_comment(self,comment, date, likes, title):
		for x in posts:
			if title == x.title:
				pst = x.title
		comment1 = Comment(comment, date, likes, self, pst)
		comments.append(comment1)
		print(self.name + " has commented " + comment + " on the post- " + pst)

	def get_useInfo(self):
		my_post = []
		for x in posts:
			if self.email == x.author:
				my_post.append(x)
		print("Name: " + self.name + "\nEmail: " + self.email + "\nPassword: " + self.password)
		print("Friends: " + str(self.friend_list) + "\nPosts: " + str(x.title))




class Post():
	def __init__ (self, comment, date, likes, author, title):
		self.comment = comment
		self.date = date
		self.likes = likes
		self.author = author
		self.title = title


	def remove_comment(self):
		self.list_comments.remove(comment)

	def the_date(self,date):
		print("posted on " + self.date)

	def add_like(self,likes):
		likes = likes + 1
		print("likes: " + str(likes) + "M")


class Comment(Post):
	def __init__ (self, comment, date, likes, author, title):
		Post.__init__(self, comment, date, likes, author, title)
		self.comment = comment



user1 = User("shoba", "shoba2004@meet.mit.sho", "shoba_the_king")
user2 = User("doba", "doba334@meet.mit.sym", "doba55512")

Iemail = input("what is your email?")
Ipass = input("what is your password?")
for x in users:
	if Iemail == x.email and Ipass == x.password:
		print(x.name + " you are logged in!")


user2.add_friend(user1.email)
user1.add_friend(user2.email)
user1.post("hey", "21.10", 32, "fir post")
user2.post("you", "3.2", 4, "se post")
user1.get_useInfo()
user2.remove_friend(user1.email)

user1.add_comment("yryyrry", "3.24", 233, "se post")

