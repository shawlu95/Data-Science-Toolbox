from sklearn.datasets import fetch_openml
import warnings
warnings.filterwarnings('ignore')

mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
y_train_5 = (y_train == "5")  # True for all 5s, False for all other digits.
y_test_5 = (y_test == "5")