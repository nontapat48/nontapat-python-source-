print("=" * 50)
print("Age check")
print("=" * 50)

age = int(input("Enter age: "))

if age >= 0 and age <= 12:
    print("You're Child")

if age >= 13 and age <= 19:
    print("You're Teenager")

if age >= 20 and age <= 59:
    print("You're Adult")

if age >= 60:
    print("You're Senior")