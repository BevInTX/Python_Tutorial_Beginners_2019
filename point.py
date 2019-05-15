########################################################################
class Point:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

def main():
    point1 = Point(10, 20)
    print(point1.x, point1.y)
    point1.draw()
    point1.move()

if __name__ == "__main__":
    
    main()
        
        
    
    