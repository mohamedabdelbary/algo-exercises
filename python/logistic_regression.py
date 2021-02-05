"""
Implement Logistic regression/perceptron algorithm for classification. The implementation, should have a fit
method that accepts a list of lists of features, and a list of corresponding targets each a 1-hot encoded list
for the correct class.

The trained model should have a predict method that accepts a single set of features and produces the target
prediction.

Bonus - report on accuracy of the model.

NOTE: You can only use numpy and pandas for numerical computation.
"""
import random
import numpy as np
import pandas as pd


def batches(it, size=10):
    n = next(it, None)
    while n:
        batch = [n]
        i = 1
        while i < size:
            n = next(it, None)
            if n:
                batch.append(n)
            else:
                break
            i += 1
        if batch:
            yield batch


def _one_hot_encode(value, categories):
    i = 0
    one_hot_vec = [0] * len(categories)
    while value != categories[i]:
        i += 1

    if i >= len(categories):
        return None

    one_hot_vec[i] = 1
    return one_hot_vec


def _get_feature_stats(records, features):
    """
    get mean and std deviations for features specified
    """
    d = dict()
    for f in features:
        mean = np.mean([r[f] for r in records])
        std = np.std([r[f] for r in records])
        d[f] = {"mean": mean, "std": std}

    return d


def _prepare(records):
    x_features = sorted([k for k in records[0].keys() if k != 'species'])
    target_categories = sorted(list(set(r['species'] for r in records)))
    # 1-hot encode target variable
    for r in records:
        r.update({"target": _one_hot_encode(r['species'], target_categories)})

    x_features_mean_vars = _get_feature_stats(records, x_features)
    # Standardise all input features to be 0 mean and unit variance
    X = [[(r[f] - x_features_mean_vars[f]["mean"]) / x_features_mean_vars[f]["std"] for f in x_features]
         for r in records]
    y = [r['target'] for r in records]
    return X, y


def _get_accuracy(preds, out):
    correct = []
    for p, r in zip(preds, out):
        r_enum = enumerate(r)
        correct_class = [i[0] for i in r_enum if i[1] == 1][0]
        correct.append(1 if correct_class == p else 0)

    return 100 * sum(correct) / len(correct)


class LogisticRegression(object):
    def __init__(self, runs=10, epochs=1000, lr=0.001, print_every=50):
        self._runs = runs
        self._epochs = epochs
        self._lr = lr
        self._weights = None
        self._print_every = print_every

    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @classmethod
    def _sigmoid_prime(cls, x):
        sig = cls._sigmoid(x)
        return sig * (1 - sig)

    def fit(self, X, y):
        final_weights = None
        final_error = None
        for r in range(self._runs):
            print(f"Training for the {r + 1} time.")
            weights, error = self._train(X, y)
            if final_weights is None or error < final_error:
                print("Found lower error, updating final model weights")
                final_weights = weights
                final_error = error

            print("====================")

        self._weights = final_weights

    def _train(self, X, y):
        weights = np.random.rand(len(X[0]), len(y[1]))
        bias = np.random.rand(len(y[1]))
        errors = []
        for e in range(self._epochs):
            for batch in batches(zip(X, y)):
                X_np, y_np = np.array([t[0] for t in batch]), np.array([t[1] for t in batch])
                h = np.matmul(X_np, weights) + bias
                out = self._sigmoid(h)
                # Prediction error
                error = out - y_np
                # keep track of the error on the final epoch
                if e == self._epochs - 1:
                    errors.append(np.mean(error))
                error_prime = self._sigmoid_prime(error)
                # Weight adjustment is proportional to the derivative of the error.
                delta_w = np.matmul(X_np.T, error_prime)
                weights -= self._lr * delta_w
                bias -= self._lr

            if e % self._print_every == 0:
                print(f"Trained epoch {e}")

        return weights, np.mean(errors)

    def predict(self, x):
        x = np.array(x)
        sig = self._sigmoid(np.matmul(x, self._weights))
        return max(enumerate(sig), key=lambda t: t[1])[0]

    def get_params(self):
        return self._weights


if __name__ == "__main__":
    # Test on Iris flowers dataset
    records = list(pd.read_csv("../data/iris.csv").T.to_dict().values())
    # Shuffle input data
    random.shuffle(records)
    # Prepare inputs and targets
    X, y = _prepare(records)
    # Split into train and test
    train_size = 2 * len(X) // 3
    X_train, y_train = X[:train_size], y[:train_size]
    X_test, y_test = X[train_size:], y[train_size:]
    model = LogisticRegression()
    model.fit(X_train, y_train)

    print("====Finished training====")
    print(f"Final model weight: {model.get_params()}")

    preds = []
    correct = []
    for idx in range(len(X_test)):
        x = X_test[idx]
        y = y_test[idx]
        pred = model.predict(x)
        preds.append(pred)
        print(f"Input {x}, model predicted: {pred}, and true target is {y}")

    print(f"Model accuracy is {_get_accuracy(preds, y_test)}%")
