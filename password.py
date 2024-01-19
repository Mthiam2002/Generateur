import random

mini="abcdefghijklmnopqrstuvwxyz"
maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombres="0123456789"
symboles="$-_*"

all= mini + maj + nombres + symboles
length = 16
mdp="" .join(random.sample(all,length))

print(mdp)