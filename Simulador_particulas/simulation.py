import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter


from particle import Particle


class Simulation:
    def __init__(self, width, height, num_particles, particles_radius, dt, seed):
        self.width = width
        self.height = height
        self.particles = []
        self.num_particles = num_particles
        self.particles_radius = particles_radius
        self.dt = dt
        self.particles_types = {
            1:  ('#C0392B', random.random()), 
            2:  ('#8E44AD', random.random()),
            3:  ('#2980B9', random.random()),
            4:  ('#3498DB', random.random()),
            5:  ('#1ABC9C', random.random()),
            6:  ('#27AE60', random.random()),
            7:  ('#F1C40F', random.random()),
            8:  ('#D35400', random.random()),
            9:  ('#17202A', random.random()),
            10: ('#566573', random.random())
        }
        self.total_energy = []
        self.seed = seed
        self.create_particles()
    
    
    def create_particles(self):
        """Create the particles."""
        random.seed(self.seed)
        for i in range(self.num_particles):
            particle_type = random.randint(1,10)
            while True:
                position = np.array([random.randint(1, self.width - 1), random.randint(1, self.height - 1)], dtype=np.float64)
                new_particle = False
                for particle in self.particles:
                    if np.array_equal(position, particle.position):
                        new_particle = True
                
                if not new_particle:
                    velocity = np.array([random.uniform(-2,2), random.uniform(-2,2)], dtype=np.float64) 
                    acceleration = np.array([0, 0])
                    self.particles.append(Particle(position, velocity, acceleration, self.particles_types[particle_type][1], self.particles_types[particle_type][0], self.particles_radius, i+1))
                    break
    
    
    def calculate_total_energy(self):
        energy = 0
        for particle in self.particles:
            particle.update_energy()
            energy += particle.energy

        self.total_energy.append(energy)
        
    
    # def update_particles(self):
    #     """Updates the particles velocity and check for collsions."""
    #     if self.force == "attractive":
    #         self.attractive_forces_between_particles()

    #     if self.force == "repulsive":
    #         self.repulsive_forces_between_particles()
        
    #     for i in range(self.num_particles):
    #         if self.force == "restorative":
    #             self.restorative_force(self.particles[i])

    #         if self.force == "attractive":
    #             self.attractive_force(self.particles[i], i)

    #         if self.force == "repulsive":
    #             self.repulsive_force(self.particles[i], i)
            
    #         self.particles[i].update_velocity(self.dt)
    #         self.particles[i].update_position(self.dt, self.width, self.height)
        
    #         for j in range(i+1, self.num_particles):
    #             if np.linalg.norm(self.particles[i].position - self.particles[j].position) <= self.particles[i].radius + self.particles[j].radius:
    #                 self.handle_particles_collisions(self.particles[i], self.particles[j])
    #                 diff_vec = self.particles[i].position - self.particles[j].position
    #                 # 'clip' is how much the balls are clipped
    #                 clip = self.particles[i].radius + self.particles[j].radius - np.linalg.norm(self.particles[i].position - self.particles[j].position)
    #                 # Creating normal vector between balls
    #                 diff_norm = diff_vec / np.linalg.norm(self.particles[i].position - self.particles[j].position)
    #                 # Creating 'clip_vec' vector that moves ball out of other
    #                 clip_vec = diff_norm * clip
    #                 # Set new position
    #                 self.particles[i].position = self.particles[i].position + clip_vec
    
    
    def handle_particles_collisions(self, p1, p2):
        """Checks if two particles collided with each other. If so, updates both particles velocities."""
        p1.update_position(-self.dt, self.width, self.height)
        p2.update_position(-self.dt, self.width, self.height)
        # Atualizar as velocidades das partículas de acordo com as fórmulas de colisões elásticas 2D
        M = p1.mass + p2.mass
        r1, r2 = p1.position, p2.position
        d = np.linalg.norm(r1 - r2)**2
        v1, v2 = p1.velocity, p2.velocity
        u1 = v1 - 2*p2.mass / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        u2 = v2 - 2*p1.mass / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
        p1.velocity = u1
        p2.velocity = u2
                    
                    
                    # p1.velocity = p1.velocity - (2*p2.mass / (p1.mass + p2.mass)) * (np.dot(p1.velocity - p2.velocity, p1.position - p2.position) / np.linalg.norm(p1.position - p2.position)**2) * (p1.position - p2.position) 
                    # p2.velocity = p2.velocity - (2*p1.mass / (p1.mass + p2.mass)) * (np.dot(p2.velocity - p1.velocity, p2.position - p1.position) / np.linalg.norm(p2.position - p1.position)**2) * (p2.position - p1.position) 

            
    def apply_force(self, particle):
        """Each child class must rewrite this method according to the simulation force type."""
        raise NotImplementedError




    def restorative_force(self, particle):
        """Updates particle acceleration based on the type of simulation."""
        particle.acceleration = - 0.1 * (particle.position - np.array([10, 10])) / particle.mass



    # def attractive_force(self, particle, num):
    #     acceleration = np.array([0,0])
    #     for i in range(self.num_particles):
    #         for j in range(num, self.num_particles):
    #             if i == num:
    #                 acceleration = acceleration + self.forces[i,j]
    #             elif i < num and j == num:
    #                 acceleration = acceleration - self.forces[i,j]

    #     particle.acceleration = acceleration / particle.mass


    # def attractive_forces_between_particles(self):
    #     forces = []
    #     for i in range(self.num_particles):
    #         row = [np.array([0, 0]) for _ in range(i+1)]
    #         for j in range(i+1, self.num_particles):
    #             vet_uni = (self.particles[i].position - self.particles[j].position) / self.particles[i].distance(self.particles[j])
                
    #             row.append(-2 / (self.particles[i].distance(self.particles[j])**2) * vet_uni)
    #         forces.append(row)

    #     self.forces = np.asarray(forces)


    # def repulsive_force(self, particle, num):
    #     acceleration = np.array([0,0])
    #     for i in range(self.num_particles):
    #         for j in range(num, self.num_particles):
    #             if i == num:
    #                 acceleration = acceleration + self.forces[i,j]
    #             elif i < num and j == num:
    #                 acceleration = acceleration - self.forces[i,j]

    #     particle.acceleration = acceleration / particle.mass


    # def repulsive_forces_between_particles(self):
    #     forces = []
    #     for i in range(self.num_particles):
    #         row = [np.array([0, 0]) for _ in range(i+1)]
    #         for j in range(i+1, self.num_particles):
    #             vet_uni = (self.particles[i].position - self.particles[j].position) / self.particles[i].distance(self.particles[j])
                
    #             row.append(5 / (self.particles[i].distance(self.particles[j])**2) * vet_uni)
    #         forces.append(row)

    #     self.forces = np.asarray(forces)


    def animate(self, _):
        self.ax.clear()
        self.ax.set(xlim=(0,self.width), ylim=(0,self.height))
        self.update_particles()
        self.calculate_total_energy()
        for particle in self.particles:
            plt.scatter(particle.position[0], particle.position[1], color=particle.color)



    def make_animation(self, path=None, save=False):
        fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', 'box')
        anim = FuncAnimation(fig, self.animate, frames=2200, interval=2)

        if save:
            matplotlib.rcParams['animation.ffmpeg_path'] = r'C:\Users\guton\Documents\ffmpeg\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe'
            writervideo = FFMpegWriter(fps=60) 
            anim.save(path, writer=writervideo)

        else:
            plt.show()
            plt.close()


    def make_energy_graphic(self, color, linewidth, save=False, directory=None, ls='-'):
        plt.clf()
        plt.plot([i*self.dt for i in range(len(self.total_energy))], self.total_energy, color=color, ls=ls, linewidth=linewidth)
        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Energia")
        plt.title("Energia ao longo do tempo")
        if save:
            plt.savefig(directory)
        else:
            plt.show()
        plt.clf()