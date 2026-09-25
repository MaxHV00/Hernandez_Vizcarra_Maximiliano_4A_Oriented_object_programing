class Post:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def show(self):
        print(f"{self.author.name} has post: {self.text}")


class Comment:
    def __init__(self, text, author, post):
        self.text = text
        self.author = author
        self.post = post

    def show(self):
        print(f"{self.author.name} commented on {self.post.author.name}'s post: {self.text}")


class User:
    def __init__(self, name, email, age, password):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__password = password

    @property
    def name(self):
        return self.__name

    def create_post(self, text):
        return Post(text, self)

    def show_post(self, post):
        print(f"{self.name} has post: {post.text}")

    def create_comment(self, text, post):
        return Comment(text, self, post)

    def send_message(self, text, receiver):
        print(f"{self.name} sends a message to {receiver.name}: {text}")


user = User("Carlos", "carlos@email.com", 20, "1234")
post = user.create_post("I am learning Python!")
user.show_post(post)
