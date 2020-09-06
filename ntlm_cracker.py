import binascii
import hashlib
from time import time


def title_box():
    """Creates title box"""
    print("            **********************")
    print("            *     MD5 Cracker    *")
    print("            *        by          *")
    print("            *     Azan Shahid    *")
    print("            **********************")

def ntlm_hash(string):
    """generate ntlm hash"""
    return binascii.hexlify(hashlib.new('md4', string.encode('utf-16le')).digest()).decode('utf-8')

def crack(hash, wordlist):
    """crack ntlm hash"""
    try:
        with open(wordlist) as wordlist:
            a = wordlist.readlines()
            for each in a:
                if each.endswith('\n'):
                    word = each.strip()  # remove space and \n from start and end
                else:
                    word = each
                print("Trying ---> ", word)
                if ntlm_hash(word) == hash:
                    print("Found  ---> ", word)
                    break
    except IOError:
        print("I/O error occured")
        print("Cannot open wordlist")

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
    print(f"Time taken is {int(float(stop-start))}")

if __name__=="__main__":
    main()
