# Week 4: AI Safety and Failure Modes

## Section 2: Evaluation | Learning Outcome 2

**Theme:** When AI goes wrong: Understanding and anticipating failure

**Core Question:** *"Should we use it?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Identify common failure modes in healthcare AI systems
- Analyse the mechanisms and impacts of algorithmic bias
- Evaluate the risks of automation bias and deskilling
- Apply safety thinking to AI deployment decisions

---

## Content

### 4.1 Taxonomy of AI Failures

**Performance Failures: When AI is Simply Wrong**

All AI systems make errors. The questions are:
- How often? (Error rate)
- When? (Failure conditions)
- How wrong? (Severity of errors)
- Detectable? (Can we recognise failures?)

**Distribution Shift: When the World Changes**

AI trained on historical data assumes the future resembles the past:
- New diseases (COVID-19 broke many models)
- Changing practices (new treatments, guidelines)
- Seasonal variations
- Institutional changes (new EHR, different documentation)

**Adversarial Vulnerabilities: When AI Can Be Fooled**

AI can fail in unexpected ways:
- Small input changes causing large output changes
- Adversarial examples designed to fool AI
- Edge cases not represented in training

**Integration Failures: Technically Sound AI That Fails in Practice**

Many AI failures are sociotechnical, not purely technical:
- Poor workflow integration
- Alert fatigue and ignored warnings
- Unintended consequences of automation
- Failure to account for real-world conditions

### 4.2 Algorithmic Bias in Healthcare

**Sources of Bias**

| Source | Mechanism | Example |
|--------|-----------|---------|
| Data | Historical patterns reflect historical biases | Risk scores trained on healthcare utilisation (which is itself biased) |
| Labels | Human annotators bring biases | Diagnostic labels influenced by patient demographics |
| Model | Algorithmic choices affect groups differently | Thresholds optimised for majority population |
| Deployment | Different access to AI benefits | AI tools only available in well-resourced settings |

**Case Studies**

*Pulse Oximetry and Skin Pigmentation*
- Systematic overestimation of oxygen saturation in dark-skinned patients
- Not "AI" per se, but illustrates how clinical algorithms can embed bias
- Amplified by AI systems that use SpO2 as input

*Dermatology AI and Skin Tone*
- Models trained predominantly on light skin underperform on dark skin
- Consequences for equity in diagnostic accuracy
- Challenge of dataset diversity

*Risk Scores and Race*
- Commercial algorithms using healthcare costs as proxy for health needs
- Black patients systematically assigned lower risk scores
- Led to reduced access to care management programs

**Measuring and Detecting Bias**

Fairness metrics (each with trade-offs):
- Demographic parity: Equal prediction rates across groups
- Equalised odds: Equal true/false positive rates across groups
- Calibration: Equal accuracy of probability estimates across groups

**The Australian Context**

What biases might affect Australian populations?
- Indigenous health disparities
- Rural/remote vs. metropolitan
- Socioeconomic gradients
- Migrant and refugee populations
- Age-related biases

### 4.3 Human-AI Interaction Failures

**Automation Bias: Over-trusting AI**

Tendency to accept AI recommendations without critical evaluation:
- "The computer says..."
- Reduced vigilance when AI is present
- Failure to notice AI errors
- Particularly problematic when AI is usually right

**Automation Complacency: Reduced Vigilance**

Related to automation bias but distinct:
- Decreased attention when monitoring automated systems
- Slow to detect failures
- Skill degradation over time

**Deskilling: Atrophy of Clinical Capabilities**

If AI routinely performs a task:
- Clinicians may lose proficiency
- What happens when AI is unavailable?
- Particularly concerning for rare but critical skills

**Alert Fatigue: When Too Many Warnings Mean None Are Heeded**

Overalerting leads to:
- Ignoring alerts
- Workarounds to dismiss alerts quickly
- Missing genuine critical alerts among noise

**Accountability Gaps**

When AI contributes to error, who is responsible?
- The clinician who used the AI?
- The health service that deployed it?
- The vendor who developed it?
- Unclear accountability may discourage reporting and learning

### 4.4 Safety Engineering Principles

**Defence in Depth**

AI should be one layer in a multi-layer safety system:
- Not the sole safeguard
- Independent checks where possible
- Human oversight as backup

**Graceful Degradation**

Systems should fail safely:
- Maintain function when AI fails
- Clear fallback procedures
- No catastrophic failure from AI unavailability

**Human-in-the-Loop vs. Human-on-the-Loop**

*Human-in-the-loop:* AI makes recommendations; humans decide
*Human-on-the-loop:* AI acts; humans monitor

Different risk profiles and appropriate for different applications.

**The Importance of Uncertainty Quantification**

AI that knows what it doesn't know:
- Confidence scores that are well-calibrated
- Flagging cases outside training distribution
- Refusing to predict rather than guessing

---

## Aeromedical Thread

### Heightened Failure Consequences in Retrieval

**Limited Backup Options**

- No specialist consultation at 30,000 feet
- Limited equipment for alternative approaches
- Extended time to definitive care
- Single-crew-member scenarios

**Extended Patient Contact Time**

- Consequences of errors compound over long transport
- Less opportunity for course correction
- Deterioration during transport

**Inability to "Call for Help"**

- Connectivity limitations
- No second opinion available
- Autonomous decision-making requirements

**Compounding Failures**

- AI failure + equipment failure + communication failure = ?
- Need to consider failure combinations
- Redundancy planning

### Case Analysis: AI Failure Scenarios

In-class exercise: Analyse hypothetical AI failure scenarios during aeromedical transport:
- Deterioration prediction that misses a critical change
- Medication dosing recommendation error
- False reassurance from monitoring AI
- AI unavailable during critical phase

---

## Learning Activities

### Pre-Class Preparation

1. **AI Incident Reports**
   - Read the three provided AI incident reports
   - For each, identify: What failed? Why? What was the harm?

2. **Bias Detection Exercise**
   - Complete the provided exercise examining a dataset for bias indicators
   - Document potential disparities observed

### In-Class Activities

1. **Failure Mode and Effects Analysis (FMEA)** (Groups, 45 mins)
   - Apply FMEA methodology to a clinical AI system
   - Identify potential failure modes
   - Assess severity, likelihood, and detectability
   - Propose mitigations

2. **Automation Bias Debate** (Structured debate, 20 mins)
   - Motion: "AI clinical decision support does more harm than good because of automation bias"
   - Teams argue for/against
   - Debrief on nuances

3. **Acceptable Error Rates Discussion** (Facilitated, 20 mins)
   - What error rate would you accept from AI?
   - How does this compare to human error rates?
   - Does it depend on the consequence?

### Post-Class Activities

1. **Safety Analysis**
   - Select an AI system relevant to your practice
   - Document potential failure modes
   - Propose safety mitigations
   - This feeds into Assessment 2

---

## Indicative Resources

### Required Reading

- Obermeyer, Z., et al. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447-453.

### Recommended Reading

- FDA adverse event reports for AI/ML medical devices
- UK MHRA. Guidance on AI as a Medical Device.
- Cabitza, F., et al. (2017). Unintended consequences of machine learning in medicine. *JAMA*, 318(6), 517-518.

---

## Session Summary

This week examined how AI systems fail and the risks they pose:

1. AI fails in multiple ways: performance, distribution shift, adversarial, integration
2. Algorithmic bias can systematically disadvantage already marginalised groups
3. Human-AI interaction creates new failure modes: automation bias, complacency, deskilling
4. Safety engineering principles should guide AI deployment
5. Aeromedical contexts amplify failure consequences

**Next Week:** We'll examine the ethical and regulatory frameworks that govern healthcare AI in Australia.
