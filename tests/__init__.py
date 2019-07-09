def pyRun():
    import os
    os.system("start /wait cmd /c py.test test_Suite.py")


if __name__ == '__main__':
    pyRun()
