# Lists
# students = ["Harry", "Hermione", "Ron"]
# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(students[i])

# for i in range(len(students)):
#     print(i + 1, students[i])

# Dictionary
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# # print(students["Hermione"])

# for student in students:
#     print(student, students[student], sep=' - ')

students = [
    {"name": "Hermione", "House": "Geyffindor", "Patronus": "Otter"},
    {"name": "Harry", "House": "Geyffindor", "Patronus": "Stag"},
    {"name": "Ron", "House": "Geyffindor", "Patronus": "Jack Russel Terrier"},
    {"name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students:
    print(student["name"])