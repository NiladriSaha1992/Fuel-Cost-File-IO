""" Defining modules """
import math


# calculate cpg
def calcCpg(Octane):
  Octane = round(Octane, 2)
  if Octane <= 89.00:
    return 6.00
  elif Octane >= 89.01 and Octane <= 90.99:
    return 8.00
  elif Octane >= 91.00 and Octane <= 94.99:
    return 10.45
  elif Octane >= 95.00 and Octane <= 120.00:
    return 23.94
  else:
    return 36.98
  

# calculate fuel cost
def calcFuelCost(m, mpg, cpg):
  FuelCost = m / mpg * cpg
  return math.ceil(FuelCost)
  