# Week 3: Data Foundations for Healthcare AI

## Section 1: Foundations | Learning Outcome 1

**Theme:** Garbage in, garbage out: The critical role of data in AI performance

**Core Question:** *"What is this?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Analyse how training data shapes AI system behaviour and limitations
- Evaluate the generalisability challenges of AI models across populations
- Assess data quality, provenance, and governance requirements
- Understand the particular characteristics of Australian health data

---

## Content

### 3.1 Training Data: The Foundation of AI Behaviour

**How Training Data Determines What AI Can Do**

An AI system can only learn patterns present in its training data:
- A model trained on adult data cannot reliably assess children
- A model trained on one hospital may fail at another
- A model trained on historical data embeds historical biases

**Data Labelling: The Hidden Human Labour**

"Ground truth" labels are created by humans:
- Radiologists annotating images
- Clinicians coding diagnoses
- Researchers defining outcomes

This introduces subjectivity, variability, and potential error into "objective" AI systems.

**The Problem of Historical Bias**

Healthcare AI trained on historical data learns historical patterns—including:
- Diagnostic disparities across demographic groups
- Treatment allocation biases
- Documentation patterns that vary by patient characteristics

**Data Quantity vs. Data Quality Trade-offs**

More data isn't always better:
- Large, noisy datasets vs. small, curated datasets
- Quantity needed depends on problem complexity
- Quality issues can be amplified at scale

### 3.2 Healthcare Data Characteristics

**Structured Data**

- Electronic health record fields
- Pathology results
- Vital signs
- Medication records
- Demographic information

Challenges: Missing fields, coding inconsistencies, system variations

**Unstructured Data**

- Clinical notes (free text)
- Medical imaging
- Audio recordings
- Waveform data (ECG, continuous monitoring)

Challenges: Extraction complexity, interpretation variability, storage requirements

**The Challenge of Missing Data**

Data is rarely missing at random in healthcare:
- Sicker patients may have more data (more tests ordered)
- Certain populations may have less documentation
- Absence of data may itself be informative

**Temporal Dynamics**

Healthcare data changes over time:
- Seasonal patterns in presentations
- Changes in coding practices
- New treatments altering outcomes
- Pandemic effects disrupting patterns

### 3.3 Generalisability and Australian Context

**Why US-trained Models May Fail in Australian Populations**

Most published healthcare AI is trained on US data:
- Different disease prevalence
- Different demographic composition
- Different healthcare system structures
- Different documentation practices

**Dataset Shift: When Deployment Differs from Training**

Types of shift:
- **Population shift:** Different patient characteristics
- **Temporal shift:** Patterns change over time
- **Institutional shift:** Different practices between sites

**Underrepresented Populations**

Groups often underrepresented in training data:
- Indigenous Australians
- Rural and remote populations
- Culturally and linguistically diverse communities
- Older adults
- People with disabilities

**Australian Health Datasets: What Exists and What's Missing**

Available datasets:
- AIHW national collections
- State-based linked data
- Disease registries
- Research cohorts

Gaps:
- Limited primary care data
- Fragmented across jurisdictions
- Variable quality and completeness

**Indigenous Health Data Sovereignty**

Critical considerations:
- Community control over Indigenous health data
- Principles of Indigenous data governance
- Risks of AI perpetuating colonial patterns
- Importance of Indigenous-led research

### 3.4 Data Governance Essentials

**Privacy Frameworks**

- Privacy Act 1988 and Australian Privacy Principles
- My Health Record legislation
- State and territory health records acts
- Research ethics requirements

**Consent and Secondary Use**

- Primary purpose vs. secondary use of clinical data
- Opt-in vs. opt-out models
- De-identification and re-identification risks
- Consumer expectations and trust

**Data Sharing Barriers in Federated Australian Healthcare**

- State-based data custodianship
- Incompatible systems and standards
- Risk aversion in data governance
- Lack of national health data infrastructure

---

## Aeromedical Thread

### Data Challenges Specific to Retrieval

**Sparse Pre-hospital Documentation**

- Limited information from referring centres
- Variable documentation quality
- Time pressure reducing data capture
- Verbal handovers losing detail

**Variability in Referring Centre Capabilities**

- Different IT systems (or none)
- Different pathology/imaging availability
- Rural centres with limited diagnostics
- Communication technology limitations

**Transport-Specific Physiological Patterns**

Models trained on hospital data may not apply to transport:
- Altitude effects on physiology
- Movement and vibration artefacts
- Different monitoring equipment
- Compressed clinical trajectories

**Connectivity Constraints**

- Inability to access cloud-based AI during transport
- Need for models that work with intermittent data
- Edge computing requirements

---

## Learning Activities

### Pre-Class Preparation

1. **Validation Study Analysis**
   - Read the provided AI validation study
   - Identify training population characteristics
   - Note any reported limitations related to data
   - Consider how findings might apply to your population

### In-Class Activities

1. **Case Study: AI Failures from Data Issues** (Small Groups, 30 mins)
   - Groups analyse assigned case studies of AI failures
   - Identify the data-related root causes
   - Present findings and lessons learned

2. **Data Source Mapping** (Groups, 25 mins)
   - Identify data sources in your health service that could train AI
   - Assess quality, completeness, and representativeness
   - Identify gaps that would limit AI development

3. **Generalisability Assessment** (Facilitated Discussion, 25 mins)
   - Given a US-developed AI tool, what validation would you need?
   - What population differences matter most?
   - How would you test for bias in your setting?

### Post-Class Activities

1. **Data Audit Exercise**
   - Select a clinical AI application (from provided list)
   - Document the training data characteristics (if available)
   - Assess likely generalisability to Australian healthcare
   - Identify potential bias sources

---

## Practical Exercise 3: Data Exploration and Bias Detection (Colab)

### Objective

Examine a healthcare dataset to understand how data characteristics shape AI behaviour.

### Exercise Overview

Using a synthetic (but realistic) clinical dataset, you'll explore how data quality and composition affect what an AI can learn.

### Part A: Dataset Exploration

```python
import pandas as pd
import matplotlib.pyplot as plt

ed_data = pd.read_csv('synthetic_ed_data.csv')

# Basic exploration
print("Dataset shape:", ed_data.shape)
print("\nColumn types:")
print(ed_data.dtypes)
print("\nMissing values:")
print(ed_data.isnull().sum())
```

### Part B: Demographic Analysis

```python
# Examine who is represented in this dataset
print("Age distribution:")
print(ed_data['age'].describe())

print("\nGender breakdown:")
print(ed_data['gender'].value_counts(normalize=True))

print("\nIndigenous status:")
print(ed_data['indigenous_status'].value_counts(normalize=True))

print("\nPostcode distribution (urban vs rural):")
print(ed_data['remoteness_category'].value_counts(normalize=True))
```

**Key Questions:**
- Does this dataset reflect the population you serve?
- Which groups might be underrepresented?
- What happens if an AI trained on this data is deployed elsewhere?

### Part C: Outcome Analysis by Subgroup

```python
# Check if outcomes vary by demographic group
for group in ['gender', 'indigenous_status', 'remoteness_category']:
    print(f"\n--- Outcomes by {group} ---")
    outcome_by_group = ed_data.groupby(group)['adverse_outcome'].mean()
    print(outcome_by_group)
```

### Part D: Missing Data Patterns

```python
# Missing data is rarely random
missing_analysis = ed_data.groupby('indigenous_status').apply(
    lambda x: x.isnull().mean()
)
print("Missing data rates by Indigenous status:")
print(missing_analysis[['pathology_results', 'vital_signs', 'social_history']])
```

**Discussion Points:**
- If vital signs are more often missing for certain patient groups, what might this mean?
- If an AI is trained to use vital signs for prediction, how will it handle missing data?
- What does differential documentation tell us about healthcare equity?

### Part E: Simulating Dataset Shift

```python
# Compare two time periods or locations
training_data = ed_data[ed_data['year'] < 2022]
deployment_data = ed_data[ed_data['year'] >= 2022]

print("Training data characteristics:")
print(training_data[['age', 'acuity_score']].describe())

print("\nDeployment data characteristics:")
print(deployment_data[['age', 'acuity_score']].describe())
```

### Deliverable

Complete analysis notebook with written observations on potential bias sources and data quality issues.

---

## Indicative Resources

### Required Reading

- Chen, I.Y., et al. (2021). Ethical Machine Learning in Healthcare. *Annual Review of Biomedical Data Science*, 4, 123-144.

### Recommended Reading

- Australian Institute of Health and Welfare. Data governance frameworks and resources.
- Mayi Kuwayu Study. Resources on Indigenous data sovereignty.
- Obermeyer, Z., et al. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447-453.

---

## Session Summary

This week emphasised the critical role of data in AI system performance:

1. Training data fundamentally determines what an AI can and cannot do
2. Healthcare data has unique characteristics that create AI challenges
3. Models may not generalise across populations, institutions, or time
4. Australian context requires attention to underrepresented populations
5. Data governance creates both protections and barriers

**Next Week:** We move from understanding *what AI is* to evaluating *whether we should use it*—examining safety, failure modes, and the risks of AI in clinical settings.

---

## Section 1 Formative Assessment Summary

**Weekly Learning Demonstrations:**

- **Week 1:** AI encounter reflection (ungraded, peer-shared)
- **Week 2:** Technical explanation exercise (peer feedback)
- **Week 3:** Data audit preliminary findings (tutor feedback)

**Summative Assessment 1: Technical Foundations Analysis**

Due end of Week 4. See [Assessment 1 Brief](../../assessments/assessment-1-technical-foundations/) for details.
