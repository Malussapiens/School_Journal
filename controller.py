import model
import view

initials = ['Фамилия', 'Имя']

def get_student_entry():
    temp = []
    for name in initials:
        temp.append(view.get_user_input(name))
    model.add_student(tuple(temp))
# # Добавляем предмет(ы)
# while input('Добавить предмет (д/н)').lower() != 'н':
#     model.add_subject(view.get_user_input('Введите название предмета:'))
# else:
#     print('Всего доброго!')

# # Печатаем запись
# view.show_entry(model.get_subjects())

get_student_entry()

for key in model.students:
    view.show_entry(model.get_student(key))


# model.add_student()

