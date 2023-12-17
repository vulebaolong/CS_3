class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        for khoaHoc in self.khoaHoc:
            khoaHoc.thongTinKhoaHoc()

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        print(f"Tên khóa học: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi}")

# Tạo các đối tượng Học viên và Khóa học
hv1 = HocVien("HV001", "Nguyen Van A", "01/01/2000")
hv2 = HocVien("HV002", "Tran Thi B", "02/02/2001")

kh1 = KhoaHoc("KH001", "Python cơ bản", "Offline", 1000000)
kh2 = KhoaHoc("KH002", "Machine Learning", "Online", 1500000)

# Đăng ký khóa học cho học viên
hv1.dangKyKhoaHoc(kh1)
hv1.dangKyKhoaHoc(kh2)

hv2.dangKyKhoaHoc(kh2)

# Hiển thị danh sách khóa học đã đăng ký của từng học viên
print("Danh sách khóa học đã đăng ký của học viên 1:")
hv1.hienThiKhoaHoc()

print("\nDanh sách khóa học đã đăng ký của học viên 2:")
hv2.hienThiKhoaHoc()
