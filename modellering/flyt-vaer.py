grader = int(input("Hvor mange grader er det ute?: "))

if grader > 15:
    print("Ha en fin dag i varmen!")
else:
    print("Ta på jakke")
    type = input("Regner det? ")
    if type.lower == "ja":
        print("Ta med paraply")

i = 0
while i < 20:
    i += 2
    print(i)