# {First_name+Last_name: {subj.name:[mark1, mark2, ...]}}
students = dict()
students = {'Иванов Иван':{}}
# Список предметов: [name1, name2, ....]
# subjects = list()
subjects = ['Химия', 'Физика', 'Математика']

# список оценок
marks = ['1', '2', '3', '4', '5']

def get_subjects():
    return tuple(subjects)

def add_subject(subj_name:str):
    if subj_name not in subjects:
        subjects.append(subj_name)

def get_student(key):
    return tuple([key, students[key]])

def get_students_list():
    for key in students:
        get_student(key)


def assign_subjects_to_student():
    for stud in students:
        for subj in subjects:
            students[stud][subj] = []

def add_student(initials:tuple): 
        students[' '.join(initials)] = {}

def get_mark():
    pass

# (students[stud][subj], mark)
def set_student_mark(): 
    for stud in students:
        for subj in students[stud]:
            students[stud][subj].append('5')

# todo: Добавить функции, апдейтящие студентов новыми предметами
#       Добавить функцию, апдейтящую нового студена предметами
assign_subjects_to_student()
set_student_mark()
print(students)