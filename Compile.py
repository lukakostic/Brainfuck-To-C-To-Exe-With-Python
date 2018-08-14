#Made by Luka Kostic
import BF_2_C as bf2c
import os
from time import sleep

def Open_Script():
    file = open("bf.txt","r")
    return file.read()
    
def Compile_To_C(bf):
    bf_Compiler = bf2c.BF_2_C(bf)
    return bf_Compiler.c

def Save_C_File(c):
    file = open("Generated\\bf.c","w")
    file.write(c)
    file.close()

def C_To_Exe():
    dir_path = os.path.dirname( os.path.realpath(__file__)  )                                  # Get current folder
    dir_path2 = dir_path.replace("\\","\\\\")                                                  # Replace \ with \\ because it gives errors otherwise

    if os.path.exists("Generated\\Compiled.exe"):
        os.remove("Generated\\Compiled.exe")
    
    os.system(  "TCC\\tcc.exe -o Generated\\Compiled.exe {}\\Generated\\bf.c ".format(dir_path2)  )     # Start tcc with arguments for what and where to compile

def Start_Exe():
    os.system("Generated\\Compiled.exe")

bf = ""
c = ""

bf = Open_Script()
c = Compile_To_C(bf)
Save_C_File(c)
C_To_Exe()
Start_Exe()

#sleep(2.1) # Time in seconds before closing

while(2>1): # Dont close
    pass
