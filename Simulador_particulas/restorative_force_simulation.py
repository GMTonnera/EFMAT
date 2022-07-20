import numpy as np


from simulation import Simulation


class Restorative_Force_Simulation(Simulation):
    def __init__(self, width, height, num_particles, particles_radius, dt, seed):
        super().__init__(width, height, num_particles, particles_radius, dt, seed)


    def update_particles(self):
        for i in range(self.num_particles):
            self.apply_force(self.particles[i], i)
            self.particles[i].update_velocity(self.dt)
            self.particles[i].update_position(self.dt, self.width, self.height)
        
            for j in range(i+1, self.num_particles):
                if np.linalg.norm(self.particles[i].position - self.particles[j].position) <= self.particles[i].radius + self.particles[j].radius:
                    self.handle_particles_collisions(self.particles[i], self.particles[j])
                    diff_vec = self.particles[i].position - self.particles[j].position
                    # 'clip' is how much the balls are clipped
                    clip = self.particles[i].radius + self.particles[j].radius - np.linalg.norm(self.particles[i].position - self.particles[j].position)
                    # Creating normal vector between balls
                    diff_norm = diff_vec / np.linalg.norm(self.particles[i].position - self.particles[j].position)
                    # Creating 'clip_vec' vector that moves ball out of other
                    clip_vec = diff_norm * clip
                    # Set new position
                    self.particles[i].position = self.particles[i].position + clip_vec



    def apply_force(self, particle, num):
        particle.acceleration = - 0.1 * (particle.position - np.array([10, 10])) / particle.mass