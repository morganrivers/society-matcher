import pulp
from pulp import LpMaximize, LpProblem, LpVariable

interests = {}
resources = {}

r = input('enter interest in resilience on scale 1-3: \n\
       1: same as default society \n\
       2:partially off-grid \n\
       3: entire supply chain and all food is generated locally\n')

interests["resilience"] = r

s = input('enter interest in sustainability on scale 1-3: \n\
       1: same as default society \n\
       2: close to carbon neutral \n\
       3: carbon negative\n')

interests["sustainability"] = s

g = input('enter interest in communal governance on scale 1-3: \n\
       1: radical self-reliance \n\
       2: chores 4-5 hours a week \n\
       3: meetings every day, we are all relying on each other as a big polyamorous family\n')

interests["governance"] = g

# print("")
# print("now for resources")

# f = input('enter your financial resources: \n\
#        1: I got nothing\n\
#        2: can contribute rent $500 a month \n\
#        3: I\'m rich and can give you >$10k \n')

# resources["financial"] = f

communities = {}
communities["earthship"] = {}
communities["praxis"] = {}
communities["slabcity"] = {}

communities["slabcity"]["resilience"] = 1
communities["slabcity"]["sustainability"] = 1
communities["slabcity"]["governance"] = 1

communities["praxis"]["resilience"] = 2
communities["praxis"]["sustainability"] = 2
communities["praxis"]["governance"] = 2

communities["earthship"]["resilience"] = 3
communities["earthship"]["sustainability"] = 3
communities["earthship"]["governance"] = 2

model = LpProblem(name="optimization_matching", sense=LpMaximize)

for ckey, cvalue in communities.items():
    print(ckey, '->', cvalue)
    score = 0
    for ikey, ivalue in cvalue.items():

        score = score + 2 - abs(ivalue-int(interests[ikey]))

    print('score ' + ckey+': '+str(score)) 

# Initialize the variable to maximize
z = LpVariable(name="Least_Humans_Fed_Any_Month", lowBound=0)

