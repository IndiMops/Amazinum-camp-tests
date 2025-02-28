import numpy as np

coin_probs = np.array([0.8, 0.9, 0.1, 0.2, 0.3])
# Initial distribution of apostryor probability (evenly, 0.2 for each coin)
priors = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

def update_priors(priors, outcome, coin_probs):
    """
    Function to update the initial probability (prior) based on the observed toss outcome.
    
    Args:
    - priors: current aposterior probability for each coin.
    - outcome: observed result ('H' for the eagle, 'T' for the grid).
    - coin_probs: the probability of falling 'eagle' for each coin.
    
    Returns:
    - posterior: updated probability distribution after observation.
    """
    # calculate the probability of observation for each coin.
    likelihoods = np.where(outcome == 'H', coin_probs, 1 - coin_probs)
    
    # calculate the unnecessary posterior, multiplying current probabilities on the probability of observation
    unnormalized = priors * likelihoods
    
    # Normalize posterior so that the amount of probability is equal to 1
    posterior = unnormalized / np.sum(unnormalized)
    
    return posterior

# list of observed coin toss results ('H' - Eagle, 'T' - rescity)
tests = ['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H']

predicted_probs = []

# copy the initial probability to have a variable to update after each observation
current_priors = priors.copy()

for outcome in tests:
    # update current probabilities based on a observed result
    current_priors = update_priors(current_priors, outcome, coin_probs)
    
    # we calculate the projected probability of falling 'eagle' for the next toss
    next_flip_prob = np.dot(current_priors, coin_probs)
    
    predicted_probs.append(round(float(next_flip_prob), 2))

print("Projected probability for next tossed after each test:", predicted_probs)
