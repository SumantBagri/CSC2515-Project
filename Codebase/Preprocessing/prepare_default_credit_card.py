import pandas as pd
from sklearn.model_selection import train_test_split

# pip install --upgrade xlrd

data = pd.read_excel('default of credit card clients.xls', header=1)

X = data.iloc[:, :-1]
y = data[data.columns[-1]].apply(lambda x: 1 if x == 1 else -1)

# X = (X - X.mean()) / X.std()  # standardization
X = X.drop(["ID"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=1)


def write_fields(data, labels, filename):
    X = data.values
    y = labels.values
    with open(filename, "w") as file:
        for row in range(data.shape[0]):
            file.write(str(y[row]) + "\t" + "\t".join(map(str, X[row])) + "\n")


train_filename = "result_train"
validation_filename = "result_validation"
test_filename = "result_test"

write_fields(X_train, y_train, train_filename)
write_fields(X_val, y_val, validation_filename)
write_fields(X_test, y_test, test_filename)

with open(train_filename + '.cd', 'w') as file:
    file.write('0\tTarget\n')
    for col in range(data.shape[1]):
        file.write('{}\tCateg\n'.format(col + 1))
