# 113885764
from typing import List


def decoding_instructions(instruction: str) -> str:
    stack: List[tuple] = []
    current_digit: int = 0
    result: List[str] = []

    for i in instruction:
        if i.isdigit():
            current_digit: int = current_digit * 10 + int(i)
        elif i == '[':
            stack.append((current_digit, result))
            current_digit: int = 0
            result: List[str] = []
        elif i == ']':
            prev_num, prev_str = stack.pop()
            result: List[str] = prev_str + result * prev_num
        else:
            result.append(i)

    return ''.join(result)


if __name__ == '__main__':
    print(decoding_instructions(input()))
