def solve_day1(file_name):
    list1 = []
    list2 = []
    file = open(file_name, "r")
    for line in file:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    difference_sum = calculate_difference_sum(list1, list2)
    number_product = calculate_product_number_appearience(list1, list2)

    print(f"result: difference_sum (task1) = {difference_sum}, number_product (task2) = {number_product}")


def calculate_difference_sum(list1, list2):
    list1.sort()
    list2.sort()

    full_difference = 0
    for x, y in zip(list1,list2):
        if x > y:
            full_difference += x - y
        else:
            full_difference += y - x

    return full_difference

def calculate_product_number_appearience(list1, list2):
    test_map = {}
    total_product = 0

    for number in list2:
        if test_map.get(str(number)) is None:
            test_map[str(number)] = 1
        else:
            test_map[str(number)] += 1

    for number in list1:
        if test_map.get(str(number)):
            total_product += test_map[str(number)] * number

    return total_product

solve_day1("puzzle_input")