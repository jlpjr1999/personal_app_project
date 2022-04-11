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
    
    def connect(self, other):
        """ Create a symmetrical connection to another Person object.
        
        Args:
            other (Person): another Person object.
            
        Side effects:
            Modifies self.connections and other.connections.
        """
        if other not in self.connections:
            self.connections.add(other)
            other.connect(self)
