a = [5, 10, 15, 20, 25]
print(a[0], a[-1])

number = [4, 7, 1, 9, 3]
largest_number = number[0]
for n in number:
    if n > largest_number:
        largest_number = n
print(largest_number)

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
print(sum_of_numbers)

numbers = [1, 2, 3, 4]
reverse_numbers = []
for i in range(len(numbers)-1, -1, -1):
    reverse_numbers.append(numbers[i])
print(reverse_numbers)

numbers = [2, 5, 8, 11, 14]
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)
print(len(even_numbers))