soA = 2
soB = 3

students = [
    {
        "id": 1,
        "name": "Vũ Lê Bảo Long",
        "pointT": 2,
        "pointV": 3,
        "pointH": 4,
    },
    {
        "id": 2,
        "name": "Nguyễn Thị Huỳnh Nhi",
        "pointT": 5,
        "pointV": 6,
        "pointH": 7,
    },
    {
        "id": 3,
        "name": "Nguyễn Thị Ái Vy",
        "pointT": 5,
        "pointV":3,
        "pointH": 7,
    },
    {
        "id": 4,
        "name": "Nguyễn Thị Giàu",
        "pointT": 5,
        "pointV": 6,
        "pointH": 3,
    },
    {
        "id": 5,
        "name": "Nguyễn Thị Giỏi",
        "pointT":1,
        "pointV": 2,
        "pointH": 3,
    },
]

for student in students:
    avenger = (student['pointT'] + student['pointV'] + student['pointH']) / 3
    if avenger > 5:
        print(f"In thông tin các sinh viên có điểm trung bình lớn hơn 5: {student}")

for student in students:
    if student['pointH'] < 5:
        print(f"In ra các sinh viên có điểm hoá dưới 5: {student}")
