# Handling conditions

One of the fairly common scenarios you'll run into in programming is making decisions. Your program needs to compare values and execute code based upon some logical outcome. 
you might be wondering if there is the equivalent of a switch case in Python. Some other languages have this notion of a compound conditional known as switch and case. And the answer is no. Python, in it's efforts to be simple, sticks to the if else construct, and uses elif as a substitute for writing a switch case block. 

Conditional execution can be completed using the [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) statement

`if` syntax

```python
if expression:
    # code to execute
else:
    # code to execute
```

[Comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

- < less than
- < greater than
- == is equal to
- \>= greater than or equal to
- <= less than or equal to
- != not equal to
