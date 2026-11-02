import numpy as np

class EuropeanAsianOption():

    #initializing option parameters
    def __init__(
            self,
            strike,
            maturity,
            observation_times=None,
            option_type="call",
            averaging_method="geometric"
    ):
        if strike <=0 or maturity <=0 : 
            raise ValueError(
                "Maturity and Strike must be positive"
            )
        if option_type not in ("call","put"):
            raise ValueError(
                "option_type must be either call or put"
            )
        if averaging_method not in ("arithmetic","geometric"):
            raise ValueError(
                "Invalid averaging method."
            )

        self.strike=strike
        self.maturity=maturity
        self.observation_times=observation_times
        self.option_type=option_type
        self.averaging_method=averaging_method

    #calculating payoff
    def payoff(self,average):

            if self.option_type=="call":
                return np.maximum(average-self.strike ,0)

            return np.maximum(self.strike-average,0)

    