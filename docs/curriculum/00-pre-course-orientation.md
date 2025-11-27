# Pre-Course: Google Colab Orientation

## Technical Preparation Module

**Duration:** Self-paced, approximately 2 hours  
**When:** Complete in the week before Week 1

## Purpose

This self-paced module ensures all students can navigate Google Colab before the course begins. The goal is not to make you a programmer, but to give you sufficient technical exposure to:

- Understand what happens "under the hood" when AI systems are trained and run
- Critically evaluate vendor claims about AI capabilities
- Communicate effectively with technical teams
- Recognise the difference between AI hype and operational reality

## Learning Objectives

By completing this module, you will be able to:

- Access and navigate the Google Colab environment
- Understand the concept of a computational notebook
- Execute pre-written code cells and observe outputs
- Save work and manage files in Google Drive
- Troubleshoot common issues

## Technical Requirements

- Modern web browser (Chrome recommended)
- Google account (personal or institutional)
- Stable internet connection
- No software installation required

---

## Part 1: Getting Started (30 mins)

### What is Google Colab?

Google Colab (Colaboratory) is a free, cloud-based platform that lets you run Python code in your browser. Think of it as a "living document" that combines:

- **Text explanations** (like a Word document)
- **Executable code** (that actually runs and produces results)
- **Outputs** (graphs, tables, results)

For this course, you'll use Colab to see how AI/ML systems actually work—without needing to become a programmer.

### Why Colab for This Course?

- **No installation required** — runs entirely in your browser
- **Free GPU access** — can run real ML models without expensive hardware
- **Pre-installed libraries** — common AI/ML tools ready to use
- **Shareable** — instructors can distribute notebooks; students can share work
- **Persistent** — notebooks save to Google Drive

### Accessing Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with a Google account (personal or institutional)
3. You'll see the Colab welcome screen with options to create or open notebooks

### Exercise 1.1: Open Your First Notebook

1. Click **"New Notebook"** to create a blank notebook
2. Notice the two types of cells:
   - **Text cells** — for explanations (like this document)
   - **Code cells** — for running Python code
3. The notebook auto-saves to your Google Drive under "Colab Notebooks"
4. Give your notebook a name by clicking "Untitled0.ipynb" at the top

---

## Part 2: Running Code (30 mins)

### Understanding Code Cells

Code cells contain Python instructions. For this course, you don't need to write code from scratch—just run what's provided and modify parameters to explore behaviour.

### Exercise 1.2: Your First Code Execution

In a code cell, type (or copy) the following and press **Shift+Enter** to run:

```python
print("Hello, Healthcare AI!")
```

The output appears below the cell. Congratulations—you've run Python code.

### Exercise 1.3: Running a Simple Calculation

Try this clinical example:

```python
# Calculate a NEWS2 score component
respiratory_rate = 22

if respiratory_rate >= 21 and respiratory_rate <= 24:
    rr_score = 2
    print(f"Respiratory rate {respiratory_rate}: NEWS2 score = {rr_score}")
```

Notice how the code makes a decision based on clinical parameters—this is the foundation of rule-based clinical decision support.

### Exercise 1.4: Modifying Parameters

Change the `respiratory_rate` value to different numbers and re-run the cell. Observe how the output changes.

```python
# Try different values: 12, 18, 25, 30
respiratory_rate = 12  # <-- Change this number

if respiratory_rate <= 8:
    rr_score = 3
elif respiratory_rate <= 11:
    rr_score = 1
elif respiratory_rate <= 20:
    rr_score = 0
elif respiratory_rate <= 24:
    rr_score = 2
else:
    rr_score = 3

print(f"Respiratory rate {respiratory_rate}: NEWS2 score = {rr_score}")
```

This is the core skill you'll use throughout the course: running provided code and modifying inputs to explore AI behaviour.

---

## Part 3: Working with Pre-built Notebooks (30 mins)

Most course exercises use pre-built notebooks. You'll open them, run the cells, and modify parameters to explore behaviour.

### Exercise 1.5: Opening a Shared Notebook

**📓 [Open Pre-Course Orientation Notebook](../practicals/colab-notebooks/00-orientation.ipynb)**

--8<-- "practicals/_colab-instructions.md"

After opening the notebook:
1. Save a copy to your Drive (File → Save a copy in Drive)
2. Work through the guided exercises in the notebook

### Key Operations to Practice

| Action | How |
|--------|-----|
| Run a single cell | Shift+Enter or click the Play button |
| Run all cells | Runtime → Run all |
| Restart if stuck | Runtime → Restart runtime |
| Add a comment | In a code cell, use `#` before your text |
| Download notebook | File → Download → Download .ipynb |

### Exercise 1.6: Cell Execution Order

**Important concept:** Cells must often be run in order. Try this:

1. Create a new notebook
2. In the first cell, type: `patient_name = "Jane Smith"`
3. In the second cell, type: `print(f"Patient: {patient_name}")`
4. Run only the second cell — you'll get an error
5. Now run the first cell, then the second — it works

This demonstrates that code cells build on each other. If you get unexpected errors, try running cells from the top.

---

## Part 4: Troubleshooting Common Issues (15 mins)

| Problem | Solution |
|---------|----------|
| "Runtime disconnected" | Click "Reconnect" or Runtime → Reconnect |
| Code won't run | Check you're connected; try Runtime → Restart runtime |
| Output looks wrong | Run cells in order from the top |
| Lost your work | Check Google Drive → Colab Notebooks |
| Need more computing power | Runtime → Change runtime type → GPU |
| Variables seem wrong | Runtime → Restart runtime → Run all cells |

### Understanding Error Messages

When code fails, Colab shows an error message. Don't panic—these are often informative:

- **NameError** — You're using a variable that hasn't been defined yet. Run earlier cells.
- **SyntaxError** — There's a typo in the code. Check for missing quotes or brackets.
- **ModuleNotFoundError** — A required library isn't loaded. Run the import cells at the top.

For course exercises, if you encounter an error you can't resolve, post in the discussion forum with:
1. The error message
2. Which notebook and cell you were running
3. What you were trying to do

---

## Part 5: Self-Assessment Checklist

Before Week 1, confirm you can:

- [ ] Access Google Colab and sign in
- [ ] Create a new notebook
- [ ] Run a code cell using Shift+Enter
- [ ] Modify a variable value and re-run
- [ ] Open a shared notebook and copy to your Drive
- [ ] Run all cells in sequence
- [ ] Restart the runtime if needed
- [ ] Find your saved notebooks in Google Drive
- [ ] Download a notebook to your computer

---

## Support Resources

- **Troubleshooting guide:** Available on unit LMS
- **Discussion forum:** Post technical questions
- **Optional drop-in session:** Week 1 for additional support (time TBC)
- **Video walkthroughs:** Available on unit LMS

## What's Next?

In Week 1, you'll use your Colab skills to run pre-trained AI models and observe their behaviour on clinical scenarios. The focus will be on understanding what AI does, not on writing code.

---

## Appendix: Accessibility Notes

- All exercises can be completed with screen reader software
- Video walkthroughs include captions
- Alternative formats available on request
- Keyboard navigation fully supported
- Works on tablets (desktop/laptop recommended for best experience)
