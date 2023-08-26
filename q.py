password = 'a123456'
count = 3

while True:
    PWD = input('請輸入密碼: ')
    if PWD == password:
        print('恭喜 登入成功 !')
        break
    else:
        count = count - 1
        if count > 0:
            print('輸入錯誤, 您剩下', count, '次登入機會')
        else:
            break
