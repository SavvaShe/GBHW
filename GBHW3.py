# 1
def get_div(*args):

    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'result  {get_div()}')


# 2
'''
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
'''
def get_user (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(get_user(surname = 'Shebarin', name = 'Savva', year = '2002', city = 'Moscow', email = 'errordef@mail.ru', telephone = '8-800-555-35-35'))



# 3
def get_sum(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {get_sum(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')


# 4
def my_func(x, y):
    return x ** y
    
  
print(my_func(2, -3)) 
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
print(power(2,-3))    

# 5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()


# 6
'''
1 Вариант
def func(a):
        return a.title()
print(func("abca dsd"))
'''

'''
2 Вариант
'''
def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func("hello world"))