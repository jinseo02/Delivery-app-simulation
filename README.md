# Delivery-app-simulation
배달 앱 시퀀스 다이어그램 및 코드 구현

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

# 샘플 코드에 대한 평가.
1. 가독성 평가.
- 시퀀스 다이어그램 흐름을 따라 제작하였기에 전체적으로 가독성이 높다고 생각됨.
- 함수의 이름을 자연어인 한글로 정의하여 가독성을 높임.
- 구조체, 주석처리로 순서를 가시적으로 구현함.
- print 함수로 흐름을 직관적으로 파악할 수 있음.

2. 응집도 평가.
- 각 함수는 위의 주석처리한 대로 하나의 기능만 수행함.
- 따라서, 이전 교수님께서 강조하신 '유지보수' 측면에 이로움이 있을 것이라고 판단됨.

3. 결합도 평가
- 구조화된 함수 간의 데이터 전달은 오직 order를 통해 이뤄짐.
- 다른 주문 시스템으로 대체하거나 확장할 때 유리하다고 생각함.
