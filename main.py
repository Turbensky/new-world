def calculate_digit_sum(num):
    return sum(int(digit) for digit in str(num))

max_num = 0
max_sum = 0
num_entered = False

while True:
    num = int(input("Введите целое число (для завершения введите 0): "))
    if num == 0:
        if not num_entered:
            print("Вы не ввели ни одного числа, кроме нуля.")
        break
    num_entered = True
    
    digit_sum = calculate_digit_sum(num)
    if digit_sum > max_sum:
        max_num = num
        max_sum = digit_sum

if max_num != 0:
    print("Число с максимальной суммой цифр:", max_num)
