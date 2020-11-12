import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    evidance = list()
    labels = list()
    row = list()

    with open(filename) as file:
        for j, item in enumerate(file):
            if(j == 0):
                continue
            row = []
            for i, el in enumerate(item.split(',')):
                # print(el)
                if(i in {0,2,4,11,12,13,14}):
                    row.append(int(el))
                elif(i in {1,3,5,6,7,8,9}):
                    row.append(float(el))
                elif(i==10):
                    if(el == "Jan"):
                        row.append(int(0))
                    elif(el == "Feb"):    
                        row.append(int(1))
                    elif(el == "Mar"):    
                        row.append(int(2))
                    elif(el == "Apr"):    
                        row.append(int(3))
                    elif(el == "May"):    
                        row.append(int(4))
                    elif(el == "June"):    
                        row.append(int(5))
                    elif(el == "Jul"):    
                        row.append(int(6))
                    elif(el == "Aug"):    
                        row.append(int(7))
                    elif(el == "Sep"):    
                        row.append(int(8))
                    elif(el == "Oct"):    
                        row.append(int(9))
                    elif(el == "Nov"):    
                        row.append(int(10))
                    elif(el == "Dec"):    
                        row.append(int(11))
                    else:
                        print("wrong month Exit")
                        quit()
                elif(i==15):
                    if(el == 'Returning_Visitor'):
                        row.append(int(1))
                    else:
                        row.append(int(0))
                elif(i==16):
                    if(el == 'TRUE'):
                        row.append(int(1))
                    else:
                        row.append(int(0))  
                elif(i==17):
                    if(el == 'TRUE\n' or el == 'TRUE'):
                        row.append(int(1))
                    else:
                        row.append(int(0))
                else:
                    print("Incorrect value")

            evidance.append(row)
            # print(item.split(',')[-1])
            if(item.split(',')[-1] == 'FALSE\n'):
                labels.append(0)
            else:
                labels.append(1)

            # print(labels)
    return (evidance, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)

    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    truePositiveCounter = 0
    trueNegativeCounter = 0
    truePositiveCorrect = 0
    trueNegativeCorrect = 0
    
    sensitivity = 0
    specificity = 0

    for i in range(len(labels)):
        if labels[i] == 1:
            truePositiveCounter += 1
            if(labels[i] == predictions[i]):
                truePositiveCorrect += 1
        elif labels[i] == 0:
            trueNegativeCounter += 1
            if(labels[i] == predictions[i]):
                trueNegativeCorrect += 1

    sensitivity = truePositiveCorrect / truePositiveCounter
    specificity = trueNegativeCorrect / trueNegativeCounter

    return sensitivity, specificity

if __name__ == "__main__":
    main()
