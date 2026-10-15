# AI LEARNINGS

A practical and beginner-friendly repository for learning Machine Learning and Deep Learning through Jupyter notebooks, guided examples, and hands-on exercises.

This collection is designed to help learners understand core AI concepts by working directly with code, datasets, and real examples rather than only reading theory.

## Repository Goals

- Learn the fundamentals of machine learning algorithms and workflows
- Explore deep learning concepts with TensorFlow-based notebooks
- Practice with real datasets and interactive experimentation
- Build confidence through step-by-step examples in Jupyter notebooks

## What is Included

### Machine Learning
The `Machine_Learning/` section contains notebooks and examples covering:

- Regression
  - Linear Regression
  - Multivariate Regression
  - One-hot encoding for categorical data
  - Training and testing split strategies
  - Model saving and loading
- Classification
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Naive Bayes
  - Decision Tree
  - Random Forest
  - Support Vector Method
- Clustering
  - K-Means Clustering
- Feature engineering and preprocessing
  - Tokenization
  - Outlier detection (IQR, Percentile, Z-score)
  - Encoding and data preparation
- Dimensionality reduction
  - Principal Component Analysis (PCA)
- Model evaluation and tuning
  - K-fold Cross Validation
  - Hyperparameter Tuning
- Embeddings and representation learning

### Deep Learning
The `Deep_Learning/` folder includes foundational deep learning notebooks such as:

- `Loss_cost_function.ipynb` — Understand loss functions and cost computation
- `Matrix_Multiplication.ipynb` — Learn matrix operations used in neural networks
- `MNIST_Dataset_TF.ipynb` — Build and train a TensorFlow model on the MNIST dataset
- `Penguin_Dataset_TF.ipynb` — Explore TensorFlow classification using the penguin dataset

## Folder Structure

```text
AI_LEARNINGS/
├── README.md
├── Machine_Learning/
│   ├── Decision Tree/
│   ├── Embeddings/
│   ├── Hyperparameter Tuning/
│   ├── K-fold Cross Validation/
│   ├── K-Means Clustering/
│   ├── KNN Classifier/
│   ├── Linear Regression/
│   ├── Logistic Regression/
│   ├── Naive Bayes/
│   ├── Outlier_IQR/
│   ├── Outlier_Percentile/
│   ├── Outlier_zscore_std_deviation/
│   ├── Principal Component Analysis/
│   ├── Random Forest/
│   ├── Support Vector Method/
│   ├── Tokenization/
│   └── Print_uppercase_letters_from_text.py
├── Deep_Learning/
│   ├── Loss_cost_function.ipynb
│   ├── Matrix_Multiplication.ipynb
│   ├── MNIST_Dataset_TF.ipynb
│   └── Penguin_Dataset_TF.ipynb
└── Data/
    └── ...sample datasets and learning resources
```

## How to Use This Repository

1. Clone or download the repository.
2. Open the folder in VS Code, Jupyter Notebook, or JupyterLab.
3. Select a topic based on your learning goal.
4. Open the relevant notebook and run cells in sequence.
5. Explore the code, modify parameters, and experiment with your own data.

## Recommended Learning Path

### Beginner
- `Machine_Learning/Linear Regression/`
- `Machine_Learning/Logistic Regression/`
- `Machine_Learning/KNN Classifier/`

### Intermediate
- `Machine_Learning/Random Forest/`
- `Machine_Learning/Principal Component Analysis/`
- `Machine_Learning/Outlier_IQR/`
- `Machine_Learning/K-fold Cross Validation/`

### Deep Learning
- `Deep_Learning/Matrix_Multiplication.ipynb`
- `Deep_Learning/Loss_cost_function.ipynb`
- `Deep_Learning/Penguin_Dataset_TF.ipynb`
- `Deep_Learning/MNIST_Dataset_TF.ipynb`

## Environment Setup

Python 3.10+ is recommended.

Create a virtual environment and install the required libraries:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib seaborn scikit-learn notebook jupyterlab
```

For deep learning examples, install TensorFlow as well:

```bash
python -m pip install tensorflow
```

## Tools and Platform

These notebooks are intended to be used with:

- VS Code
- Jupyter Notebook
- JupyterLab
- Python environments with notebooks enabled

## Notes

- This repository is suitable for self-learning and practical experimentation.
- Learners are encouraged to modify examples and try different parameters.
- Some notebooks may depend on additional packages or datasets that are included in the project structure.

## Who Can Use This Repository?

This repository is useful for:

- Students learning AI and ML fundamentals
- Beginners exploring Python-based data science workflows
- Developers who want practical implementation examples
- Anyone looking to build a strong foundation in machine learning and deep learning

## License

This repository is for learning and educational purposes. Please check the repository licensing details before reusing or distributing it publicly.

---

If you want to build further on this repository, you can add:

- individual notebook descriptions
- dataset links and source references
- practice exercises and assignments
- project-based case studies
- a topic-wise roadmap for learners
