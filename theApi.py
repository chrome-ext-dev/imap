import time
import names
from imbox import Imbox

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def getEmail(email):
    count = 0
    done = False
    funcName = "Getting Confirmation Code"
    global code

    print('Started To Get Conf Code')

    while not done:
        try:
            #CODE START HERE
            with Imbox('imap-mail.outlook.com',
                    username=email['email'],
                    password=email['password'],
                    ssl=True,
                    ssl_context=None,
                    starttls=False) as imbox:
                        print('Connected To Imap...')
                        quora_mail = imbox.messages(sent_from='confirm@account.pinterest.com', unread=True)
                        for uid, message in quora_mail:
                            # print(message.body)
                            time.sleep(2)
                            code = message.body['plain'][0]
                            print(code)
                            final_code = find_between( code, 'following URL in your browser: ', 'Pinterest')
                            final_code = final_code.rstrip()
                            return final_code
            
            if (code != ''):
                done = True

        except:
            print('Atempt ' + str(count) + ' on ' + funcName + ' failed')
            count += 1
            time.sleep(5)
            if (count >= 3):
                return False
            continue
        return True

def randomUser(gender):
    full_name = names.get_full_name(gender=gender)
    full_name_arr = full_name.split()

    user = {
        'fullname' : full_name,
        'firstname' : full_name_arr[0],
        'lastname' : full_name_arr[1]
    }
    return user
