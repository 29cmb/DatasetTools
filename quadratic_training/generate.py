import random
import math
import os
from datetime import datetime
from tqdm import tqdm
import sys

def get_large_number():
    sign = 1 if random.random() > 0.5 else -1
    magnitude = random.randint(1, 100000000)
    return sign * magnitude

def solve_quadratic(a, b, c):
    discriminant = b * b - 4 * a * c
    
    if discriminant < 0:
        return "No real solutions"
    
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return f"{x1} and {x2}"

def generate_quadratic_question():
    while True:
        a = get_large_number()
        b = get_large_number()
        c = get_large_number()
        
        solution = solve_quadratic(a, b, c)
        if solution != "No real solutions":
            break
    
    question = f"{a}x^2 + {b}x + {c}"
    return f"The question is {question} | The answer is {solution}"

def main(num_files):
    max_size = 500 * 1000 * 1000  # 500 MB
    
    for i in range(num_files):
        filename = "generated/" + datetime.now().strftime("%Y%m%d_%H%M%S") + f"_{i}.txt"
        current_size = 0
        
        with open(filename, 'w') as f:
            with tqdm(total=max_size, unit='B', unit_scale=True, desc=f"Generating file {i+1}/{num_files}") as pbar:
                while current_size < max_size:
                    question = generate_quadratic_question() + "\n"
                    f.write(question)
                    current_size += len(question.encode('utf-8'))
                    pbar.update(len(question.encode('utf-8')))
                pbar.colour = 'green'

if __name__ == "__main__":
    num_files = int(input("Enter the number of files to create: "))
    main(num_files)