import random

suits = ["โพดำ", "โพแดง", "ข้าวหลามตัด", "ดอกจิก"]
points = list(range(2, 15))

def get_card_name(card):
    point, suit = card
    point_map = {11: "J", 12: "Q", 13: "K", 14: "A"}
    name = point_map.get(point, str(point))
    return f"{name} {suit}"

def get_card_color(card):
    point, suit = card
    if suit in ["โพแดง", "ข้าวหลามตัด"]:
        return "แดง"
    else :
        return "ดำ"

def draw_card():
    point = random.choice(points)
    suit = random.choice(suits)
    return (point, suit)

def card_guessing_game():
    print("=== ยินดีต้อนรับสู่เกม CARD GUESSING GAME! ===")
    print("ทายไพ่ 4 รอบเพื่อเอาชนะ ทายผิดแพ้ทันที!\n")

    card1 = draw_card()

    while True:
        try:
            color = input("รอบที่ 1 [1: แดง / 2: ดำ] พิมพ์ 1 หรือ 2: ").strip()
            if color not in ["1", "2"]:
                raise ValueError("โปรดพิมพ์เฉพาะ '1' หรือ '2' เท่านั้น")
            break
        except ValueError as e:
            print(f"[ข้อผิดพลาด]: {e}")

    if color == "1" :
        choice = "แดง"
    else :
        choice = "ดำ"

    actual_color = get_card_color(card1)
    print(f"ไพ่ใบที่ 1 คือ: {get_card_name(card1)} (สี{actual_color})")

    if choice != actual_color:
        print(" คุณทายผิด คุณแพ้แล้ว")
        return

    print("ถูกต้อง ผ่านเข้ารอบถัดไป\n")

    card2 = draw_card()

    while True:
        try:
            value = input(f"รอบที่ 2 ไพ่ใบถัดไปจะ [1: สูง / 2: ต่ำ] กว่า {get_card_name(card1)} พิมพ์ 1 หรือ 2: ").strip()
            if value not in ["1", "2"]:
                raise ValueError("โปรดพิมพ์เฉพาะ '1' หรือ '2' เท่านั้น")
            break
        except ValueError as e:
            print(f"[ข้อผิดพลาด]: {e}")

    if value == "1" :
        choice = "สูง"
    else :
        choice = "ต่ำ"

    print(f"ไพ่ใบที่ 2 คือ: {get_card_name(card2)}")

    if card2[0] == card1[0]:
        print(" แต้มเท่ากัน ถือว่าทายผิด คุณแพ้แล้ว")
        return

    is_higher = card2[0] > card1[0]
    if (choice == "สูง" and not is_higher) or (choice == "ต่ำ" and is_higher):
        print(" คุณทายผิด คุณแพ้แล้ว")
        return

    print("ถูกต้อง ผ่านเข้ารอบถัดไป\n")

    card3 = draw_card()

    min_val = min(card1[0], card2[0])
    max_val = max(card1[0], card2[0])

    while True:
        try :
            scope = input(f"รอบที่ 3 ไพ่ใบถัดไปจะ [1: อยู่ในขอบเขต / 2: อยู่นอกขอบเขต] ของ ({get_card_name(card1)} - {get_card_name(card2)}) พิมพ์ 1 หรือ 2: ").strip()
            if scope not in ["1", "2"]:
                raise ValueError ("กรุณาพิมพ์ 1 หรือ 2")
            break
        except ValueError as e :
            print(f"[ข้อผิดพลาด] : {e}")

    if scope == "1" :
        choice = "ใน"
    else :
        choice = "นอก"

    print(f"ไพ่ใบที่ 3 คือ: {get_card_name(card3)}")

    is_inside = min_val < card3[0] < max_val
    if (choice == "ใน" and not is_inside) or (choice == "นอก" and is_inside):
        print(" คุณทายผิด คุณแพ้แล้ว")
        return

    print("ถูกต้อง ผ่านเข้ารอบสุดท้าย")

    card4 = draw_card()

    suit_map = {
        "1": "โพดำ",
        "2": "โพแดง",
        "3": "ข้าวหลามตัด",
        "4": "ดอกจิก",}

    while True:
        try :
            valuesuit = input("รอบที่ 4 เลือกดอกไพ่ [1: โพดำ / 2: โพแดง / 3: ข้าวหลามตัด / 4: ดอกจิก] พิมพ์ 1-4: ").strip()
            if valuesuit not in suit_map:
                raise ValueError ("กรุณาพิมพ์ตัวเลข '1', '2', '3' หรือ '4' เท่านั้น")
            break
        except ValueError as e :
            print(f"[ข้อผิดพลาด] : {e}")

    choice = suit_map[valuesuit]

    print(f"ไพ่ใบที่ 4 คือ: {get_card_name(card4)}")

    if choice == card4[1]:
        print(" ยินดีด้วย คุณทายถูกครบทั้ง 4 รอบ ชนะเกม CARD GUESSING GAME! ")
    else:
        print(" คุณทายผิด คุณแพ้แล้ว น่าเสียดายจริงๆ T-T ")

card_guessing_game()