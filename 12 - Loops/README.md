# Loops

## For loops

[For loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) takes each item in an array or collection in order, and assigns it to the variable you define.

``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

## While loops

### [While Loop] Statements
Python utilizes the while loop similarly to other popular languages. The while loop evaluates a condition then executes a block of code if the condition is true. The block of code executes repeatedly until the condition becomes false.

[While loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) perform an operation as long as a condition is true.

The basic syntax is:

```python
counter = 0
while counter < 10:
   # Execute the block of code here as
   # long as counter is less than 10
```

``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```
