import json
with open("players.json", 'r') as file:
    data=json.load(file)
p1=data['player']
d={}
for wkr in p1:
    for k,v in wkr.items():
        if k=="role" and v=="Wicket-keeper":
            print("There is one wicket-keeper in a BTeam:", k,v)




