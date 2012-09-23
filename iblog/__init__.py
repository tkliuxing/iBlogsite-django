import sys
#sys.path.append('./lib')
VERSION = ('0', '1')
BUILD = "1"


def get_package_version():
    return ".".join(VERSION) + "-build-" + BUILD


def is_release():
    return True
