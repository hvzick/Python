class Youtube:
    def __init__(self, n, s=0, f=0):
        self.name = n
        self.subs = s
        self.following = f

    def follow(self, user):
        user.subs += 1
        self.following += 1


user1 = Youtube('Hazik')
user2 = Youtube('Faik')
user1.follow(user2)
user2.follow(user1)
print(user1.name)
print(user1.subs)
print(user1.following)
print(user2.name)
print(user2.subs)
print(user2.following)
