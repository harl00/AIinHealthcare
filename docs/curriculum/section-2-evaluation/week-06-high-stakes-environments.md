# Week 6: AI in High-Stakes Environments

## Section 2: Evaluation | Learning Outcome 2

**Theme:** When failure is not an option: AI in critical and remote care

**Core Question:** *"Should we use it?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Evaluate additional safety requirements for AI in time-critical settings
- Analyse the unique challenges of AI deployment in resource-constrained environments
- Design appropriate human-AI interaction models for high-stakes decisions
- Develop criteria for AI suitability in aeromedical and critical care contexts

---

## Content

### 6.1 Characteristics of High-Stakes Clinical AI

**Time Pressure**

When there's no time to question the algorithm:
- Split-second decisions
- No opportunity for deliberation
- Verification impossible in the moment
- Trust must be established beforehand

**Consequence Severity**

Irreversible decisions and actions:
- Treatment initiation that can't be undone
- Resource allocation with opportunity costs
- Triage decisions affecting survival
- Downstream effects of early errors

**Limited Redundancy**

Fewer backup systems available:
- Single point of care
- No specialist consultation
- Limited equipment alternatives
- Isolation from additional resources

**Expertise Scarcity**

AI as force multiplier vs. crutch:
- Extending expertise to non-specialists
- Supporting rare situation recognition
- Risk of inappropriate reliance
- Deskilling in rare but critical scenarios

### 6.2 Remote and Austere Environment Challenges

**Connectivity Constraints**

What happens when the cloud is unreachable?
- Satellite communication limitations
- Dead zones and blackspots
- Bandwidth restrictions
- Latency for real-time applications

**Edge Computing: AI That Runs Locally**

Processing on local devices:
- No connectivity dependency
- Hardware limitations
- Update and maintenance challenges
- Model performance vs. model size trade-offs

**Power and Hardware Reliability**

Austere environment considerations:
- Battery life
- Temperature extremes
- Vibration and motion
- Environmental exposure (dust, moisture)

**Maintenance and Updates**

Distributed systems challenges:
- Keeping models current
- Version control across fleet
- Rollback capabilities
- Validation of updates

### 6.3 Human-AI Teaming in Critical Care

**Cognitive Load Considerations**

AI that helps vs. AI that distracts:
- Information overload risk
- Attention competition
- Mental workload in emergencies
- Interface design for stress conditions

**Decision Authority Models**

When should AI recommend vs. act?

| Model | AI Role | Human Role | Appropriate When |
|-------|---------|------------|------------------|
| AI-assisted | Provides information | Full decision authority | High uncertainty, complex decisions |
| AI-advised | Makes recommendation | Approves/overrides | Moderate time pressure, verifiable |
| AI-supervised | Acts autonomously | Monitors, can intervene | Well-defined, rapid response needed |
| AI-autonomous | Acts independently | Post-hoc review | Very rapid, AI clearly superior |

**Team Dynamics**

How AI changes crew resource management:
- New "team member" to integrate
- Communication about AI inputs
- Shared mental models including AI
- Leadership when AI disagrees

**Training for Appropriate Trust Calibration**

Neither over-trust nor under-trust:
- Understanding AI capabilities and limits
- Recognising AI uncertainty signals
- Practicing override decisions
- Maintaining non-AI skills

### 6.4 Aeromedical-Specific Considerations

**Pre-hospital AI Applications**

*Triage and Dispatch*
- Severity assessment from call information
- Resource matching (air vs. road, team composition)
- Multi-incident prioritisation
- Predicted transport time optimisation

*Scene Assessment Support*
- Mass casualty triage assistance
- Environmental hazard identification
- Resource estimation

**In-Flight Monitoring and Prediction**

*Deterioration Detection*
- Pattern recognition from continuous monitoring
- Prediction of decompensation
- Alert systems for crew
- Altitude-aware vital sign interpretation

*Treatment Response Monitoring*
- Tracking response to interventions
- Dose adjustment support
- Complication prediction

**Point-of-Care Diagnostics**

*AI-Augmented Assessment*
- Ultrasound interpretation assistance
- ECG analysis
- Pathology result interpretation
- Image capture and remote interpretation

**Handover and Documentation**

*AI Support for Communication*
- Structured handover generation
- Real-time documentation
- Referral communication preparation
- Receiving hospital briefing

**Mass Casualty and Disaster Response**

*Coordination Support*
- Victim tracking
- Resource allocation optimisation
- Triage consistency
- Situation awareness synthesis

---

## Aeromedical Deep Dive

This week is entirely focused on the aeromedical context, integrating all prior content into the specific operational environment of retrieval medicine.

### Case Discussions

**Case 1: The Trusted Algorithm**
An AI system recommends not transporting a patient due to low predicted benefit. The clinician disagrees. How should this be resolved?

**Case 2: The Silent Failure**
During transport, the AI monitoring system fails to alert to a subtle deterioration pattern. Post-hoc analysis shows the pattern was outside training distribution.

**Case 3: The Connectivity Gap**
A cloud-based decision support tool becomes unavailable during a critical phase of transport. What should have been in place?

**Case 4: The Conflicting Advice**
The AI triage system recommends a different resource allocation than experienced dispatch staff. Who decides?

### Criteria Development Exercise

Develop criteria for evaluating whether a specific AI application is suitable for aeromedical deployment:

Consider:
- Clinical benefit magnitude
- Failure mode severity
- Connectivity requirements
- Training requirements
- Backup procedures
- Monitoring feasibility
- Regulatory pathway

---

## Learning Activities

### Pre-Class Preparation

1. **Case Study Review**
   - Read provided case studies of AI in critical care and retrieval services
   - Note success factors and failure contributors

2. **Environmental Scan**
   - Research AI applications in international retrieval services
   - Prepare brief summary for in-class sharing

### In-Class Activities

1. **Tabletop Simulation** (Groups, 45 mins)
   - Scenario-based exercise with AI decision support
   - Experience AI recommendations under time pressure
   - Debrief on decision-making process

2. **Suitability Criteria Development** (Groups, 30 mins)
   - Develop criteria for AI suitability in aeromedical contexts
   - Consider different types of AI applications
   - Present and refine as class

3. **Position Paper Outline** (Individual, 15 mins)
   - Begin position paper on a contested AI application
   - Identify key arguments for and against
   - This feeds into Assessment 2

### Post-Class Activities

1. **Position Paper Outline**
   - Complete position paper outline
   - Submit for tutor feedback (feeds into Assessment 2)

---

## Indicative Resources

### Required Reading

- Literature review on AI in emergency medical services (provided)

### Recommended Reading

- International aeromedical service AI implementation reports
- Human factors research on AI in aviation and critical care
- Autonomous systems in healthcare: lessons from other domains

---

## Session Summary

This week focused on the specific challenges of AI in high-stakes, time-critical, and resource-constrained environments:

1. High-stakes settings amplify both AI benefits and risks
2. Remote and austere environments create unique technical challenges
3. Human-AI teaming requires careful design for critical care contexts
4. Aeromedical retrieval demands particular attention to failure modes
5. Criteria for AI suitability must reflect operational realities

**Next Week:** We shift from evaluation to application—examining how to actually implement AI safely in healthcare settings.

---

## Section 2 Formative Assessment Summary

**Weekly Learning Demonstrations:**

- **Week 4:** Safety analysis (tutor feedback)
- **Week 5:** Regulatory pathway map (peer review)
- **Week 6:** Position paper outline (tutor feedback—feeds into Assessment 2)

**Summative Assessment 2: Critical Evaluation Report**

Due end of Week 8. See [Assessment 2 Brief](../../assessments/assessment-2-critical-evaluation.md) for full details.
