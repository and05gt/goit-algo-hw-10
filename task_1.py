import pulp

model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Maximize the total quantity of products (1 unit of lemonade + 1 unit of juice)
model += lemonade + fruit_juice, "Total_Products"

# Water: 2 units for Lemonade + 1 unit for Juice <= 100
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# Sugar: 1 unit per Lemonade <= 50
model += 1 * lemonade <= 50, "Sugar_Constraint"

# Lemon juice: 1 unit per Lemonade <= 30
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# Fruit puree: 2 units per Juice <= 40
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Quantity of 'Lemonade': {lemonade.varValue}")
print(f"Quantity of 'Fruit Juice': {fruit_juice.varValue}")
print(f"Total quantity of products: {pulp.value(model.objective)}")
