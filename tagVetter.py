#! python3
# tagVetter.py simple python script to search js files for potentially malicious functionality
import sys, os
#from colorama import init, Fore, Back, Style ##This module isn't installed in the correct directory, find and correct to display flags in Red when searched
#init()

malwareFlags = [
    'iframe'
    , 'script'
    , 'document.write'
    , '&lt;'
    , '&gt;'
    , 'XMLHttpRequest'
    , 'ActiveXObject'
    , 'onkeypress'
    , 'event.keyPress'
    , 'keyCode'
    , 'keyChar'
    , 'fromCharCode'
    , '.location'
    , 'eval('
    , 'execute'
    , 'input'
    , 'password'
    , 'user'
    , '[type='
]

if len(sys.argv) < 2:
    print('Usage: python tagVetter.py [file.js] - search javascript file for potentially malicious functionality')
    sys.exit()

jsFile = sys.argv[1]

with open(os.path.dirname(os.path.realpath(sys.argv[0])) + '\\' + jsFile, encoding="utf8") as inF:
    lineNum = 1
    for line in inF:
        for flag in malwareFlags:
            if flag.lower() in line.lower():
                #line.replace(flag, Fore.RED + flag + Style.RESET_ALL)
                print(str(flag) + ' found on line: ' +  str(lineNum) + '\nCONTEXT: ' + str(line).lstrip())
        lineNum = lineNum + 1