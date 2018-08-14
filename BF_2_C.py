#Made by Luka Kostic
class BF_2_C:
    bf = ""
    c = ""

    def Compile_C(self):
        self.c = ""

        
        for i, ch in enumerate(self.bf): #Ignores unknown commands so you can comment
          
            if(ch=='.'):
                self.c += """printf("%c",cells[pointer]);\n"""
            if(ch==','):
                self.c += """
scanf("%c%*c", & inp);
cells[pointer] = inp[0];
"""
            if(ch=='+'):
                self.c += "cells[pointer]+=1;\n"
            if(ch=='-'):
                self.c += "cells[pointer]-=1;\n"
            if(ch=='>'):
                self.c += "pointer+=1;\n"
            if(ch=='<'):
                self.c += "pointer-=1;\n"
            if(ch=='['):
                self.c+="""int c{} = pointer;
while(cells[c{}]>0){{
""".format(str(i),str(i))
            if(ch==']'):
                self.c+="} \n"
                
        self.c = self.wrap(self.c)
        
    def __init__(self,txt):
        self.bf = txt
        self.Compile_C()

    def wrap(self,txt): # Add stuff that encapsulates bf to make it work (the cells, main function, etc.)
        pre = """
#include <stdio.h>
#include <stdlib.h>

int cells[9999]; // all cells
int pointer = 0; // current cell
char inp[256]; // used for input

int main () 
{


"""
        post = """

while(1){}


return 0;

}

"""
        
        return pre + txt + post;
        
