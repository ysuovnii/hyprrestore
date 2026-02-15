import subprocess
import json 

try : 
    resHypr = subprocess.Popen(
        ["hyprctl", " clients", "-j"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True
    )

    out, err = resHypr.communicate()

    if resHypr.returncode != 0 :
        print("Error : ", err)
        exit(1)

    clients = json.loads(out)

    with open("./sessions/session.json", "w") as f :
        json.dump(clients, f) 

    print("session.json saved!")


except Exception as e :
    print("Exception : ", e)
    exit(-1)


