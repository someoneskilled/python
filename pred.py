class Human:
    def __init__(self, name):
        self.name = name

class Intelligent:
    def __init__(self, entity):
        self.entity = entity

def is_some_humans_intelligent(humans):
    for human in humans:
        if isinstance(human, Intelligent):
            return True
    return False

# Example usage
alice = Human("Alice")
bob = Human("Bob")
charlie = Intelligent(Human("Charlie"))

humans = [alice, bob, charlie]

if is_some_humans_intelligent(humans):
    print("Some humans are intelligent.")
else:
    print("No humans are intelligent.")
