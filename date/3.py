import os
[print(_dir) for _dir in os.listdir('/') if os.path.isdir(_dir)]