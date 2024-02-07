def countStudents(students, sandwiches):
    count = 0
    while students and sandwiches:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0  
        else:
            student = students.pop(0)
            students.append(student)
            count += 1

        if count >= len(students):
            break

    return len(students)

print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))
print(countStudents([1,1,0,0], [0,1,0,1]))
