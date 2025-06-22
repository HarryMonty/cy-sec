import hashlib

hashed_file = open("hash.txt", "r")
hash_code = hashed_file.read()

with open("wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        poss_pass = line.strip()
        enc_pass = hashlib.sha256(poss_pass.encode()).hexdigest()
        if enc_pass == hash_code:
            print("Password found: ", poss_pass, " aka ", enc_pass)
            break
        else:
            print("Attempting: ", poss_pass)
    else:
        print("Password not found.")
        