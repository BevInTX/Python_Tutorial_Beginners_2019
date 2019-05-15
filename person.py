class Person:
    
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"hello, I am {self.name}")

def main():
    
    bev = Person("Bev")
    bev.talk()

if __name__ == "__main__":
    
    main()