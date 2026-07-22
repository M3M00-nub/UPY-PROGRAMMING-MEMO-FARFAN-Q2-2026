
users = {
    'jpedrozo':{'password': '1234', 'rol': 'professor',   'name': 'Jorge Pedrozo'},
    'dgamboa':{'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'},
    'jperez':{'password': '1234', 'rol': 'student',     'name': 'Juan Pérez'},
    'dromo':{'password': '1234', 'rol': 'student',     'name': 'Daniela Romo'},
    'mjuarez':{'password': '1234', 'rol': 'student',     'name': 'Mauricio Juárez'},
    'mlopez':{'password': '1234', 'rol': 'student',     'name': 'María López'},
    'auh':{'password': '1234', 'rol': 'student',     'name': 'Abraham Uh'},
    'amolina':{'password': '1234', 'rol': 'student',     'name': 'Armando Molina'}
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0,
        'Differential Calculus': 7.8, 'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4,
        'Differential Calculus': 6.2, 'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5,
        'Differential Calculus': 7.0, 'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2,
        'Differential Calculus': 9.0, 'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'auh': {
        'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8,
        'Differential Calculus': 6.0, 'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'amolina': {
        'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5,
        'Differential Calculus': 6.6, 'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}


logged_in = False

while logged_in == False:
    print("₊˚ ✧ ‿︵‿୨୧‿︵‿ ✧ ₊˚ SCHOOL MANAGMENT SYSTEM ₊˚ ✧ ‿︵‿୨୧‿︵‿ ✧ ₊˚")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]['password'] == password:
        logged_in = True
        role = users[username]['rol']
        name = users[username]['name']
        print("\nBienvenid@!, " + name + " (" + role + ")")
        print("₊˚ ✧ ‿︵‿୨୧‿︵‿ ✧ ₊˚")
    else:
        print("Wrong user/password!\n")



if role == 'student':
    print("⋆⁺₊⋆ ━━━━⊱༒︎ • ༒︎⊰━━━━ ⋆⁺₊⋆ School Report: " + name + " ⋆⁺₊⋆ ━━━━⊱༒︎ • ༒︎⊰━━━━ ⋆⁺₊⋆")
    aprobadas = set()
    pendientes = set()
    for subject in subjects:
        grade = notes[username][subject]
        print(subject + ": " + str(grade))
        if grade >= 7.0:
            aprobadas.add(subject)
        else:
            pendientes.add(subject)
    print("\nApproved:  ", aprobadas)
    print("Pending: ", pendientes)


elif role == 'professor':
    print("╭┈ • ┈ ୨୧ ┈ • ┈╮ STUDENT LIST ╭┈ • ┈ ୨୧ ┈ • ┈╮")

    for student_key in notes:
        print("- " + student_key + " → " + users[student_key]['name'])

    print()
    student_to_edit = input("Enter the username of the student to grade: ")

    if student_to_edit in notes:
        print("\nSubjects:")

        for subject in subjects:
            print("- " + subject)

        subject_to_edit = input("\nEnter the subject to edit: ")

        if subject_to_edit in notes[student_to_edit]:
            new_grade = input("Enter the new grade: ")

            old_grade = notes[student_to_edit][subject_to_edit]

            print("\nDo you confirm (yes/no)?")
            print(f"{subject_to_edit}: {old_grade} ==> {new_grade}")
            confirm = input()

            if confirm.lower() == "yes":
                notes[student_to_edit][subject_to_edit] = float(new_grade)
                print("\nGrade updated successfully.")
                print(users[student_to_edit]['name'] + " - " + subject_to_edit + ": " + str(new_grade))
            elif confirm.lower() == "no":
                print("\nGrade change cancelled.\n")

        else:
            print("\nEsa materia no existe.\n")

    else:
        print("\nEse usuario no existe.\n")



elif role == 'coordinator':
    print("⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠄,  COORDINATOR REPORT⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠄, \n")
    print("PROFESSORS:")
    print("Jorge Pedrozo (jpedrozo)\n")

    print("STUDENTS:")
    for student_key in notes:
        print("- " + student_key + " → " + users[student_key]['name'])

    print("\nRECORDS:")
    for student_key in notes:
        print("\n" + users[student_key]['name'] + " (" + student_key + ")")
        for subject in subjects:
            grade = notes[student_key][subject]
            print("  " + subject + ": " + str(grade))