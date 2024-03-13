
from usefull import *
from time import sleep

p = []
arq = 'people.txt'


if fileExist(arq) == False:
    print('Not found!')
    create(arq)
while True:
    title('MAIN MENU')

    option = menu(['Show users: ','New user','Exit'])

    if option == '1':
        title('USERS JOINED')
        op(arq)
    elif option == '2':
        title('NEW USER')
        name = str(input('Enter new user name: '))
        age = str(input("Enter user's age: "))
        register(arq,name,age)


    elif option == '3':
        title('EXITING...')
        sleep(1)
        break
    else:
        print('\033[31mINVALID!\033[m')
    