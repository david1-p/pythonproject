import random

input("Enter 키를 누르면 시작합니다...")

p1Name = input("플레이어1 이름을 입력해주세요: ")
p2Name = input("플레이어2 이름을 입력해주세요: ")
playerNames = p1Name[:11].center(11) + "    " + p2Name[:11].center(11)

print(
    """ 여기 두 개의 상자가 있습니다:
      
  ----------          ----------
  /         /|        /         /|
+---------+ |       +---------+ |
|  RED    | |       |  GOLD   | | 
|  BOX    | /       |  BOX    | /
+---------+/        +---------+/"""
)

print()
print(playerNames)
print()
print(p1Name + ", RED BOX가 너 앞에 있어.")
print(p2Name + ", GOLD BOX가 너 앞에 있어.")
print()
print(p1Name + ", 너는 상자 안을 볼 수 있어.")
print(p2Name.upper() + ", 눈을 감고 보지마!")
input("When " + p2Name + " has closed their eyes, press Enter...")
print()

print(p1Name + " here is the inside of your box:")

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print(
        """
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|         __________
  /   ||   /|        /         /|
+---------+ |       +---------+ |
|  RED    | |       |  GOLD   | | 
|  BOX    | /       |  BOX    | /
+---------+/        +---------+/
(carrot!)"""
    )
    print(playerNames)
else:
    print(
        """
   _________
  |         |
  |         |
  |_________|         __________
 /         /|        /         /|
+---------+ |       +---------+ |
|  RED    | |       |  GOLD   | | 
|  BOX    | /       |  BOX    | /
+---------+/        +---------+/
(no carrot!)"""
    )
    print(playerNames)

input("Press Enter to continue...")

print("\n" * 100)  # 화면을 깨끗하게 만든다.
print(p1Name + ", tell " + p2Name + " to open their eyes.")
input("Press Enter to continue...")

print()
print(p1Name + ", say one of the following sentences to " + p2Name + ".")
print(" 1) There is a carrot in my box.")
print(" 2) There is not a carrot in my box.")
print()
input("Then press Enter to continue...")

print()
print(p2Name + "," + p1Name + "상자 바꾸고 싶니? Yes/No")

while True:
    response = input(". ").upper()
    if not (response.startswith("Y") or response.startswith("N")):
        print(p2Name + ", Yes or No.")
    else:
        break

firstBox = "RED "  # 'D' 다음에 공백이 있음에 주의하자.
secondBox = "GOLD"

if response.startswith("Y"):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print(
    """HERE ARE THE TWO BOXED:
    
  __________          __________
 /         /|        /         /|
+---------+ |       +---------+ |
|    {}   | |       |  {}     | | 
|  BOX    | /       |  BOX    | /
+---------+/        +---------+/""".format(
        firstBox, secondBox
    )
)
print(playerNames)

input("Press Enter to reveal the winner...")
print()

if carrotInFirstBox:
    print(
        """
   ___VV____           _________
  |   VV    |         |         |
  |   VV    |         |         |
  |___||____|         |_________|
  /   ||   /|        /         /|
+---------+ |       +---------+ |
|  {}     | |       |  {}     | | 
|  BOX    | /       |  BOX    | /
+---------+/        +---------+""".format(
            firstBox, secondBox
        )
    )

else:
    print(
        """
   _________          ___VV____ 
  |         |        |   VV    |
  |         |        |   VV    |
  |_________|        |___||____|
 /         /|       /    ||   /|
+---------+ |      +---------+ |
|  {}     | |      |  {}     | |
|  BOX    | /      |  BOX    | /
+---------+        +---------+/""".format(
            firstBox, secondBox
        )
    )

print(playerNames)

# 'carrotInFirstBox' 변수에 따라 판단
if carrotInFirstBox:
    print(p1Name + " is the winner!")
else:
    print(p2Name + " is the winner!")
