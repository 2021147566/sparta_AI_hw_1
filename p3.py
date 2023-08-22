import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        return f"{self.name}: {self.username}"

    def create_member():
        num_members = int(input("How many members do you want to create? "))
        print("\n")
        for num in range(num_members):
            print("{0:-^27}".format(" Member Info "))
            name = input("{:>12}".format("Name: "))
            username = input("{:>12}".format("ID: "))
            password = input("{:>12}".format("Password: "))
            member = Member(name, username, password)
            members.append(member)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def create_post():
        num_posts = int(input("How many posts do you want to create? "))
        for num in range(num_posts):
            title = input("\n Post title: ")
            content = input("Post content: ")
            author_username = input("Post author ID: ")
            post = Post(title, content, author_username)
            posts.append(post)


# Create member instances
members = []
Member.create_member()

while len(members) < 3:
    print("Member number is less than 3. Please create more members.")
    Member.create_member()

# Display member names
print("\n")
print("{0:-^27}".format(" RESULT "))
for member in members:
    print(member.display())
print("\n")

# Create post instances
posts = []

Post.create_post()

for member in members:
    love = sum(1 for post in posts if post.author == member.username)
    while love < 3:
        print(f"{member.username} has less than 3 posts. Please create more posts.")
        Post.create_post()
        love = sum(1 for post in posts if post.author == member.username)

# Display titles of posts by a specific user
specific_user = input("ID of the author: ")
for post in posts:
    if post.author == specific_user:
        print(f"Post title by {specific_user}: {post.title}")

# Display titles of posts containing a specific word in content
specific_word = input("Keyword:")
for post in posts:
    if specific_word.lower() in post.content.lower():
        print(f"Post title containing '{specific_word}': {post.title}")
