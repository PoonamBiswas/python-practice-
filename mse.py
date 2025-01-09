def mse(y_pred, y_true):
    if len(y_pred)!=len(y_true):
        raise ValueError("Unequal length of list")
    sqmer = [(t-p)** 2 for t,p in zip(y_true,y_pred)]
    return sum(sqmer)/len(sqmer)

# Example usage
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print("MSE:", mse(y_true, y_pred))
    