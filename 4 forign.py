import json
with open("players.json", 'r') as file:
    data=json.load(file)
p1=data['player']
print(p1)
for cou in p1:
    for k,v in cou.items():
        if k=="country" and v!="India":
            p=[k,v]
            print("foreign players in team BTeam: ", p)