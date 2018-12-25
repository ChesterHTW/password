password = 'a123456'
x = 3
while True:
    userpassword = input('請輸入密碼：')
    if userpassword == password:
        print('成功登入！')
        break
    else:
        x = x - 1
        if x > 0:
        	print('密碼錯誤，還有', x,'次機會！')
        else:
            print('密碼錯誤次數過多，暫時無法輸入！')
            break