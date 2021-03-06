import os, re, sys, urllib2, platform, subprocess, threading
# can also use sys.platform()

try:
    regex = r'(?<=shoutcast_stream":").[^"]*'
    site = 'http://www.iheart.com/live/1013-kdwb-1201/'
    data = urllib2.urlopen(site).read()
    radioLink = re.search(regex, data).group()

except Exception, linkError:
    sys.exit(linkError)

osp = platform.system()
if (osp == 'Linux'):
    sys.exit(radioLink)

elif (osp == 'Windows'):

    try:
        os.chdir('C:\Program Files (x86)\VideoLAN\VLC')
        
    except Exception, noVlc:
        sys.exit(radioLink)

    try:
        # complicated bad code, i could not find any other way
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
else:
    sys.exit('OS is not Linux or Windows, but here is the link:\n' + radioLink)

'''
windows media player can also be used (You will have to implement yourself)
location: "C:\Program Files (x86)\Windows Media Player"
launchCommand = 'wmplayer.exe "' + radioLink +'"'
'''
