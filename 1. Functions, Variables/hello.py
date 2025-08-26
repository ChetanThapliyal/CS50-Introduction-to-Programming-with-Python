# print ("Hello, World!!")

name = input("What is your name? ").strip().title()


# first, last = name.split()


# print(f"Hello, {name}!")
# print(f"Hello, {first}!")
# print(f"Hello, {last}!")


def hello(to="world"):
    print("Hello,", to)

hello(name)
hello()