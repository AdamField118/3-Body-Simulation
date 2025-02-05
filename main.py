import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class Body:
    def __init__(self, r, radius, mass, v, color):
        self.r = r
        self.radius = radius
        self.mass = mass
        self.v = v
        self.color = color
        self.orbit = [(r[0],r[1],r[2])]

def update_position(body, dt):
    body.r[0] += body.v[0] * dt
    body.r[1] += body.v[1] * dt
    body.r[1] += body.v[2] * dt

def update_velocity(body, force, dt):
    a = [force[0] / body.mass, force[1] / body.mass, force[2] / body.mass]
    body.v[0] += a[0] * dt
    body.v[1] += a[1] * dt
    body.v[2] += a[2] * dt

def gravitational_force(body1, body2):
    G = 1.0
    R = [body2.r[0] - body1.r[0], body2.r[1] - body1.r[1], body2.r[2] - body1.r[2]]
    RdotR = R[0]**2 + R[1]**2 + R[2]**2
    normR = math.sqrt(RdotR)
    force = [((G * body1.mass * body2.mass * R[0]) / (RdotR * normR)), ((G * body1.mass * body2.mass * R[1]) / (RdotR * normR)),((G * body1.mass * body2.mass * R[2]) / (RdotR * normR))]
    return (force)

def simulate(bodies, dt):
    for body in bodies:
        net_force = [0, 0, 0]
        for other_body in bodies:
            if body != other_body:
                force = gravitational_force(body, other_body)
                net_force[0] += force[0]
                net_force[1] += force[1]
                net_force[2] += force[2]
        update_velocity(body, net_force, dt)
    for body in bodies:
        update_position(body, dt)
        body.orbit.append((body.r[0], body.r[1], body.r[2]))

def animate(frame, bodies, scatters, lines):
    dt = 0.1
    simulate(bodies, dt)

    for i, body in enumerate(bodies):
        updated_points = list(zip(*body.orbit))
        lines[i]._verts3d = updated_points
        scatters[i]._offsets3d = ([body.r[0]], [body.r[1]], [body.r[2]])

# Create instances of body with initial coordinates and velocities
v = 3
L = 1

#(r, radius, mass, v, color)
body_A = Body([1, 1, 2], 0.1, 100, [0, 0, 0], 'yellow')
body_B = Body([L * 2, 1, 3], 0.1 , 30, [-v / 2, v * math.sqrt(3) / 2, 0], 'blue')
body_C = Body([0, 0, -2], 0.1, 30, [v, -v * math.sqrt(3) / 2, 0], 'darkgrey')

# Create a list of bodies
bodies = [body_A, body_B, body_C]

# Configure the animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatters = [ax.scatter([], [], [], color=body.color, s=100) for body in bodies]
lines = [ax.plot([], [], [], color=body.color, linewidth=0.5)[0] for body in bodies]

ani = FuncAnimation(fig, animate, fargs=(bodies, scatters, lines), frames=range(100), interval=50)

# Adjust limits of axis
min_limit = -L*10
max_limit = L*10
ax.set_xlim(min_limit, max_limit)
ax.set_ylim(min_limit, max_limit)
ax.set_zlim(min_limit, max_limit)

# Interactive axis
ax.view_init(elev=20, azim=30)

# Show the animation
plt.show()