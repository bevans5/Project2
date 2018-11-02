import binary_hash

b_hash = binary_hash.binary_hash
#print(b_hash)


def encrypt(message):
    ans = []
    message = list(message)

    for letter in message:
        x = b_hash[letter]
        ans.append(x)
        word = "-".join(ans)
    print(word)

encrypt('hello')
