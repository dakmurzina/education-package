import users, organizations

if __name__ == "__main__":
    print(f"The module \"Users\" contains Human, Teacher, and Student classes and {dir(users.Human)}, {dir(users.Student)}, and {dir(users.Teacher)} methods.")
    print(f"The module \"Organization\" contains School class and {dir(organizations.School)} methods.")
else:
    print("The modules \"Users\" and \"Organizations\" were successfully imported.")

