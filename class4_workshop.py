# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    for idx, movie in enumerate(movie_list, start=1):  
        print(f"{idx}. {movie['movie_name']} ราคา {movie['ticket_price']}")



# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย done
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    if age_restriction == "G":
        return True
    else:
        if user_age >= age_restriction :
            return True
        else :
            print("อายุน้อยเกินไป")
            return False


# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Sci-Fi' บวกเพิ่ม 50 บาท done
    # ถ้าไม่ใช่ คืนราคาเดิม
    if genre == "Sci-Fi":
        base_price + 50
    return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง done
    show_movies()
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5) done
    def movie_input () :
        movie_choice = int(input("เลือกตัวเลขของลำดับหนังที่จะดู : "))
        if movie_choice not in [1,2,3,4,5]:
            ("ข้อมูลที่กรอกไม่ถูกต้อง, กรุณาเลือกใหม่อีกครั้ง")
            movie_input()
        else:
            return movie_choice 
    movieChoice = movie_input()
    # 3. รับอายุผู้ใช้
    userAge = input()
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก done
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง
    print("กด 1 : แสดงหนังทั้งหมด | กด 2 : ซื้อตั๋วหนัง")
    # รับค่าตัวเลือกเมนูจากผู้ใช้ 
    menu = input("เลือกเมนู: ")

    # TODO: ตรวจสอบเมนูที่เลือก 
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
    if menu == 1:
        show_movies()
    elif menu == 2:
        buy_ticket()
    else:
        print("เมนูไม่ถูกต้อง")
        main()

# เรียก main เพื่อเริ่มโปรแกรม


