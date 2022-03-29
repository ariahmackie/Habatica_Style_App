from Email import Email
receiver_address = 'test.user.email.for.ariah@gmail.com'

newemail = Email(receiver_address ,"test email", "hello. this is a test" )
newemail.send()

try:
    statement
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except Expection as e:
    print(e.__class__.__name__)
else:
    print("neither value error or type error")
finally:
    print("cleanup code that is always called")
