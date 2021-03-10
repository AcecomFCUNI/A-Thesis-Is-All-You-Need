import sys
import json
from pprint import pprint
namefile=sys.argv[1]
iter=sys.argv[2]
with open('data.json') as f:
    data = json.load(f)
print('precision test-training')
print(str(data["val_acc"][iter])+'  '+str(data["acc"][iter]))
print('error test-training')
print(str(data["val_loss"][iter])+'  '+str(data["loss"][iter]))
