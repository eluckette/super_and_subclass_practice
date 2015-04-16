"""This file should have our melon-type classes in it."""
BASE_PRICE = 5

class Melon(object):

    def __init__(self, species, color, imported, shape, seasons):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons

class Watermelon(Melon):

    def get_price(self, qty):
         
        total = qty * BASE_PRICE

        if qty >= 3:
            total = .75 * total

        return total

    def __init__(self, species = 'Watermelon', color = 'green', imported = False, shape = 'natural', seasons = ['Fall', 'Summer']):
        
        return super(Watermelon, self).__init__(species, color, imported, shape, seasons)


class Canteloupe(Melon):

    def get_price(self,qty):
        total = qty * BASE_PRICE

        if qty >= 5:
            total = .5 * total

        return total

    def __init__(self, species = 'Canteloupe', color = 'tan', imported = False, shape = 'natural', seasons =['Spring', 'Summer']):

        return super(Canteloupe, self).__init__(species, color, imported, shape, seasons)

class Casaba(Melon):

    def get_price(self, qty):
        total = qty * 1.5 * (BASE_PRICE + 1)
        
        return total

    def __init__(self, species = 'Casaba', color = 'green', imported = True, shape = 'natural', seasons = ['Winter', 'Fall']):
        return super(Casaba,self).__init__(species, color, imported, shape, seasons)

class Sharlyn(Melon):

    def get_price(self, qty):
        total = qty * 1.5 * BASE_PRICE
        
        return total

    def __init__(self, species = 'Sharlyn', color = 'tan', imported = True, shape = 'natural', seasons = ['Summer']):
        return super(Sharlyn, self).__init__(species, color, imported, shape, seasons)

class SantaClaus(Melon):

    def get_price(self, qty):
        total = qty * 1.5 * BASE_PRICE
        
        return total

    def __init__(self, species = 'SantaClaus', color = 'green', imported = True, shape = 'natural', seasons = ['Winter','Spring']):
        return super(SantaClaus,self).__init__(species, color, imported, shape, seasons)

class Christmas(Melon):

    def get_price(self, qty):
        total = qty * BASE_PRICE
        
        return total

    def __init__(self, species = 'Christmas', color = 'green', imported = False, shape = 'natural', seasons = ['Winter','Spring']):
        return super(Christmas,self).__init__(species, color, imported, shape, seasons)

class HornedMelon(Melon):

    def get_price(self, qty):
        total = qty * 1.5 * BASE_PRICE
        
        return total

    def __init__(self, species = 'HornedMelon', color ='yellow', imported = True, shape = 'natural', seasons =['Summer']):
        return super(HornedMelon,self).__init__(species, color, imported, shape, seasons)

class Xigua(Melon):

    def get_price(self, qty):
        total = qty * 1.5 * (2 * BASE_PRICE)
        
        return total

    def __init__(self, species = 'Xigua', color = 'black', imported = True, shape = 'square', seasons = ['Summer']):
        return super(Xigua,self).__init__(species, color, imported, shape, seasons)

class Ogen(Melon):

    def get_price(self, qty):
        total = qty * (BASE_PRICE + 1)
        
        return total

    def __init__(self, species = 'Ogen', color = 'tan', imported = False, shape = 'natural', seasons = ['Spring','Summer']):
        return super(Ogen,self).__init__(species, color, imported, shape, seasons)





