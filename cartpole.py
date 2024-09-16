import math

class CartPole:
  def __init__(self, x, xdot, theta, thetadot, lenght, x_weight, weight, gravity=-9.81):
    self.x = x
    self.xdot = xdot
    self.theta = theta
    self.thetadot = thetadot
    self.lenght = lenght
    self.x_weight = x_weight
    self.weight = weight
    self.gravity = gravity

  def sim_step(self, force, dt=0.05, drag=1.02):
    # calculate accelerations
    x_acc = force / (self.x_weight + self.weight)
    theta_acc = (self.gravity * math.sin(self.theta) - 
                 self.lenght * self.thetadot**2 * math.sin(self.theta) * math.cos(self.theta) +
                 x_acc * math.cos(self.theta)) / (self.lenght * (4/3 - self.weight * math.cos(self.theta)**2 / (self.x_weight + self.weight)))

    # update velocities and positions
    self.xdot += x_acc * dt
    f = self.xdot * dt
    temp = True
    if self.x >= -1.5:
        if f < 0:
            self.x += f
        temp = False
    elif self.x <= 1.5:
        if f > 0:
            self.x += f
        temp = False
    if temp:
       self.x += f
    self.thetadot += theta_acc * dt
    self.theta += self.thetadot * dt

    # normalize theta to [-pi, pi]
    self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))/drag

# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

class PlotCartPole:
    def __init__(self, cart_pole):
        self.cart_pole = cart_pole
        self.fig, self.ax = plt.subplots()
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)

    def init(self):
        return self.line,

    def simulate(self, i):
        self.ax.cla()  # clear the axis
        self.cart_pole.sim_step(int(random.randrange(-100,100)/10))  # simulate one step
        x_cart = self.cart_pole.x
        y_cart = 0
        x_pendulum = x_cart + self.cart_pole.lenght * np.sin(self.cart_pole.theta)
        y_pendulum = -self.cart_pole.lenght * np.cos(self.cart_pole.theta)
        self.x_data = [x_cart, x_pendulum]  # reset x_data
        self.y_data = [y_cart, y_pendulum]  # reset y_data
        self.line, = self.ax.plot(self.x_data, self.y_data, 'o-')  # re-create the line
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        return self.line,

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.simulate, frames=200, init_func=self.init, blit=True, interval=50)
        
        plt.show()
cart_pole = CartPole(x=0, xdot=0, theta=math.pi/4, thetadot=0, lenght=1, x_weight=1, weight=0.1)
plot_cart_pole = PlotCartPole(cart_pole)
plot_cart_pole.animate()

