import subprocess
import urllib.request as urlreq

# chromedriver_location = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
#
# geckodriver_location = 'https://github.com/mozilla/geckodriver/releases/latest'
# https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
# https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz

driverdict = {
           'chromedriver':'https://chromedriver.storage.googleapis.com/LATEST_RELEASE',
           'geckodriver':'https://github.com/mozilla/geckodriver/releases/latest',
}

drivers = list(driverdict.keys())

def getCurrentVer(drv):
    return subprocess.getoutput(f"{drv} --version").split()[:2]

def drvLookUp(drv):
    return urlreq.urlopen(driverdict[drv])

def checkVer(drivers):
    # cl = getLatestVer(drivers[0])
    # gl = getLatestVer(drivers[1])

    # clatest = cl.readline().decode("utf-8")
    # glatest = gl.geturl()
    #
    #
    # print(type(clatest), clatest)
    # print(type(glatest), glatest)
    match_msg = ' <-- You are up to date.'
    c_cur = getCurrentVer('chromedriver')[1]
    cc = c_cur[:c_cur.rfind('.')]

    cl = getLatestVer('chromedriver').readline().decode('utf-8')
    c_lat = cl
    c_match = ''
    if cc == c_lat:
        c_match = match_msg

    gc = getCurrentVer('geckodriver')[1]
    gl = getLatestVer('geckodriver').geturl()
    g_lat = gl[gl.rindex('/v')+2:]

    g_match = ''
    if gc == g_lat:
        g_match = match_msg

    print(f"{'Driver'.ljust(20, ' ')} {'Installed'.rjust(10,' ')} {'Latest'.rjust(8,' ')}")
    print(f"{'chromedriver'.ljust(20,' ')} {cc.rjust(10,' ')} {c_lat.rjust(8,' ')} {c_match}")
    print(f"{'geckodriver'.ljust(20,' ')} {gc.rjust(10,' ')} {g_lat.rjust(8,' ')} {g_match}")

def getLatestVer(drv):
    info = drvLookUp(drv)
    if drv == 'chromedriver':
        return info.readline().decode('utf-8')
    elif drv == 'geckodriver':
        url = info.geturl()
        return url[url.rindex('/v')+2:]
    else:
        print("Invalid driver value")
        return -1

def checkVers(drivers):
    print(f"{'Driver'.ljust(20, ' ')} {'Installed'.rjust(10,' ')} {'Latest'.rjust(8,' ')}")
    for d in drivers:
        inst_ver = getCurrentVer(d)[1]
        if d == 'chromedriver':
            inst_ver = inst_ver[:inst_ver.rfind('.')]

        latest_ver = getLatestVer(d)

        match = ''
        if inst_ver == latest_ver:
            match = ' <-- You are up to date.'

        print(f"{d.ljust(20,' ')} {inst_ver.rjust(10,' ')} {latest_ver.rjust(8,' ')} {match}")


checkVers(drivers)
# for d in drivers.keys():
#     cv = getCurrentVer(d)
#     lv = getLatestVer(d)
#     print(cv, lv)



