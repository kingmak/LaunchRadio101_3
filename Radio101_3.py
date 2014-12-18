import os, re, urllib2, subprocess, threading

print 'You Need Windows 7'
print 'You Need VLC Media Player\n'
raw_input('if you have the above press enter else exit the program')

regex = r'(?<=shoutcast_stream":").[^"]*'
site = 'http://www.iheart.com/live/1013-kdwb-1201/'
data = urllib2.urlopen(site).read()
radioLink = re.search(regex, data).group()

os.chdir('C:\Program Files (x86)\VideoLAN\VLC')

# complicated bad code, i coud find no other way
def callVLC():
    subprocess.call(["vlc", "-vvv", radioLink])

VLCstart = threading.Thread(target = callVLC)
class MyThread(threading.Thread):
    def run(self):
        VLCstart.start()

thread = MyThread()
thread.daemon = True
thread.start()

#very bad
os.system('TASKKILL /F /IM python.exe')

'''
if you turn it into py2exe then u can do what i did:
os.system('TASKKILL /F /IM 101_3.exe')
'''
