"""
Blackjack
"""
# Provide your solution here
def calculate_score(a: int, b: int, c: int) -> int:
    sum = a + b + c
    list = [a, b, c]

    for i in list:
         if 1 < i < 11:
            return sum








calculate_score(9, 9, 9)

# if 1 < numbers < 11:
    #     if sum <= 21:
    #         return sum
    #     elif sum > 21 and a = 11 or b = 11 or c = 11:
"""
Even Numbers
"""
def even_positive_numbers(numbers: [int]):
    new_list = []

    for i in numbers:
        if i % 2 == 0 and i >= 0:
            new_list.append(i)

    return new_list

even_positive_numbers(numbers=[1, 2, 3])
# Provide your solution here
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(even_positive_numbers(numbers=[1, 2, 3]))
    print(calculate_score(9, 9, 9))

