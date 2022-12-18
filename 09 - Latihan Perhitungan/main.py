# LATIHAN KONVERSI SATUAN

# PROGRAM KONVERSI TEMPERATUR

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# CELCIUS
print("===== CELCIUS =====")
suhu = float(input("Masukkan suhu dalam celcius : "))
print("Suhu =", suhu, "Celcius")
# REAMUR
reamur = (4/5) * suhu
print("Suhu dalam Reamur =", reamur, "Reamur")
# Fahrenheit
fahrenheit = ((9/5) * suhu) + 32
print("Suhu dalam Fahrenheit =", fahrenheit, "Fahrenheit")
# Kelvin
Kelvin = suhu + 273
print("Suhu dalam Kelvin =", Kelvin, "Kelvin")

print("\n===== REAMUR =====")
# CELCIUS
celcius = (5/4) * suhu
print("Reamur dalam Celcius =", celcius)
# FAHRENHEIT
fahrenheit = ((9/4) * suhu) + 32
print("Reamur dalam Fahrenheit =", fahrenheit)
# KELVIN
kelvin = ((5/4) * suhu) + 273
print("Reamur dalam Kelvin =", kelvin)

print("\n===== FAHRENHEIT =====")
# CELCIUS
celcius = (5/9 * (suhu - 32))
print("Fahrenheit dalam Celcius =", celcius)
# REAMUR
reamur = (4/9 * (suhu - 32))
print("Fahrenheit dalam Reamur =", reamur)

print("\n===== KELVIN =====")
# CELCIUS
celcius = suhu - 273
print("Kelvin dalam Celcius =", celcius)
# REAMUR
reamur = (4/5 * (suhu - 273))
print("Kelvin dalam Reamur =", reamur)


print("\n")
