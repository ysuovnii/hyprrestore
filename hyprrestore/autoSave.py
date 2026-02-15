import save
import sys

try :
    save.save_session()

except Exception as e :
    print("Exception : ", e)
    sys.exit(-1)
