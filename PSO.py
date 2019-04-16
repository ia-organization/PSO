import random
import math

class Particle:
    def __init__(self, v1, v2, x1, x2, pBest = None):
        self.v1  = v1
        self.v2 = v2
        self.x1 = x1
        self.x2 = x2
        self.pBest = pBest
    
    def f6_Schaffer(self):
        return 0.5 + (math.sin(math.sqrt(self.x1**2 + self.x2**2))**2 - 0.5)/(1+ 0.001*(self.x1**2 + self.x2**2))**2


    def fPbest(self, fp):
        if self.pBest == None:
            self.pBest = fp
        elif self.pBest > fp:
            self.pBest = fp


#step 1
QTD_PARTICLE = 20
domMin = -100
domMax = 100
vMax = 15
vMin = -15


#step 3
INITIAL_V1 = random.randint(vMin,vMax)
INITIAL_V2 = random.randint(vMin,vMax)

particle_list = []
gbest = 100000

#constantes de inércia
c1, c2 = 2.05

#step 2
for i in range (QTD_PARTICLE):
    x1 = random.randint(domMin,domMax)
    x2 = random.randint(domMin,domMax)
    particle_list.append(Particle(INITIAL_V1, INITIAL_V2, x1, x2)

for k in range(int(input("Iteracoes: "))):
    #step 4
    for i in range(QTD_PARTICLE):
        fp = particle_list[i].f6_Schaffer()
        
        particle_list[i].fPbest(fp)

        #step 5
        if particle_list[i].pBest < gbest:
            gbest = particle_list[i].pbest

        
        x1 = particle_list[i].x1
        x2 = particle_list[i].x2
        v1 = particle_list[i].v1
        v2 = particle_list[i].v2

        r1 = random.randint(100)/100
        r2 = random.randint(100)/100

        #step 6
        particle_list[i].v1 = v1 + c1*r1*(particle_list[i].pBest - x1) + c2*r2*(gbest - x1)
        particle_list[i].v2 = v2 + c1*r1*(particle_list[i].pbest - x2) + c2*r2*(gbest - x2)

        # delimitação de velocidade entre -15 e 15
        if particle_list.v1 > vMax:
            particle_list.v1 = vMax
        if particle_list.v1 < vMin:
            particle_list.v1 = vMin

        if particle_list.v2 > vMax:
            particle_list.v2 = vMax
        if particle_list.v2 < vMin:
            particle_list.v2 = vMin

        particle_list[i].x1 = x1 + particle_list[i].v1
        particle_list[i].x2 = x2 + particle_list[i].v2


        # delimitação do domínio
        if particle_list[i].x1 > domMax:
            particle_list[i].x1 = domMax
            particle_list[i].v1 = 0

        if particle_list[i].x2 > domMax:
            particle_list[i].x2 = domMax
            particle_list[i].v2 = 0

        if particle_list[i].x1 < domMin:
            particle_list[i].x1 = domMin
            particle_list[i].v1 = 0

        if particle_list[i].x2 < domMin:
            particle_list[i].x2 = domMin
            particle_list[i].v2 = 0

        #fim delimitação do domínio
    #fim for iteracoes