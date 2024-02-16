
def reverseVowels( s):
    vowels = ['a','e','i','o','u']
    vowels_upper = ['A','E','I','O','U']
    store_v = [] 
    for char in s:
        if char.islower():
            if char in vowels:
                store_v.append(char)
        if char.isupper():
            if char in vowels_upper:
                store_v.append(char)
            
    store_v.reverse()
    z= 0
    string = list(s)
    print(string)
    for i in range(len(string)):
        if string[i] in vowels:
            string[i] = store_v[z]
            z += 1
        elif string[i] in vowels_upper:
            string[i] = store_v[z]
            z += 1

    x = ''.join(string)
    return x