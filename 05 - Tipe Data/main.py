# 05 - TIPE DATA

# 1. Tipe Data : Angka Satuan (Integer)
from ctypes import c_double
data_integer = 9
print("Data : ", data_integer, "| Bertipe : ", type(data_integer))

# 2. Tipe Data : Angka Dengan Koma (Float)
data_float = 5.5
print("Data : ", data_float, "| Bertipe : ", type(data_float))

# 3. Tipe Data : Kumpulan Karakter (String)
data_string = "Hello World"
print("Data : ", data_string, "| Bertipe : ", type(data_string))

# 4. Tipe Data : Biner True/False (Boolean)
data_bool = True
print("Data : ", data_bool, "| Bertipe : ", type(data_bool))

# TIPE DATA KHUSUS

# 1. Bilangan Kompleks
data_kompleks = complex(5, 6)
print("Data : ", data_kompleks, "| Bertipe : ", type(data_kompleks))

# 2. Tipe Data Dari Bahasa C

data_c_double = c_double(10.5)
print("Data : ", data_c_double, "| Bertipe : ", type(data_c_double))
