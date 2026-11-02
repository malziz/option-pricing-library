import numpy as np 

from option_pricing.contracts.european import EuropeanOption

option1_call=EuropeanOption(
    strike=100,
    maturity=1.0,
    option_type="call"
)

final_prices = np.array([80,100,120])


print("option payoff is :", option1_call.payoff(final_prices))