import hashlib
def main():
    #make user put in username and password for user they want to access
    uname = input("Please provide your username")
    pword = input("Please provide your password")
    
    #encodes password so we can hash it, we do this because we are going to check the stored password hash with the inserted password hash
    penc = pword.encode()
    pcrypt = hashlib.sha512()
    pcrypt.update(penc)

    #open txt file we want to compare with
    with open("shadow.txt", "r") as shadow:
        shadowstr = shadow.read()
        #split at : so we get a list where we have ["username","hash","username","hash"] and so on. then we know that the hash that comes after username is that usernames password
        shadowsplit = shadowstr.split(":")
        #check if username in list
        if uname in shadowsplit:
            #check if the password to the user you are trying to access maches the file
            if shadowsplit[shadowsplit.index(uname)+1] == pcrypt.hexdigest():
                print("You're successfully logged in")
            else:
                print("Obs! The provided username and password do not match.")
        else:
            print("Obs! The provided username and password do not match.")
main()
