from pycosmicwrap import CosmicWrap

# create an object with rest api url, rpc url and denom as arguments
osmosis = CosmicWrap(lcd='https://rpc.osmosis.zone:443',
                       rpc='https://lcd.osmosis.zone',
                       denom='uosmo')

# Once the module is imported and the object is created we can start using
# the object to interact with the blockchain

# Let's define an address
my_address = 'osmo1f8rcf47jpqq2thq9vjsap9y0eclzqeqxaxusl2'

# Let's create a variable with your balance
my_address_balance = osmosis.query_balances(my_address)

# or just print it out
print(my_address_balance)

# check all of your delegations
my_delegations = osmosis.query_delegations_by_address(my_address)

# and print them out
print(my_delegations)

# check all of your staking rewards
print(osmosis.query_rewards(my_address))