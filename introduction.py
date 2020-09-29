class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self,name):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")


def main():
    # Set name of Shark object
    sammy = Shark("Sammy")
    sammy.swim("fish")
    sammy.be_awesome()


if __name__ == "__main__":
    main()