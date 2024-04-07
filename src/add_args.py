import os
from add import add_two_nums

if __name__ == "__main__":
	a = int(os.environ.get("A"))
	b = int(os.environ.get("B"))
    
	print(f"Operands: a = {a}; b = {b}")

	summ = add_two_nums(a, b)
	print(f"{a} + {b} = {summ}")
	print("Bye")

