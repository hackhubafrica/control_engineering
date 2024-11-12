import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def vehicle(v ,t ,u ,load):
    #  inputs 
    #  v = vehicle velocity(m/s)
    #  t =time (sec)
    #  load = passener load + cargo(kg)
    Cd = 0.24     # drag coefficient 
    rho = 1.225    #  air density (kg/m^3)
    h = 5.0     # cross-section area(m^2)
    Fp = 30     # thrust(n)
    m = 500       #  vehicl mass(kg)

    #  calculate derivative of velocity
    dv_dt = (1.0/(m + load)) * (Fp*u - 0.5*rho*Cd*A*v**2)
    return dv_dt

def linear(v ,t ,u,load):
    u_ss = 40   # 5%
    v_ss = 40.4  # m/s
    
    Cd = 0.24
    rho = 1.225
    h = 5.0
    Fp = 30
    m = 500

    alpha = Fp(m+load)
    beta = -rho * A * Cd * v_ss/(m + load)
    dv_dt = alpha * (u - u_ss) + beta * (v -v_ss)
    return dv_dt

t = 60.0
nsteps = 61
delta_t = t/nsteps -1
ts = np.linspace(0 ,t ,nsteps)

step = np.zeros(nsteps)
step[11:] = 40.0

# passwnger + cargo
load = 200.0

v0 = 0.0
vs = np.zeros(nsteps)
vsl = np.zeros(nsteps)

for i in range(nsteps -1):
    u = step[i]
    # clip inputs to -50% to 100%
    if u >= 100.0:
        u = 100.0
    if u <= -50.0:
        u = -50.0
    v = odeint(vehicle,v0[0,delta_t],args=(u,load)) 
    v0=v[i+1]  # take last value as initial condition
    vs[i +1] = v0   #store velocity for plotting



v0 = 0.0
for i in range(nsteps -1):
    u = step[i]
    # clip inputs to -50% to 100%
    if u >= 100.0:
        u = 100.0
    if u <= -50.0:
        u = -50
    v = odeint(linear ,v0[0,delta_t],args=(u,load)) 
    v0=v[i+1]
    vsl[i +1] = v0


plt.figure()
plt.subplot(2 ,1,1)   
plt.plot(ts ,vs, 'b--',linewidth=3,label='Non-linear')
# plt.plot(ts ,vsl, 'k--',linewidth=3,label = 'linear')
# plt.ylabel('Velocity m/s')
# plt.legend(loc=2)
# plt.subplot(2,1,2)
# plt.plot(ts,step,'r--',linewidth=3)
# plt.xlabel('gas pedal')
# plt.show()


