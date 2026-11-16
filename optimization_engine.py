import numpy as np
from scipy.optimize import linprog

class SupplyChainOptimizer:
    """
    Core Linear Programming Backend Engine.
    Balances raw factory capacities against distribution network demands.
    """
    def __init__(self, production_costs, holding_costs, shipping_costs, capacities, demand):
        self.prod_costs = np.array(production_costs)
        self.hold_costs = np.array(holding_costs)
        self.ship_costs = np.array(shipping_costs)
        self.capacities = np.array(capacities)
        self.demand = np.array(demand)
        self.num_factories = len(self.prod_costs)
        self.num_warehouses = len(self.hold_costs)
        
    def solve(self):
        # 1. Structure the objective cost function
        c = []
        for f in range(self.num_factories):
            for w in range(self.num_warehouses):
                c.append(self.prod_costs[f] + self.ship_costs[f][w] + self.hold_costs[w])
                
        # 2. Build Factory Capacity Inequality Constraints (<=)
        A_ub, b_ub = [], []
        for f in range(self.num_factories):
            row = [0] * (self.num_factories * self.num_warehouses)
            for w in range(self.num_warehouses):
                row[f * self.num_warehouses + w] = 1
            A_ub.append(row)
            b_ub.append(self.capacities[f])
            
        # 3. Build Warehouse Demand Equality Constraints (==)
        A_eq, b_eq = [], []
        for w in range(self.num_warehouses):
            row = [0] * (self.num_factories * self.num_warehouses)
            for f in range(self.num_factories):
                row[f * self.num_warehouses + w] = 1
            A_eq.append(row)
            b_eq.append(self.demand[w])
            
        # 4. Enforce non-negative bounds
        bounds = [(0, None) for _ in range(self.num_factories * self.num_warehouses)]
        
        # 5. Execute solver
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        
        if not result.success:
            return {"status": "Failed", "message": "Optimization constraints are structurally infeasible."}
            
        allocation = result.x.reshape(self.num_factories, self.num_warehouses)
        return {
            "status": "Success",
            "total_minimum_cost": float(round(result.fun, 2)),
            "optimal_routing": allocation.tolist()
        }

# =====================================================================
# SYNTHETIC BASELINE TEST BED (Allows buyers to run it instantly)
# =====================================================================
if __name__ == "__main__":
    print("--- Executing Supply Chain Optimization Core ---")
    
    # Define hardcoded baseline data for developer validation
    sample_production_costs = [12.50, 18.20]
    sample_holding_costs = [1.80, 2.20, 2.90]
    sample_shipping_costs = [[4.50, 5.20, 6.10], [6.00, 7.80, 8.50]]
    sample_capacities = [600, 450]
    sample_demand = [300, 400, 250]
    
    optimizer = SupplyChainOptimizer(
        sample_production_costs,
        sample_holding_costs,
        sample_shipping_costs,
        sample_capacities,
        sample_demand
    )
    
    print(optimizer.solve())
