#!/usr/bin/env python3.10
'''markdown
# 📝 Practice Assigment: Academic Introduction

Write a Python program that asks the user a series of questions about themselves and then prints a short academic introduction.

## Requirements
1. Use the `input()` function to ask the user for:
   - Name  
   - Age  
   - Degree or field of study  
   - Student registration number
   - Favorite subject or course  
   - Hobby  
   - Favorite food  
   - Possible experience in Python  
   - Desired career to study  

2. Do not store the answers in variables.

3. Use **strings** (concatenation or f-strings) to create a formatted introduction that includes all the collected information.

4. Display the introduction using `print()`.

---

## Example Interaction

```python
1 | Enter your name: Alice
2 | Enter your age: 20
3 | What degree/field are you studying? High School
4 | What is your student registration number (SRN)? A0XXXXXX
5 | What is your favorite subject or course? Python course
6 | What is your favorite hobby? Reading
7 | What is your favorite food? Pizza
8 | What is your experience in Python? Just starting!
9 | What career would you like to study? Software Engineering

```

**Output:**

```console
Hello! My name is Alice and I am 20 years old.
I am currently studying High School and my SRN is A0XXXXXX.
My favorite subject/course is Python course. In my free time, I enjoy Reading,
and my favorite food is Pizza. Regarding Python, my experience is: Just starting!
In the future, I would like to pursue a career in Software Engineering.
````

---

### ✨ Challenge Hint
- Remember: `input()` always returns a string.  
- You can use **f-strings** for cleaner formatting, e.g.:  
  ```python
  f"My name is {input("Enter your name: ")} and I am {input("Enter your age: ")} years old."
````
'''

# Here your code:
print(f'''\nHello! My name is {input("Enter your name: ")} and I am {input("Enter your age: ")} years old.
I am currently studying {input("What degree/field are you studying? ")} and my SRN is {input("What is your student registration number (SRN)? ")}.
My favorite subject/course is {input("What is your favorite subject or course? ")}. In my free time, I enjoy {input("What is your favorite hobby? ")},
and my favorite food is {input("What is your favorite food? ")}. Regarding Python, my experience is: {input("What is your experience in Python? ")}
In the future, I would like to pursue a career in {input("What career would you like to study? ")}.''')
