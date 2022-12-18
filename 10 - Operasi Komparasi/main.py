# Operasi Komparasi
# Nilainya hanya true / false
# >, <, >=, <=, ==, !=, is, is no

a = 4
b = 2

# LEBIH BESAR DARI
print("\n===== LEBIH BESAR DARI ( > ) =====")
hasil = a > 3
print(a, ">", 3, " = ", hasil)
hasil = b > 3
print(b, ">", 3, " = ", hasil)
hasil = b > 2
print(b, ">", 2, " = ", hasil)

# LEBIH KECIL DARI
print("\n===== LEBIH KECIL DARI ( < ) =====")
hasil = a < 3
print(a, "<", 3, " = ", hasil)
hasil = b < 3
print(b, "<", 3, " = ", hasil)
hasil = b < 2
print(b, "<", 2, " = ", hasil)

# LEBIH BESAR DARI
print("\n===== LEBIH BESAR DARI ATAU SAMA DENGAN ( >= ) =====")
hasil = a >= 3
print(a, ">=", 3, " = ", hasil)
hasil = b >= 3
print(b, ">=", 3, " = ", hasil)
hasil = b >= 2
print(b, ">=", 2, " = ", hasil)

# LEBIH KECIL DARI atau SAMA DENGAN
print("\n===== LEBIH KECIL DARI ATAU SAMA DENGAN ( <= ) =====")
hasil = a <= 3
print(a, "<=", 3, " = ", hasil)
hasil = b <= 3
print(b, "<=", 3, " = ", hasil)
hasil = b <= 2
print(b, "<=", 2, " = ", hasil)

# SAMA DENGAN (==)
print("\n===== SAMA DENGAN ( == ) =====")
hasil = a == 4
print(a, "==", 4, " = ", hasil)
hasil = a == 3
print(a, "==", 3, " = ", hasil)

# TIDAK SAMA DENGAN ( != )
print("\n===== TIDAK SAMA DENGAN ( != ) =====")
hasil = a != 4
print(a, "!=", 4, " = ", hasil)
hasil = a != 3
print(a, "!=", 3, " = ", hasil)

# 'is' sebagai komparasi objek
# membandingkan sesama objek bukan literal
print("\n===== KOMPARASI IS ( is ) =====")
x = 5
y = 5
z = 6

hasil = x is y
print(x, "is", y, " = ", hasil)
hasil = x is z
print(x, "is", z, " = ", hasil)

print("\n===== KOMPARASI IS NOT ( is not ) =====")
x = 5
y = 5
z = 6

hasil = x is not y
print(x, "is not", y, " = ", hasil)
hasil = x is not z
print(x, "is not", z, " = ", hasil)


print("\n")
