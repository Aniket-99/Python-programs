word = input("Enter A word: ")
data = " "
reverse = []

for val in word.split(" "):
    reverse.append(val)

reverse.sort(reverse=True)
print(reverse)

data = data.join(reverse)
print(data.swapcase())


