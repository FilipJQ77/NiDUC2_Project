# używanie innych plików - po prostu import nazwa_pliku
# import random
# import time
import data

# lista = data.generate_random_data(10)
# data.print_data_bool(lista)

# lista2 = data.generate_random_data(5)
# data.print_data_bool(lista2)

# lista.append(True)
# data.print_data_bool(lista)
# lista2.remove(True)
# data.print_data_bool(lista2)

# lista = data.generate_random_data(10)
# data.encode_hamming(lista)

lista = data.generate_random_data(4)
data.print_data(lista)
lista = data.encode_parity(lista)
data.print_data(lista)
lista = data.decode_parity(lista)
if lista is not None:
    data.print_data(lista)
else:
    print("oof")