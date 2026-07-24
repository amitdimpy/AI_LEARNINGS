# AI LEARNINGS

AI_LEARNINGS is a hands-on machine learning repository built to help learners explore common ML algorithms, workflows, and datasets through Jupyter notebooks and practical examples.

## Repository Overview

This repository covers a broad range of machine learning concepts including:

- Regression (single and multivariate linear regression)
- Classification (Logistic Regression, KNN, Naive Bayes, Decision Trees, Random Forest, Support Vector Machines)
- Clustering (K-Means)
- Model evaluation techniques (training/testing split, K-fold cross validation)
- Feature engineering and preprocessing (one-hot encoding, outlier detection, tokenization)
- Dimensionality reduction (Principal Component Analysis)
- Model persistence and export using `joblib` and `pickle`

Most of the content is delivered as Jupyter notebooks for interactive learning, and includes supporting CSV datasets when available.

## How to Use

1. Open this repository in VS Code or your preferred Jupyter environment.
2. Install Python dependencies such as `numpy`, `pandas`, `scikit-learn`, `matplotlib`, and `seaborn` if needed.
3. Open a notebook file (`*.ipynb`) in the folder of interest.
4. Run the cells sequentially to explore data loading, preprocessing, model training, evaluation, and interpretation.

> Note: `ABOUT.md` includes an introductory overview of the repository and its learning objectives.

## Folder Structure and Contents

### Root Files
- `ABOUT.md` — Repository purpose and learning objectives.
- `README.md` — This file.
- `Print_uppercase_letters_from_text.py` — A simple Python script demonstrating text processing.

### Decision Tree
- `decision_tree.ipynb` — Decision tree implementation and analysis.
- `salaries.csv` — Example dataset used to train and evaluate the decision tree.

### Embeddings
- `Embeddings.ipynb` — Notebook exploring embedding techniques for text or feature representation.

### Hyperparameter Tuning
- `Hyperparameter_tuning.ipynb` — Examples of tuning model hyperparameters to improve performance.

### K-fold Cross Validation
- `K_fold_cross_validation.ipynb` — Demonstrates K-fold cross validation for model validation and stability.

### K-Means Clustering
- `K-means_clustering.ipynb` — K-Means clustering example for unsupervised data segmentation.

### KNN Classifier
- `KNN_Classification_iris_dataset.ipynb` — K-Nearest Neighbors classification on the Iris dataset.
- `KNN_digit_dataset.ipynb` — KNN classification example for digit recognition.

### Linear Regression

#### `Linear Regression/singlevariate`
- `Linear_Regression.ipynb` — Single-variable linear regression with basic prediction examples.
- `area_price.csv` — Dataset for simple regression.
- `predict_price.csv`, `predict_price_new.csv`, `predict_area_price.csv`, `predict_area_price_new.csv` — Dataset files used for prediction exercises.

#### `Linear Regression/multivariate`
- `Multivariate_LinearRegression_Hiring_Eg.ipynb` — Multivariate regression example using hiring data.
- `Mutlivariate_Linear_Regression.ipynb` — Another multivariate regression notebook.
- `hiring.csv`, `hiring_ML.csv` — Hiring dataset files.
- `houseprice.csv`, `houseprice_ohe.csv` — House price datasets, including one-hot encoded data.
- `multi_area_price.csv`, `multi_area_price_ML.csv` — Multi-feature house pricing examples.

#### `Linear Regression/one-hot-encoding`
- `multivar_houseprice.ipynb` — One-hot encoding applied to a housing dataset.
- `one_hot_encoding.py.ipynb` — Demonstrates one-hot encoding within regression workflows.

#### `Linear Regression/save_model_file`
- `Save_to_file_model.ipynb` — Shows how to save and load trained models using `joblib` and `pickle`.
- `model_joblib/` — Directory likely containing saved joblib model artifacts.
- `model_pickle/` — Directory likely containing saved pickle model artifacts.

#### `Linear Regression/training-testing`
- `training-testing.ipynb` — Training/test split techniques for model evaluation.
- `carprices.csv` — Automobile pricing dataset used in the notebook.

### Logistic Regression
- `Binary Classification/binary_classification.ipynb` — Logistic regression binary classification example.
- `Binary Classification/insurance.csv` — Dataset used for logistic regression modeling.

### Naive Bayes
- `Naive_Bayes_I.ipynb` — First Naive Bayes classification example.
- `Naive_Bayes_II.ipynb` — Second Naive Bayes example.
- `NaiveBayes.md` — Reference notes and explanations for Naive Bayes.

### Outlier Detection
- `Outlier_IQR/Outlier_IQR.ipynb` — Interquartile range outlier detection.
- `Outlier_IQR/weight-height.csv` — Sample dataset for IQR analysis.
- `Outlier_Percentile/Outlier_Percentile_housingdata.ipynb` — Percentile-based outlier detection for housing data.
- `Outlier_Percentile/Outlier_Percentile_creditcard.ipynb` — Credit card outlier detection example.
- `Outlier_zscore_std_deviation/Outlier_Zscore_std_deviation.ipynb` — Outlier detection using Z-score and standard deviation.

### Principal Component Analysis
- `Principal Component Analysis/Principal Component Analysis.ipynb` — PCA for dimensionality reduction and feature exploration.
- `Principal Component Analysis/converted_heart_dataset.csv` — Processed heart disease dataset used in PCA.
- `Principal Component Analysis/raw_merged_heart_dataset.csv` — Raw heart dataset before conversion.

### Random Forest
- `random_forest.ipynb` — Random Forest classification or regression example.

### Support Vector Method
- `support_vector_method.ipynb` — Support Vector Machine implementation and evaluation.

### Tokenization
- `Tokenization/Tokenization.ipynb` — Text tokenization and preprocessing experiments.

## Notes

- The notebooks are ideal for learners who want to step through ML concepts interactively.
- Datasets are included at the folder level and are ready to use with the notebooks.
- Keep Python packages up to date for compatibility with scikit-learn notebook code.

## Recommended Setup

1. Install Python 3.10+.
2. Create a virtual environment.
3. Install common ML dependencies:

```bash
python -m pip install numpy pandas scikit-learn matplotlib seaborn notebook jupyterlab
```

4. Launch Jupyter or open notebooks in VS Code.

---

If you want to extend the repository, consider adding README sections for individual notebooks or updating sample datasets with newer examples.
