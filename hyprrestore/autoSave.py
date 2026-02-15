import save
import sys

try :
    save.saveSession()

except Exception as e :
    print("Exception : ", e)
    sys.exit(-1)
