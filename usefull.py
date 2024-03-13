from time import sleep

def line(n = 30):
    print('-'*n)

def title(txt, n = 30):
    line()
    print(txt.center(n))
    line()

def menu(list):
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[34m - {item}\033[m')
        c += 1
    line()
    opt = str(input('Choose your option: '))
    return opt

def fileExist(t):
    try:
        a = open(t,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def create(name):
    try:
        f = open(name,'wt+')
    except:
        print('Error in file creation!')
    else: 
        print(f'File {name} created!')

def op(file):
    try:
        a = open(file, 'rt')
    except:
        print('Error reading file')
    else:
        sleep(0.2)
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<20}{data[1]:>3} years')
        sleep(1)

def register(arc,n = 'unknown',a = 0):
    try:
        txt = open(arc,'at',encoding = 'utf-8')
    except:
        print('Error!')
    else:
        try:
            txt.write(f'{n};{a}\n')
        except:
            print('Error!')
