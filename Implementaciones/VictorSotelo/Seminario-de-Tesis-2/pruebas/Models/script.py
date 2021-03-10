import sys
import json
from pprint import pprint
namefile=sys.argv[1]
iter=int(sys.argv[2])-1
with open(namefile) as f:
    data = json.load(f)
print('precision test-training')
print(str(data["val_acc"][iter])+'  '+str(data["acc"][iter]))
print('error test-training')
print(str(data["val_loss"][iter])+'  '+str(data["loss"][iter]))
