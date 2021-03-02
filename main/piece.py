import hexy as hx

class PieceTemplate(hx.HexTile):
    '''
    Interntal class to hold basic information
    about piece types. Generated when importing
    from settings file.
    '''
    def __init__(self, health, distance, attack):
        self.health = health
        self.distance = distance
        self.attack = attack

EmptyTemplate = PieceTemplate(0, 0, 0)

class Piece:
    EMPTY = 0
    INFANTRY = 1
    DEFENSE = 2
    SPEED = 3 

    '''
    Holds information about a piece on the board.
    Stores coordinates, piece type, owner, and 
    the PlayerTemplate it is based on.
    '''
    def __init__ (self, coordinates, p_type, player, template = EmptyTemplate):
        self.coordinates = coordinates
        self.p_type = p_type
        self.player = player
        self.max_health = template.health
        self.health = template.health
        self.distance = template.distance
        self.attack = template.attack
        self.template = template

    def get_piece_coords(self):
        return self.coordinates

    def get_piece_type(self):
        return self.p_type

    def get_player(self):
        return self.player

    def set_coords(self, new_coords):
        self.coordinates = new_coords

    def get_current_health(self):
        return self.health

    def get_distance(self):
        return self.distance

    def get_attack(self):
        return self.attack

    def get_template(self):
        return self.template
