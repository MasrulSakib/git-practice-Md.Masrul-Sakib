from datetime import date
from utils import add, subtract, multiply

print("--- Personal Info ---")
print("My name is Md. Masrul Sakib")
print("Today's date is", date.today())

print("\n--- Calculator Results ---")
print("The sum of 5 and 3 is:", add(5, 3))
print("The difference between 10 and 4 is:", subtract(10, 4))
print("The product of 6 and 7 is:", multiply(6, 7))

print("\n--- Error Handling Tests ---")
print("Invalid input test:", add("hello", 5))