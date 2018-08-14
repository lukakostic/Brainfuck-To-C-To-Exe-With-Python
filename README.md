# Brainfuck-To-C-To-Exe-With-Python
Used python to make a brainfuck to C compiler, then used TCC to compile to exe, all automatically

TCC = Tiny C Compiler

Start Compile.py, then check the Generated folder, should have a .c and a .exe

Starts the compiled exe automatically

bf.txt is where brainfuck goes. Ignores unknown letters so you can comment.

Syntax:
~~~
+ add to current cell
- subtract from current cell
> next cell
< previous cell
. print cell value as ascii
, read cell value as ascii
[ loop inside while cell the loop started at > 0
] close loop bracket
~~~

All code is very simple and commented, you could easily add more commands!


![bf](https://user-images.githubusercontent.com/41348897/44120230-0710bdfc-a01c-11e8-8e23-46a0d7b9b149.png)
