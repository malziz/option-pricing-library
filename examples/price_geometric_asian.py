from option_pricing.models.gbm import GBM
from option_pricing.contracts.european_asian import EuropeanAsianOption
from option_pricing.engines.geometric_asian_formula import GeometricAsianFormula
from option_pricing.engines.monte_carlo import MonteCarloEngine
import numpy as np 

model=  GBM(
    spot=100,
    rate=0.05,
    volatility=0.20
)

#pricing geometric asian option
#in this first example, we are using the closed form therefore specifying observation_times

option= EuropeanAsianOption(
    strike=100,
    maturity=1,
    observation_times= np.linspace(
    1/12,
    1,
    12),
    option_type="call"
)

engine=GeometricAsianFormula(model)

price = engine.price(option)

print(f"Geometric Asian call closed formula price: {price:.2f}")


#this is a different example, we don't have discrete observation times here therefore we don't expect to compare the two option values
#we are using standard monte carlo to price a geometric asian option
engine2=MonteCarloEngine(model,seed=42)

standard_result=engine2.price(option,payoff_style="geometric")
print(f"Option price using standrd Monte Carlo : {standard_result["price"]:.4f}")
print(f"Monte carlo standard error : {standard_result["standard_error"]:.4f}")

#we are using antithetic variates monte carlo to price the same option
engine_antithetic=MonteCarloEngine(model,seed=42,antithetic=True)

antithetic_result=engine_antithetic.price(option,payoff_style="geometric")
print(f"Option price using Monte Carlo : {antithetic_result["price"]:.4f}")
print(f"Monte carlo antithetic error : {antithetic_result["standard_error"]:.4f}")

#checking the VRF to see if variance did indeed reduce with antithetic variates (need to be higher than 1)
variance_reduction_factor = (
    standard_result["standard_error"]**2
    /antithetic_result["standard_error"]**2
)

print (f"Variance reduction factor : {variance_reduction_factor:.2f}")

#pricing arithmetic asian option using the same standard monte carlo engine

option2= EuropeanAsianOption(
    strike=100,
    maturity=1,
    option_type="call"
)

standard_result2=engine2.price(option,payoff_style="arithmetic")
print(f"Arithmetic Asian price using standrd Monte Carlo : {standard_result2["price"]:.4f}")
print(f"Monte carlo standard error : {standard_result2["standard_error"]:.4f}")
