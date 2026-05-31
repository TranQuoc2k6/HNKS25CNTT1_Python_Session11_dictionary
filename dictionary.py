
"""
    distionary: từ điển_ đây là kiểu dữ liệu dùng để lưu trữ dữ liệu dưới dạng key và value
    - vd: lưu thông tin của một sinh viên , lưu thông tin của một sản phẩm bài viết, bình luận,..
    - cú pháp:
        my_distionary = {
            key: value
        }
"""


# Cú pháp khai báo dictionary
user = {
    "name" : "Trần Anh Quốc",
    "age": 18,
    "isMarried": False,
    "hobbie": ["Cầu lông", "Bơi lội"]
}

# Truy xuất giá trị trong dictionary
print(f"Tên: {user['name']}")
print(f"Tuổi: {user["age"]}")
print(f"Trạng thái hôn nhân: {user['isMarried']}")
print(f"Sở thích cá nhân: {user['hobbie']}")
for i in range(len(user["hobbie"])):
    print(f"Sở thích: {user['hobbie'][i]}")


product = {
    "product_name": "Iphone 14pro",
    "product_id": "IP002",
    "product_price": 14000000,
    "product_quantity": 3
}
