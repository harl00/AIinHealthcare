# Week 7: Implementation Frameworks

## Section 3: Application | Learning Outcome 3

**Theme:** From evaluation to action: Structured approaches to AI deployment

**Core Question:** *"How do we govern it?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Apply clinical AI implementation frameworks to deployment decisions
- Design validation strategies appropriate to healthcare AI
- Develop governance structures for AI oversight
- Create readiness assessment criteria for AI adoption

---

## Content

### 7.1 Implementation Science for Healthcare AI

**Why Technically Sound AI Often Fails in Practice**

The gap between AI development and successful deployment:
- Technical performance ≠ clinical utility
- Laboratory conditions ≠ real-world conditions
- Algorithm success ≠ workflow success
- Individual tool success ≠ system success

**Implementation Frameworks**

Moving from software deployment to sociotechnical systems thinking:
- Technology is only one component
- People, processes, and culture matter
- Change is organisational, not just technical
- Implementation is a process, not an event

**Stakeholder Engagement**

Essential stakeholders in AI implementation:
- Clinical end users (multiple disciplines)
- Patients and consumers
- IT and informatics
- Clinical governance
- Executive leadership
- Regulators
- Vendors

Each brings legitimate interests and concerns.

**Change Management Principles**

- Create urgency and vision
- Build coalition of support
- Communicate continuously
- Enable action and remove barriers
- Generate short-term wins
- Consolidate and embed change

### 7.2 Clinical Validation Requirements

**Levels of Evidence for Healthcare AI**

Adapted from traditional evidence hierarchies:
- Analytic validation (does it measure what it claims?)
- Clinical validation (does it perform in clinical data?)
- Clinical utility (does it improve outcomes?)

**Local Validation: Why External Validation Isn't Enough**

Published performance may not reflect local performance:
- Different populations
- Different workflows
- Different data systems
- Different clinical practices

Local validation is essential before deployment.

**Prospective vs. Retrospective Evaluation**

| Approach | Advantages | Limitations |
|----------|------------|-------------|
| Retrospective | Fast, cheap, large samples | Historical data may not reflect future |
| Prospective | Real-world validity | Slow, expensive, smaller samples |

Often need both: retrospective first, then prospective confirmation.

**Silent Mode Deployment**

Testing before trusting:
- AI runs but outputs not shown to clinicians
- Compare AI recommendations to actual decisions
- Identify discordance and investigate
- Build confidence before "going live"

**Ongoing Validation**

The work doesn't end at go-live:
- Continuous monitoring of performance
- Detecting drift over time
- Responding to changes in population or practice
- Regular recalibration or retraining

### 7.3 Governance Structures

**AI Governance Committee**

Composition:
- Clinical leadership (multiple disciplines)
- Consumer representative
- IT/informatics
- Clinical governance/safety
- Legal/risk management
- Ethics expertise
- Executive sponsor

Charter:
- Approval authority for AI deployment
- Ongoing oversight of deployed AI
- Incident review and response
- Policy development

**Clinical Informatics Leadership**

Need for expertise in:
- AI/ML technical understanding
- Clinical workflow analysis
- Implementation science
- Data governance
- Health informatics

**Vendor Management**

- Clear accountability for performance
- Access to model information (appropriate transparency)
- Update and maintenance provisions
- Exit clauses and data portability
- Liability allocation

**Incident Reporting and Learning Systems**

- Clear definition of AI incidents
- Low-barrier reporting
- Investigation processes
- Feedback loops for improvement
- Connection to safety and quality systems

**Policy Frameworks**

- AI-specific policies or integrated into existing governance?
- Approval and procurement policies
- Use policies for clinicians
- Monitoring and review policies
- Incident response policies

### 7.4 Readiness Assessment

**Organisational Readiness**

*Culture*
- Innovation orientation
- Learning culture
- Safety culture
- Tolerance for change

*Capability*
- Data infrastructure
- Informatics expertise
- Clinical leadership
- Governance capacity

*Capacity*
- Resources for implementation
- Ongoing operational support
- Training capacity

**Technical Readiness**

- Infrastructure: computing, connectivity, integration
- Data: quality, accessibility, governance
- Integration: EHR, workflows, other systems
- Interoperability: standards compliance

**Workforce Readiness**

- Skills: technical literacy, AI understanding
- Attitudes: openness, appropriate scepticism
- Training: needs assessment, capacity to deliver

**Patient and Community Readiness**

- Awareness of AI in healthcare
- Trust in AI applications
- Concerns and preferences
- Engagement in governance

---

## Aeromedical Thread

### Implementation Challenges for Retrieval Services

**Multi-Site Operations**

- Consistent deployment across bases
- Training across distributed workforce
- Version control and updates
- Performance monitoring at scale

**Variable Referring Hospital IT**

- Integration with diverse systems
- Data availability and quality
- Communication of AI outputs
- Interoperability challenges

**Aircraft/Vehicle System Integration**

- Hardware installation and certification
- Power and connectivity
- Display and interface design
- Interference and safety considerations

**Cross-Jurisdictional Governance**

When operating across state boundaries:
- Multiple governance frameworks
- Different regulatory environments
- Coordinating oversight
- Incident reporting across jurisdictions

---

## Learning Activities

### Pre-Class Preparation

1. **Implementation Case Studies**
   - Read provided AI implementation case studies
   - Identify success factors and implementation challenges

2. **Readiness Self-Assessment**
   - Complete organisational readiness assessment tool for your service
   - Identify major gaps and strengths

### In-Class Activities

1. **Implementation Planning Workshop** (Groups, 45 mins)
   - Groups develop deployment roadmap for a case study AI system
   - Include: validation, governance, training, go-live, monitoring
   - Present and receive peer feedback

2. **Governance Structure Design** (Groups, 25 mins)
   - Design governance structure for AI in a health service
   - Define committee composition, charter, and processes
   - Consider how this fits with existing governance

3. **Readiness Gap Analysis** (Pairs, 20 mins)
   - Review each other's readiness assessments
   - Identify common themes and differences
   - Discuss strategies to address gaps

### Post-Class Activities

1. **Implementation Plan Draft**
   - Draft implementation plan section for capstone project
   - Include: validation approach, governance, training, monitoring

---

## Practical Exercise 7: Local Validation Simulation (Colab)

### Objective

Understand the validation requirements for deploying an AI model in a new clinical environment.

### Scenario

A vendor offers a deterioration prediction model trained on US hospital data. Before deploying it in your Australian health service, you need to validate its performance locally.

### Part A: Load the "Vendor" Model

```python
import joblib
vendor_model = joblib.load('vendor_deterioration_model.pkl')

# What do we know about this model?
print("Model type:", type(vendor_model).__name__)
print("Expected features:", vendor_model.feature_names_in_)
```

### Part B: Prepare Local Validation Data

```python
local_data = pd.read_csv('australian_hospital_data.csv')

# Check compatibility
print("Local data columns:", local_data.columns.tolist())
print("Missing required features:", 
      set(vendor_model.feature_names_in_) - set(local_data.columns))
```

### Part C: External Validation

```python
local_predictions = vendor_model.predict(local_features)
local_probabilities = vendor_model.predict_proba(local_features)[:, 1]

print("=== Vendor-Reported Performance (US data) ===")
print("AUC: 0.85, Sensitivity: 0.78, Specificity: 0.82")

print("\n=== Local Validation Performance (AU data) ===")
print(f"AUC: {roc_auc_score(local_labels, local_probabilities):.3f}")
```

### Part D: Go/No-Go Decision Framework

```python
validation_report = {
    'model_name': 'Vendor Deterioration Predictor v2.1',
    'validation_date': '2024-XX-XX',
    'local_sample_size': len(local_data),
    'vendor_claimed_auc': 0.85,
    'local_validated_auc': local_auc,
    'performance_gap': 0.85 - local_auc,
    'acceptable_threshold': 0.75,
    'recommendation': 'PROCEED' if local_auc >= 0.75 else 'DO NOT PROCEED',
    'conditions': ['Requires 3-month silent running', 
                   'Subgroup monitoring required',
                   'Clinical override mandatory']
}
```

### Deliverable

Completed validation report suitable for governance committee review.

---

## Indicative Resources

### Required Reading

- Sendak, M.P., et al. (2020). A Path for Translation of Machine Learning Products into Healthcare Delivery. *EMJ Innovations*.

### Recommended Reading

- NHS AI Lab. Implementation guidance.
- Australian Commission on Safety and Quality in Health Care. Clinical Governance Framework.

---

## Session Summary

This week provided frameworks for implementing AI in healthcare settings:

1. Implementation requires attention to people, process, and culture—not just technology
2. Local validation is essential before deployment
3. Governance structures must provide effective oversight without blocking innovation
4. Readiness assessment helps identify gaps before implementation
5. Aeromedical services face additional complexity from distributed operations

**Next Week:** We'll examine how to integrate AI into clinical workflows and manage the human-AI relationship.
