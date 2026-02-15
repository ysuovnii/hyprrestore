import json 
import subprocess

def restoreSession() :
    try : 
        with open("./sessions/session.json", "r") as f :
            clients = json.load(f)

            for client in range(len(clients)) :
                app = clients[client]["class"]

                openApp = subprocess.Popen(
                    [app],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            print("Session Restored!")
                
    except Exception as e : 
        print("Exception : ", e)
        exit(-1)

if __name__ == "__main__" :
    restoreSession()