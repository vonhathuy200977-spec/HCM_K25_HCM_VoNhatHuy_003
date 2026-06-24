class CourseRegistration:
    def __init__(self, id, student_name, course_name,
                 tuition_fee, discount, extra_fee):
        self.id = id
        self.student_name = student_name
        self.course_name = course_name
        self.tuition_fee = tuition_fee
        self.discount = discount
        self.extra_fee = extra_fee
        self.total_fee = 0
        self.fee_type = ""
    def calculate_total_fee(self):
        self.total_fee = (
            self.tuition_fee - self.discount + self.extra_fee
        )
    def classify_fee(self):
        if self.total_fee < 3000000:
            self.fee_type = "Thấp"
        elif self.total_fee < 7000000:
            self.fee_type = "Trung bình"
        elif self.total_fee < 15000000:
            self.fee_type = "Cao"
        else:
            self.fee_type = "Rất cao"
    @staticmethod
    def check_input(prompt):
        while True:
            value = input(prompt).strip()
            if not value:
                print("Không được để trống!")
                continue
            return value
    @staticmethod
    def check_int(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Không được nhập số âm!")
                    continue
                return value
            except ValueError:
                print("Vui lòng nhập số nguyên!")

class CourseRegistrationManager:
    def __init__(self):
        self.registrations = []
    def find_by_id(self, registration_id):
        for registration in self.registrations:
            if registration.id.lower() == registration_id.lower():
                return registration
        return None
    def add_registration(self):
        registration_id = CourseRegistration.check_input("Nhập mã đăng ký: ")
        if self.find_by_id(registration_id):
            print("Mã đăng ký đã tồn tại!")
            return
        student_name = CourseRegistration.check_input("Nhập tên học viên: ")
        course_name = CourseRegistration.check_input("Nhập tên khóa học: ")
        tuition_fee = CourseRegistration.check_int("Nhập học phí gốc: ")
        discount = CourseRegistration.check_int(
            "Nhập giảm giá: "
        )

        extra_fee = CourseRegistration.check_int(
            "Nhập phụ phí: "
        )

        registration = CourseRegistration(
            registration_id,
            student_name,
            course_name,
            tuition_fee,
            discount,
            extra_fee
        )

        registration.calculate_total_fee()
        registration.classify_fee()

        self.registrations.append(registration)

        print("Thêm đăng ký thành công!")

    def show_all(self):
        if not self.registrations:
            print("Danh sách đăng ký đang rỗng!")
            return

        print("-" * 120)

        print(
            f"{'Mã ĐK':<10}"
            f"{'Học viên':<20}"
            f"{'Khóa học':<20}"
            f"{'Học phí':<15}"
            f"{'Giảm giá':<15}"
            f"{'Phụ phí':<15}"
            f"{'Tổng phí':<15}"
            f"{'Phân loại':<15}"
        )

        print("-" * 120)

        for registration in self.registrations:
            print(
                f"{registration.id:<10}"
                f"{registration.student_name:<20}"
                f"{registration.course_name:<20}"
                f"{registration.tuition_fee:<15}"
                f"{registration.discount:<15}"
                f"{registration.extra_fee:<15}"
                f"{registration.total_fee:<15}"
                f"{registration.fee_type:<15}"
            )

    def update_registration(self):
        registration_id = input(
            "Nhập mã đăng ký cần cập nhật: "
        ).strip()

        registration = self.find_by_id(registration_id)

        if registration is None:
            print("Không tìm thấy đăng ký!")
            return

        registration.tuition_fee = CourseRegistration.check_int(
            "Nhập học phí mới: "
        )

        registration.discount = CourseRegistration.check_int(
            "Nhập giảm giá mới: "
        )

        registration.extra_fee = CourseRegistration.check_int(
            "Nhập phụ phí mới: "
        )

        registration.calculate_total_fee()
        registration.classify_fee()

        print("Cập nhật thành công!")

    def delete_registration(self):
        registration_id = input(
            "Nhập mã đăng ký cần xóa: "
        ).strip()

        registration = self.find_by_id(registration_id)

        if registration is None:
            print("Không tìm thấy đăng ký!")
            return

        choice = input(
            "Bạn có chắc muốn xóa? (Y/N): "
        ).strip()

        if choice.lower() == "y":
            self.registrations.remove(registration)
            print("Xóa thành công!")
        else:
            print("Đã hủy thao tác!")

    def search_registration(self):
        registration_id = input(
            "Nhập mã đăng ký cần tìm: "
        ).strip()

        registration = self.find_by_id(registration_id)

        if registration is None:
            print("Không tìm thấy đăng ký!")
            return

        print("-" * 120)

        print(
            f"Mã ĐK: {registration.id}\n"
            f"Học viên: {registration.student_name}\n"
            f"Khóa học: {registration.course_name}\n"
            f"Học phí gốc: {registration.tuition_fee}\n"
            f"Giảm giá: {registration.discount}\n"
            f"Phụ phí: {registration.extra_fee}\n"
            f"Tổng phí: {registration.total_fee}\n"
            f"Phân loại: {registration.fee_type}"
        )


def menu():
    print("""
==================== MENU ====================

1. Hiển thị danh sách đăng ký khóa học
2. Thêm đăng ký khóa học
3. Cập nhật đăng ký khóa học
4. Xóa đăng ký khóa học
5. Tìm kiếm đăng ký khóa học
6. Thoát

===============================================
""")


def main():
    manager = CourseRegistrationManager()

    sample = CourseRegistration(
        "N101",
        "Huy",
        "Python",
        5000000,
        500000,
        200000
    )

    sample.calculate_total_fee()
    sample.classify_fee()

    manager.registrations.append(sample)

    while True:
        menu()

        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_registration()
            case "3":
                manager.update_registration()
            case "4":
                manager.delete_registration()
            case "5":
                manager.search_registration()
            case "6":
                print("Đã thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


main()