#Q1:Ask the user for a string and check whether it is a palindrome or not. is a string which is same when we read it forward & backward. Eg- "madam", "racecar" etc.
#[Hint: A palindrome string is equal to its reversed version. We can use a loop to reverse the string manually.]
from numpy import concatenate


user_input = input("Enter a string: ")
reversed_input = ""
for char in user_input:
    reversed_input = char + reversed_input
if user_input == reversed_input:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Q2:Given a list of integers, compute the average of all numbers in the list.
marks = [85, 90, 78, 92, 88]
avg = sum(marks) / len(marks)
print("The average is:", avg)

#Q3:Input two lists of integers from the user. Merge them into one list and sort the result.Eg-, list1 = [1, 2, 7] list2 = [2, 4, 5] result = [1, 2, 4, 5, 7].
input1 = input("Enter the input1: ")
input2 = input("Enter the input2: ")
lis1 = []
list2 = []
for i in input1.split():
    lis1.append(int(i))
for j in input2.split():
    list2.append(int(j))
merged_list = lis1 + list2
a = set(merged_list)
merged_list = list(a)
merged_list.sort()
print( merged_list)

#Q4:Given a tuple of  integers,create:
# •A tuple of all even numbers
# •A tuple of all odd numbers
turple = (0,1,2,3,4,5,6,7,8,9,10)
for even in turple:
    if even % 2 == 0:
        print("the even number is:",even)
for odd in turple:
    if odd % 2 != 0:
        print("the odd number is:",odd)

#Q5:Create a dictionary where:
# •Keys = student names
# •Values = marks(integer)
# Write a menu - based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)depending on the operation they want to perform on the dictionary:
# 1 A.-Add a student
# 2 B.-Update marks
# 3 C.-Search for a student
# 4 D.-Display all students and marks
d = {}
choice = input("Enter your choice: ")
if choice == 'A':
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    d[name] = marks
    print(d)
elif choice == 'B':
    name = input("Enter student name to update marks: ")
    if name in d:
        marks = int(input("Enter new marks: "))
        d[name] = marks
        print(d)
    else:
        print("Student not found.")
elif choice == 'C':
    name = input("Enter student name to search: ")
    if name in d:
        print(f"Marks for {name}: {d[name]}")
    else:
        print("Student not found.")
elif choice == 'D':
    print(d)
#Q6:Given a list of words;
# words =["apple","banana","kiwi","cherry","mango"]Create a dictionary that maps each word to its length. Example:{"apple": 5, "banana": 6, "kiwi": 4, ...}
words = ["apple", "banana", "kiwi", "cherry", "mango"]
d = {}
for word in words:
    d[word] = len(word)
print(d)
#Q7:Write a program that takes a string from the user and prints the number of spaces in the string
user_string = input("Enter a string: ")
count = 0
for char in user_string:
    if char == " ":
        count += 1
print(f"The number of spaces in the string is: {count}")
#Q8:Write a program to check whether two lists share no common elements. Q8# share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]# share common elements list1 =[1,2,3] list2 =[3,4][hint-usesets]
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
common = set(list1).intersection(set(list2))
if common:
    print("The lists share common elements.")
else:
    print("The lists do not share common elements.")
#Q9:Given a list,print all elements that appear more than once in the list[hint-use sets]
l = [1,2,2,2,3,4,4,5,6,6]

a = set()
d = set()
for num in l:
    if num in a:
        d.add(num)
    else:
        a.add(num)
print(list(d))

#Q10:Ask the user for a string and print:
#  •All unique characters
#  •The count of unique characters
character = input("Enter character : ")
U_character = set(character)
print(sorted(U_character))
print(len(U_character))