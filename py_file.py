""" A simple social network for tracking connections between people. """

class Person:
    """ A person in the social network. 
    
    Attributes:
        name (str): the person's name.
        connections (set of Person): other people in the social network
            who know this person.
    """
    def __init__(self, name):
        """ Initialize a new Person object. """
        self.name = name
        self.connections = set()

    def connect(self, person2):
        """ Connect with person2. 
        
        Args:
            Person2 (Person): the other person to connect to.
        """
        