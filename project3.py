import sys

bitmap = """
..........................
*                        *
**                      **      
***                    ***
****                  ****
*****                *****
******              ******
*******            *******
******              ******
*****                *****
****                  ****
***                    ***
**                      **
*                        *                        
.........................."""

print("Enter the message to display in the bitmap:")
message = input("> ")
if message == "":
    sys.exit()

# 루프를 돌며 bitmap의 각 행을 반복한다.:
for line in bitmap.splitlines():
    # 루프를 돌며 각 행의 문자에 대해 반복한다:
    for i, bit in enumerate(line):
        if bit == " ":
            # bitmap의 해당 위치가 공백이므로 빈 공백을 출력한다:
            print(" ", end="")
        else:
            # message의 문자를 출력한다.
            print(message[i % len(message)], end="")
    print()  # 줄바꿈
