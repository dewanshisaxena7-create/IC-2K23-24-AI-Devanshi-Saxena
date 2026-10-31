
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def iris_classification():
    """Classify Iris flowers using Decision Tree."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict test data
    y_pred = model.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)

    print("IRIS FLOWER CLASSIFICATION SYSTEM")
    print("---------------------------------")
    print("Model Accuracy:", accuracy)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=iris.target_names
        )
    )

    # Predict a new flower
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(sample)

    print("New Flower Prediction:")
    print(iris.target_names[prediction[0]])

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=iris.target_names
    )

    display.plot(cmap="Blues")
    plt.title("Iris Classification Confusion Matrix")
    plt.savefig("iris_confusion_matrix.png")
    plt.show()


if __name__ == "__main__":
    iris_classification()
