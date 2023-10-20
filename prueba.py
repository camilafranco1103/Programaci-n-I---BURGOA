#Suma de los digitos de un solo numero
def add_nums(number):
    sum_numbers = 0
    while number != 0:
        digit_number = number%10
        sum_numbers += digit_number 
        number = (number-digit_number)/10
    return sum_numbers