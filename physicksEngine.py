from Errors import *
from math import *


class Vec2:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y
    
    def norm(self):
        try:
            return self / self.mag()
        except ZeroDivisionError:
            return Vec2(1, 0)

    def __add__(self, other):
        if type(other) != Vec2:
            raise TypeError(f"Can't add Vec2 and {type(other)} not suported")
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) != Vec2:
            raise TypeError(f"Can't subtract Vec2 and {type(other)} not suported")
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, value: int | float):
        if type(value) not in [int, float]:
            raise TypeError(f"Can't multuply Vec2 by {type(value)} not suported")
        return Vec2(self.x*value, self.y*value)
    
    def __truediv__(self, value: int | float):
        if type(value) not in [int, float]:
            raise TypeError(f"Can't devide Vec2 by {type(value)} not suported")
        return Vec2(self.x/value, self.y/value)

    def mag(self):
        return sqrt(abs(self.x + self.y))

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

class Geometry:
    def __init__(self, config_file: str):
        self.edges = []
        self.vertesies = []
        
        stage = 0

        with open(config_file, "r") as file:
            for n, line in enumerate(file.readlines()):
                if line == "|\n":
                    stage += 1
                    continue

                x, y = line.split(" ")

                try:
                    tuple_ = (int(x), int(y))
                except ValueError:
                    raise FileFormatError(f"format error on line {n} | {line}")
                
                match stage:
                    case 0:
                        self.vertesies.append(tuple_)
                    case 1:
                        self.edges.append(tuple_)
                    case _:
                        raise FileFormatError(f"format error too many states")
                

    def __repr__(self) -> str:
        return f"edges: {self.edges}\nvertesies: {self.vertesies}"

class Object:
    def __init__(self, geometry: Geometry):
        pass

if __name__ == "__main__":
    #geometry = Geometry("geometryes/sqere.geo")
    #print(geometry)

    vec = Vec2(5, 6)
    print(vec.norm())