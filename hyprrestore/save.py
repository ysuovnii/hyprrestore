import subprocess
import json 
import os 

def saveSession():
    try : 
        if not os.path.exists("./sessions") :
            os.makedirs("./sessions")

        sessionFile = "./sessions/session.json"

        if os.path.exists(sessionFile) and os.path.getsize(sessionFile) > 0 :
            with open(sessionFile, "r") as f :
                try:
                    clients = json.load(f)
                except json.JSONDecodeError :
                    clients = []
        else :
            clients = []
        
        resHypr = subprocess.Popen(
            ["hyprctl", "clients", "-j"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )

        out, err = resHypr.communicate()


        try :
            nClients = json.loads(out)
        except json.JSONDecodeError :
            nClients = []
            
        clients = nClients 

        with open(sessionFile, "w") as f :
            json.dump(clients, f, indent=4) 

        print("session.json saved!")


    except Exception as e :
        print("Exception : ", e)
        exit(-1)

if __name__ == "__main__" :
    saveSession()


