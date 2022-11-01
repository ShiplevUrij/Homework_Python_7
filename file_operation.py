from user_interface import get_data as gd

info = gd()
def writing_csv ():
    file = 'Phonebook.csv'
    print('data', info)
    with open (file, 'a') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_docx ():
    file = 'Phonebook.docx'
    with open (file, 'a') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nПримечание: {info[3]}\n\n\n')

def open_csv ():
    with open('Phonebook.csv', 'r') as data:
        text_phone = data.read()
    print(text_phone)