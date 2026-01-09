from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from td_idf_model import X_train, y_train, y_test, X_test, label_encoder

model = LogisticRegression(max_iter=1000)

#training
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy= accuracy_score(y_test, y_pred)
print(f"\n Global accuracy: {accuracy:.2f} ({accuracy*100:.1f})")

#confusion matrix
target_names = label_encoder.classes_

confusion_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix, annot= True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
plt.ylabel("True category")
plt.xlabel("Predicted category")
plt.title("Confusion Matrix")
plt.show()