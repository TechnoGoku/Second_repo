import random

def get_numbers_ticket(min, max, quantity):
    try:
        unique_random_numbers = list()
        ranges = list(range(min_number,max_number))
        if min_number >= 1 and max_number <= 1000:
            unique_random_numbers = random.sample(ranges, k=quantity_number)
            sorted_unique_numbers = sorted(unique_random_numbers)
            print(f"Ваші числа: {sorted_unique_numbers}")
            return sorted_unique_numbers
        else:
            print("Потрібно ввести числа у межах заданих параметрів.")
            print(unique_random_numbers)
            return unique_random_numbers
    except ValueError:
        print("Потрібно задати такий діапазон, який зможе охопити числа між мінімальним і максимальним значенням!")
    
    


min_number = int(input("Введіть вашу мінімальну цифру не менше 1: "))
max_number = int(input("Введіть вашу максимальну цифру не більше 1000: "))
quantity_number = int(input("Введіть кількість чисел, які потрібно обрати між мінимальним та максимальним значенням: "))
get_numbers_ticket(min_number, max_number, quantity_number)
