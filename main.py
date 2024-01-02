import sys, os
# Rest of the imports
#
#

def check_venv():
    if os.getenv("VIRTUAL_ENV"):
        print("Running inside a virtual environment.")
    else:
        print("Not running inside a virtual environment.")
        sys.exit()        

# Rest of definitions
#
#

if __name__ == '__main__':
    check_venv()

    # Rest of the code
    #
    #
        