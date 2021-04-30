import yaml

with open("../switches.yaml", "r") as f:
    data = yaml.safe_load(f)

interface = ["ssh " + 
    data["SW1"]["user"]["name"] + ":" + 
    data["SW1"]["user"]["password"] + "@" +
    data["SW1"]["mgmt_ip"] + " -p " +
    str(data["SW1"]["port"]),
    "ssh " + 
    data["SW2"]["user"]["name"] + ":" + 
    data["SW2"]["user"]["password"] + "@" +
    data["SW2"]["mgmt_ip"] + " -p " +
    str(data["SW2"]["port"])
    ]
print(interface)