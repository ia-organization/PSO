import random
import math

class Gbest:
    positions = list()
    value = 99999


class Pbest:
    positions =list()
    value = 99999


class Particle:
    positions = list()
    velocity = list()
    pBest = None

    def __init__(self):
        self.pBest = Pbest()
    
    def saveBestpBest(self, fp):
        if self.pBest.value == None:
            self.pBest.value = fp
            self.pBest.positions = self.positions[:]
        elif self.pBest.value > fp:
            self.pBest.value = fp
            self.pBest.positions = self.positions[:]
    
    def fitness(self):
        calc_dimensions = 0
        for d in self.positions:
            calc_dimensions += d ** 2
        
        return 0.5 + (math.sin(math.sqrt(calc_dimensions))**2 - 0.5)/(1+ 0.001*(calc_dimensions))**2



class Swarm:

    particles = list()
    lst_gbest = list()
    gBest = None
    dom_position = 0
    dom_velocity = 0
    c1 = c2 = 2.05

    def __init__(self, numb_particle, numb_dimensions, dom_position, dom_velocity):
        self.gBest = Gbest()
        self.dom_velocity = dom_velocity
        self.dom_position = dom_position

        for p in range(numb_particle):
            positions = []
            velocity = []
            particle = Particle()
            for d in range(numb_dimensions):
                positions.append(random.randint((dom_position * (-1)), dom_position))
                velocity.append(random.randint((dom_velocity * (-1)), dom_velocity))
            particle.positions = positions[:]
            particle.velocity = velocity[:]
            self.particles.append(particle)        
    
    def update_positions(self):
        for p in self.particles:
            for i in range(len(p.positions)):
                p.positions[i] = p.positions[i] + p.velocity[i]
            
                if p.positions[i] > self.dom_position:
                    p.positions[i] = self.dom_position
                    p.velocity[i] = 0
                
                if p.positions[i] < (self.dom_position * (-1)):
                    p.positions[i] = (self.dom_position * (-1))
                    p.velocity[i] = 0
                
    def update_velocity(self):
        for p in self.particles:
            r1 = random.random()
            r2 = random.random()

            for i in range(len(p.velocity)):
                social = self.c1*r1*(p.pBest.positions[i] - p.positions[i])
                cognitive = self.c2*r2*(self.gBest.positions[i] - p.positions[i])
                p.velocity[i] = p.velocity[i] + cognitive + social

                if p.velocity[i] > self.dom_velocity:
                    p.velocity[i] = self.dom_velocity
                
                if p.velocity[i] < (self.dom_velocity * (-1)):
                    p.velocity[i] = (self.dom_velocity * (-1))

    def optimize(self):
        self.lst_gbest = list()
        for p in self.particles:
            fp = p.fitness()
            p.saveBestpBest(fp)

            if p.pBest.value < self.gBest.value:
                self.gBest.value = p.pBest.value
                self.gBest.positions = p.pBest.positions[:]
            
            self.lst_gbest.append(self.gBest.value)


def PSO(numb_iterations, numb_particle, numb_dimensions, range_position, range_velocity):
    swarm = Swarm(numb_particle, numb_dimensions, range_position, range_velocity)
    dic_results = {}

    for k in range(numb_iterations):
        swarm.optimize()
        swarm.update_velocity()
        swarm.update_positions()
        dic_results[k] = swarm.lst_gbest[:]
    
    return dic_results

if __name__ == "__main__":
    print(PSO(100, 20, 3, 100, 15))