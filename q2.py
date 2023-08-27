password = 'a123456'
count = 3
while count > 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('恭喜登入成功 !')
        break
    else:
        count = count - 1
        if count > 0:
            print('登入失敗 還有', count, '次機會')
        else:
            print('登入失敗!')        

