import numpy as np
from scipy.stats import norm , gmean


class MonteCarloEngine():

    def __init__(self,model,n_paths=100_000,n_steps=252,seed=None,antithetic=False):
        
        if n_paths<2 or n_steps<1 :
            
            raise ValueError("n_paths must be at least 2 \n " \
            "n_steps must be greater than 1 ")

        if antithetic and n_paths%2 != 0:
            raise ValueError ("n_paths must be even when using antithetic variates.")
        
        self.model=model
        self.n_paths=n_paths
        self.n_steps=n_steps
        self.seed=seed
        self.antithetic=antithetic

    
    def price(self,option,payoff_style="vanilla"):

        if payoff_style not in (
            "vanilla",
            "arithmetic",
            "geometric"
            ):
            raise ValueError("Invalid payoff_style.")


        paths=self.model.simulate_paths(
            maturity=option.maturity,
            n_steps=self.n_steps,
            n_paths=self.n_paths,
            seed=self.seed,
            antithetic=self.antithetic
        )

        #if vanilla , we take the simulated prices at maturity
        if payoff_style=="vanilla":
            final_prices=paths[:,-1]

        #if arithmetic asian, we calulcate the arithmetic mean of the simulated prices
        elif payoff_style=="arithmetic":
            final_prices=np.mean(paths,axis=1)

        #if geometric asian, we calulcate the geometric mean of the simulated prices
        elif payoff_style=="geometric":
            final_prices=np.exp(
                np.mean(np.log(paths),axis=1)
                )
        
        payoffs=option.payoff(final_prices)

        #payoffs are calculated differently if antithetic variates 
        if self.antithetic : 
            
            n_pairs=self.n_paths//2

            payoffs= (
                payoffs[:n_pairs]+payoffs[n_pairs:]
            )/2


        discount_factor=np.exp(- self.model.rate * option.maturity)

        price=discount_factor*np.mean(payoffs)

        #Monte Carlo standard error to quantify uncertainty 
        standard_error=(
            discount_factor
            *np.std(payoffs,ddof=1)
            / np.sqrt(len(payoffs))
        )

        return{
            "price": price,
            "standard_error":standard_error
        }

    #building confidence intervals from the resulting option price and the std error
    def confidence_interval(self,result,confidence_level=0.95):

        if not 0<confidence_level<1:
            raise ValueError ("confidence_level must be between 0 and 1.")
        
        option_price=result["price"]
        std_error=result["standard_error"]

        critical_value=norm.ppf( (1+confidence_level) / 2)

        lower_bound= option_price-critical_value*std_error
        upper_bound= option_price+critical_value*std_error

        return { 
            "confidence level": confidence_level,
            "lower bound" : lower_bound,
            "upper bound" : upper_bound
             }

