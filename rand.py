import numpy as np


coin_flips = np.random.choice(['Heads', 'Tails'], size=10)
print("Coin flip", coin_flips)


dice_rolls = np.random.randint(1,7, size=5)
print("Dice rolls", dice_rolls)


# np.random.seed(42)

# print("Random number with seed", np.random.rand(5))




# rand_nums = np.random.rand(5)
# print("Random", rand_nums)

# rand_ints = np.random.randint(1,7, size=5)
# print("Rand int", rand_ints)

# randn_nums = np.random.randn(5)
# print("randn", rand_nums)

# choice = np.random.choice(['Heads', 'Tails'], size=5)
# print("Chocie", choice)