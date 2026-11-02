import numpy as np 
from scipy.stats import norm

class GeometricAsianFormula:

    def __init__(self,model):
        self.model=model

    def price(self,option):

        S=self.model.spot
        r=self.model.rate
        q=self.model.dividend_yield
        sigma=self.model.volatility
        K=option.strike

        obs_times=np.asarray(option.observation_times)

        n=len(obs_times)

        if n == 0:
            raise ValueError("At least one observation is required.")

        if np.any(obs_times <= 0):
            raise ValueError("Observation times must be positive.")

        if np.any(obs_times > option.maturity):
            raise ValueError("Observation times cannot exceed maturity.")

        if np.any(np.diff(obs_times) <= 0):
            raise ValueError("Observation times must be strictly increasing.")

        if sigma <= 0:
            raise ValueError("Volatility must be positive.")


        m_g= (
            np.log(S)
            +(r-q-0.5*sigma**2)
            * np.mean(obs_times)
            )

        min_matrix=np.minimum.outer(
            obs_times,
            obs_times
            )


        v_g= (
            (sigma**2)
            *np.sum(min_matrix)
            /(n**2)
        )

        F_g=np.exp(m_g+v_g/2)
        
        d_1=(
            np.log(F_g/K)+v_g/2
            )/np.sqrt(v_g)

        d_2=d_1-np.sqrt(v_g)

        discount=np.exp(-r*option.maturity)

        if option.option_type=="call":

            return discount*(
                F_g*norm.cdf(d_1)
                -K*norm.cdf(d_2)
            )
        elif option.option_type=="put":

            return discount*(
                K*norm.cdf(-d_2)
                -F_g*norm.cdf(-d_1)
            )
        
        
        