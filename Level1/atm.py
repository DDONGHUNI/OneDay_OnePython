# ATM 기능

import datetime

money = 0
history = [] #거래내역 조회 배열

print("===== ATM MENU =====")
print("1. 잔액조회")
print("2. 입금")
print("3. 출금")
print("4. 거래내역 조회")
print("0. 종료")
print("====================")

while True:

    atm = input("원하는 메뉴를 선택하세요: ")

    if (atm == "1"):
        print(f"현재 잔액은 {money}원입니다.\n")
    
    elif (atm == "2"):
        try:
            plus = int(input("입금액을 입력하세요 : "))
            if plus > 0:
                money += plus
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                record = f"[{now}] 입금: +{plus:,}원 (잔액: {money:,}원)"
                history.append(record)
                print(f"[입금 완료] 현재 잔액 : {money:,}원\n")
            else:
                print("[오류] 1이상 정수를 입력하세요.\n")
        except ValueError:
            print("숫자만 입력해주세요.\n")

    elif (atm == "3"):
        try:
            minus = int(input("출금액을 입력하세요 : "))
            if minus > money:
                print("잔액이 부족합니다.")
            elif minus <= 0:
                print("0보다 큰 금액을 입력해주세요.")
            else:
                money -= minus
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                record = f"[{now}] 출금: -{minus:,}원 (잔액: {money:,}원)"
                history.append(record)
                print(f"출금 후 잔액은 {money:,}원입니다.\n")
        except ValueError:
            print("숫자만 입력해주세요.")
            
    elif (atm == "4"):
        print("===== 거래내역 조회 =====")
        if not history:
            print("거래 내역이 없습니다.\n")
        else:
            for record in history[::-1]:
                print(record)
        print("========================\n")

    elif (atm == "0"):
        print("ATM을 종료합니다.\n")
        break
        
    else:
        print("메뉴에 있는 번호를 다시 입력해주세요.\n")