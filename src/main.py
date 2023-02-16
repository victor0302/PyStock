import matplotlib.pyplot as plt
import numpy as np
from src.prediction import y_new_pred



# Plot the predicted values
plt.plot(np.arange(len(y_new_pred)), y_new_pred)
plt.title("Predicted Stock Prices")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()
