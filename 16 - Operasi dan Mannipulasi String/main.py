# Operasni dan manipulasi string

# 1. Menyambung string (Concatenation)
print("\n")
nama_depan = "Rony"
nama_belakang = "Setiawan"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari", nama_lengkap, "adalah", str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di dalam string
o = "o"
status = o in nama_lengkap
print(o, "ada di", nama_lengkap, "=", status)

O = "O"
status = O in nama_lengkap
print(O, "ada di", nama_lengkap, "=", status)

z = "z"
status = z not in nama_lengkap
print(z, "ada di", nama_lengkap, "=", status)

# Mengulang String
print("Wk"*10)
print(10*"awok")

# Indexing
print("Index ke-0", nama_lengkap[0])
print("Index ke-1", nama_lengkap[1])
print("Index ke-2", nama_lengkap[2])
print("Index ke-3", nama_lengkap[3])
print("Index ke-[0:3]", nama_lengkap[0:4])
print("Index ke-[0,2,4,6,8,10]", nama_lengkap[0:11:2])

# Item paling kecil
print("Item paling kecil = ", min(nama_lengkap))
# Item paling besar
print("Item paling besar = ", max(nama_lengkap))

# ascii code
ascii_code = ord(" ")
print("ASCII Code untuk spasi adalah", str(ascii_code))
data = 120
print("Char untuk ASCII 120 adalah", chr(data))

# operator dalam bentuk method
data = "Rony Setiawan"
jumlah = data.count("a")
print("Jumlah 'a' pada data adalah", jumlah)

print("\n")
