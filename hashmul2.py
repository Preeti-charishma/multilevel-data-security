import hashlib
import random
 
# {'sha256', 'sha384', 'sha224', 'sha512', 'sha1', 'md5'}
# ripemd160

pw = input("Enter password:")
s=""

# hashlib.<enc>(str.encode()).hexdigest()

def sha384_enc():
    global pw, s
    pw = hashlib.sha384(pw.encode()).hexdigest()
    print("sha384:",pw)
    s+="1"
    return pw, s

def sha512_enc():
    global pw, s
    pw = hashlib.sha512(pw.encode()).hexdigest()
    print("sha512:", pw)
    s+="2"
    return pw, s

def md5_enc():
    global pw, s
    pw = hashlib.md5(pw.encode()).hexdigest()
    print("md5:", pw)
    s+="3"
    return pw, s

def sha256_enc():
    global pw, s
    pw = hashlib.sha256(pw.encode()).hexdigest()
    print("sha256:", pw)
    s+="4"
    return pw, s

def sha224_enc():
    global pw, s
    pw = hashlib.sha224(pw.encode()).hexdigest()
    print("sha224:", pw)
    s+="5"
    return pw, s

def sha1_enc():
    global pw, s

    pw = hashlib.sha1(pw.encode()).hexdigest()
    print("sha1:", pw)
    s+="6"
    return pw, s

def ripemd160_enc():
    global pw, s
    pw = pw.encode()
    hash = hashlib.new("ripemd160")
    hash.update(pw)
    pw = hash.hexdigest()
    print("ripemd160:", pw)
    s+="7"
    return pw, s


#-------------#

def sha384_dec():
    global pw2
    pw2 = hashlib.sha384(pw2.encode()).hexdigest()
    print("sha384:",pw2)
    return pw2

def sha512_dec():
    global pw2
    pw2 = hashlib.sha512(pw2.encode()).hexdigest()
    print("sha512:", pw2)
    return pw2

def md5_dec():
    global pw2
    pw2 = hashlib.md5(pw2.encode()).hexdigest()
    print("md5:", pw2)
    return pw2

def sha256_dec():
    global pw2
    pw2 = hashlib.sha256(pw2.encode()).hexdigest()
    print("sha256:", pw2)
    return pw2

def sha224_dec():
    global pw2
    pw2 = hashlib.sha224(pw2.encode()).hexdigest()
    print("sha224:", pw2)
    return pw2

def sha1_dec():
    global pw2
    pw2 = hashlib.sha1(pw2.encode()).hexdigest()
    print("sha1:", pw2)
    return pw2

def ripemd160_dec():
    global pw2
    pw2 = pw2.encode()
    hash = hashlib.new("ripemd160")
    hash.update(pw2)
    pw2 = hash.hexdigest()
    print("ripemd160:", pw2)
    return pw2

r = random.randint(10, 35)

for i in range(r):
    c = random.randint(1,7)
    if c==1:
        sha384_enc()
    elif c==2:
        sha512_enc()
    elif c==3:
        md5_enc()
    elif c==4:
        sha256_enc()
    elif c==5:
        sha224_enc()
    elif c==6:
        sha1_enc()
    elif c==7:
        ripemd160_enc()


print("final", pw)
print("s=",s)


pw2 = input("Enter pass again:")
order = s
print("order=", order)
for i in order:
    if i=='1':
        sha384_dec()
    elif i=='2':
        sha512_dec()
    elif i=='3':
        md5_dec()
    elif i=='4':
        sha256_dec()
    elif i=='5':
        sha224_dec()
    elif i=='6':
        sha1_dec()
    elif i=='7':
        ripemd160_dec()




print(pw)
print(pw2)
    

