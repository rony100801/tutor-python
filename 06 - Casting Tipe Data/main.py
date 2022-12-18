# OPERATOR CASTING TIPE DATA
# Tipe Data = int, float, str, boolean

print("\n")

# INTEGER
print("===== INTEGER =====")
data_int = 10
print("Data : ", data_int, " | Tipe : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data : ", data_float, " | Tipe : ", type(data_float))
print("Data : ", data_str, " | Tipe : ", type(data_str))
print("Data : ", data_bool, " | Tipe : ", type(data_bool))

# FLOAT
print("\n")
print("===== FLOAT =====")
data_float = 10.5
print("Data : ", data_float, " | Tipe : ", type(data_float))

data_int = int(data_float)  # Dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("Data : ", data_int, " | Tipe : ", type(data_int))
print("Data : ", data_str, " | Tipe : ", type(data_str))
print("Data : ", data_bool, " | Tipe : ", type(data_bool))

# BOOLEAN
print("\n")
print("===== BOOLEAN =====")
data_bool = True
print("Data : ", data_bool, " | Tipe : ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Data : ", data_int, " | Tipe : ", type(data_int))
print("Data : ", data_str, " | Tipe : ", type(data_str))
print("Data : ", data_float, " | Tipe : ", type(data_float))

# STRING
print("\n")
print("===== STRING =====")
data_str = "10"
print("Data : ", data_str, " | Tipe : ", type(data_str))

data_int = int(data_str)  # Harus Angka
data_str = str(data_str)  # Harus Angka
data_bool = bool(data_str)  # Kosong / True
print("Data : ", data_int, " | Tipe : ", type(data_int))
print("Data : ", data_str, " | Tipe : ", type(data_str))
print("Data : ", data_bool, " | Tipe : ", type(data_bool))


print("\n")
