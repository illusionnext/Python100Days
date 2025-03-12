import sys

name = input("What is your name?").title()
print(f"Hello {name}! Welcome to the Band Name Generator", file=sys.stderr, end="!\n")

city = input("What is your favorite city?").strip().replace(" ", "")
pet = input("What is your favorite pet name ever?").strip().replace(" ", "")
print(
    f"Your band name could one of these {pet}{city}🐈‍⬛🌆 or {city}{pet}🌆🐈‍⬛",
    file=sys.stderr,
    end="!\n",
)
