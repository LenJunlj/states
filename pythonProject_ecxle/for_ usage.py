fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
for key in student:
    print(key)

student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
for key, value in student.items():
    print(key, value)

for i in range(1, 5):
    print(i)

word = "Hello"
for char in word:
    print(char)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
for number, letter in zip(numbers, letters):
    print(number, letter)

fin=open("word.txt")
fin_read=fin.readline()
print(fin_read)







