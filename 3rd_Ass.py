print("🧠  Control Flow & Loops")

# Program 1: Check age category
age = int(input("Enter your age: "))

if age >= 65:
    print("You are a senior citizen.")
elif age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
elif age >= 3:
    print("You are a child.")
else:
    print("You are a toddler.")


# Program 2: Print odd numbers from 1 to 30
print("Odd numbers between 1 and 30:")
for num in range(1, 31):
    if num % 2 != 0:
        print(num, end=" ")
print()


# Program 3: Print multiples of 5 in reverse from 50 to 5
print("Multiples of 5 from 50 to 5:")
for i in range(20, 4, -5):
    print(i)




print("📚  Lists, Tuples & Dictionary")

# Program 1: List of car brands and print each one
cars = ["Toyota", "Honda", "BMW", "Suzuki", "Hyundai"]
print("Available car brands:", cars)



# Program 2: Tuple of favorite foods and print last item
foods = ("Biryani", "Pizza", "Pasta", "Burger")
print("Favorite food:", foods)


# Program 3: Dictionary of books and their authors
books = {
    "1984": "George Orwell",
    "The Alchemist": "Paulo Coelho",
    "Harry Potter": "J.K. Rowling"
}

print("Book Authors:",books)




print("  Set & Frozenset")

# Program 1: Create set from list of animals with duplicates
animals = ["Cat", "Dog", "Parrot", "Dog", "Cat"]
unique_animals = set(animals)
print("Original list of animals:", animals)
print("Unique animals in set:", unique_animals)


# Program 2: Set operations with A and B
A = {"apple", "banana", "cherry"}
B = {"banana", "cherry", "date"}

print("Items in either A or B:", A | B)
print("Items in both A and B:", A & B)


# Program 3: Create a frozenset from vowels and try to add item
vowels = ['a', 'e', 'i', 'o', 'u']
f_vowels = frozenset(vowels)
print("Frozenset of vowels:", f_vowels)

# Uncommenting below line will cause error
# f_vowels.add('y')  # Cannot add to frozenset
