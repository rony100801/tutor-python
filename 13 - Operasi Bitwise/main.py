# OPERASI BITWISE

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n====== OR =====")
print("Nilai :", a, "| binary  :", format(a, "08b"))
print("Nilai :", b, "| binary  :", format(b, "08b"))
print("------------------------------ OR")
print("Nilai :", c, "| binary :", format(c, "08b"))

# bitwise AND (&)
c = a & b
print("\n====== AND =====")
print("Nilai :", a, "| binary :", format(a, "08b"))
print("Nilai :", b, "| binary :", format(b, "08b"))
print("------------------------------ AND")
print("Nilai :", c, "| binary :", format(c, "08b"))

# bitwise XOR (^)
c = a ^ b
print("\n====== XOR =====")
print("Nilai :", a, "| binary  :", format(a, "08b"))
print("Nilai :", b, "| binary  :", format(b, "08b"))
print("------------------------------ XOR")
print("Nilai :", c, "| binary :", format(c, "08b"))

# bitwise NOT (~)
print("\n====== NOT =====")
c = ~a
print("Nilai :", a, "| binary  :", format(a, "08b"))
print("------------------------------ NOT")
print("Nilai :", c, "| binary:", format(c, "08b"))

# Shifting Right (>>)
print("\n====== >> =====")
c = a >> 2
print("Nilai :", a, "| binary  :", format(a, "08b"))
print("------------------------------ >>")
print("Nilai :", c, "| binary  :", format(c, "08b"))

# Shifting Left (<<))
print("\n====== << =====")
c = a << 2
print("Nilai :", a, "| binary  :", format(a, "08b"))
print("------------------------------ <<")
print("Nilai :", c, "| binary :", format(c, "08b"))


print("\n")
