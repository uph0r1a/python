A , B , TongTienRut = map(int, input().split())
TienLon, TienNho = max(A,B), min(A,B)
SoTienLon = TongTienRut // TienLon
TienThua = TongTienRut % TienLon
SoTienNho = TienThua // TienNho
TienThua = TienThua % TienNho
print(SoTienLon+SoTienNho+TienThua)