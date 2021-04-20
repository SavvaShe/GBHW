# 1
my_int = 10
my_float = 1.4
my_string = "hello world"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Moscow', 'country': 'Russia'}

super_list = [my_int, my_float, my_string, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')


# 2
my_list = ['1', 'b', '3', 'd', ]
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)


#3
number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month_list = list(month_dict.values())
    if number <= 2 or number == 12:
        seasons = 'Winter'
    elif number > 2  and number<= 5:
        seasons = 'Spring'
    elif number > 5 and number<= 8:
        seasons = 'Summer'
    elif number > 8 and number<= 11:
        seasons = 'Autumn'    
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Month from list is {month_list[i]},seasons is {seasons}")
            break
    print(f"Month from dict is {month_dict[number]},seasons is {seasons}")
else:
    print("You made a mistake")
    

# 4
my_str = input("Enter string: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i} : {el};")


5
my_list = [74765, 4234, 321, 2]
print(f'Rating before your result {my_list}')
number = int(input("Enter your result : "))
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(f'Rating with your result {my_list}')


# 6
my_dict = []
number = int(input("Enter product number: "))
for i in range(number):
    features = {}
    f_key = input("Enter feature product: ")
    f_value = input("Enter feature value product: ")
    features[f_key] = f_value
    my_dict.append(tuple([number, features]))
print(my_dict)
analysis = {}
for i in my_dict:
    for f_key, f_value in i[1].items():
        if f_key in analysis:
            analysis[f_key].append(f_value)
        else:
         analysis[f_key] = [f_value]
print(analysis)