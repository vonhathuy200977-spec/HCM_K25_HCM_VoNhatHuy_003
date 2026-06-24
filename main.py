class  CourseRegisration():
    def __init__(self, id, student_name,course_name,tuition_fee,discount,extra_fee):
        self.id = id
        self.student_name = student_name
        self.course_name = course_name
        self.tuition_fee = tuition_fee
        self.discount = discount
        self.extra_fee = extra_fee
        self.total_fee = 0
        self.fee_type = ""
    def calculate_total_fee(self):
        self.total_fee = self.tuition_fee - self.discount + self.extra_fee
    def classify_fee(self):
        if self.total_fee < 3000000:
            self.fee_type = "Thấp"
        elif self.total_fee < 7000000:
            self.fee_type = "Trung bình"
        elif self.total_fee <15000000:
            self.fee_type = "Cao"
        else:
            self.fee_type = "Rất Cao"
    @staticmethod
    def check_int(prompt):
        while True:
            input_num = input(prompt)
            try:
                num = int(input_num)
                if not num:
                    print("không được để trống")
                    continue
                if num < 0:
                    print("không được nhập số âm")
                    continue
                return num
            except ValueError:
                print("vui lòng nhập số")
    @staticmethod
    def check_input(prompt):
        while True:
            check_input = input(prompt)
            if not check_input:
                print("không được để rỗng")
                continue
            return check_input


class CourseRegisrationManager:
    def __init__(self):
        self.registrations = []
    # def find_by_id():
        
         
            
    def add_registrations(self):
        id_regis = CourseRegisration.check_input("hãy nhập id: ")
        name_regis = CourseRegisration.check_input("hãy nhập tên học viên: ")
        course_regis = CourseRegisration.check_input("hãy nhập tên khóa học: ")
        tuition_regis = CourseRegisration.check_int("hãy nhập học phí gốc: ")
        discount_regis = CourseRegisration.check_int("hãy nhập giảm giá: ")
        extra_regis = CourseRegisration.check_int("hãy nhập phụ phí: ")
        new_regis = CourseRegisration.calculate_total_fee(self)
        new_regis = CourseRegisration.classify_fee(self)
        self.registrations.append(new_regis)
        print("đã thêm thành công")
    def show_all(self):
        if not self.registrations:
            print("Danh sách đăng ký khóa học đang rỗng")
            return
        print(f"{"Mã đăng ký"} | {"Họ tên học viên"} | {"Tên khóa học"} | {"Học phí gốc"} | {"Giảm giá"} | {"Phụ phí"} | {"Tổng học phí"} | {"Phân loại học phí"}")
        for regis in self.registrations:
            print(f"{regis.id:<10} | {regis.student_name:<10} | {regis.course_name:<10} | {regis.tuition_fee:<10} | {regis.discount:<10} | {regis.extra_fee:<10} | {regis.total_fee:<10} | {regis.fee_type:<10}")

    def update_registrations(self):
        id_input = input("hãy nhập mã đăng ký cần cập nhật")
        found = False
        for regis in self.registrations:
            if id_input.strip().lower() == id :
                found = True
                new_tuition = CourseRegisration.check_int("hãy nhập học phí gốc: ")
                new_discount = CourseRegisration.check_int("hãy nhập giảm giá: ")
                new_fee = CourseRegisration.check_int("hãy nhập phụ phí: ")
                print("cập nhật học phí công")
            else:
                print("không tìm thấy ")
                found = False
            
            
    def delete_registrations(self):
        id_input = input("hãy nhập mã đăng ký cần cập nhật")
        found = False
        for regis in self.registrations:
            if id_input.strip().lower() == id :
                found = True
                del_choice = input("bạn có muốn xóa đăng ký khóa học không")
                match del_choice:
                    case "Y/y":
                        print("xóa đăng ký khóa học thành công")
                        self.registrations.remove(id_input)
                    case "N/n":
                        print("hủy thao tác")
                        break
                    case _:
                        print("lựa chọn của bạn không hợp lệ")

    def search_registrations(self):
        pass

def menu():
    print("""
    ========================MENU========================
    1.Hiển thị danh sách đăng ký khóa học
    2.Thêm đăng ký khóa học mới
    3.Cập nhật khóa học mới
    4.Xóa đăng ký khóa học
    5.Tìm kiếm đăng ký
    6.Thoát
    =====================================================
""")
    
def main():
    manage_regis = CourseRegisrationManager()
    manage_regis = [
        CourseRegisration("n101","huy","cntt",100,10,15)
    ]
    while True:
        menu()
        choice = input("hãy nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                manage_regis.show_all()
            case "2":
                manage_regis.add_registrations()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("đã thoát khỏi chương trình")
            case _:
                print("lựa chọn của bạn ko hợp lệ")


main()