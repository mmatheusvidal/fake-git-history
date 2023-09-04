import json
from datetime import datetime

print(datetime.strftime(datetime.now(), "%H:%M:%S"))
print(datetime.strftime(datetime.now(), "%d/%m/%Y"))
with open('tasks.json') as f:
    data = json.load(f)
    print(data['tasks'][-1])
#write
#with open('tasks.json', 'w') as f:
 #   json.dump(data, f)