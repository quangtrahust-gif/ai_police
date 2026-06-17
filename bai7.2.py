# bai7_2.py
ds = [10, 20, 30]
print("Ban đầu:", ds)

ds.append(40)           # thêm cuối
print("Sau append:", ds)

ds.insert(1, 15)        # chèn 15 vào vị trí 1
print("Sau insert:", ds)

ds[2] = 25              # sửa phần tử thứ 2 (20 thành 25)
print("Sau sửa:", ds)

ds.remove(30)           # xóa giá trị 30
print("Sau remove:", ds)

phan_tu_cuoi = ds.pop() # lấy và xóa cuối
print("Phần tử lấy ra:", phan_tu_cuoi)
print("Sau pop:", ds)
