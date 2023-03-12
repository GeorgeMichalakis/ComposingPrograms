"""
Every programming language has three mechanisms:
Primitive expression and statements: Building blocks
Means of combination: Which compound elements are built fro msimpler ones
Means of abstraction: which compound elements can be named and manipulated as units

Expression

infix notation (between the operands)

Call expression -> Applies a function to some arguments

max(7.5,9.5)

Call expression has subexpressions:
Operator is max
Operand#1 7.5
Operand#2 9.5

Pure functions: Have some input (argument) and retrn some output ->Applying them has no effect apart from 

Non pure functions (apart from returning an ouput maybe printing as well for example)

Pure functions are restricted in that they cannot have side effects or change behavior over time. Imposing these restrictions yields substantial benefits. First, pure functions can be composed more reliably into compound call expressions


Pure functions are restricted in that they cannot have side effects or change behavior over time. Imposing these restrictions yields substantial benefits. First, pure functions can be composed more reliably into compound call expressions. We can see in the non-pure function example above that print does not return a useful result when used in an operand expression. On the other hand, we have seen that functions such as max, pow and sqrt can be used effectively in nested expressions.

Second, pure functions tend to be simpler to test. A list of arguments will always lead to the same return value, which can be compared to the expected return value. Testing is discussed in more detail later in this chapter.

Third, Chapter 4 will illustrate that pure functions are essential for writing concurrent programs, in which multiple call expressions may be evaluated simultaneously.

By contrast, Chapter 2 investigates a range of non-pure functions and describes their uses.

For these reasons, we concentrate heavily on creating and using pure functions in the remainder of this chapter. The print function is only used so that we can see the intermediate results of computations.
"""