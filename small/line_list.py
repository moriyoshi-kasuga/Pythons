print("数字を空白で分けて入力してください(一行ずつlistにしてそれらを入れたlistを出力します)")

list_all: list[list[int]] = []
while True:
    string = input("入力してください(cで終了します): ")
    if string == "c":
        break
    list_all.append(list(map(int, string.split())))
print(list_all)
