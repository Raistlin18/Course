# def calculate_rectangle_area(width, height):
#     return width * height

# def print_rectangle_area(width_from_user, height_from_user):
#     area = calculate_rectangle_area(width_from_user, height_from_user)
#     print('A négyszög területe ' + str(area) + ' négyzetméter.')

# print_rectangle_area(2, 4)

# def kor_kerulet(r):
#     return 2 * r * 3.14

# def kor_terulet(r):
#     return r ** 2 * 3.14

# def print_kerulet_terulet(user_r):
#     print(f'A(z) {user_r} sugarú kör kerülete: {kor_kerulet(user_r)}, a területe pedig: {kor_terulet(user_r)}')

# print_kerulet_terulet(5)

variable = 10

def local_scope():
    variable = 20
    print('Local variable in the function: ' + str(variable))

local_scope()

print('Global variable: ' + str(variable))