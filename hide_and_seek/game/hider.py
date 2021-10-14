import random

class Hider:

    def __init__(self):

        #Chose Where the hider is
        self.location = random.randint(1,1000)
        self.distance = [0, 0]

    # Give a hint of how close the seeker is
    def get_hint(self):
        hint = "Shall we start"
        if self.distance[-1] == 0:
            hint = "You found Me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "Your getting Warmer."
        elif self.distance[-1] < self.distance[-2]:
            hint = "Your getting Colder"
        return hint
    

    #see how close the finder is
    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)