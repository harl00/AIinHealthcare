# Week 5: Ethics and Regulatory Landscape

## Section 2: Evaluation | Learning Outcome 2

**Theme:** Governance frameworks: Navigating ethics, law, and regulation

**Core Question:** *"Should we use it?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Apply ethical frameworks to healthcare AI deployment decisions
- Navigate the Australian regulatory environment for AI medical devices
- Analyse medico-legal implications of AI-assisted clinical decisions
- Evaluate organisational ethical obligations in AI adoption

---

## Content

### 5.1 Ethical Frameworks for Healthcare AI

**Bioethical Principles Applied to AI**

*Autonomy*
- Informed consent for AI-assisted care
- Patient right to refuse AI involvement
- Transparency about AI's role in their care
- Respect for patient preferences

*Beneficence*
- AI should provide genuine benefit
- Evidence of improved outcomes
- Appropriate clinical applications
- Avoiding AI for AI's sake

*Non-maleficence*
- Do no harm through AI
- Understanding and mitigating risks
- Avoiding premature deployment
- Monitoring for harm after deployment

*Justice*
- Equitable access to AI benefits
- Fair distribution of AI risks
- Avoiding exacerbation of disparities
- Representation in AI development

**The Transparency Imperative**

Explainability and interpretability:
- Can the AI's reasoning be understood?
- Can decisions be explained to patients?
- Can clinicians critically evaluate recommendations?

Levels of transparency:
- Algorithm transparency (how it works)
- Training data transparency (what it learned from)
- Decision transparency (why this specific output)

**Consent and AI**

What should patients know?
- That AI is being used
- What the AI does
- How it influences their care
- Limitations and uncertainties
- Their right to opt out

**Justice Considerations**

- Who benefits from healthcare AI?
- Who bears the risks?
- Is access equitable?
- Are harms distributed fairly?

### 5.2 Australian Regulatory Framework

**TGA Regulation of Software as a Medical Device (SaMD)**

The Therapeutic Goods Administration regulates AI as medical devices when they:
- Are intended for therapeutic use
- Meet the definition of a medical device
- Are supplied in Australia

**Risk Classification for AI Medical Devices**

| Class | Risk Level | Examples |
|-------|------------|----------|
| I | Low | General wellness apps |
| IIa | Low-medium | Clinical decision support (non-diagnostic) |
| IIb | Medium-high | Diagnostic AI, treatment recommendations |
| III | High | AI directly controlling treatment delivery |

**Regulatory Requirements by Class**

- Evidence requirements scale with risk
- Clinical evidence expectations
- Post-market surveillance obligations
- Quality management systems

**The Evolving Regulatory Landscape**

- TGA SaMD guidance updates
- International harmonisation efforts
- Adaptive/continuous learning AI challenges
- Emerging regulatory approaches

**Post-Market Surveillance**

- Ongoing performance monitoring requirements
- Adverse event reporting
- Responsibilities of sponsors vs. users

### 5.3 Professional and Legal Considerations

**AHPRA and Professional Obligations**

- Medical Board Code of Conduct implications
- Scope of practice considerations
- Competency requirements for AI-augmented practice
- Continuing professional development

**Medical Board Guidelines**

- Technology in practice guidelines
- Telehealth guidelines (relevant principles)
- Expectations for clinical judgement
- Documentation requirements

**Medico-legal Liability**

Current uncertainty includes:
- Standard of care when AI is available
- Liability for following vs. overriding AI
- Disclosure obligations
- Duty to use AI if beneficial?

Emerging principles:
- Clinician remains responsible for clinical decisions
- AI is a tool, not a decision-maker
- Documentation of AI use and reasoning
- Informed consent requirements

**Documentation Requirements**

When AI informs decisions:
- Record that AI was used
- Document the AI recommendation
- Record your clinical reasoning
- Note any discordance and resolution

**Indemnity and Insurance**

- Medical indemnity coverage for AI-assisted practice
- Institutional coverage considerations
- Gaps in current insurance frameworks

### 5.4 Organisational Ethics

**Health Service Obligations**

- Due diligence in AI procurement
- Governance structures for AI oversight
- Staff training and competency
- Incident reporting systems
- Patient communication about AI use

**Equity of Access**

- Ensuring AI doesn't widen disparities
- Rural and remote considerations
- Affordability and funding
- Digital literacy requirements

**Workforce Implications**

- Managing disruption ethically
- Consultation with affected staff
- Training and reskilling
- Appropriate use of AI-enabled efficiency gains

**Vendor Relationships**

- Conflicts of interest
- Intellectual property considerations
- Dependency and lock-in risks
- Vendor accountability for performance

---

## Aeromedical Thread

### Cross-Jurisdictional Regulatory Complexity

**Multi-jurisdictional Operations**

Aeromedical services often operate across boundaries:
- State/territory health regulations
- Multiple employer relationships
- Different hospital systems
- Interstate retrievals

**Aviation Regulatory Overlay**

CASA requirements intersect with health regulation:
- Electronic devices in aircraft
- Connectivity and communication systems
- Crew workload considerations
- Fatigue management implications

**The Particular Medico-legal Context**

Remote and autonomous practice considerations:
- Extended scope of practice
- Limited supervision
- Time-critical decision-making
- Documentation challenges during transport

---

## Learning Activities

### Pre-Class Preparation

1. **Regulatory Review**
   - Read the TGA SaMD guidance document (key sections indicated)
   - Note classification criteria and evidence requirements

2. **Ethics Framework Analysis**
   - Review one published AI ethics framework
   - Identify how it addresses the four bioethical principles

### In-Class Activities

1. **Ethical Case Analysis** (Small Groups, 30 mins)
   - Groups receive AI deployment scenarios with ethical tensions
   - Apply ethical frameworks to analyse the dilemma
   - Present recommendations with reasoning

2. **Mock Governance Committee** (Role play, 40 mins)
   - Simulate a governance committee deliberation on AI procurement
   - Roles: clinicians, executives, IT, legal, consumer representative
   - Reach a decision with conditions

3. **Regulatory Pathway Mapping** (Individual, 15 mins)
   - Select an AI application
   - Map the regulatory pathway it would require in Australia
   - Identify evidence requirements

### Post-Class Activities

1. **Regulatory Pathway Map**
   - Complete detailed regulatory pathway for a selected AI application
   - Peer review before next session

---

## Practical Exercise 5: Measuring Algorithmic Fairness (Colab)

### Objective

Apply fairness metrics to evaluate AI model performance across demographic groups.

### Exercise Overview

Building on Week 3's data exploration, you'll train a model and systematically evaluate whether it performs equitably across different patient populations.

### Part A: Train a Clinical Prediction Model

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Prepare features and labels
features = ed_data[['age', 'vital_signs_composite', 'acuity_score', 'comorbidity_count']]
labels = ed_data['adverse_outcome']

# Train model
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Generate predictions
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]
```

### Part B: Overall Performance Metrics

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

print("=== Overall Model Performance ===")
print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
print(f"Precision: {precision_score(y_test, predictions):.3f}")
print(f"Recall (Sensitivity): {recall_score(y_test, predictions):.3f}")
print(f"AUC-ROC: {roc_auc_score(y_test, probabilities):.3f}")
```

### Part C: Stratified Performance Analysis

```python
def performance_by_group(test_data, predictions, probabilities, group_column):
    """Calculate performance metrics for each subgroup"""
    results = []
    for group_value in test_data[group_column].unique():
        mask = test_data[group_column] == group_value
        group_results = {
            'group': group_value,
            'n': mask.sum(),
            'accuracy': accuracy_score(y_test[mask], predictions[mask]),
            'recall': recall_score(y_test[mask], predictions[mask]),
            'auc': roc_auc_score(y_test[mask], probabilities[mask]) if mask.sum() > 10 else None
        }
        results.append(group_results)
    return pd.DataFrame(results)

# Analyse by Indigenous status
print("\n=== Performance by Indigenous Status ===")
print(performance_by_group(test_data, predictions, probabilities, 'indigenous_status'))
```

### Part D: Fairness Metrics

```python
# Common fairness metrics

# 1. Demographic Parity: Equal positive prediction rates?
positive_rate_by_group = test_data.groupby('indigenous_status').apply(
    lambda x: predictions[x.index].mean()
)
print("Positive prediction rate by group:", positive_rate_by_group)

# 2. Equalised Odds: Equal TPR and FPR across groups?
# 3. Calibration: Equal accuracy of probability estimates?
```

### Discussion Questions

- If the model has lower recall for Indigenous patients, what are the clinical implications?
- Is a 5% difference in AUC between groups acceptable? Who decides?
- If disparities exist, is the problem the model, the training data, or the underlying healthcare system?

### Deliverable

Completed fairness analysis with governance recommendation (500 words) on whether the model should be deployed.

---

## Indicative Resources

### Required Reading

- Australian AI Ethics Framework. Department of Industry, Science and Resources.
- TGA. Software as a Medical Device regulatory guidance.

### Recommended Reading

- AHPRA/Medical Board. Technology and telehealth guidelines.
- Mello, M.M., & Guha, N. (2024). Understanding liability risk from using health care AI tools. *NEJM*.

---

## Session Summary

This week examined the ethical and regulatory frameworks governing healthcare AI:

1. Bioethical principles provide a foundation for evaluating AI
2. Australian regulation through TGA is evolving but provides a framework
3. Professional and legal obligations for AI-assisted practice remain uncertain
4. Organisations have ethical obligations in AI procurement and deployment
5. Aeromedical services face additional complexity from cross-jurisdictional operations

**Next Week:** We'll focus specifically on AI in high-stakes environments—examining the additional safety requirements for time-critical, remote, and austere settings.
