from random import randint
import sys
import os.path
from os import path

#---------------{begin class}------------#
# MERGING FUNCTION #
def merge():
 with open("result1.txt") as xh:
  with open('result.txt') as yh:
    with open("combo.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file
      for i in range(len(xlines)):
        line = ylines[i].strip() + ':' + xlines[i]
        zh.write(line)
#END MERGING FUNCTION
def carry_on():
  print("Press 'Y' to continue or 'E' to exit")
  me=str(input())
  if me =='Y':
    logo()
  else:
     sys.exit(0)
# MAIN FUNCTION
def logo():
   x = """

   (  ____ \(  ____ )(  ___  )(  ____ )| \    /\|\     /|(  __  \ / ___   )  (  ___ \ (  ___  )\__   __/  |\     /|/  \     (  __   )
   | (    \/| (    )|| (   ) || (    )||  \  / /( \   / )| (  \  )\/   )  |  | (   ) )| (   ) |   ) (     | )   ( |\/) )    | (  )  |
   | (_____ | (____)|| (___) || (____)||  (_/ /  \ (_) / | |   ) |    /   )  | (__/ / | |   | |   | |     | |   | |  | |    | | /   |
   (_____  )|  _____)|  ___  ||     __)|   _ (    \   /  | |   | |   /   /   |  __ (  | |   | |   | |     ( (   ) )  | |    | (/ /) |
         ) || (      | (   ) || (\ (   |  ( \ \    ) (   | |   ) |  /   /    | (  \ \ | |   | |   | |      \ \_/ /   | |    |   / | |
   /\____) || )      | )   ( || ) \ \__|  /  \ \   | |   | (__/  ) /   (_/\  | )___) )| (___) |   | |       \   /  __) (_ _ |  (__) |
   \_______)|/       |/     \||/   \__/|_/    \/   \_/   (______/ (_______/  |/ \___/ (_______)   )_(        \_/   \____/(_)(_______)
                                                                                                                      
   +----------------------------------+--------------------------------------------+
   | 1)Mass Phone Number Generator (Worldwide)|| 2) Combolist phone format maker   |
   |                                00)Exit..                                       |
   +----------------------------------+--------------------------------------------+	  
        """
   print(x)
   print("Make a choice ...")
   CHOICE=str(input())
   if CHOICE =='1':
     gen()   
     carry_on()
   elif CHOICE =='2':
      comobolist_maker()
   else:
     logo()



# [1]FIRST FUNCTION #
def gen():
  #first step
  #quantity...
 print("How many phone numbers do you want me to generate? : ")
 quantity=int(input())
  #country code
 print("Write your countrycode (EXAMPLE : ALGERIA='+213')")
 code=str(input())
 if quantity<0:
   print("Quantity must be greater than 0... ")
   print(chr(27)+'[2j')
   gen()
 else:
   myFile = open("result.txt",'w')
   for i in range(quantity):
       myFile.write(code+random_with_N_digits(10)+"\n")
   print("") 
# [1]SECOND FUNCTION #
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))
# [2]FIRST FUNCTION #
def comobolist_maker():
  print("WARNING INPUT FILE MUST BE 'result.txt' ")
  input_file="result.txt"
  f = open(input_file, "r")
  myFile = open("result1.txt",'w')
  for x in f:
     temp=x
     temp=temp[4:-5]
     myFile.write(temp+"\n")
# [2]SECOND FUNCTION #

#---------------{end class}--------------#
logo()
a=str(path.exists('result.txt'))
b=str(path.exists('result1.txt'))
if a == b:
  merge()
