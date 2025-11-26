# Week 10: Current AI Landscape in Healthcare

## Section 4: Synthesis | Learning Outcome 4

**Theme:** State of play: What's actually working (and what isn't)

**Core Question:** *"What comes next?"*

---

## Learning Objectives

By the end of this session, students will be able to:

- Survey the current state of AI deployment in Australian healthcare
- Analyse international exemplars and their applicability to Australian context
- Evaluate the evidence base for deployed healthcare AI systems
- Identify gaps between AI hype and operational reality

---

## Content

### 10.1 AI in Australian Healthcare Today

**Deployed Systems**

Current operational AI in Australian healthcare:

*Medical Imaging*
- Radiology AI (chest X-ray, mammography, CT)
- Ophthalmology screening (diabetic retinopathy)
- Pathology AI (emerging)
- Dermatology AI (limited deployment)

*Clinical Decision Support*
- Sepsis prediction/alerting
- Deterioration early warning
- Drug interaction checking
- Diagnostic support tools

*Administrative*
- Clinical coding assistance
- Scheduling optimisation
- Documentation support
- Revenue cycle applications

**Australian Success Stories**

Examples of effective AI implementation:
- [Case studies to be developed with current examples]
- Key success factors
- Transferable lessons

**Cautionary Tales**

Examples where AI hasn't delivered:
- [Case studies to be developed]
- What went wrong
- Lessons learned

**The Vendor Landscape**

Who's selling AI to Australian health services:
- International vendors localising products
- Australian-developed solutions
- Academic/research spinoffs
- Startup ecosystem
- Procurement and evaluation challenges

### 10.2 International Perspectives

**UK NHS AI Lab**

National coordination approach:
- Centralised evaluation and guidance
- National implementation support
- Evidence generation programs
- Regulatory alignment

Lessons for Australia:
- Benefits of coordination
- Resource requirements
- Transferable frameworks

**US Health System Implementations**

Scale and fragmentation:
- Large health system deployments
- Vendor-driven market
- Variable evidence standards
- Rapid commercialisation

Lessons for Australia:
- Scale opportunities and risks
- Evidence generation models
- Regulatory differences

**European Approaches**

Regulation-led development:
- EU AI Act implications
- CE marking requirements
- Privacy (GDPR) integration
- Ethical frameworks

Lessons for Australia:
- Regulatory alignment opportunities
- Ethical framework development
- Cross-border considerations

**Emerging Economy Innovations**

Necessity-driven AI:
- Resource-constrained solutions
- Task-shifting applications
- Mobile-first approaches
- Scalability lessons

Lessons for Australia:
- Rural and remote applications
- Efficient deployment models
- Appropriate technology

### 10.3 Evidence and Outcomes

**What Does the Evidence Actually Show?**

Systematic review findings:
- Many promising results in development
- Fewer rigorous clinical trials
- Limited real-world outcome data
- Publication bias concerns

**The Gap Between Trial and Reality**

Why real-world performance differs:
- Controlled conditions vs. messy reality
- Selected populations vs. all comers
- Research support vs. routine care
- Novelty effects and attention

**Measuring AI Impact**

Dimensions of impact:
- Clinical outcomes (mortality, morbidity)
- Process outcomes (efficiency, timeliness)
- Economic outcomes (cost, resource use)
- Experience outcomes (clinician, patient)

Measurement challenges:
- Attribution (was it the AI?)
- Timeframes (when do benefits appear?)
- Unintended consequences
- System-level effects

**Publication Bias and Missing Studies**

What we don't know:
- Failed implementations rarely published
- Negative results underreported
- Vendor-sponsored research biases
- The graveyard of abandoned projects

### 10.4 Aeromedical and Emergency Services AI

**International Retrieval Service Innovations**

*Dispatch and Tasking*
- AI-assisted triage
- Resource allocation optimisation
- Demand prediction

*Clinical Decision Support*
- Diagnostic assistance
- Treatment recommendations
- Risk stratification

*Operational Support*
- Flight planning
- Weather integration
- Crew scheduling

**Emergency Dispatch AI**

Current applications:
- Call prioritisation
- Protocol adherence support
- Resource recommendations
- Quality assurance

Evidence and concerns:
- Performance data
- Equity considerations
- Implementation challenges

**In-Field Diagnostic Support**

Emerging capabilities:
- Point-of-care ultrasound AI
- ECG interpretation
- Vital sign pattern recognition
- Symptom checkers for field use

**Search and Rescue Applications**

AI applications in SAR:
- Search pattern optimisation
- Survivor detection
- Resource coordination
- Terrain and weather analysis

---

## Aeromedical Thread

### Deep Dive: International Aeromedical AI

Detailed examination of AI currently deployed or trialled in aeromedical services globally:

**European Services**
- Scandinavian HEMS innovations
- UK air ambulance technology
- Swiss Rega systems

**North American Services**
- US flight programs
- Canadian remote area services
- Integration approaches

**Australian/NZ Developments**
- Current state assessment
- Trials and pilots
- Strategic directions

**Critical Analysis**

For each exemplar:
- What's actually deployed vs. aspirational?
- What evidence exists?
- What would transfer to Australian context?
- What barriers exist?

---

## Learning Activities

### Pre-Class Preparation

1. **Environmental Scan**
   - Identify AI currently deployed or considered in your health service
   - Assess current state: operational, pilot, evaluation, aspirational

2. **International Case Study**
   - Research one international AI implementation in detail
   - Prepare brief summary for class sharing

### In-Class Activities

1. **Evidence Appraisal Workshop** (Groups, 40 mins)
   - Groups critically appraise published AI implementation studies
   - Assess strength of evidence
   - Identify gaps and limitations
   - Report key findings

2. **Guest Presentations** (If available, 30 mins)
   - Presentations from health services with deployed AI
   - Q&A and discussion
   - Lessons learned

3. **Gap Analysis Exercise** (Pairs, 20 mins)
   - Compare international exemplars to Australian context
   - Identify transferable elements
   - Note barriers and adaptations needed

### Post-Class Activities

1. **Current State Analysis**
   - Complete current state analysis section for capstone project
   - Document relevant deployed systems and evidence base

---

## Practical Exercise 10: Clinical LLM Experimentation (Colab)

### Objective

Systematically evaluate large language model capabilities and limitations for clinical applications.

### Part A: Setting Up LLM Access

```python
import anthropic

client = anthropic.Anthropic(api_key="PROVIDED_FOR_COURSE")

def query_llm(prompt, system_prompt="You are a helpful clinical assistant."):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

### Part B: Clinical Knowledge Assessment

```python
clinical_questions = [
    "What are the diagnostic criteria for sepsis according to Sepsis-3?",
    "Describe the management of a tension pneumothorax in the pre-hospital setting.",
    "What are the contraindications to thrombolysis in acute ischaemic stroke?",
]

for question in clinical_questions:
    print(f"Q: {question}\n")
    print(f"A: {query_llm(question)}\n")
```

### Part C: Probing for Limitations

```python
# Test for fabrication
response = query_llm("What did the RETRIEVAL-2 trial show about adrenaline dosing?")
# Note: This is a fictional trial

# Test for temporal limits
response = query_llm("What are the latest 2024 ANZCOR guidelines?")

# Test for Australian-specific knowledge
response = query_llm("What PBS restrictions apply to apixaban in Australia?")
```

### Deliverable

Completed evaluation notebook with structured assessment of LLM capabilities and limitations for three clinical use cases.

---

## Indicative Resources

### Required Reading

- Selected peer-reviewed AI implementation studies (provided)

### Recommended Reading

- Australian Digital Health Agency reports
- International aeromedical conference proceedings
- Lancet Digital Health: current issue

---

## Session Summary

This week surveyed the current state of healthcare AI:

1. AI is deployed in Australian healthcare, but scale and maturity vary
2. International exemplars offer lessons but require contextual adaptation
3. The evidence base for healthcare AI has significant gaps
4. Real-world performance often differs from published results
5. Aeromedical services internationally are exploring AI applications

**Next Week:** We'll look forward—examining emerging technologies and trends that will shape healthcare AI.
