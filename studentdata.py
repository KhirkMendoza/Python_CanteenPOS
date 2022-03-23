def student_data():
    """
---------- Enter Details ----------
    """

    student_name_269 = input("Student Name: ")
    id_269 = input("ID Number: ")
    year_269 = input("Year Level: ")
    course_section_269 = input("Course and Section: ")

    student_dict = {
        'Student_Name': student_name_269,
        'ID': id_269,
        'Year': year_269,
        'Course_Section': course_section_269,
        'Wallet_Value': 150.00
    }

    print("\nYour Details:")
    print('Student Name: ' + student_dict['Student_Name'].title())
    print('ID Number: ' + student_dict['ID'].title())
    print('Year Level: ' + student_dict['Year'].title())
    print("Course and Section: " + student_dict['Course_Section'].title())
    print('Initial Wallet Value: ' + str(student_dict['Wallet_Value']))

    confirm = ' '
    while confirm != 'yes':
        confirm = input("\nChange Details? (Yes or No): ").lower()
        if confirm == 'no':
            return student_dict
    return student_data()


print(student_data.__doc__)
sd = student_data()
