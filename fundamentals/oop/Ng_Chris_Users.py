class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_cards_points = 0
    def display_intro(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_cards_points}")
        return self
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
        return self
    def spend_points(self, amount):
        if self.gold_cards_points < amount:
            print("Not Enough Reward Points")
        else:
            self.gold_cards_points = (self.gold_cards_points - amount)
        return self

user_chris = user("Chris","Ng","ngchris123@hotmail.com", 28)
user_ela = user("Ela", "Tedjokusumo", "berrybug@gmail.com", 25)
user_kya = user("Kya", "Tedjokusumo", "kya@gmail.com", 2)

# user_chris.enroll() #enrolling new user
# print(user_chris.is_rewards_member)

# print(user_chris.gold_cards_points)
# user_chris.spend_points(50) #spending points
# print(user_chris.gold_cards_points)

# user_ela.enroll() #testing with new user
# print(user_ela.gold_cards_points)
# user_ela.spend_points(80) #testing with different value
# print(user_ela.gold_cards_points)

# user_chris.enroll() #testing to see a response when a member is already a member
# user_kya.spend_points(40) # testing to see response if member attempts to spend more points that member has available

# user_chris.display_intro()
# user_ela.display_intro()
# user_kya.display_intro()

#to be more efficient
user_chris.display_intro().enroll().spend_points(50).display_intro()
user_ela.display_intro().enroll().spend_points(80).display_intro()
user_kya.display_intro().spend_points(40).display_intro()