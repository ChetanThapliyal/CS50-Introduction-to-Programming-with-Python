print("meow")
print("meow")
print("meow")

# ---
i = 3
while i != 0:
    print("meow")
    i = i - 1
# ---
i = 0
while i < 3:
    print("meow")
    i = i + 1
# ---
for i in [0, 1, 2]:
    print("meow")
# ---
for i in range(3):
    print("meow")
# ---
for _ in range(3):
    print("meow")
# ---
print("meow\n"*3, end="")
# ---
while True:
    n = int(input("Enter value for n: "))
    if n < 0:
        continue
    else:
        break
# ---
while True:
    n = int(input("Enter value for n: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

def main():
    meow(3)

def get_number():
    while True:
        n = int(input("Enter value for n: "))
        if n > 0:
            break
# ---
def meow(n):
    for _ in range(n):
        print("meow")



# camelcase = input("camelcase: ")

# for letter in camelcase:
#     if letter.isupper():
#         print("_" + letter.lower(), end="")
#     else:
#         print(letter, end="")
# print()