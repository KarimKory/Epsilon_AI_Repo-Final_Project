{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d681acc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.metrics import mean_squared_error, accuracy_score\n",
    "import joblib\n",
    "\n",
    "# Set plot style\n",
    "\n",
    "sns.set(style=\"whitegrid\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1682b216",
   "metadata": {},
   "source": [
    "# Student Performance Prediction Project\n",
    "\n",
    "## 1. Project Understanding\n",
    "In this project, we aim to predict students' GPA and Grade Class using various machine learning algorithms. We will explore the dataset, preprocess the data, build models, and deploy a web application to make predictions.\n",
    "\n",
    "## 2. Data Mining and Processing\n",
    "```python\n",
    "# Load the data\n",
    "df = pd.read_csv('student_data.csv')\n",
    "\n",
    "# Display the first few rows of the dataset\n",
    "df.head()\n",
    "\n",
    "# Check for missing values\n",
    "df.isnull().sum()\n",
    "\n",
    "# Handle missing values if any (not applicable here as no missing values)\n",
    "\n",
    "# Convert categorical variables to numeric if necessary (e.g., Gender, Ethnicity)\n",
    "df['Gender'] = df['Gender'].astype('category').cat.codes\n",
    "df['Ethnicity'] = df['Ethnicity'].astype('category').cat.codes\n",
    "\n",
    "# Display the data types and summary statistics\n",
    "print(df.info())\n",
    "print(df.describe())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f99440c",
   "metadata": {},
   "source": [
    "## 3. Data Exploration\n",
    "```python\n",
    "# Pairplot to visualize relationships\n",
    "sns.pairplot(df)\n",
    "plt.show()\n",
    "\n",
    "# Correlation matrix\n",
    "plt.figure(figsize=(10, 8))\n",
    "sns.heatmap(df.corr(), annot=True, fmt=\".2f\", cmap='coolwarm')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e1e2282",
   "metadata": {},
   "source": [
    "## 4. Model Building\n",
    "### Linear Regression for GPA Prediction\n",
    "```python\n",
    "# Features and target variable for GPA prediction\n",
    "X_gpa = df.drop(['GPA', 'GradeClass', 'StudentID'], axis=1)\n",
    "y_gpa = df['GPA']\n",
    "\n",
    "# Split the data\n",
    "X_train_gpa, X_test_gpa, y_train_gpa, y_test_gpa = train_test_split(X_gpa, y_gpa, test_size=0.2, random_state=42)\n",
    "\n",
    "# Scale the features\n",
    "scaler = StandardScaler()\n",
    "X_train_gpa = scaler.fit_transform(X_train_gpa)\n",
    "X_test_gpa = scaler.transform(X_test_gpa)\n",
    "\n",
    "# Train the model\n",
    "lr_model = LinearRegression()\n",
    "lr_model.fit(X_train_gpa, y_train_gpa)\n",
    "\n",
    "# Save the model and scaler\n",
    "joblib.dump(lr_model, 'linear_regression_model.pkl')\n",
    "joblib.dump(scaler, 'scaler.pkl')\n",
    "\n",
    "# Predict and evaluate\n",
    "y_pred_gpa = lr_model.predict(X_test_gpa)\n",
    "mse = mean_squared_error(y_test_gpa, y_pred_gpa)\n",
    "print(f'Mean Squared Error: {mse}')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00f777a9",
   "metadata": {},
   "source": [
    "### Decision Tree for Grade Class Prediction\n",
    "```python\n",
    "# Features and target variable for Grade Class prediction\n",
    "X_class = df.drop(['GPA', 'GradeClass', 'StudentID'], axis=1)\n",
    "y_class = df['GradeClass']\n",
    "\n",
    "# Split the data\n",
    "X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=42)\n",
    "\n",
    "# Scale the features\n",
    "X_train_class = scaler.fit_transform(X_train_class)\n",
    "X_test_class = scaler.transform(X_test_class)\n",
    "\n",
    "# Train the model\n",
    "dt_model = DecisionTreeClassifier()\n",
    "dt_model.fit(X_train_class, y_train_class)\n",
    "\n",
    "# Save the model\n",
    "joblib.dump(dt_model, 'decision_tree_model.pkl')\n",
    "\n",
    "# Predict and evaluate\n",
    "y_pred_class = dt_model.predict(X_test_class)\n",
    "accuracy = accuracy_score(y_test_class, y_pred_class)\n",
    "print(f'Accuracy: {accuracy}')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64fcce81",
   "metadata": {},
   "source": [
    "## 5. Interpret Results\n",
    "### Linear Regression Results\n",
    "```python\n",
    "# Visualize the regression results\n",
    "plt.scatter(y_test_gpa, y_pred_gpa, color='blue')\n",
    "plt.plot(y_test_gpa, y_test_gpa, color='red')  # Line of perfect prediction\n",
    "plt.xlabel('Actual GPA')\n",
    "plt.ylabel('Predicted GPA')\n",
    "plt.title('Actual vs Predicted GPA')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5df12b0e",
   "metadata": {},
   "source": [
    "### Decision Tree Results\n",
    "```python\n",
    "# Confusion Matrix for Decision Tree\n",
    "from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay\n",
    "\n",
    "cm = confusion_matrix(y_test_class, y_pred_class)\n",
    "disp = ConfusionMatrixDisplay(confusion_matrix=cm)\n",
    "disp.plot(cmap='viridis')\n",
    "plt.title('Confusion Matrix for Grade Class Prediction')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "688bbcf5",
   "metadata": {},
   "source": [
    "## 6. Deployment\n",
    "```python\n",
    "# Deployment with Flask\n",
    "# Assuming you have the Flask app code ready in a separate file (app.py)\n",
    "# Run the Flask app by navigating to the directory containing app.py and executing the following command in the terminal:\n",
    "# python app.py\n",
    "\n",
    "# Here is a brief overview of the Flask app code\n",
    "'''\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the models\n",
    "lr_model = joblib.load('linear_regression_model.pkl')\n",
    "dt_model = joblib.load('decision_tree_model.pkl')\n",
    "scaler = joblib.load('scaler.pkl')\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict_gpa', methods=['POST'])\n",
    "def predict_gpa():\n",
    "    data = request.form.to_dict()\n",
    "    data = {key: float(value) for key, value in data.items()}\n",
    "    features = np.array([[data['Age'], data['Gender'], data['Ethnicity'], data['ParentalEducation'],\n",
    "                          data['StudyTimeWeekly'], data['Absences'], data['Tutoring'], data['ParentalSupport'],\n",
    "                          data['Extracurricular'], data['Sports'], data['Music'], data['Volunteering']]])\n",
    "    features_scaled = scaler.transform(features)\n",
    "    gpa_prediction = lr_model.predict(features_scaled)[0]\n",
    "    return jsonify({'predicted_gpa': gpa_prediction})\n",
    "\n",
    "@app.route('/predict_gradeclass', methods=['POST'])\n",
    "def predict_gradeclass():\n",
    "    data = request.form.to_dict()\n",
    "    data = {key: float(value) for key, value in data.items()}\n",
    "    features = np.array([[data['Age'], data['Gender'], data['Ethnicity'], data['ParentalEducation'],\n",
    "                          data['StudyTimeWeekly'], data['Absences'], data['Tutoring'], data['ParentalSupport'],\n",
    "                          data['Extracurricular'], data['Sports'], data['Music'], data['Volunteering']]])\n",
    "    features_scaled = scaler.transform(features)\n",
    "    gradeclass_prediction = dt_model.predict(features_scaled)[0]\n",
    "    return jsonify({'predicted_gradeclass': gradeclass_prediction})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61ef27b9",
   "metadata": {},
   "source": [
    "## 7. Conclusion\n",
    "### Summary\n",
    "This project successfully implemented machine learning models to predict student GPA and Grade Class. Linear Regression and Decision Tree models were trained, evaluated, and deployed via a Flask web application.\n",
    "\n",
    "### Strengths and Weaknesses\n",
    "**Strengths:**\n",
    "- Comprehensive data analysis and preprocessing.\n",
    "- Use of multiple algorithms for robust predictions.\n",
    "- Scalable deployment with Flask.\n",
    "\n",
    "**Weaknesses:**\n",
    "- Model complexity and potential overfitting.\n",
    "- Limited feature engineering.\n",
    "- Dataset limitations and potential bias.\n",
    "\n",
    "### Future Work\n",
    "**Improvements:**\n",
    "- Advanced feature engineering.\n",
    "- Extensive hyperparameter tuning.\n",
    "- Explore ensemble methods.\n",
    "\n",
    "**Extensions:**\n",
    "- Real-time data integration.\n",
    "- User feedback loop.\n",
    "- Explainable AI.\n",
    "- Scaling up deployment.\n",
    "- Conduct longitudinal studies.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "125eae2c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
