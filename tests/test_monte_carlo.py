from option_pricing.models.gbm import GBM
from option_pricing.contracts.european import EuropeanOption
from option_pricing.engines.monte_carlo import MonteCarloEngine
from option_pricing.engines.black_scholes import BlackScholesEngine


model=GBM(
    spot= 100,
    rate= 0.05,
    volatility=0.2
)

option=EuropeanOption(
    strike= 105,
    maturity=3,
    option_type="call"
)

engine1=MonteCarloEngine(
    model,
    n_paths=100_000,
    seed=42)

standard_result=engine1.price(option)
#ci_99=engine1.confidence_interval(standard_result, confidence_level=0.99)

print(f"Option price using Monte Carlo : {standard_result["price"]:.4f}")
print(f"Monte carlo standard error : {standard_result["standard_error"]:.4f}")

"""
print(f"CI at level {ci_99['confidence level']:.2f},"
      f" \n lower bound {ci_99['lower bound']:.4f}, "
      f" \n upper bound {ci_99['upper bound']:.4f}"
      ) 
"""


engine2=MonteCarloEngine(
    model,
    n_paths=100_000,
    seed=13,
    antithetic=True)

antithetic_result=engine2.price(option)
#ci_99=engine2.confidence_interval(antithetic_result, confidence_level=0.99)

print(f"Option price using Monte Carlo : {antithetic_result["price"]:.4f}")
print(f"Monte carlo standard error : {antithetic_result["standard_error"]:.4f}")

variance_reduction_factor = (
    standard_result["standard_error"]**2
    /antithetic_result["standard_error"]**2
)

print (f"Variance reduction factor : {variance_reduction_factor:.2f}")

engine2=BlackScholesEngine(model)
result2=engine2.price(option)
print(f"option price using closed form is : {result2:.2f}")