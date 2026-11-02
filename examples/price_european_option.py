from option_pricing.models.gbm import GBM
from option_pricing.contracts.european_vanilla import EuropeanVanillaOption
from option_pricing.engines.monte_carlo import MonteCarloEngine
from option_pricing.engines.black_scholes import BlackScholesEngine

#example of pricing an option using Black and Scholes

model=GBM(
    spot= 100,
    rate= 0.05,
    volatility=0.2
)

option=EuropeanVanillaOption(
    strike= 105,
    maturity=3,
    option_type="call"
)

engine_BS=BlackScholesEngine(model)
result_BS=engine_BS.price(option)
print(f"Option price using Black and Scholes is : {result_BS:.2f}")


#pricing the same option using monte Carlo and checking confidence interval
engine2=MonteCarloEngine(
    model,
    seed=42)

standard_result=engine2.price(option)
ci_99=engine2.confidence_interval(standard_result, confidence_level=0.95)

print(f"Option price using Standard Monte Carlo : {standard_result["price"]:.4f}")
print(f"Monte carlo standard error : {standard_result["standard_error"]:.4f}")

print(f"Standard Monte Carlo at level {ci_99['confidence level']:.2f},"
      f" \n lower bound {ci_99['lower bound']:.4f}, "
      f" \n upper bound {ci_99['upper bound']:.4f}"
      ) 

#pricing the same option using antithetic variates to reduce vriance
engine3=MonteCarloEngine(
    model,
    seed=42,
    antithetic=True)

antithetic_result=engine3.price(option)

print(f"Option price using Antithetic variates Monte Carlo : {antithetic_result["price"]:.4f}")
print(f"Antithetic variates Monte carlo standard error : {antithetic_result["standard_error"]:.4f}")

ci_99_antithetic=engine2.confidence_interval(antithetic_result, confidence_level=0.95)

print(f"Antithetic Monte Carlo at level {ci_99_antithetic['confidence level']:.2f},"
      f" \n lower bound {ci_99_antithetic['lower bound']:.4f}, "
      f" \n upper bound {ci_99_antithetic['upper bound']:.4f}"
      ) 

#checking the VRF to see if variance did indeed reduce with antithetic variates (need to be higher than 1)
variance_reduction_factor = (
    standard_result["standard_error"]**2
    /antithetic_result["standard_error"]**2
)

print (f"Variance reduction factor : {variance_reduction_factor:.2f}")

