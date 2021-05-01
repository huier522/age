driving = input('請問你有開車嗎？')
if driving != '有' and driving != '沒有':
    print('只能輸入有或沒有')
    raise SystemExit
age = int(input('請問你幾歲？'))

if driving == '有':
    if age >= 18:
        print('合格！要記得安全駕駛哦～')
    else:
        print('你知道你無照駕駛嗎？這樣犯法～')
elif driving == '沒有':
    if age >= 18:
        print('抽空去考駕照吧！')
    else:
        print('要記得考到駕照才能去開車哦～')