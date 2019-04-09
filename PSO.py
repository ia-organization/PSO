import random

class Particle:
    def __init__(self, v1, v2, x1, x2, pBest = None):
        self.v1  = v1
        self.v2 = v2
        self.x1 = x1
        self.x2 = x2
        self.pBest = pBest
    
    def f6_Schaffer(self):
        


QTD_PARTICLE = 20
DOM = [-100, 100]
RANGE_VEL = [-15,15]

INITIAL_V1 = random.randint(-15,15)
INITIAL_V2 = random.randint(-15,15)

particle_list = []

for i in range (QTD_PARTICLE):
    x1 = random.randint(-100,100)
    x2 = random.randint(-100,100)
    particle_list.append(Particle(INITIAL_V1, INITIAL_V2, x1, x2)
