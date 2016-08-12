import os

def parser(x):
    string = str(x)
    if len(string) % 3 == 1:
        string = "00" + string
    elif len(string) % 3 == 2:
        string = "0" + string
    holder = []
    while len(string) != 0:
        y = string[0] + string [1] + string [2]
        holder.append(y)
        string = string[3:]
    passw = ""
    for i in holder:
        if int(i) < 33:
            passw = passw + chr(int(i) + 93)
        elif int(i) <127:
            passw = passw + chr(int(i))
        else:
            q = int(i)
            while q > 126:
                q = q - 93
            passw = passw + chr(q)
    return passw

def int_maker(length):
    d = os.urandom(length)
    c = int(d.encode('hex'), 16)
    return c
def pass_maker(length):
    return(parser(int_maker(length)))
x = int(raw_input("Enter an integer corresponding to password strength: " ))
print pass_maker(x)
