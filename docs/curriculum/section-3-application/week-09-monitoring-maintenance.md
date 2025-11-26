# Week 9: Monitoring, Maintenance, and Incident Response

## Section 3: Application | Learning Outcome 3

**Theme:** Eternal vigilance: Keeping AI safe after deployment

**Core Question:** *"How do we govern it?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Design monitoring systems for deployed healthcare AI
- Identify and respond to AI performance degradation
- Develop incident response protocols for AI failures
- Apply continuous improvement principles to AI governance

---

## Content

### 9.1 Performance Monitoring

**What to Monitor**

*Technical Performance*
- Accuracy metrics (sensitivity, specificity, AUC)
- Calibration (are probability estimates accurate?)
- Processing time and availability
- System errors and failures

*Fairness Metrics*
- Performance across demographic groups
- Disparate impact indicators
- Changes in equity over time

*Utilisation Patterns*
- How often is AI used?
- Override rates
- User engagement patterns
- Workarounds and avoidance

*User Behaviour*
- Response to AI recommendations
- Time spent with AI outputs
- Documentation patterns
- Feedback and complaints

**Detecting Model Drift**

AI performance can degrade over time:
- Population drift: patient characteristics change
- Concept drift: relationships between variables change
- Data drift: input data quality or format changes

Detection approaches:
- Statistical process control
- Performance threshold alerts
- Regular scheduled audits
- Comparative analysis over time

**Dashboards and Reporting**

Making monitoring actionable:
- Real-time vs. periodic reporting
- Appropriate audiences for different metrics
- Escalation triggers
- Integration with quality reporting

**Benchmarking**

Knowing what "good" looks like:
- Comparison to published performance
- Comparison to pre-AI performance
- Comparison across sites/time
- Realistic expectations

### 9.2 Maintenance and Updates

**The AI Lifecycle**

Deployment is not the end:
- Initial deployment (version 1.0)
- Performance monitoring
- Issue identification
- Update development
- Update validation
- Update deployment
- Continued monitoring

**Managing Model Updates**

Validation before deployment:
- Same rigour as initial deployment
- Regression testing (did we break anything?)
- Performance comparison
- Staged rollout options

**Version Control and Rollback**

Essential capabilities:
- Track which version is deployed where
- Maintain previous versions
- Rapid rollback if problems emerge
- Clear change documentation

**Vendor Dependency**

What happens when the vendor changes?
- Contractual protections
- Data portability
- Model access and transparency
- Exit planning

### 9.3 Incident Response

**Defining AI Incidents**

What counts as a problem?
- AI error contributing to patient harm
- AI error detected before harm
- AI unavailability affecting care
- Near-misses and close calls
- Systematic bias discovered
- Unexpected behaviour patterns

**Investigation Frameworks**

Root cause analysis for AI failures:
- Was it a technical failure?
- Was it an integration failure?
- Was it a human-AI interaction failure?
- Was it a governance failure?

Investigation should be:
- Non-punitive (for appropriate use)
- Systematic
- Focused on system improvement
- Connected to action

**Reporting Obligations**

*Internal*
- Clinical incident systems
- AI governance committee
- Executive leadership

*External*
- TGA adverse event reporting (if applicable)
- Professional boards (if applicable)
- Coroner (if applicable)
- Insurers

**Learning from Incidents**

Closing the loop:
- Root cause to contributing factors
- Contributing factors to system changes
- System changes to implementation
- Implementation to monitoring
- Feedback to governance

### 9.4 Graceful Degradation and Contingency

**Designing for Failure**

What happens when AI is unavailable?
- Planned downtime procedures
- Unplanned outage response
- Degraded mode operations
- Recovery procedures

**Maintaining Non-AI Capabilities**

Avoiding dangerous dependency:
- Skills maintenance for AI-augmented tasks
- Non-AI backup procedures
- Training for AI-free practice
- Regular drills without AI

**Communication During Outages**

Managing expectations:
- Clinician notification
- Patient communication (if relevant)
- Documentation during outage
- Escalation procedures

**Recovery Procedures**

Returning to AI-augmented practice:
- Verification before resumption
- Catch-up for missed AI inputs
- Communication of restoration
- Post-incident review

---

## Aeromedical Thread

### Operational Continuity in Retrieval

**Maintaining Mission Capability**

When AI systems fail during operations:
- Pre-flight checks and contingencies
- In-flight failure protocols
- Communication with coordination centres
- Mission continuation criteria

**Redundancy Planning**

For remote operations:
- Edge computing backup
- Multiple connectivity paths
- Non-AI clinical protocols
- Team training for degraded operations

**Coordination Challenges**

During system outages:
- Communication with referring centres
- Communication with receiving hospitals
- Dispatch and tasking adjustments
- Documentation continuity

**Cross-Jurisdictional Incident Reporting**

When operating across boundaries:
- Which system to report to?
- Coordination between jurisdictions
- Shared learning mechanisms
- Governance notification

---

## Learning Activities

### Pre-Class Preparation

1. **Incident Review**
   - Read provided AI incident reports and post-implementation studies
   - Note investigation approaches and findings

2. **Monitoring Metrics**
   - Draft monitoring metrics for your capstone AI system
   - Consider technical, fairness, and utilisation metrics

### In-Class Activities

1. **Incident Investigation Exercise** (Groups, 40 mins)
   - Tabletop exercise investigating AI incident
   - Apply root cause analysis framework
   - Develop recommendations
   - Present findings

2. **Monitoring Dashboard Design** (Pairs, 25 mins)
   - Design monitoring dashboard for AI system
   - Select key metrics and visualisations
   - Define escalation triggers
   - Peer critique

3. **Contingency Planning** (Groups, 25 mins)
   - Develop contingency plan for AI system failure
   - Consider different failure scenarios
   - Define roles and procedures
   - Test against scenarios

### Post-Class Activities

1. **Monitoring and Incident Response Plan**
   - Complete monitoring and incident response section for capstone project
   - Include: metrics, thresholds, escalation, contingency

---

## Indicative Resources

### Required Reading

- FDA guidance on AI/ML-based Software as a Medical Device action plan

### Recommended Reading

- ECRI Institute. Resources on health technology incident investigation.
- Business continuity planning frameworks

---

## Session Summary

This week focused on the ongoing work of keeping AI safe after deployment:

1. Monitoring must track technical performance, fairness, and utilisation
2. Model drift can degrade performance over time
3. Updates require validation before deployment
4. Incident response should be systematic and learning-focused
5. Contingency planning ensures continued capability when AI fails

**Next Week:** We shift to synthesis—examining the current landscape of AI in healthcare and what's actually working.

---

## Section 3 Formative Assessment Summary

**Weekly Learning Demonstrations:**

- **Week 7:** Implementation plan draft (tutor feedback)
- **Week 8:** Training needs analysis (peer review)
- **Week 9:** Monitoring framework (tutor feedback—feeds into capstone)

**Capstone Draft Checkpoint**

Due end of Week 9. Students submit draft capstone project structure and preliminary content for tutor feedback before final development.

See [Assessment 3: Capstone Brief](../../assessments/assessment-3-capstone/) for details.
