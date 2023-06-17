class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
# ... (class definition and large list of players here)
    @classmethod
    def create_team(cls, data):
        new_team = []
        for members in data:
            new_team.append(cls(members))
        return new_team

# Write your for loop here to populate the new_team variable with Player objects.
    

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

kevin_durant = Player(kevin)
print(kevin_durant.name)

jason_tatum = Player(jason)
print(jason_tatum.name)

Player.create_team(kevin)