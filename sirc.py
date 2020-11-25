import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

###############################
# SIRC differential equations #
###############################
def sirc(y, timepoints, N, beta, gamma, epsilon, tau, rho):

    """
    Function to compute derivatives of the SIRC differential equations
    """
    S, I, R, C = y

    dSdt = (-beta * S * I) - (epsilon * beta * S * C)
    dIdt = (beta * S * I) + (epsilon * beta * S * C) - (gamma * I)
    dRdt = (1 - rho) * (gamma * I) + (tau * C)
    dCdt = (rho * gamma * I) - (tau * C)

    return dSdt, dIdt, dRdt, dCdt

##############
# Parameters #
##############
contact_rate = 7 #number of contacts per day
transmission_probability = 0.08 #transmission probability
infectious_period = 10 #infectious period
reduced_transmission_rate = 0.09 #chronic carriers compared to acute infections
acute_infections_proportion = 0.67 #acute infections that become carriers
length_of_time_in_carrier_state = 15 #length of time in carrier state

#######################
# Dynamics parameters #
#######################
beta = contact_rate * transmission_probability #transmission rate
gamma = 1 / infectious_period #recovery rate
epsilon = reduced_transmission_rate #reduced transmission rate
tau = 1 / length_of_time_in_carrier_state #carrier state
rho = acute_infections_proportion #acute infections

#####################################
# Initial values of sub-populations #
#####################################
X = 980 #susceptible hosts
Y = 20 #infectious hosts
Z = 0 #recovered hosts
V = 0 #carrier hosts

N = X + Y + Z + V #Total population

#######################################################
# Initial state values for the differential equations #
#######################################################
S0 = X/N
I0 = Y/N
R0 = Z/N
C0 = V/N

y = S0, I0, R0, C0 #initial conditions vector

#################################################
# Integrate the SIRC equations over a time grid #
#################################################
timepoints = np.linspace(0, 50, 50)

##############################
# Simulate the SIRC epidemic #
##############################
output = odeint(sirc, y, timepoints, args=(N, beta, gamma, epsilon, tau, rho))
S0, I0, R0, C0 = output.T

#######################################################
# Plot dynamics of susceptibles, infectious, carriers #
# and recovered sub-populations in the same plot      #
#######################################################
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

ax.plot(timepoints, S0, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(timepoints, I0, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(timepoints, R0, 'g', alpha=0.5, lw=2, label='Recovered')
ax.plot(timepoints, C0, 'k', alpha=0.5, lw=2, label='Carrier')

ax.set_xlabel('Time (days)')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0, 1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')

legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)

plt.show()
