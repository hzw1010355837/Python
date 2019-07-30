print('PyDev console: using IPython 7.6.1\n')

import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['I:\\score', 'I:\\score\\Python\\day01', 'I:\\score\\Python\\day02', 'I:/score'])
import os

os.getcwd()
os.chdir(os.path.join(os.getcwd(), "Python/day03/"))
os.getcwd()


def f():
    a = 2
    return lambda k: a ** k


g = f()
"""g.a 
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\site-packages\IPython\core\interactiveshell.py", line 3325, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-8-7888bff24f3d>", line 1, in <module>
    g.a
AttributeError: 'function' object has no attribute 'a'
"""

g.__closure__
c = g.__closure__[0]
c.cell_contents  # 2
# %hist -f ./matedata.py
