
#include <stdio.h>
#include <stdlib.h>

int cells[9999]; // all cells
int pointer = 0; // current cell
char inp[256]; // used for input

int main () 
{


cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
int c18 = pointer;
while(cells[c18]>0){
pointer+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
pointer+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
cells[pointer]+=1;
pointer-=1;
pointer-=1;
cells[pointer]-=1;
} 
pointer+=1;
pointer+=1;
cells[pointer]+=1;
pointer-=1;
pointer-=1;
pointer+=1;
printf("%c",cells[pointer]);
pointer+=1;
printf("%c",cells[pointer]);
int c148 = pointer;
while(cells[c148]>0){

scanf("%c%*c", & inp);
cells[pointer] = inp[0];
printf("%c",cells[pointer]);
} 


while(1){}


return 0;

}

