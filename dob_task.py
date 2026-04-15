import os

names = []
birthdates = []

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "DOB.txt")

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        item_list = line.strip().split()

        full_name = item_list[0] + " " + item_list[1]
        date_of_birth = " ".join(item_list[2:])

        names.append(full_name)
        birthdates.append(date_of_birth)

print("The list of names are:\n")
for name in names:
    print(f"{name}\n")

print("\nThe list of birthdates are:\n")
for date in birthdates:
    print(f"{date}\n")


