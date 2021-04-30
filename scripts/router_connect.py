import json

with open("../routers.json", "r") as f:
    data = json.load(f)

interface = ["ssh " + 
    data["R1"]["user"]["name"] + ":" + 
    data["R1"]["user"]["password"] + "@" +
    data["R1"]["mgmt_ip"] + " -p " +
    str(data["R1"]["port"]),
    "ssh " + 
    data["R2"]["user"]["name"] + ":" + 
    data["R2"]["user"]["password"] + "@" +
    data["R2"]["mgmt_ip"] + " -p " +
    str(data["R2"]["port"])
    ]
print(interface)