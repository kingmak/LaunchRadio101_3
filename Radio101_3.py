import os, re, urllib2, subprocess, threading

print 'You Need Windows 7'
print 'You Need VLC Media Player\n'
raw_input('if you have the above press enter else exit the program')

regex = r'(?<=shoutcast_stream":").[^"]*'
site = 'http://www.iheart.com/live/1013-kdwb-1201/'
data = urllib2.urlopen(site).read()
radioLink = re.search(regex, data).group()

try:
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
except Exception, e:
    print str(e)
    raw_input('')

'''
if you turn it into an exe via py2exe then use:
os.system('TASKKILL /F /IM NAME_OF_UR_EXE.exe')

windows media player can also be used, but for now code only for VLC, you can change if you want

location: "C:\Program Files (x86)\Windows Media Player"
exeName = wmplayer.exe
launchCommand = 'wmplayer.exe "' + radioLink +'"'
'''
