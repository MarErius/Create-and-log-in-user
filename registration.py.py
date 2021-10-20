
import hashlib

def main():
    #make user put in what they want as username and password
    uname = input("Please provide your username?")
    print("welcome,",uname)
    pword = input("Please choose a password")
    
    #encodes password so we can hash it
    penc = pword.encode()
    #hash it as sha512
    pcrypt = hashlib.sha512()
    pcrypt.update(penc)
    #open txt file we want to write the user to
    shadow = open("shadow.txt", "a")
    #we need to use hashdigest() to get the hash.
    shadow.write((uname+":"+pcrypt.hexdigest()+":"))
    shadow.close()
    print("Congratulations! Your registration is completed!")
main()
