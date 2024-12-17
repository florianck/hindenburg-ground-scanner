import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rosrunner/projects/hindenburg-ground-scanner/src/install/groundscanner'
