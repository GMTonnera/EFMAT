from resistive_force_simulation import Resistive_Force_Simulation
from attractive_force_simulation import Attractive_Force_Simulation
from repulsive_force_simulation import Repulsive_Force_Simulation
from restorative_force_simulation import Restorative_Force_Simulation


WIDTH = 20
HEIGHT = 20
NUM_PARTICLES = 30
PARTICLES_RADIUS = 0.25
DELTA_TIME = 0.01
FORCE = "repulsive"
SEED = 10
LINE_WIDTH = 2
COLOR = "ForestGreen"
DIRECTORY = r"graphics\\"
LINE_STYLE = '-'


s1 = Resistive_Force_Simulation(WIDTH, HEIGHT, NUM_PARTICLES, PARTICLES_RADIUS, DELTA_TIME, SEED)
s2 = Attractive_Force_Simulation(WIDTH, HEIGHT, NUM_PARTICLES, PARTICLES_RADIUS, DELTA_TIME, SEED)
s3 = Repulsive_Force_Simulation(WIDTH, HEIGHT, NUM_PARTICLES, PARTICLES_RADIUS, DELTA_TIME, SEED)
s4 = Restorative_Force_Simulation(WIDTH, HEIGHT, NUM_PARTICLES, PARTICLES_RADIUS, DELTA_TIME, SEED)

s1.make_animation(path=r'animations\resistive.mp4', save=True)
s1.make_energy_graphic(COLOR, LINE_WIDTH, save=True, directory=DIRECTORY+"g_resistive.png", ls=LINE_STYLE)

s2.make_animation(path=r'animations\attractive.mp4', save=True)
s2.make_energy_graphic(COLOR, LINE_WIDTH, save=True, directory=DIRECTORY+"g_attractive.png", ls=LINE_STYLE)

s3.make_animation(path=r'animations\repulsive.mp4', save=True)
s3.make_energy_graphic(COLOR, LINE_WIDTH, save=True, directory=DIRECTORY+"g_repulsive.png", ls=LINE_STYLE)

s4.make_animation(path=r'animations\restorative.mp4', save=True)
s4.make_energy_graphic(COLOR, LINE_WIDTH, save=True, directory=DIRECTORY+"g_restorative.png", ls=LINE_STYLE)
