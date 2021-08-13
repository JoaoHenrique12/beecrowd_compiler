import os
import sys
from tools.Manager import Manager


if __name__ == "__main__":
    print(sys.path)
    action = sys.argv[1:]

    alfred = Manager()
    alfred.identify(action)
