import hashlib
def main():
    uname = input("Please provide your username")
    pword = input("Please provide your password")

    penc = pword.encode()
    pcrypt = hashlib.sha512()
    pcrypt.update(penc)


    with open("shadow.txt", "r") as shadow:
        shadowstr = shadow.read()
        shadowsplit = shadowstr.split(":")
        if uname in shadowsplit:
            if shadowsplit[shadowsplit.index(uname)+1] == pcrypt.hexdigest():
                print("You're successfully logged in")
            else:
                print("Obs! The provided username and password do not match.")
        else:
            print("Obs! The provided username and password do not match.")
main()