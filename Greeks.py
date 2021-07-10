def call_price(spot, strike, risk_free_rate, vol, time_to_maturity):
    S = spot
    K = strike
    r = risk_free
    v = vol
    t = time_to_maturity
    d1 = (np.log(S/K) + (r + ((v*v)/2)) * t) / (v * sqrt(t))
    d2 = d1 - (v * sqrt(t))
    call = (norm.cdf(d1) * S) - (norm.cdf(d2) * K * exp(-r*t))
    return call

def put_price(spot, strike, risk_free_rate, vol, time_to_maturity):
    S = spot
    K = strike
    r = risk_free
    v = vol
    t = time_to_maturity
    d1 = (np.log(S/K) + (r + ((v*v)/2)) * t) / (v * sqrt(t))
    d2 = d1 - (v * sqrt(t))
    put = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put

def n_prime(d1):
    n_prime_d1 = (exp(-(d1*d1)/2)) * (1/sqrt(2 * pi))
    return n_prime_d1

def call_greeks(d1, n_prime_d1, S, K, r, v, t, d2):
    call_delta = np.round(norm.cdf(d1), 4)
    call_gamma = np.round(n_prime_d1 / (S * v * sqrt(t)), 4)
    call_vega = np.round(S * sqrt(t) * n_prime_d1, 4)
    call_theta = np.round(-((S * n_prime_d1 * v) / (2 * sqrt(t))) - (r * K * exp(r*t) * norm.cdf(d2)), 4)
    call_rho = np.round(K * t * exp(r * t) * norm.cdf(d2), 4)
    return call_delta, call_gamma, call_vega, call_theta, call_rho

def put_greeks(d1, n_prime_d1, S, K, r, v, t, d2):
    put_delta = np.round(norm.cdf(d1) - 1, 4)
    put_gamma = np.round(n_prime_d1 / (S * v * sqrt(t)), 4)
    put_vega = np.round(S * sqrt(t) * n_prime_d1, 4)
    put_theta = np.round(-((S * n_prime_d1 * v) / (2 * sqrt(t))) + (r * K * exp(-r * t) * (1 - norm.cdf(d2))), 4)
    put_rho = np.round(-K * t* exp(-r * t) * (1 - norm.cdf(d2)), 4)
    return put_delta, put_gamma, put_vega, put_theta, put_rho
