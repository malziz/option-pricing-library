import numpy as np

class EuropeanVanillaOption():

    #initializing Vanilla Option parameters
    def __init__(self, 
                strike: float, 
                maturity : int ,
                option_type="call"):

        if strike<=0 or maturity <=0 :
            raise ValueError(
                "Maturity and Strike must be positive"
            )
        if option_type not in ("call","put"):
            raise ValueError(
                "option_type must be either 'call' or 'put'.  "
            ) 
        
        self.strike=strike
        self.maturity=maturity
        self.option_type=option_type

    #calculate payoff at maturity
    def payoff(self, spot_maturity):
        
        if self.option_type=="call":
            return np.maximum(spot_maturity-self.strike,0)
            
        return np.maximum(self.strike-spot_maturity,0)
            
            