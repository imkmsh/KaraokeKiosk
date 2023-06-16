admin_pw = "0000"
members = []
rooms = []
income = []


def home():
    print("MS 코인 노래방에 오신 것을 환영합니다.")
    print("관리자 모드 (99)")
    home_action = input("회원 결제 (1) / 비회원 결제 (2) / 회원가입 (3)\n")
    if home_action == "1":
        login()
    elif home_action == "2":
        pay()
    else:
        register()
    

def register():
    global members
    id_check = True
    id = input("등록할 ID를 입력하세요.")
    for member in members:
        if member["id"] == id:
            id_check = False
    if id_check:
        pw = input("사용 가능한 ID입니다. 비밀번호를 설정하세요.\n")
        pw_check = input("비밀번호를 한 번 더 입력하세요.\n")
        if pw != pw_check:
            print("비밀번호가 일치하지 않습니다. 다시 입력하세요.")
        else:
            members.append({"id": id, "pw": pw, "money": 0})
            print("회원가입이 완료되었습니다.")
    else:
        register()
    
   
def login():
    pass


def charge():
    pass


def room():
    pass
          
          
def pay():
    pass
          
def admin():
    global admin_pw
    pw = input("관리자 페이지입니다. 비밀번호를 입력하세요.\n")
    if pw != admin_pw:
        print("잘못된 비밀번호입니다. 다시 입력하세요.")
    else:
        admin_action = input("비밀번호 변경 (1) / 매출 확인 (2)\n")
        if admin_action == "1":
            checking_new_pw = True
            while checking_new_pw:
                new_pw = input("변경할 비밀번호를 입력하세요.\n")
                new_pw_check = input("변경할 비밀번호를 입력하세요.\n")
                if new_pw == new_pw_check:
                    checking_new_pw = False
                    print("비밀번호가 변경되었습니다.")
                    admin()
        else:
            print(f"매출 누적액입니다. \t{sum(income)} 원")
            print(f"1회 최고 매출액입니다.\t {max(income)} 원")  


# 실행부


