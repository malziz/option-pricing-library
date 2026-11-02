# Option Pricing Library

A Python library for quantitative option pricing, developed from scratch as an ongoing project to explore derivative pricing models, numerical methods, and Monte Carlo simulation.

**Status:** Work in progress — new models, pricing methods, and improvements will be added over time.

## Features

### Stochastic Models
- **Geometric Brownian Motion (GBM):** Simulates underlying asset price paths under the risk-neutral measure.
- Support for continuous dividend yields.

### Option Contracts
- **European vanilla options:** Call and put contracts.
- **European Asian options:** Arithmetic and geometric average-price call and put contracts.

### Pricing Engines

| Pricing Method | Supported Options |
|---|---|
| Black–Scholes analytical formula | European vanilla options |
| Geometric Asian closed-form solution | European geometric Asian options |
| Monte Carlo simulation | Vanilla, arithmetic Asian, and geometric Asian options |

### Variance Reduction
- **Antithetic variates:** Optional variance reduction technique for Monte Carlo pricing, using negatively correlated random paths to improve simulation efficiency.

## Technologies

- Python
- NumPy
- SciPy

## Project Structure

```text
option_pricing_library/
├── src/
│   └── option_pricing/
│       ├── models/
│       ├── contracts/
│       └── engines/
├── tests/
├── examples/
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd option_pricing_library
```

Install the library in editable mode:

```bash
python -m pip install -e .
```

## Project Development

This library is an ongoing personal project focused on progressively developing a practical understanding of quantitative option pricing and implementing the corresponding methods in Python.

Future extensions may include:
- Control variates for Monte Carlo simulation.
- Additional stochastic processes and underlying asset models.
- Further exotic option contracts.
- Additional numerical pricing methods.
- Model validation, convergence analysis, and sensitivity calculations (Greeks).

## Disclaimer

This project is intended for educational and research purposes. It is not designed for production trading or investment decision-making.