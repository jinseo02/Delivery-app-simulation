class Order:
    def __init__(self, user_name, menu, price):
        self.user_name = user_name
        self.menu = menu
        self.price = price

# 1. 사용자 주문 요청.
def 사용자_주문요청():
    print("[사용자] 메뉴를 선택합니다.")
    return Order("홍길동", "불고기 피자", 15000)

# 2. 앱 >>> 서버로 주문 전송.
def 앱_주문전송(order):
    print(f"[앱] 서버에 주문 전송: {order.menu} (₩{order.price})")

# 3. 서버 >>> 결제 시스템.
def 서버_결제요청(order):
    print(f"[서버] {order.user_name}님의 '{order.menu}' 결제 요청")
    print("[결제 시스템] 결제 완료")
    return True

# 4. 서버 >>> 식당.
def 서버_식당전달(order):
    print(f"[서버] 식당에 '{order.menu}' 주문 전달")
    print("[식당] 주문 수락 및 조리 시작")

# 5. 서버 >>> 라이더 시스템.
def 서버_라이더요청():
    print("[서버] 라이더 호출 요청")
    print("[라이더 시스템] 배달 기사 배정 완료")

# 6. 앱 >>> 사용자.
def 앱_알림(order):
    print(f"[앱] {order.user_name}님, 주문이 완료되었습니다. 배달이 곧 시작됩니다.")

# 전체 흐름 실행.
def main():
    order = 사용자_주문요청()
    앱_주문전송(order)

    if 서버_결제요청(order):
        서버_식당전달(order)
        서버_라이더요청()
        앱_알림(order)
    else:
        print("[앱] 결제 실패. 주문이 취소되었습니다.")

if __name__ == "__main__":
    main()