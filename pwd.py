import random
def main() :
       outfile = open("HASHES.txt","a")
       
       site=input("Enter the name of website: ")
       lower="abcdefghijklmnopqrstuvwxyz"
       upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       numbers= "0123456789"
       symbols="[]{}()*;/,_-"
       all = lower +upper+numbers+symbols
       length = 16
       password = "".join(random.sample(all,length))
       text= "The password of "+site+" is: "+password
       outfile.write("\n"+text)
       outfile.close()

       
main()