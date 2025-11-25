# Week 1: Introduction to AI in Healthcare

## Section 1: Foundations | Learning Outcome 1

**Theme:** Demystifying AI: From hype to operational understanding

**Core Question:** *"What is this?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Distinguish between artificial intelligence, machine learning, and traditional software
- Identify the major categories of AI applications in healthcare
- Articulate why AI literacy matters for healthcare practitioners

---

## Content

### 1.1 Defining the Landscape

**What AI Is (and Isn't)**

- Separating marketing claims from technical reality
- The AI hierarchy: AI → Machine Learning → Deep Learning → Generative AI
- Rule-based systems vs. learning systems: different approaches, different strengths
- Why "AI" has become an overloaded term

**Why Healthcare is Both Promising and Challenging for AI**

- Rich data availability vs. data quality challenges
- High-stakes decisions requiring reliability
- Regulatory and ethical complexity
- Workforce implications and resistance

### 1.2 Categories of Healthcare AI

**Diagnostic Support**
- Medical imaging analysis (radiology, pathology, dermatology)
- Differential diagnosis assistance
- Early detection and screening applications

**Clinical Decision Support Systems**
- Alert and reminder systems
- Drug interaction checking
- Guideline-based recommendations

**Predictive Analytics**
- Patient deterioration prediction (e.g., sepsis, cardiac arrest)
- Readmission risk scoring
- Resource demand forecasting

**Administrative AI**
- Scheduling optimisation
- Clinical documentation and coding
- Revenue cycle management

**Conversational AI**
- Virtual health assistants
- Symptom checkers
- Mental health chatbots

### 1.3 The Australian Healthcare AI Context

**Current State of Adoption**
- Where AI is actually deployed in Australian health services
- Gap between pilot projects and operational systems
- Barriers to adoption: technical, cultural, regulatory

**Key Stakeholders**
- Clinicians: end users and domain experts
- Health services: purchasers and implementers
- Regulators: TGA, AHPRA, state health departments
- Vendors: commercial providers and their incentives
- Patients: ultimate beneficiaries and risk-bearers

**Unique Challenges of Federated Australian Healthcare**
- State-based health systems
- Public-private mix
- Geographic dispersion and rural health
- Indigenous health considerations

---

## Aeromedical Thread

### AI Applications in Retrieval Medicine: An Overview

The aeromedical context presents unique opportunities and challenges for AI:

**Current and Emerging Applications**
- Triage and dispatch decision support
- Resource allocation optimisation
- Patient deterioration prediction during transport
- Point-of-care diagnostic assistance
- Clinical documentation and handover support

**Unique Constraints**
- Remote decision-making with limited backup
- Connectivity limitations during transport
- Time-critical interventions
- Small, high-performing teams
- Cross-jurisdictional operations

**Why This Context Matters**
Throughout this course, we'll use aeromedical retrieval as a lens for examining AI. The high-stakes, resource-constrained, time-critical nature of retrieval medicine amplifies both the potential benefits and risks of AI systems.

---

## Learning Activities

### Pre-Class Preparation

1. **AI Literacy Self-Assessment**
   - Complete the provided questionnaire to establish your baseline understanding
   - Identify your current AI encounters in practice

2. **Media Analysis Exercise**
   - Read the three provided media articles about healthcare AI
   - Note the specific claims made about AI capabilities
   - Identify any red flags or unsupported assertions

### In-Class Activities

1. **Marketing vs. Reality Analysis** (Small Groups, 30 mins)
   - Groups receive AI product marketing materials
   - Task: Identify specific claims and categorise as verifiable, plausible, or hype
   - Share findings and discuss common patterns

2. **AI Touchpoint Mapping** (Pairs, 20 mins)
   - Map all current or potential AI touchpoints in your clinical environment
   - Categorise by: diagnostic, decision support, predictive, administrative
   - Identify which you interact with vs. which operate invisibly

3. **Large Group Discussion** (30 mins)
   - What surprised you about AI in your environment?
   - Where is AI most/least appropriate in healthcare?
   - What would you need to know before trusting an AI system?

### Post-Class Activities

1. **Reflective Journal Entry** (300 words)
   - Describe a personal encounter with AI in clinical practice
   - What did you understand about how it worked?
   - How did you decide whether to trust its output?

---

## Practical Exercise 1: Exploring AI Outputs (Colab)

### Objective

Interact with pre-trained AI models to observe their behaviour and limitations.

### Exercise Overview

Using a provided Colab notebook, you will:

**Part A: Run a Pre-trained Image Classifier**
- Load a model trained to identify chest X-ray findings
- Submit sample images and observe predictions
- Note confidence scores and how they vary with image quality

**Part B: Interact with a Clinical Language Model**
- Use a provided API connection to query a medical LLM
- Test it with clinical scenarios and observe responses
- Document instances where the model is helpful vs. problematic

**Part C: Compare Rule-based vs. ML Approaches**
- Run a traditional clinical decision rule (e.g., Wells criteria calculator)
- Run an ML-based prediction on the same scenario
- Reflect on differences in transparency and behaviour

### Key Questions to Address

- What did the AI get right? What did it get wrong?
- How confident was the AI in its predictions? Was that confidence warranted?
- What would happen if you relied on this AI in your clinical practice?

### Deliverable

Short reflection (300 words) comparing AI behaviour to your clinical expectations.

---

## Indicative Resources

### Required Reading

- Topol, E. (2019). *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*. Chapter 1: Introduction.

### Recommended Reading

- Rajkomar, A., Dean, J., & Kohane, I. (2019). Machine Learning in Medicine. *New England Journal of Medicine*, 380(14), 1347-1358.
- Australian Digital Health Agency. AI in Healthcare resources. [Link to be added]

### Multimedia

- [Video] What is Machine Learning? (Google, 10 mins) [Link to be added]
- [Podcast] AI in Healthcare episode selection [Link to be added]

---

## Session Summary

This week established the foundational vocabulary and conceptual framework for understanding AI in healthcare. Key takeaways:

1. AI is a broad term encompassing many different technologies with different capabilities
2. Healthcare AI spans diagnostic, predictive, decision support, and administrative applications
3. Australian healthcare presents unique opportunities and challenges for AI adoption
4. Aeromedical retrieval amplifies both the potential benefits and risks of AI
5. Critical evaluation of AI claims requires understanding what AI actually does

**Next Week:** We'll dive deeper into *how* AI systems work—the architecture and algorithms that power healthcare AI applications.
