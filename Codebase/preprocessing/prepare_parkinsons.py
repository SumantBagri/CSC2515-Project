import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('parkinsons_updrs.data')

X = data.loc[1:, data.columns != 'total_UPDRS']
y = data.loc[1:, 'total_UPDRS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=1)


def write_fields(data, labels, filename):
    X = data.values
    y = labels.values
    with open(filename, "w") as file:
        for row in range(data.shape[0]):
            file.write(str(y[row]) + "\t" + "\t".join(map(str, X[row])) + "\n")


train_filename = "parkinsons_train"
validation_filename = "parkinsons_validation"
test_filename = "parkinsons_test"

write_fields(X_train, y_train, train_filename)
write_fields(X_val, y_val, validation_filename)
write_fields(X_test, y_test, test_filename)

with open(train_filename + '.cd', 'w') as file:
    file.write('0\tTarget\n')
