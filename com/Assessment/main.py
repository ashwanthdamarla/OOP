import pandas as pd
from datetime import datetime


def NegativeNumberException(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0:
            return func(*args, **kwargs)
        else:
            raise ArithmeticError(
                'A number needs to be a positive integer to call the function {}. Your chosen value: {}'.format(
                    func.__name__, *args))

    return wrapper


factorial_arr = []


@NegativeNumberException
def factorial(n):
    if len(factorial_arr) == 0:
        factorial_arr.append(1)

    if len(factorial_arr) - 1 < int(n):
        for i in range(len(factorial_arr), int(n) + 1):
            factorial_arr.append(i * factorial_arr[i - 1])
    return factorial_arr[len(factorial_arr) - 1]


def factorial_recursion(n):
    if n >= 0:
        if int(n) == 0 or int(n) == 1:
            return 1
        return int(n) * factorial_recursion(int(n) - 1)
    else:
        raise ArithmeticError(
            'A number needs to be a positive integer to call the function {}. Your chosen value: {}'.format(
                factorial_recursion.__name__, n))


@NegativeNumberException
def fibonacci(number):
    if int(number) == 0 or int(number) == 1:
        return int(number)
    return int(number) + fibonacci(int(number) - 1)


list_pascal_triangle = []


@NegativeNumberException
def pascal_triangle(n):
    if int(n) < len(list_pascal_triangle):
        print('returning cached value')
        return [list_pascal_triangle[i] for i in range(n + 1)]

    for i in range(len(list_pascal_triangle), n + 1):
        if i == 0:
            list_pascal_triangle.append([1])
            continue
        dump = []
        for j in range(0, i):
            if j == 0:
                dump.append(1)
                continue
            if j == i:
                dump.append(1)
                continue
            if j == int(i / 2):
                if i % 2 == 0:
                    dump.extend(dump[::-1])
                else:
                    dump.extend([list_pascal_triangle[i - 1][j - 1] + list_pascal_triangle[i - 1][j], *dump[::-1]])
            elif j <= int(i / 2):
                dump.append(list_pascal_triangle[i - 1][j - 1] + list_pascal_triangle[i - 1][j])
        # print(dump)
        list_pascal_triangle.append(dump)
    return list_pascal_triangle


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def calculate(*args, **kwargs):
    if 'add' == kwargs['operation']:
        return args[0] + args[1]
    if 'subtract' == kwargs['operation']:
        return args[0] - args[1]


def calculate_v2(func, *args):
    return func(*args)


if __name__ == '__main__':
    '''
        Calculation arithmetic operations using keyword parameters
    '''
    print(calculate(1, 2, operation='add'))
    print(calculate(2, 1, operation='subtract'))

    '''
        Calculating arithmetic operations through passing operating function to calculator 
    '''
    print(calculate_v2(add, 1, 2))
    print(calculate_v2(subtract, 1, 2))
    print(calculate_v2(multiply, 1, 2))

    '''
        Banking Dataset questions
    '''
    bank_df = pd.read_csv('bank.csv', sep=';')
    print(bank_df.head())
    print(bank_df.columns)
    ################
    print()
    print('Average Balance by age:')
    print(bank_df.groupby('age')['balance'].mean())

    ################
    print()
    print('Age with highest loans:')
    df = bank_df[bank_df.loan == 'yes'].groupby('age')['loan'].count()
    df = df.reset_index()
    print(df.iloc[df['loan'].argmax()])

    # print(pd.cut(bank_df['age'], 4))

    ################
    bins = [0, 20, 40, 60, 120]
    labels = ['<20', '>20, <40', '>40, <60', '>60']
    bank_df['age-group'] = pd.cut(bank_df['age'], bins=bins, labels=labels, right=False)
    print()
    print('Counts across different age groups:')
    print(bank_df.groupby('age-group')['age-group'].count())

    ################
    print()
    print('Average Balance by job category:')
    print(bank_df.groupby('job')['balance'].mean())

    ################
    print()
    print('Average Balance by job category and across different age values:')
    print(bank_df.groupby(['job', 'age'])['balance'].mean())

    ################
    print()
    print('Maximum Impact on campaign by age group:')
    df2 = bank_df.groupby('age-group')['campaign'].sum()
    df2 = df2.reset_index()
    print(df2.iloc[df2['campaign'].argmax()])

    ################
    print()
    print('Maximum Impact on campaign by education:')
    df3 = bank_df.groupby('education')['campaign'].sum()
    df3 = df3.reset_index()
    print(df3.iloc[df3['campaign'].argmax()])

    '''
        Factorial Calculation through recursion and caching via looping 
    '''
    print()
    print()
    start = datetime.now()
    x = 0
    y = 0
    for i in range(900):
        x = factorial_recursion(i)
    end = datetime.now()
    print('Time for execution 900 loops for recursive factorial: ', end - start)

    print()
    start = datetime.now()
    for i in range(900):
        y = factorial(i)
    end = datetime.now()
    print('Time for execution 900 loops for cached factorial:    ', end - start)

    '''
        Calculating Pascal Triangle 
    '''
    print()
    print()
    print(pascal_triangle(10))
    print()
    print()
    print(pascal_triangle(9))
    print()
    print()
    print(pascal_triangle(11))

    '''
        Calculating Fibonacci Sequence 
    '''
    print()
    print()
    print('Fibonacci of {} is {}'.format(10, fibonacci(10)))

    '''
        Testing NegativeNumberException 
    '''
    print()
    print()
    print(pascal_triangle(-1))
