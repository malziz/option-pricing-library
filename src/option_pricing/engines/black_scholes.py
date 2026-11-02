import numpy as np 
from scipy.stats import norm

class BlackScholesEngine():

    
    def __init__(self,model):
        
        self.model=model

    #Black and scholes closed formula for European Vanilla options
    def price(self,option):

        S=self.model.spot
        K=option.strike
        r=self.model.rate
        sigma=self.model.volatility
        q=self.model.dividend_yield
        T=option.maturity


        d_1= (np.log(S/K)
              +(r - q + 0.5 * sigma**2)*T
              )/ (sigma * np.sqrt(T))
        
        d_2= d_1-sigma*np.sqrt(T)

        if option.option_type=="call":
            return (
                S*np.exp(-q*T)*norm.cdf(d_1)
                -K*np.exp(-r*T)*norm.cdf(d_2)
            )
        elif option.option_type=="put":
            return (
                K*np.exp(-r*T)*norm.cdf(-d_2)
                -S*np.exp(-q*T)*norm.cdf(-d_1)
            )
                