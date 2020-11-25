install.packages('deSolve')
library (deSolve)

sirc_model = function (current_timepoint, state_values, parameters)
{
  # create state variables (local variables)
  S = state_values [1]        # susceptibles
  I = state_values [2]        # infectious
  R = state_values [3]        # recovered
  C = state_values [4]        # carriers
  
  with ( 
    as.list (parameters),     # variable names within parameters can be used 
    {
      # compute derivatives
      dS = (-beta * S * I) - (epsilon * beta * S * C)
      dI = (beta * S * I) + (epsilon * beta * S * C) - (gamma * I)
      dR = (1 - rho) * (gamma * I) + (tau * C) 
      dC = (rho * gamma * I) - (tau * C)
      
      # combine results
      results = c (dS, dI, dR, dC)
      list (results)
    }
  )
}

contact_rate = 7                 # number of contacts per day
transmission_probability = 0.08      # transmission probability
infectious_period = 11             # infectious period
reduced_transmission_rate = 0.09     # chronic carriers compared to acute infections
acute_infections_proportion = 0.67     # acute infections that become carriers
length_of_time_in_carrier_state = 7     # length of time in carrier state

beta_value = contact_rate * transmission_probability
gamma_value = 1 / infectious_period
epsilon_value = 0.09
tau_value = 1 / length_of_time_in_carrier_state
rho_value = 0.67

Ro = beta_value / gamma_value
parameter_list = c (beta = beta_value, gamma = gamma_value, epsilon = epsilon_value, tau = tau_value, rho = rho_value)
V = 2          # carrier hosts
X = 17282      # susceptible hosts
Y = 19          # infectious hosts
Z = 768         # recovered hosts
N = V + X + Y + Z

initial_values = c (S = X/N, I = Y/N, C = V/N, R = Z/N)
timepoints = seq (0, 50, by=1)
output = lsoda (initial_values, timepoints, sirc_model, parameter_list)
