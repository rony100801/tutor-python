# Latihan Komparasi dan Logika
# Membuat gabungan area rentang dari angka

# # +++++3-----10+++++
print("\n")
# inputUser = float(input("Masukkan angka < 3 atau > 10 : "))
# # print(inputUser)

# # +++++3-----
# isKurangDari = (inputUser < 3)
# print("Kurang dari 3 = ", isKurangDari)

# # -----10+++++
# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 = ", isLebihDari)

# # 3-----10
# isCorrect = (isKurangDari or isLebihDari)
# print("Angka yang anda masukkan =", isCorrect)

# print("===============")

# # -----3+++++10-----
# inputUser = float(input("Masukkan angka > 3 dan < 10 : "))

# # ------3+++++
# lebihDari3 = (inputUser > 3)
# print("Lebih dari 3 = ", lebihDari3)

# # +++++10-----
# isKurangDari = (inputUser < 10)
# print("Kurang dari 10 =", isKurangDari)

# # 3+++++10
# isCorrect = (lebihDari3 and isKurangDari)
# print("Angka yang anda masukkan =", isCorrect)

# SOAL NO 1
# -----0+++++5-----8+++++11-----
inputUser = float(input("Masukkan angka > 0 dan < 5 atau > 8 dan < 11 : "))

# ----0+++++
angka0 = (inputUser > 0)
angka5 = (inputUser < 5)
angka8 = (inputUser > 8)
angka11 = (inputUser < 11)
hasilAkhir = ((angka0 and angka5) or (angka8 and angka11))
print("Hasil Akhir = ", hasilAkhir)

# SOAL NO 2
# +++++0-----5+++++8-----11+++++
angka0 = (inputUser < 0)
angka5 = (inputUser > 5)
angka8 = (inputUser < 8)
angka11 = (inputUser > 11)
hasilAkhir = ((angka0 or angka5) and (angka8 or angka11))
print("Hasil Akhir = ", hasilAkhir)

print("\n")
