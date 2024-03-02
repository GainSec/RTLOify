import os
import string
import argparse
import shutil
import pathlib

parser = argparse.ArgumentParser()

parser.add_argument('--f', nargs='?', const='', help='Filename Mode')
parser.add_argument('--s', nargs='?', const='', help='String Mode')
parser.add_argument('--d', nargs='?', const='', help='Entire Directory Mode')
parser.add_argument('--sd', nargs='?', const='', help='Source Directory')
parser.add_argument('--dd', nargs='?', const='', help='Desination Directory')

args = parser.parse_args()

f = args.f
s = args.s
d = args.d
sd = args.sd
dd = args.dd

def AddRTLOCharToFilename(basefilename):
    name, ext = os.path.splitext(basefilename)
    global modifiedfilename
    modifiedfilename = "{name}\u202e{ext}".format(name=name, ext=ext)

def RunAddRTLOCharToFilename():
    RTLOFilename()
    AddRTLOCharToFilename(basefilename)
    os.rename(basefilename, modifiedfilename)
    print('Original Filename was: '+ basefilename)
    print('Filename with RTLO Character before the extension is: ' + modifiedfilename)

def RTLOFilename():
    global basefilename
    filecheck = os.path.exists(f)
    print('Filecheck is: ', filecheck)
    if filecheck is True:
        basefilename = f
    else:
        print('File does not exist, creating it now. ')
        if f is '':
            basefilename = input('Enter Filename: ')
            with open(basefilename, 'w+') as samplefile:
                samplefile.write('GainSec is Cool')
        else:
            basefilename = f
            with open(basefilename, 'w+') as samplefile:
                samplefile.write('GainSec is Cool')

def AddRTLOCharToString(basestring):
    name, ext = os.path.splitext(basestring)
    global modifiedstring
    modifiedstring = "{name}\u202e{ext}".format(name=name, ext=ext)

def RunAddRTLOCharToString():
    RTLOString()
    AddRTLOCharToString(basestring)
    print('Original String was: '+ basestring)
    print('String with RTLO Character before the extension is: ' + modifiedstring)

def RTLOString():
    global basestring
    if s is not '':
        basestring = s
    else:
        basestring = input('Enter String: ')

def RTLODirectoryCopyFilesToDst():
    global DesinationDirectory
    if sd is None:
        SourceDirectory = input('Enter Source Directory: ')
        print('Source Directory is: ', SourceDirectory)
    else:
        SourceDirectory = sd
        print('Source Directory is: ', SourceDirectory)
    if dd is None:
            DesinationDirectory = input('Enter Desination Directory: ')
            print('Desination Directory is: ', DesinationDirectory)
    else:
        DesinationDirectory = dd
        print('Desination Directory is: ', DesinationDirectory)
    os.makedirs(DesinationDirectory,exist_ok=True)
    for file_name in os.listdir(SourceDirectory):
        print(file_name)
        newfilename=DesinationDirectory+file_name
        shutil.copy2(SourceDirectory+file_name, DesinationDirectory+file_name)
    
def RTLODirectoryRename():
    for filename in os.listdir(DesinationDirectory):
        name, ext = os.path.splitext(filename)
        directorymodifiedfilename = "{name}\u202e{ext}".format(name=name, ext=ext)
        print(directorymodifiedfilename)
        print(DesinationDirectory+filename)
        os.rename(DesinationDirectory+filename, DesinationDirectory+directorymodifiedfilename)

def RunRTLODirectory():
    RTLODirectoryCopyFilesToDst()
    RTLODirectoryRename()

def Banner():
    print(' _____ _______ _      ____  _  __       ')
    print('|  __ \\__   __| |    / __ \\(_)/ _|      ')
    print('| |__) | | |  | |   | |  | |_| |_ _   _ ')
    print('|  _  /  | |  | |   | |  | | |  _| | | |')
    print('| | \\ \\  | |  | |___| |__| | | | | |_| |')
    print('|_|  \\_\\ |_|  |______\\____/|_|_|  \\__, |')
    print('                                   __/ |')
    print('                                  |___/ ')
    print("---------------------------------")
    print("By Jon Gaines (@GainSec)")
    print("Managing Consultant @NetSPI")
    print("---------------------------------")
    print("---------------------------------")
    print("Example For Strings:")
    print(" ")
    print("./RTLO-Maker.py --s (Interactive Mode) OR ./RTLO-Maker.py --s test.txt")
    print("---------------------------------")
    print("---------------------------------")
    print("Example For Single Files:")
    print(" ")
    print("./RTLO-Maker.py --f (Interactive Mode) OR ./RTLO-Maker.py --f ~/Payloads/test.txt")
    print("---------------------------------")
    print("---------------------------------")
    print("Example For Directories:")
    print(" ")
    print("./RTLO-Maker.py --d (Interactive Mode) OR ./RTLO-Maker.py --d --sd ~/Source/Directory --dd ~/Destination/Directory")
    print("---------------------------------")
    print("---------------------------------")

def ModeCheck(mode):
    if f is not None:
        print(f)
        mode = 'FilenameMode'
        print('Filename mode')
        return mode
    elif s is not None:
        mode = 'StringMode'
        print('String Mode')
        return mode
    elif d is not None:
        mode = 'DirectoryMode'
        print('Directory Mode')
        return mode

def Main():
    Banner()
    RunMode = ModeCheck(())
    if RunMode == 'FilenameMode':
        RunAddRTLOCharToFilename()
    elif RunMode == 'StringMode':
        RunAddRTLOCharToString()
    elif RunMode == 'DirectoryMode':
        RunRTLODirectory()
    else:
        print('You either entered too many args or forgot a required arg')


Main()