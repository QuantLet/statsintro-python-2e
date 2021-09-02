""" Demonstration of importing a Python module """

# author: ThH, date: Sept-2021

# Import standard packages
import numpy as np

# additional packages: this imports the function defined above
import L2_4_pythonFunction

# Generate test-data
testData = np.arange(-5, 10)

# Use a function from the imported module
out = L2_4_pythonFunction.incomeAndExpenses(testData)

# Show some results
print(f'You have earned {out[0]:5.2f} EUR, and spent {-out[1]:5.2f} EUR.')
