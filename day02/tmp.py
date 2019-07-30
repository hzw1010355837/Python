# IPython log file

print('PyDev console: using IPython 7.6.1\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['I:\\score', 'I:\\score\\Python\\day01', 'I:\\score\\Python\\day02', 'I:/score'])
f = open('demo.txt', 'w', buffering = 2048)
f.write("_"*2048)
f.write("9")
f1 = open('demo1.txt', 'w', buffering=1)
f1.write('asdadasdasd')
f1.write("/n")
f1.write("asdfsdfasdf/n")
f1.write("a")
f2 = open('demo2.txt', 'w', buffering=0)
f2 = open('demo2.txt', 'w', buffering=0)
# get_ipython().run_line_magic('logstart', './tmp.py')
# get_ipython().run_line_magic('logstop', './tmp.py')
