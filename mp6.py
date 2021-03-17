import csv

def show_menu():
    print("(1)Input Project Details")
    print("(2)View Projects")
    print("(3)Schedule Projects")
    print("(4)Get Project")
    print("(5)Exit")


def enter_project():

    infile = open("proj.csv", "r")
    creader = csv.reader(infile)
    id_number = input("Enter ID Number: ")
    flag = True
    while flag:
        for row in infile:
            if id_number in row:
                print("ID already exists.")
                id_number = input("Enter ID Number: ")

            else:
                flag = False

    infile.close()
    project_title = input("Enter project title: ")
    project_size = input("Enter number of pages: ")
    project_priority = input("Enter priority: ")




    file = open("proj.csv", "a", newline="\n")
    cwriter = csv.writer(file)
    cwriter.writerow([project_priority, project_title, project_size, id_number])

    file.close()



def show_submenu2():
    print("(1)One Project")
    print("(2)Show completed project")
    print("(3)Show all projects")


def submenu21(proj_id):
    file = open("proj.csv", "r", encoding='utf-8-sig')
    table = csv.DictReader(file)
    proj = {}

    try:
        for row in table:
            proj[row["ID"]] = {k: v for k, v in row.items() if k != 'ID'}
        print(proj[proj_id])
    except EOFError:
        print("ID does not exist.")

    file.close()

def submenu23():

    with open('proj.csv', 'r') as file:
        csv_input = csv.DictReader(file)
        data = sorted(csv_input, key=lambda row: (row['Priority'], row['Size']))

    with open('queue.csv', 'w') as outfile:
        csv_output = csv.DictWriter(outfile, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)
        for rows in data:
            print(rows)


def show_submenu3():
    print("(1)Create Schedule")
    print("(2)View Updated Schedule")


def show_submenu4():
    print("unimplemented")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            enter_project()

        elif choice == "2":
            show_submenu2()
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                input_id = int(input("Enter ID to be searched: "))
                submenu21(str(input_id))

            elif sub_choice == "2":
                print("Unimplemented")

            elif sub_choice == "3":
                submenu23()

        elif choice == "3":
            print("Unimplemented")

        elif choice == "4":
            print("Unimplemented")

        elif choice == "5":
            exit()

        else:
            print("Invalid Input")


main()
