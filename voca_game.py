# 25.12.10
# 영어의 뜻을 맞추는 영단어 프로그램
# 1. json 파일의 모든 단어들이 랜덤으로 출제됨
# 2. 단어의 뜻은 여러 개일 수 있음
# 3. 문제를 맞춰야 다음 문제로 넘어갈 수 있음
# 4. 도중에 종료는 "quit"

import json
import random

with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

print("*단어를 보고 뜻을 맞춰보세요!*\n")
random.shuffle(words)

for quiz in words:
    word = quiz["word"]
    meaning = quiz["meaning"]

    while True:
        print("단어 : ", word)
        answer = input("뜻 : ").strip()
        print("-------------------")

        # 프로그램 종료
        if answer == "quit":
            print("프로그램 종료!")
            exit()

        # 답 맞추기
        user_ans = [a.strip() for a in answer.split(",")]

        if set(user_ans) == set(meaning):
            print("정답!")
            print(" : ", ", ".join(meaning))
            print("-------------------\n")
            break
        else:
            print("다시 입력하세요\n")

print("모든 문제를 다 풀었습니다!")