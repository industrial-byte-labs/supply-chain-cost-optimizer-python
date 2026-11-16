# 🏭 Lightweight Industrial Supply Chain Cost Optimizer (SciPy LP Core)

A foundational Operations Research (OR) framework implemented in Python to solve multi-echelon transportation and logistics network problems. Utilizing standard **Linear Programming (LP) optimization models (`scipy.optimize.linprog`)**, this script mathematically minimizes aggregate supply chain costs—including manufacturing production overheads and raw freight matrix tariffs—while satisfying capacity caps and localized regional market demands.

---

## 🚀 Upgrade to the Production-Ready Enterprise Bundle

This public repository contains the naked mathematical solver script intended for developer terminal testing. If you are an operations manager, supply chain director, or consultant looking to deploy this framework internally for commercial factory environments, skip the manual code adjustments.

### The Premium Enterprise Package Includes:
1. **Interactive Streamlit Web Dashboard UI:** A gorgeous, local web app layout with responsive KPI metrics cards, slider variables, and automated highlight matrix grids.
2. **Bulk Data Excel Importer/Exporter:** No coding required. Planners can drag and drop a standard corporate multi-tab spreadsheet to update factory parameters instantly.
3. **Executive Summary Report Generator:** Programmatically auto-saves localized text manifests detailing precise dispatch routing logs to attach directly to company slide decks.
4. **Complete Sample Industrial Data Hub:** Pre-populated network templates built around realistic industrial logistics parameters.

👉 **[Download the Full Enterprise Streamlit & Excel Production Suite Here](https://industrialbyte.gumroad.com/l/supply-chain-optimizer)** *(Secure Global Checkout via PayPal / Cards)*

---

## 📐 The Mathematical Constraint Optimization Model

The core logic structures a classical balance equation formulated as a minimized objective cost function vector:

\[\text{Minimize } Z = \sum_{i=1}^{M} \sum_{j=1}^{N} (P_i + S_{ij} + H_j) \cdot X_{ij}\]

Where:
* M, N = Total number of active production factories and distribution warehouses.
* \(P_i\) = Unit manufacturing cost at Plant i.
* \(S_{ij}\) = Freight transport tariff per unit from Plant i to Warehouse j.
* \(H_j\) = Localized monthly inventory holding fee at Warehouse j.
* \(X_{ij}\) = The targeted allocation quantity variable mapped between nodes.

### Matrix Constraints Enforced:
* **Capacity Boundary:** Total units dispatched from any factory cannot exceed its absolute physical monthly output limits.
* **Demand Balance:** Total combined allocation arriving at any warehouse node must exactly equal the regional consumer demand constraint.
* **Non-Negativity:** All variable allocations (\(X_{ij}\)) must be greater than or equal to zero.

---

## 🛠️ Framework Installation & Core Script Usage

### 1. Requirements Setup
This lightweight module operates strictly on baseline open-source data science tools:
```bash
pip install scipy numpy
```

### 2. Standalone Code Execution
Create a file named `optimization_engine.py`, paste the underlying core solver class code inside your environment, and execute the matrix initialization loop via your terminal workspace:
```bash
python optimization_engine.py
```

---

## ⚙️ Baseline Architecture Setup

```python
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
        c = []
        for f in range(self.num_factories):
            for w in range(self.num_warehouses):
                c.append(self.prod_costs[f] + self.ship_costs[f][w] + self.hold_costs[w])
                
        A_ub, b_ub = [], []
        for f in range(self.num_factories):
            row = [0] * (self.num_factories * self.num_warehouses)
            for w in range(self.num_warehouses):
                row[f * self.num_warehouses + w] = 1
            A_ub.append(row)
            b_ub.append(self.capacities[f])
            
        A_eq, b_eq = [], []
        for w in range(self.num_warehouses):
            row = [0] * (self.num_factories * self.num_warehouses)
            for f in range(self.num_factories):
                row[f * self.num_warehouses + w] = 1
            A_eq.append(row)
            b_eq.append(self.demand[w])
            
        bounds = [(0, None) for _ in range(self.num_factories * self.num_warehouses)]
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        
        if not result.success:
            return {"status": "Failed", "message": "Optimization constraints are structurally infeasible."}
            
        allocation = result.x.reshape(self.num_factories, self.num_warehouses)
        return {
            "status": "Success",
            "total_minimum_cost": float(round(result.fun, 2)),
            "optimal_routing": allocation.tolist()
        }
```

---

## ⚖️ Intellectual Property Terms & Software License

* **Developer Access:** The core algorithm blocks are fully open-source for personal trial, architectural educational research, and internal operational validation.
* **Commercial Restraints:** White-labeling, re-packaging, or direct commercial resale of this optimization model template layout on secondary digital asset stores or public marketplace frameworks is strictly prohibited.

---
*Maintained under a clean, secure corporate asset architecture by IndustrialByte Analytics.*

