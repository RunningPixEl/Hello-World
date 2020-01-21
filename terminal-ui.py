# reference: https://github.com/gojuukaze/terminal_layout
# https://terminal-layout.readthedocs.io/en/latest/
import time
from terminal_layout import *

ctl = LayoutCtl(TextView('id1', 'hello world!', width=20, fore=Fore.red, back=Back.green))

ctl.draw()

time.sleep(2)

view = ctl.find_view_by_id('id1')
view.text = 'hi world'
ctl.re_draw()
# Success install in jetson nano, use python3 to run it
