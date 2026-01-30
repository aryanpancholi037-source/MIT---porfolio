#import matplot to be able to graph height against time
import matplotlib.pyplot as plt
#equations
#velocity = acceleration x change in time
#position = velocity x change in time
#momentum = mass x velocity

#acceleration due to gravity m/s^2
acceleration = -9.81

#height (meters)
height = 10

gravity = - 9.81

dt = 0.01

velocity = 0

time = float(0.0)

#lists to store height and time for plotting afterwards
time_list=[]
height_list=[]

while height > 0:
    velocity = velocity + gravity*dt
    height = height + velocity * dt
    time=time+dt
    if height < 0:
        height = 0
    print("height: ",height)
    print("velocity: ",velocity)
    print("acceleration: ",acceleration)
    height_list.append(height)
    time_list.append(time)

plt.plot(time_list, height_list)
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.title("Falling Ball Simulation")

plt.show()