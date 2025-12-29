import random

def generate_complex_number(real_range=(-100, 100), imag_range=(-100, 100)):
    real_part = random.uniform(real_range[0], real_range[1])
    imag_part = random.uniform(imag_range[0], imag_range[1])
    return complex(real_part, imag_part)

def generate_multiple_complex_numbers(num=10):
    complex_numbers = []
    for _ in range(num):
        complex_numbers.append(generate_complex_number())
    return complex_numbers

random_complex_numbers = generate_multiple_complex_numbers(10)
for num in random_complex_numbers:
    print(f"Complex Number: {num}")

#This code is a generator to make random complex numbers and lists them out, every time it will output 10 different numbers. -- Thomas Harker :)