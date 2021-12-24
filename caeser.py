import caeser_list

def decode_caesar(b , shift_cnt):
    i = 0
    while i + 1 <= len(b):
        try:
            a = caeser_list.cieser.index(b[i]) + shift_cnt
        except:
            pass
        if a > 25:
            a = a - 25 - 1
        print(caeser_list.cieser[a])
        i += 1

def encode_caeser(b , shift_cnt):
    i = 0
    while i + 1 <= len(b):
        try:
            a = caeser_list.cieser.index(b[i]) - shift_cnt
        except:
            pass
        if a > 25:
            a = a + 25 + 1
        print(caeser_list.cieser[a])
        i += 1


print("文字を入力")
b = input()
print("ずらす数")
shift_cnt = input()
print("1:エンコード\n2:デコード")
select_caeser = input()

if int(select_caeser) == 1:
    encode_caeser(b, int(shift_cnt))

if int(select_caeser) == 2:
    decode_caesar(b, int(shift_cnt))


