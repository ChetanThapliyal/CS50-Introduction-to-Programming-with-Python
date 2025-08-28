# for _ in range(3):
#     print("#")

def main():
    print_square(3)
    # print_column(3)
    # print_rows(4)

# def print_column(height):
#     # for _ in range(3):
#     #     print("#")
#     print("#\n" * 3, end="")


# def print_rows(width):
#     print("?" * width)

def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("#", end="")
        print("#" * size)
        # print()


main()