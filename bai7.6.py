# bai7_6.py
so_goc = list(range(1, 21))
so_chan = [x for x in so_goc if x % 2 == 0]
so_le = [x for x in so_goc if x % 2 != 0]
print("Số gốc:", so_goc)
print("Số chẵn:", so_chan)
print("Số lẻ:", so_le)
