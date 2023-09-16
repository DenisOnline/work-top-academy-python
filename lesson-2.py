from random import randint


# step1
def fun():
    hello = "Hello"
    return hello


print(fun)
print(fun())


# step2
def first_function(arg_1, par_2):
    return arg_1 + par_2


print(first_function)
print(first_function(input(), input()))


# step3
def first_function(var_1, var_2, var_3):
    return var_1 * 0.5 + var_2 / 3 + var_3 ** 4.3


function_res_1 = first_function(1, 2, 3)
print(function_res_1)
function_res_2 = first_function(var_1=1, var_3=3, var_2=2)
print(function_res_2)
function_res_3 = first_function(1, 2, var_3=3)
print(function_res_3)


# step4
def appender(var_1, list_1=[]):
    list_1.append(var_1)
    return list_1


first = appender(1)
print(first)
other = appender(2)
print(other)
print(first)
print(first is other)


# step5


def coin_simulator():
    coin = randint(0, 1)
    if coin == 0:
        print("No")
    else:
        print("Yes")


coin_simulator()
