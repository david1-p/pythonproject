import sys, random, time

try:
    import bext
except ImportError:
    print("This program requires the bext module, which is not installed.")
    print('Please install it with "pip install bext".')
    sys.exit()

# 상수 설정:
WIDTH, HEIGHT = bext.size()
# 줄바꿈을 자동으로 추가하지 않으면 윈도우의 마지막 열에 출력할 수 없으므로,
# 넓이를 1 줄인다:
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# logo 딕셔너리에 대한 키 이름:
COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"


def main():
    bext.clear()

    # 몇 개의 로고 생성하기
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append(
            {
                COLOR: random.choice(COLORS),
                X: random.randint(0, WIDTH - 4),
                Y: random.randint(0, HEIGHT - 4),
                DIR: random.choice(DIRECTIONS),
            }
        )
        if logos[-1][X] % 2 == 1:
            # X가 짝수여야 코너에 닿을 수 있기 때문에 짝수가 되도록 한다.
            logos[-1][X] -= 1

    cornerBounces = 0  # 코너에 닿은 횟수
    while True:  # 메인 프로그램 루프
        for logo in logos:  # logos 리스트에 있는 각 logo에 대한 처리
            # logo의 현재 위치 지우기:
            bext.goto(logo[X], logo[Y])
            print("    ", end="")  # 4칸을 비워서 logo를 지운다.

            originalDirection = logo[DIR]

            # logo가 코너에 닿았는지 확인:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # logo가 왼쪽 끝에 닿았는지 확인:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # logo가 오른쪽 끝에 닿았는지 확인 (DVD 글자가 3글자라 WIDTH - 3):
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # logo가 상단 끝에 닿았는지 확인:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # logo가 하단 끝에 닿았는지 확인:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # 방향이 바뀌었으면, 색상을 바꾼다.
                logo[COLOR] = random.choice(COLORS)

            # 로고를 이동시키기
            # 터미널의 문자가 두 배 크기 때문에 X 좌표를 2씩 이동한다.
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # 코너에 닿은 횟수를 표시:
        bext.goto(5, 0)
        bext.fg("white")
        print("Corner bounces:", cornerBounces, end="")

        for logo in logos:
            # 새로운 위치에 로고를 그린다:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end="")

        bext.goto(0, 0)

        sys.stdout.flush()  # bext를 사용하는 프로그램에 필요함.
        time.sleep(PAUSE_AMOUNT)


# 프로그램이 임포트된게 아니라 실행한 것이라면 프로그램이 실행된다.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("로고 뛴다!")
        sys.exit()
