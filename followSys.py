class FollowSystem:
    def __init__(self):
        self.follows = {}  # Maps user IDs to a set of followee IDs

    def follow(self, user_id: str, followee_id: str):
        if user_id not in self.follows:
            self.follows[user_id] = set()
        self.follows[user_id].add(followee_id)
        if followee_id not in self.follows:  # Ensure every user is in the follows dict
            self.follows[followee_id] = set()

    def unfollow(self, user_id: str, followee_id: str):
        if user_id in self.follows and followee_id in self.follows[user_id]:
            self.follows[user_id].remove(followee_id)

    def get_followers(self, user_id: str):
        return [user for user, followees in self.follows.items() if user_id in followees]

    def get_mutual_followers(self, user1_id: str, user2_id: str):
        user1_followers = set(self.get_followers(user1_id))
        user2_followers = set(self.get_followers(user2_id))
        return list(user1_followers.intersection(user2_followers))

# Example usage:
fs = FollowSystem()
fs.follow("user1", "user2")
fs.follow("user3", "user2")
print(fs.get_followers("user2"))  # Should print ['user1', 'user3']
fs.follow("user1", "user3")
print(fs.get_mutual_followers("user2", "user3"))  # Should print ['user1']
fs.unfollow("user1", "user2")
print(fs.get_followers("user2")) 