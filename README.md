DSA means Data Structures and Algorithms. Data Structures are mainly used to make a program run with lesser Time Complexity and Space Complexity. And algorithms are set of instructions used to make the program run.
For example, if Data Structures are bricks,cement etc..., then Algorithms are like plan of the building or a blue print.
So, by putting them all together, we can make a code or a program to have lesser Time and Space Complexity.

Time Complexity:- The time consumed for a code to get executed.
Space Complexity:- The memory space used by a code in execution process.

Big-O notation: It is a measure used to calculate the time and space complexities of a code.

Big-O for time complexity.
refered as a*n+b. B is constant. N is number of times code runs. a is constant.
'def p(a1,a2,num):'
'pe=a1[num]/a2[num]'
'return pe'

for this code the time complexity is O(1). Because, in this code we are directly givimg the index number to arrays, so the code runs only one time. So, the time complexity is O(1).

'a=[1,2,3,4]'
'for i in a:'
'print a[i]'

this code have O(n) time complexity. Because, this code is having for loop. And loop runs n number times. So, the number of times the code runs, the time complexity is equal to that.

'a=[1,2,3,4]'

'for i in a:'
'print a[i]'



