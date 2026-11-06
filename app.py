import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Career Content Generator", page_icon="🎯", layout="wide")

CAREER_SKILLS = {
    "AI Engineer": {
        "required": ["Python", "Machine Learning", "Statistics", "Data Handling", "Model Evaluation"],
        "resources": [
            "Python: practise functions, collections, files, and object-oriented programming.",
            "Machine Learning: learn regression, classification, clustering, and model evaluation.",
            "Statistics: revise probability, distributions, mean, variance, and hypothesis basics.",
            "Data Handling: practise cleaning data with pandas and visualizing it.",
            "Model Evaluation: learn train/test split, accuracy, precision, recall, and F1-score."
        ],
        "questions": [
            "What is the difference between supervised and unsupervised learning?",
            "What is overfitting, and how can it be reduced?",
            "Explain the purpose of a training set and a test set.",
            "What is the difference between precision and recall?",
            "Describe one machine-learning project you have built."
        ]
    },
    "Data Analyst": {
        "required": ["Python", "SQL", "Statistics", "Data Visualization", "Excel"],
        "resources": [
            "Python: practise pandas data filtering, grouping, and missing-value handling.",
            "SQL: practise SELECT, WHERE, GROUP BY, JOIN, and aggregate functions.",
            "Statistics: revise averages, variation, correlation, and distributions.",
            "Data Visualization: create clear charts and explain the insights.",
            "Excel: practise formulas, pivot tables, sorting, and charts."
        ],
        "questions": [
            "What is the difference between WHERE and HAVING in SQL?",
            "How would you handle missing values in a dataset?",
            "When would you use a bar chart instead of a line chart?",
            "What does correlation tell you, and what does it not prove?",
            "Explain an insight you found from data."
        ]
    },
    "Software Developer": {
        "required": ["Python", "Java", "Data Structures", "SQL", "Problem Solving"],
        "resources": [
            "Python: practise functions, modules, exceptions, and file handling.",
            "Java: revise OOP, classes, inheritance, interfaces, and exceptions.",
            "Data Structures: practise arrays, linked lists, stacks, queues, trees, and hashing.",
            "SQL: practise table design, joins, and CRUD operations.",
            "Problem Solving: solve coding problems and explain time complexity."
        ],
        "questions": [
            "Explain the four main principles of object-oriented programming.",
            "What is the difference between an array and a linked list?",
            "What is time complexity? Explain O(n) with an example.",
            "What is a primary key in a database?",
            "How do you debug a program that produces the wrong output?"
        ]
    },
    "Web Developer": {
        "required": ["HTML", "CSS", "JavaScript", "Python", "SQL"],
        "resources": [
            "HTML: practise semantic page structure and accessible forms.",
            "CSS: practise layout, Flexbox, Grid, and responsive design.",
            "JavaScript: revise events, arrays, objects, and asynchronous basics.",
            "Python: practise backend routes and form processing.",
            "SQL: learn CRUD queries and safe handling of user input."
        ],
        "questions": [
            "What is the difference between HTML, CSS, and JavaScript?",
            "What is responsive web design?",
            "What is the difference between frontend and backend?",
            "What is a database query?",
            "How would you validate a form?"
        ]
    }
}

st.title("🎯 AI-Based Personalized Career Content Generator")
st.caption("M1-P1 | Rule-based intelligent prototype | No API key required")
st.info("This prototype uses transparent skill-matching rules. Its suggestions are guidance, not a guarantee of employment.")

with st.form("career_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Student name", placeholder="Enter your name")
        course = st.text_input("Course / branch", value="B.E. Artificial Intelligence and Machine Learning")
        year = st.selectbox("Current year", ["1st year", "2nd year", "3rd year", "4th year", "Graduate"])
        goal = st.selectbox("Target career", list(CAREER_SKILLS.keys()))
    with col2:
        interests = st.text_input("Academic interests", placeholder="e.g. AI, data science, web apps")
        skills_text = st.text_input("Your current skills (comma-separated)", placeholder="e.g. Python, Java, SQL")
        projects = st.text_area("Projects / experience (optional)", placeholder="Mention coursework, internships, or projects.")
        generate = st.form_submit_button("Generate career profile", type="primary")

if generate:
    skills = [x.strip() for x in skills_text.split(",") if x.strip()]
    skill_lookup = {s.casefold() for s in skills}
    target = CAREER_SKILLS[goal]
    matched = [s for s in target["required"] if s.casefold() in skill_lookup]
    gaps = [s for s in target["required"] if s.casefold() not in skill_lookup]
    display_name = name.strip() or "The student"
    interest_text = interests.strip() or "technology and problem-solving"

    st.subheader("1. Professional summary")
    st.write(
        f"{display_name} is a {year.lower()} student in {course or 'a technical course'} "
        f"interested in {interest_text}. Current skills include "
        f"{', '.join(skills) if skills else 'skills that are still being developed'}. "
        f"The career goal is to work as a {goal}. "
        f"{'Relevant project experience includes: ' + projects.strip() if projects.strip() else 'The next step is to build practical projects and document measurable results.'}"
    )

    st.subheader("2. Skill-gap report")
    a, b, c = st.columns(3)
    a.metric("Skills entered", len(skills))
    b.metric("Matched target skills", len(matched))
    c.metric("Skills to develop", len(gaps))
    if matched:
        st.success("Matched skills: " + ", ".join(matched))
    if gaps:
        st.warning("Suggested skills to develop: " + ", ".join(gaps))
    else:
        st.success("All listed target skills matched. Strengthen them with projects and practice.")

    st.subheader("3. Learning recommendations")
    for item in target["resources"]:
        skill = item.split(":")[0]
        if skill in gaps:
            st.markdown(f"- **Priority:** {item}")
        else:
            st.markdown(f"- {item}")

    st.subheader("4. Interview preparation")
    for i, question in enumerate(target["questions"], start=1):
        st.markdown(f"**Q{i}. {question}**")
        st.caption("Practice tip: answer in your own words and include a small example.")

    result = {
        "Student": display_name, "Course": course, "Year": year, "Career goal": goal,
        "Interests": interest_text, "Current skills": ", ".join(skills),
        "Matched skills": ", ".join(matched), "Skill gaps": ", ".join(gaps),
        "Projects / experience": projects
    }
    csv = pd.DataFrame([result]).to_csv(index=False).encode("utf-8")
    st.download_button("Download career report (CSV)", csv, "career_report.csv", "text/csv")
    report_text = (
        f"CAREER PROFILE\\nStudent: {display_name}\\nGoal: {goal}\\n"
        f"Current skills: {', '.join(skills) if skills else 'Not provided'}\\n"
        f"Matched skills: {', '.join(matched) if matched else 'None matched'}\\n"
        f"Skill gaps: {', '.join(gaps) if gaps else 'No gaps in the listed set'}\\n"
        f"Interests: {interest_text}\\nProjects: {projects or 'Not provided'}\\n"
    )
    st.download_button("Download simple report (TXT)", report_text, "career_report.txt", "text/plain")

st.divider()
st.caption("Educational prototype. Skill matching uses exact skill names; synonyms and proficiency levels are not inferred.")
