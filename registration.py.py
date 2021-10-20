
import hashlib

def main():
    uname = input("Please provide your username?")
    print("welcome,",uname)
    pword = input("Please choose a password")

    penc = pword.encode()
    pcrypt = hashlib.sha512()
    pcrypt.update(penc)
    shadow = open("shadow.txt", "a")
    shadow.write((uname+":"+pcrypt.hexdigest()+":"))
    shadow.close()
    print("Congratulations! Your registration is completed!")
main()