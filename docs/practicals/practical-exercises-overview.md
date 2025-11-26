# Practical Computing Stream: Overview

## Purpose

The practical computing stream uses Google Colab to provide hands-on experience with AI/ML systems. These exercises are designed for clinicians without programming backgrounds—the goal is demystification, not technical mastery.

By completing these exercises, you will:
- Understand what happens "under the hood" when AI systems are trained and run
- Critically evaluate vendor claims about AI capabilities
- Communicate effectively with technical teams
- Recognise the difference between AI hype and operational reality

**No prior programming experience is required.** All exercises use pre-built notebooks with guided modifications.

---

## Technical Requirements

- Modern web browser (Chrome recommended)
- Google account (personal or institutional)
- Stable internet connection
- No software installation required

---

## Exercise Schedule

| Exercise | Week | Duration | Focus |
|----------|------|----------|-------|
| [Pre-course Orientation](#pre-course-orientation) | Pre | ~2 hours | Environment navigation, basic execution |
| [Exercise 1: Exploring AI Outputs](#exercise-1-exploring-ai-outputs) | 1 | ~1.5 hours | Running models, observing predictions |
| [Exercise 2: ML Fundamentals](#exercise-2-ml-fundamentals-hands-on) | 2 | ~2 hours | Training a classifier, understanding parameters |
| [Exercise 3: Data Exploration](#exercise-3-data-exploration-and-bias-detection) | 3 | ~1.5 hours | Dataset analysis, bias indicators |
| [Exercise 5: Fairness Metrics](#exercise-5-measuring-algorithmic-fairness) | 5 | ~2 hours | Subgroup performance, fairness metrics |
| [Exercise 7: Local Validation](#exercise-7-local-validation-simulation) | 7 | ~1.5 hours | External validation, performance gaps |
| [Exercise 10: LLM Experimentation](#exercise-10-clinical-llm-experimentation) | 10 | ~2 hours | Prompt engineering, capability testing |

---

## Exercise Summaries

### Pre-course Orientation

**Objective:** Ensure all students can navigate Google Colab before the course begins.

**Skills Developed:**
- Access and navigate Colab environment
- Run code cells
- Save work to Google Drive
- Troubleshoot common issues

**Deliverable:** Self-assessment checklist completion

[Full details in curriculum/00-pre-course-orientation.md](../curriculum/00-pre-course-orientation.md)

---

### Exercise 1: Exploring AI Outputs

**Objective:** Interact with pre-trained AI models to observe their behaviour and limitations.

**Activities:**
- Run a pre-trained image classifier on medical images
- Interact with a clinical language model
- Compare rule-based vs. ML approaches

**Key Questions:**
- What did the AI get right? What did it get wrong?
- How confident was the AI? Was that confidence warranted?
- What would happen if you relied on this AI in practice?

**Deliverable:** Reflection (300 words) comparing AI behaviour to clinical expectations

---

### Exercise 2: ML Fundamentals Hands-on

**Objective:** Train a simple classifier to understand the ML process from data to prediction.

**Activities:**
- Prepare a clinical dataset for training
- Train a decision tree classifier
- Examine feature importance and model reasoning
- Experiment with parameters and data variations

**Key Learning Points:**
- ML models learn patterns from training data
- Test performance may not match training performance
- Features determine what the model can learn
- Random variation affects results

**Deliverable:** Completed notebook with reflection questions

---

### Exercise 3: Data Exploration and Bias Detection

**Objective:** Examine a healthcare dataset to understand how data characteristics shape AI behaviour.

**Activities:**
- Explore dataset demographics and distributions
- Analyse outcomes by subgroup
- Examine missing data patterns
- Simulate dataset shift

**Discussion Points:**
- Does this dataset reflect your population?
- What groups are underrepresented?
- What does missing data tell us?

**Deliverable:** Analysis notebook with observations on bias sources

---

### Exercise 5: Measuring Algorithmic Fairness

**Objective:** Apply fairness metrics to evaluate AI model performance across demographic groups.

**Activities:**
- Train a clinical prediction model
- Calculate overall performance metrics
- Stratify performance by demographic group
- Apply fairness metrics (demographic parity, equalised odds)
- Explore mitigation strategies

**Key Questions:**
- If the model has lower recall for some groups, what are the implications?
- How much disparity is acceptable?
- Is the problem the model, the data, or the healthcare system?

**Deliverable:** Fairness analysis with governance recommendation (500 words)

---

### Exercise 7: Local Validation Simulation

**Objective:** Understand validation requirements for deploying AI in a new environment.

**Scenario:** Validate a US-developed deterioration prediction model for deployment in Australian healthcare.

**Activities:**
- Load and examine a "vendor" model
- Prepare local validation data
- Compare vendor-reported vs. local performance
- Analyse performance gaps
- Complete go/no-go decision framework

**Discussion Questions:**
- How much performance degradation is acceptable?
- What if it works well overall but poorly for a subgroup?
- What additional information would you request?

**Deliverable:** Validation report for governance committee

---

### Exercise 10: Clinical LLM Experimentation

**Objective:** Systematically evaluate large language model capabilities and limitations for clinical applications.

**Activities:**
- Set up LLM API access
- Test clinical knowledge accuracy
- Evaluate clinical reasoning
- Probe for limitations (hallucination, temporal limits, Australian context)
- Experiment with prompt engineering
- Evaluate documentation support capabilities

**Key Learning Points:**
- LLMs have significant capabilities but also important limitations
- Prompt design affects output quality
- Verification of LLM outputs is essential
- Australian-specific knowledge may be limited

**Deliverable:** Evaluation notebook with structured assessment of capabilities and limitations

---

## Technical Skills Progression

### Foundation (Pre-course & Weeks 1-3)

- Execute code cells in Colab
- Interpret model outputs and predictions
- Read basic data summaries and visualisations
- Understand train/test splitting rationale

### Intermediate (Weeks 5 & 7)

- Interpret performance metrics (AUC, sensitivity, specificity)
- Calculate and interpret fairness metrics
- Conduct basic validation analysis
- Modify code parameters to explore behaviour

### Advanced (Week 10)

- Construct effective prompts for clinical LLMs
- Systematically evaluate LLM capabilities
- Identify hallucination and knowledge limitations
- Assess LLM outputs against clinical standards

---

## Assessment Integration

Practical exercises support assessments:

| Exercise | Supports |
|----------|----------|
| Exercises 1-3 | Assessment 1: Technical understanding for architecture analysis |
| Exercise 5 | Assessment 2: Direct experience with bias/fairness evaluation |
| Exercise 7 | Capstone: Validation methodology for implementation planning |
| Exercise 10 | Capstone: LLM evaluation for emerging technology analysis |

---

## Support Resources

- **Pre-built notebooks:** Distributed via LMS before each exercise
- **Video walkthroughs:** Available on LMS for each exercise
- **Troubleshooting guide:** Common issues and solutions
- **Discussion forum:** Post technical questions
- **Drop-in sessions:** Optional support sessions as scheduled

---

## Accessibility

- All exercises can be completed with screen reader software
- Video walkthroughs include captions
- Alternative formats available on request
- Keyboard navigation fully supported
- Works on tablets (desktop/laptop recommended)

---

## Frequently Asked Questions

**Do I need to know how to code?**
No. You'll run and modify pre-built code, not write from scratch. The focus is on understanding AI behaviour, not programming skills.

**What if I get stuck?**
First, try the troubleshooting guide. Then post on the discussion forum. Tutors monitor the forum and drop-in sessions are available.

**How long do exercises take?**
Approximately 1.5-2 hours each. Some students complete faster; others prefer to explore more deeply.

**Are exercises assessed?**
Exercises have deliverables that receive feedback but are not separately graded. However, they directly support the summative assessments.

**Can I work with others?**
You can discuss concepts and troubleshoot together, but complete your own exercises and write your own reflections.

**What if I want to go deeper?**
Additional resources and extension activities are provided for those who want more technical depth. These are optional.
