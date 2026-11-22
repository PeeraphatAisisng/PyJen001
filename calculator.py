"""โปรแกรมบวกเลขอย่างง่าย - PyJen001 (Peeraphat Aisising 6752410001)

วิธีใช้:
    python calculator.py 5 7      -> 5 + 7 = 12
    python calculator.py          -> ใช้ค่าตัวอย่าง 10 + 20
"""
import sys


def add(a, b):
    """คืนค่าผลบวกของ a และ b"""
    return a + b


def parse_number(text):
    """แปลงข้อความเป็นตัวเลข (จำนวนเต็มถ้าทำได้ ไม่งั้นเป็นทศนิยม)"""
    value = float(text)
    return int(value) if value.is_integer() else value


def main(argv):
    if len(argv) == 2:
        a, b = parse_number(argv[0]), parse_number(argv[1])
    else:
        a, b = 10, 20
    result = add(a, b)
    print(f"{a} + {b} = {result}")
    return result


if __name__ == "__main__":
    main(sys.argv[1:])
