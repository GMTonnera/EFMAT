import math
import numpy as np

class Particle:
    def __init__(self, position, velocity, acceleration, mass, color, radius, num) -> None:
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.radius = radius
        self.energy = (self.mass * np.linalg.norm(self.velocity)**2) / 2
        self.color = color
        self.num = num
    
    
    def update_energy(self):
        self.energy = (self.mass * np.linalg.norm(self.velocity) **2) / 2


    def distance(self, part2):
        """Return the distance between the particle and other particle."""
        return math.sqrt((self.position[0]-part2.position[0])**2 + (self.position[1]-part2.position[1])**2)

    
    def update_position(self, dt, width, height):
        "Update particle position and handdle wall collisions."
        self.position = self.position + self.velocity * dt
        if (self.position[0] - self.radius < 0):
            self.position[0] = self.radius
            self.velocity[0] = -0.99*self.velocity[0]
            
        if (self.position[0] + self.radius > width):
            self.position[0] = width - self.radius
            self.velocity[0] = -0.99*self.velocity[0]

        if (self.position[1] - self.radius < 0):
            self.position[1] = self.radius
            self.velocity[1] = -0.99*self.velocity[1]
        
        if (self.position[1] + self.radius > height):
            self.position[1] = height-self.radius
            self.velocity[1] = -0.99*self.velocity[1]



    def update_velocity(self, dt):
        """Update particle velocity ."""
        self.velocity = self.velocity + self.acceleration * dt

    
    def __str__(self):
        return f"    ***Partícula {self.num}***    \nRaio: {self.radius}\nMassa: {self.mass}\nCor: {self.color}\nX: {self.position[0]}    Y: {self.position[1]}\nVelocidade: {self.velocity}\nAceleração: {self.acceleration}"