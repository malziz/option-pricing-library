import numpy as np

class GBM : 
    """ 
    Geometric Brownian motion under the risk neutral measure
    
    """

    #initializing model parameters
    def __init__(self, spot : float, rate : float, volatility :float, dividend_yield=0.0):
        self.spot = spot
        self.rate = rate
        self.volatility = volatility
        self.dividend_yield = dividend_yield

    #simulating underlying's paths under the risk neutral geometric brownian motion
    def simulate_paths(self, maturity:float, n_steps:int, n_paths:int, seed=None,antithetic=False):

        """
        Simulate asset price paths under risk-neutrak GBM

        Parameters 
        ---------
        maturity : float
            Time to maturity in years
        n_steps : int 
            Number of time steps per path
        n_paths : int 
            Number of simulated paths
        seed : int or None
            Random seed for reproducibility

        Returns
        ------
        numpy.ndarray
            Simulated prices with shape (n_paths,n_steps+1)
        """

        #controling inconsistent inputs
        if maturity <= 0 or n_steps <= 0 or n_paths <= 0 :
            raise ValueError(
                "maturity, n_steps and n_paths must be positive"
            )

        #antithetic variates can be chosen in this method for variance reduction purposes 
        if antithetic and n_paths%2 !=0:
            raise ValueError(
                "n_paths must be even when using antithetic variates."
            )

        #initializing the random number generator
        rng=np.random.default_rng(seed)

        if antithetic :
            
            z_half=rng.standard_normal(
                (n_paths//2,n_steps)
            )

            z=np.vstack((z_half,-z_half))
        else : 
            z=rng.standard_normal((n_paths,n_steps))
            
        dt=maturity/n_steps

        #calculating asset prices, gbm solution 

        increments=(
            (
                self.rate
                -self.dividend_yield
                -0.5*self.volatility**2
            )*dt
            + self.volatility*np.sqrt(dt)*z
        )
        
        log_returns= np.cumsum(increments,axis=1)
        paths=self.spot*np.exp(
            np.column_stack(
                [np.zeros(n_paths),
                 log_returns]
            )
        )

        return paths


        