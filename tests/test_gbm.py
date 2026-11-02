from option_pricing.models.gbm import GBM

model=GBM(
    spot=100,
    rate=0.05,
    volatility=0.2,
    dividend_yield=0.02
)

paths=model.simulate_paths(
    maturity=1.0,
    n_steps=252,
    n_paths=5,
    seed=42
)

print("Shape :", paths.shape)
print("Initial prices : ", paths[:,0])
print("Final prices : ", paths[:,-1])