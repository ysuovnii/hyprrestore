import subprocess
import json 

cmd = r'''
ps -eo pid=,ppid=,user=,%cpu=,%mem=,command= | awk '
BEGIN { print "[" }
{
  printf "%s{\"pid\":%s,\"ppid\":%s,\"user\":\"%s\",\"cpu\":%s,\"mem\":%s,\"command\":\"",
         sep,$1,$2,$3,$4,$5
  for(i=6;i<=NF;i++) printf "%s%s", (i==6?"":" "), $i
  printf "\"}"
  sep=",\n"
}
END { print "\n]" }
'
'''

r1 = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE,   
    stderr=subprocess.PIPE,
    text=True
)

out, err = r1.communicate()

data = json.loads(out)

with open("s.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saved!!")
