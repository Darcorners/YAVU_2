print("Введите 1 число: ")
First = float(input())
print("Введите 2 число: ")
Second = float(input())
ResultF= float()
ResultS= float()
def Chastnoe():

    try:
        ResultF = First / Second
        print(f"Деление 1 числа на 2 = {ResultF}")
        ResultS = Second / First
        print(f"Деление 2 числа на 1 = {ResultS}")
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except ValueError:
        print('Недопустимое значение')

def Raznost():
    ResultF = First - Second
    if ResultF == 0:
        print('Разность ДОЛЖНА быть положительной')
    else:
        print(f"Разность 1 числа со 2 = {ResultF}")
    ResultS = Second - First
    if ResultS == 0:
        print('Разность ДОЛЖНА быть положительной')
    else:
        print(f"Разность 1 числа со 2 = {ResultS}")