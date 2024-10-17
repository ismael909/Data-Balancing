# Installation
Assuming you're in current directory run the following command.
```
pip install -e .
```

# Example usage

```py
# Import the functions from the installed library
from border_detection_minimal.border_detection_minimal import classify_border_and_core_points

# Generate random data points for the example (1000 points in 2D space)
import numpy as np
X = np.random.rand(1000, 2)

# Classify points into border and core points
border_points, core_points = classify_border_and_core_points(X, p=2, close=100, percentile=60)

print(f"Number of border points: {border_points.shape[0]}")
print(f"Number of core points: {core_points.shape[0]}")
```
