class Post:
    def __init__(self, content, author, number_of_likes):
        self.content = content
        self.author = author
        self.number_of_likes = number_of_likes

    def __number_of_likes(self):
        return self.number_of_likes

    def display_the_post(self, name_of_post):
        return f"Post: {str(name_of_post).capitalize()}\n" \
               f"Author: {str(self.author).capitalize()}\n" \
               f"Content: {self.content}\n" \
               f"Likes: {self.number_of_likes}"


post = Post("entertainment", "John Rock", 1298)
print(post.display_the_post("Beautiful nature"))
