import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def test():
    print('Test App Service')

def test_2():
    t_end = time.time() + 60 * 15
    while time.time() < t_end:

def test_3():
    X, y = make_classification(n_samples=1000, n_features=4,
                                n_informative=2, n_redundant=0,
                                random_state=0, shuffle=False)
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X, y)
    print(clf.predict([[0, 0, 0, 0]]))

if __name__ == "__main__":
    test_2()