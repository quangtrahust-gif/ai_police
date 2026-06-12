# bai8_6.py
# List -> Set (loại trùng)
ds_so = [1, 2, 2, 3, 4, 4, 5]
tap_so = set(ds_so)
print(f"List ban đầu: {ds_so}")
print(f"Set (không trùng): {tap_so}")

# Set -> List
ds_moi = list(tap_so)
print(f"List từ set: {ds_moi}")

# List các cặp -> Dictionary
cap_so = [("a", 1), ("b", 2), ("c", 3)]
tu_dien = dict(cap_so)
print(f"Dictionary từ list cặp: {tu_dien}")

# Dictionary -> List các tuple
danh_sach_tuple = list(tu_dien.items())
print(f"List các tuple: {danh_sach_tuple}")
