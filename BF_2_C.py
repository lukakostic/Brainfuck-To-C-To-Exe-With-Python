#Made by Luka Kostic
class BF_2_C:
    bf = ""
    c = ""
	
    def Compile_C(self):
        self.c = ""
		
        
        for i, ch in enumerate(self.bf): #Ignores unknown commands so you can comment
          
            if(ch=='.'):
                self.c += "o;\n"
            if(ch==','):
                self.c += "s;\n"
            if(ch=='+'):
                self.c += "cp++;\n"
            if(ch=='-'):
                self.c += "cp--;\n"
            if(ch=='>'):
                self.c += "p++;\n"
            if(ch=='<'):
                self.c += "p--;\n"
            if(ch=='['):
                self.c+="while(cp){{".format(str(i))
            if(ch==']'):
                self.c+="}\n"
                
        self.c = self.wrap(self.c)
        
    def __init__(self,txt):
        self.bf = txt
        self.Compile_C()

    def wrap(self,txt): # Add stuff that encapsulates bf to make it work (the cells, main function, etc.)
        pre = """
#include<stdio.h>
#include<stdlib.h>
#define cp c[p]
#define o printf("%c",cp)
#define s scanf("%c%*c",&i);cp=i[0]

int main () 
{

unsigned char c[9999]; // all cells
int p = 0; // current cell
char i[256]; // used for input

int j;for(j=0;j<9999;j++)c[j]=0; //reset all chars to 0


"""
        post = """

while(1){}

return 0;
}

"""
        
        return pre + txt + post;
        
