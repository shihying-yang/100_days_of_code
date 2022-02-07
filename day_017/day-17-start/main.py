"""Class tutorial"""


class User:
    """[summary]"""

    def __init__(self, id, username):
        """[summary]

        :param id: [description]
        :type id: [type]
        :param username: [description]
        :type username: [type]
        """
        # print("new uer being created...")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "sean")
# user_1.id = "001"
# user_1.username = "sean"

# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

user_2 = User("002", "jack")
# user_2.id = "002"
# user_2.username = "jack"

# print(user_2.id)
# print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
