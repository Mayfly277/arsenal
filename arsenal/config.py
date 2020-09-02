import os 
from os.path import dirname, abspath, expanduser

basepath = dirname(dirname(abspath(__file__)))
cheats_paths = [basepath + '/cheats/', expanduser("~")+'/.mycheats/']

messages_error_missing_arguments = 'Error missing arguments'

# set lower delay to use ESC key (in ms)
os.environ.setdefault('ESCDELAY', '25')

savevarfile = expanduser("~")+"/.arsenal.json"
