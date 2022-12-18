# OPERASI LOGIKA ATAU BOOLEAN
# not, or, and, xor

# NOT
print("\n===== NOT =====")
a = True
b = not a
print("Data A =", a)
print("---------------- NOT")
print("Data B =", b)

# OR (Jika salah satu TRUE maka akan true)
print("\n===== OR =====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, " =", c)
a = False
b = True
c = a or b
print(a, "OR", b, " =", c)
a = True
b = True
c = a or b
print(a, "OR", b, "  =", c)

# AND (Jika salah FALSE maka akan bernilai False)
print("\n===== AND =====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, " =", c)
a = False
b = True
c = a and b
print(a, "AND", b, " =", c)
a = True
b = True
c = a and b
print(a, "AND", b, "  =", c)

# XOR (Jika memiliki nilai sama akan  bernilai false)
print("\n===== XOR =====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, " =", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "  =", c)


print("\n")
