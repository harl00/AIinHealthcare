# Week 2: AI Architecture and Algorithms

## Section 1: Foundations | Learning Outcome 1

**Theme:** Under the hood: How healthcare AI systems actually work

**Core Question:** *"What is this?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Explain the fundamental architecture of machine learning systems
- Differentiate between supervised, unsupervised, and reinforcement learning
- Describe how neural networks process healthcare data
- Understand the basics of large language models and their healthcare applications

---

## Content

### 2.1 Machine Learning Fundamentals

**The Learning Paradigm**

Unlike traditional software (where programmers write explicit rules), machine learning systems learn patterns from data:

1. **Training:** The system is exposed to many examples with known outcomes
2. **Validation:** Performance is tested on held-out data during development
3. **Testing:** Final evaluation on completely unseen data
4. **Deployment:** Application to new, real-world cases

**Supervised Learning**

The system learns from labelled examples—inputs paired with correct outputs.

*Classification:* Predicting categories
- Is this lesion malignant or benign?
- Which patients will develop sepsis?
- What diagnosis does this presentation suggest?

*Regression:* Predicting continuous values
- What is this patient's risk score (0-100)?
- How long will this patient stay in hospital?
- What is the predicted blood glucose in 2 hours?

**Unsupervised Learning**

The system finds patterns in unlabelled data.

*Clustering:* Grouping similar cases
- Patient phenotyping (identifying natural subgroups)
- Disease subtype discovery
- Healthcare utilisation patterns

*Dimensionality reduction:* Simplifying complex data
- Visualising high-dimensional patient data
- Feature extraction from images or signals

*Anomaly detection:* Identifying outliers
- Unusual lab patterns suggesting error or rare conditions
- Fraud detection in claims data

**Reinforcement Learning**

The system learns through trial and error, receiving rewards for good outcomes.

- Treatment optimisation (adjusting therapy based on response)
- Resource allocation (learning efficient scheduling)
- Less common in clinical practice due to safety concerns

### 2.2 Neural Networks and Deep Learning

**From Perceptrons to Deep Networks**

Neural networks are inspired by (but don't truly replicate) biological neurons:
- **Input layer:** Receives data (vital signs, pixel values, text)
- **Hidden layers:** Transform and combine information
- **Output layer:** Produces predictions

"Deep learning" simply means neural networks with many hidden layers, enabling them to learn complex patterns.

**Convolutional Neural Networks (CNNs) for Medical Imaging**

Specialised architecture for image analysis:
- Automatically learns visual features (edges, textures, shapes)
- Hierarchical learning: simple features → complex patterns
- Applications: radiology, pathology, dermatology, ophthalmology

**Recurrent Networks and Transformers for Sequential Data**

For data with temporal or sequential structure:
- Vital sign trends over time
- Clinical note sequences
- Patient trajectories

**The "Black Box" Problem**

Deep learning models are notoriously difficult to interpret:
- Millions of parameters with no clear meaning
- Cannot easily explain *why* a prediction was made
- Tension between predictive power and transparency
- Implications for clinical trust and accountability

### 2.3 Large Language Models in Healthcare

**How LLMs Work**

Large Language Models (like GPT-4, Claude, Med-PaLM) are a specific type of neural network trained on vast text data:

1. **Tokenisation:** Text is broken into units (words or word-pieces)
2. **Attention:** The model learns which parts of the input relate to each other
3. **Generation:** Produces output one token at a time, predicting what comes next

**Clinical Applications**

- Documentation assistance and summarisation
- Clinical question answering
- Differential diagnosis brainstorming
- Patient communication drafting
- Literature synthesis

**Critical Limitations**

- **Hallucination:** Generating plausible but false information
- **Training data biases:** Reflecting biases in source material
- **Lack of grounding:** No connection to real-time patient data or truth
- **Overconfidence:** Presenting uncertain information with confidence
- **Knowledge cutoffs:** Training data has a fixed endpoint

**Current Landscape**

- General models (GPT-4, Claude) with medical capability
- Medically fine-tuned models (Med-PaLM, various clinical LLMs)
- Integrated clinical systems with LLM components
- Rapidly evolving—anything written today may be outdated soon

---

## Aeromedical Thread

### Architecture Choices for Retrieval Challenges

Different AI architectures suit different retrieval medicine applications:

| Challenge | Suitable Architecture | Example |
|-----------|----------------------|---------|
| Point-of-care ultrasound interpretation | CNN (image classification) | "Is there pericardial effusion?" |
| In-flight deterioration prediction | Recurrent/time-series models | Early warning from continuous monitoring |
| Handover documentation | LLM (text generation) | Structured summary from raw notes |
| Triage prioritisation | Classification models | Dispatch urgency scoring |
| Resource allocation | Reinforcement learning or optimisation | Which asset for which case? |

**Connectivity Considerations**

- Which models can run locally (edge computing) vs. require cloud connectivity?
- Latency requirements for real-time applications
- Graceful degradation when connectivity fails

---

## Learning Activities

### Pre-Class Preparation

1. **Interactive ML Module**
   - Complete the provided online module on ML fundamentals (approx. 45 mins)
   - Take notes on concepts you find confusing

2. **LLM Experimentation**
   - Using a public LLM (ChatGPT, Claude, etc.), test it with clinical scenarios
   - Document what it does well and where it fails

### In-Class Activities

1. **Neural Network Walkthrough** (Facilitated, 30 mins)
   - Interactive visualisation of a simple neural network
   - Trace how inputs become outputs
   - Adjust parameters and observe changes

2. **Architecture Matching Exercise** (Small Groups, 20 mins)
   - Groups receive clinical problems
   - Task: Identify which AI architecture would be appropriate and why
   - Present reasoning to class

3. **LLM Behaviour Exploration** (Hands-on, 30 mins)
   - Structured prompts to test LLM capabilities and limitations
   - Compare responses across different prompt formulations
   - Identify patterns in errors and hallucinations

### Post-Class Activities

1. **Technical Summary Exercise**
   - Choose one AI architecture covered this week
   - Write an explanation (500 words) suitable for a clinical colleague
   - Peer review in pairs before next session

---

## Practical Exercise 2: ML Fundamentals Hands-on (Colab)

**📓 [Open Exercise 2 Notebook](../../practicals/colab-notebooks/02-ml-fundamentals.ipynb)**

--8<-- "practicals/_colab-instructions.md"

### Objective

Train a simple classifier to understand the ML process from data to prediction.

### Exercise Overview

This exercise demystifies machine learning by having you train a model yourself using a simplified clinical dataset.

### Part A: Preparing the Data

```python
# You'll work with a dataset of patient observations
# Goal: Predict which patients will deteriorate within 24 hours
# Features: vital signs, lab values, demographics
# Label: deteriorated (yes/no)

import pandas as pd
data = pd.read_csv('sample_deterioration_data.csv')

print(data.head())
print(f"Dataset has {len(data)} patients")
print(f"Deterioration rate: {data['deteriorated'].mean():.1%}")
```

### Part B: Training Your First Model

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Split data into training and testing sets
# This is crucial—we test on data the model hasn't seen
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Train a simple decision tree classifier
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# See how well it performs
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.1%}")
```

### Part C: Understanding Model Behaviour

- Examine which features the model considers important
- Visualise the decision tree to see the "reasoning"
- Test what happens when you change training parameters
- Observe how performance changes with different train/test splits

### Part D: Experimentation Tasks

Modify the notebook to explore:

1. What happens if you train on only 50 patients vs. 500?
2. What if the training data has a different deterioration rate than reality?
3. What if you remove vital signs and only use demographics?

### Key Learning Points

- ML models learn patterns from training data—they can't know what they weren't shown
- Test performance may not match training performance (overfitting)
- The features you include determine what the model can learn
- Random variation affects results—the same data can produce different models

### Deliverable

Complete the guided notebook; answer embedded reflection questions.

---

## Indicative Resources

### Required Reading

- Rajkomar, A., Dean, J., & Kohane, I. (2019). Machine Learning in Medicine. *New England Journal of Medicine*, 380(14), 1347-1358.

### Recommended Reading

- Google's Machine Learning Crash Course: Selected modules on supervised learning and neural networks
- Anthropic. Claude documentation on model capabilities and limitations.

### Interactive Resources

- TensorFlow Playground: [playground.tensorflow.org](https://playground.tensorflow.org)
- CNN Explainer: Visual tool for understanding convolutional neural networks

---

## Session Summary

This week provided technical foundations for understanding how AI systems work:

1. Machine learning systems learn patterns from data through training
2. Supervised, unsupervised, and reinforcement learning address different problems
3. Neural networks power modern AI, with architectures specialised for different data types
4. Large language models represent a step-change in AI capabilities—and new risks
5. The "black box" problem creates tension between performance and explainability

**Next Week:** We'll examine the *data* that powers AI systems—how it shapes behaviour, creates biases, and determines whether systems generalise to new contexts.
