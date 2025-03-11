import sys

name = input("What is your name?").title()
print(f"Hello {name}", file=sys.stderr, end="!\n")
print(name)

city = input("What is your favorite city?").strip().replace(" ", "")
pet = input("What is your favorite pet name ever ?").strip().replace(" ", "")
print(f"Your band name is {pet}{city} ! 🐈‍⬛🌆", file=sys.stderr, end="\n")
