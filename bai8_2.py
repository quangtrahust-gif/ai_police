# bai8_2.py
# Bài toán: hai danh sách sinh viên tham gia câu lạc bộ
clb_toan = {"An", "Bình", "Chi", "Dũng"}
clb_anh = {"Bình", "Dũng", "Lan", "Mai"}

print("Tham gia CLB Toán:", clb_toan)
print("Tham gia CLB Anh:", clb_anh)

# Tham gia ít nhất một CLB
hop = clb_toan | clb_anh
print("Học sinh tham gia ít nhất một CLB:", hop)

# Tham gia cả hai
giao = clb_toan & clb_anh
print("Học sinh tham gia cả hai CLB:", giao)

# Chỉ tham gia Toán, không tham gia Anh
chi_toan = clb_toan - clb_anh
print("Chỉ tham gia CLB Toán:", chi_toan)

# Tham gia đúng một CLB
doi_xung = clb_toan ^ clb_anh
print("Tham gia đúng một CLB:", doi_xung)
