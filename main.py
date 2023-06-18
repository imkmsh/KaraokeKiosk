admin_pw = "0000"
members = [{"id": "admin", "pw": "admin", "money": 0}]
rooms = []
income = [0]
room_to_pay = 0

for i in range(10):
    rooms.append({
        "room_id": i+1,
        "using": 0
    })


def home():
    print("MS 코인 노래방에 오신 것을 환영합니다.")
    home_action = input("노래방 이용 (1) / 관리자 모드 (99)\n")
    if home_action == "1":
        room()
        pay_action = input("회원 결제 (1) / 비회원 결제 (2) / 회원가입 (3)\n")
        if pay_action == "1":
            login()
        elif pay_action == "2":
            pay()
        elif pay_action == "3":
            register()
        else:
            home()
    elif home_action == "99":
        admin()
    else:
        home()
    

def register():
    global members
    id_check = True
    id = input("등록할 ID를 입력하세요.\n")
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
            # print(members)
            home()
    else:
        retry = input("이미 등록된 아이디입니다. 다른 아이디를 사용하세요. 다시 시도 (1) / 비회원 결제 (2)\n")
        if retry == "2":
            pay()
        else:
            register()
            
    
   
def login():
    global members
    id = input("등록된 ID를 입력하세요.\n")
    now_member = False
    for member in members:
        if member["id"] == id:
            now_member = member
            continue
    if now_member:
        pw = input("비밀번호를 입력하세요.\n")
        if now_member["pw"] == pw:
            pay(id)
        else:
            fail_action = input("일치하는 사용자 정보가 없습니다.\n다시 시도 (1) / 비회원 결제 (2) / 회원 가입 (3)\n")
            if fail_action == "1":
                login()
            elif fail_action == "2":
                pay()
            else:
                register()
    else:
        fail_action = input("일치하는 사용자 정보가 없습니다.\n다시 시도 (1) / 비회원 결제 (2) / 회원 가입 (3)\n")
        if fail_action == "1":
            login()
        elif fail_action == "2":
            pay()
        else:
            register()


def room():
    global rooms
    global room_to_pay
    room_possible = []
    for room in rooms:
        if room["using"] == 0:
            room_possible.append(room["room_id"])
    room_want = int(input(f"현재 사용 가능한 방은 {room_possible}입니다. 몇 번 방을 사용하시겠습니까? (숫자만 입력)\n"))
    if room_want in room_possible:
        room_to_pay = room_want
    else:
        print("선택할 수 없는 방입니다. 다시 선택해 주세요.")
        room()
          
          
def pay(id="비회원"):
    global rooms
    global room_to_pay
    global members
    global income
    insert = int(input("1000원에 3곡입니다. 얼마를 결제하시겠습니까? (1000으로 나눠 떨어지는 숫자만 입력, 결제 취소 (0))\n"))
    if insert % 1000 != 0:
        print("잘못된 금액입니다. 다시 입력하세요.")
        pay(id)
    elif insert == 0:
        home()
        
    if id == "비회원":
        print(f"\n결제가 완료되었습니다. {room_to_pay}번 방을 사용하세요.")
        income.append(insert)
        for room in rooms:
            if room["room_id"] == room_to_pay:
                room["using"] = 1
    else:
        no_money = True
        retry = "1"
        while no_money and retry == "1":
            for member in members:
                if member["id"] == id:
                    now_money = member["money"]
            if now_money < insert:
                how_much = int(input(f"현재 잔액은 {now_money}원입니다. 얼마를 더 충전하시겠습니까? (숫자만 입력)\n"))
                for member in members:
                    if member["id"] == id:
                        member["money"] += how_much
                now_money += how_much
                retry = input("결제를 계속하시겠습니까? 예 (1) / 아니오 (2)\n")
            else:
                print(f"현재 잔액은 {now_money}원입니다. {insert}원이 사용됩니다.")
                for member in members:
                    if member["id"] == id:
                        member["money"] -= insert
                no_money = False
                print(f"\n결제가 완료되었습니다. {room_to_pay}번 방을 사용하세요.")
                income.append(insert)
                for room in rooms:
                    if room["room_id"] == room_to_pay:
                        room["using"] = 1
    # print(rooms)
    print("♪₊(˘ᵋॢ ˘ॢ⌯)*·♫\n")
    home()
    
        
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
                new_pw_check = input("변경할 비밀번호를 한 번 더 입력하세요.\n")
                if new_pw == new_pw_check:
                    checking_new_pw = False
                    print("비밀번호가 변경되었습니다.")
                    admin_pw = new_pw
        else:
            print(f"매출 누적액입니다. --------- {sum(income)} 원")
            print(f"1회 최고 매출액입니다. ----- {max(income)} 원") 
    home()


# 실행부

home()

# admin에서 비번 바꿔주고
# 없는 방 한 번 골라주고,
# 비회원 결제, 거기서 금액 한 번 잘 못 눌러주고, 2000원 결제
# 회원 결제 눌러서 회원 가입 들어가고
# 회원이 10000원 충전해서 5000원 결제
# 똑같은 회원이 2000원 결제할때 잔액 유지되는거 보여주기
# admin에서 매출액 확인