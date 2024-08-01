#beds how many are red, blue, green with probability
#if mutually exclusive just use if, if inclusive use elif
import random
class Bed:
    def __init__(self):
        self.lst = []
        self.amount = int(input("How many total beds are there: "))
    def bed_list(self):
        for _ in range(self.amount):
            random_number = random.randint(1, 5)
            if random_number == 1 or random_number == 4:
                self.lst.append("red")
            elif random_number == 2 or random_number == 3:
                self.lst.append("blue")
            else:
                self.lst.append("green")
        count_red = self.lst.count("red")
        count_green = self.lst.count("green")
        count_blue = self.lst.count("blue")
        total_count = count_blue + count_green + count_red
        print(f"There are {count_red} red beds out of {self.amount} beds")
        print(f"There are {count_green} green beds out of {self.amount} beds")
        print(f"There are {count_blue} blue beds out of {self.amount} beds")
        print(f"{total_count} out of {self.amount} beds")
def main():
    run = Bed()
    run.bed_list()
main()