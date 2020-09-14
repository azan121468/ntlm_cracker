import binascii
import hashlib
from time import time

no_of_try = 0

def title_box():
    """Creates title box"""
    print("            **********************")
    print("            *     NTLM Cracker   *")
    print("            *        by          *")
    print("            *     Azan Shahid    *")
    print("            **********************")

def ntlm_hash(string):
    """generate ntlm hash"""
    return binascii.hexlify(hashlib.new('md4', string.encode('utf-16le')).digest()).decode('utf-8')

def crack(user_hash, wordlist):
    """crack ntlm hash"""
    global no_of_try
    try:
        with open(wordlist) as wordlist:
            a = wordlist.readlines()
            for each in a:
                if each.endswith('\n'):
                    word = each.strip()  # remove space and \n from start and end
                else:
                    word = each
                print("Trying ---> "+ word)
                no_of_try+=1
                if ntlm_hash(word) == user_hash.lower():
                    print("Found  ---> ", word)
                    break
    except IOError:
        print("I/O error occured")
        print("Cannot open wordlist")
        sys.exit()

def main():
    """main part of program"""
    title_box()
    print("Enter your NTLM Hash : ",end="")
    user_input = input() or "admin"
    print("Enter your wordlist : ",end="")
    wordlist = input() or "wordlist.txt"
    start = time()
    crack(user_input, wordlist)
    stop = time()
    print(f"Time taken is {round(float(stop-start),3)} seconds")
    print(f"Average speed was {round(no_of_try/(stop-start),2)} passwords per seconds")

if __name__=="__main__":
    main()
