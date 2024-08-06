marks = {
    "Anisha": 100,
    "Shubham": 56,
    "Raj": 23,
    0: "Anisha"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Anisha": 99, "Renuka": 100})

print(marks)

print(marks.get("Anisha"))

# print(marks.get("Harry2"))          # Prints None(Not in dictionary)

# print(marks["Harry2"])              # Returns an error