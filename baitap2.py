print("="*63)
print("Trò chơi búa kéo lá")
print("="*63)
print("Đang tải...")
import random
mayselect = [1, 2, 3]
print("="*63)
while True:
    print("1. Búa")
    print("2. Kéo")
    print("3. Lá")
    you = int(input("Bạn nhập: "))
    may = random.choice(mayselect)
    if (you > 3):
        print("Không hợp lệ!")
    else:
        print("Máy nhập:", may)
        if (you == 1) and (may == 2):
            print("="*63)
            print("Thắng")
            print("="*63)
        elif (you == 2) and (may == 1):
            print("="*63)
            print("Thua")
            print("="*63)
        elif (you == 2) and (may == 3):
            print("="*63)
            print("Thắng")
            print("="*63)
        elif (you == 3) and (may == 2):
            print("="*63)
            print("Thua")
            print("="*63)
        elif (you == 3) and (may == 1):
            print("="*63)
            print("Thắng")
            print("="*63)
        elif (you == 1) and (may == 3):
            print("="*63)
            print("Thua")
            print("="*63)
        elif (you == may):
            print("="*63)
            print("Hòa!")
            print("="*63)
    print("Chơi tiếp không?")
    print("="*63)
    choice = input("Yes hay No (y/n)? ")
    print("="*63)
    if (choice == "n"):
        break
print("Vậy thì tạm biệt, chúc một ngày tốt lành")
print("           --- Thank you ---")
print("="*63)