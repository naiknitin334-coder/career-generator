# Project Report: M1-P1

## AI-Based Personalized Career Content Generator

**Student name:** Nitin Naik 
**USN:** 1CR25AI406  
**Department:** AIML  
**Subject / course code:** Agentic AI
**Submission date:** 06 November 2026

## 1\. Abstract

The Career Content Generator is a web-based educational prototype that helps students organize career information. It accepts a student's course, interests, current skills, target career, and project experience. A rule-based skill-matching module compares the student's entered skills with a predefined skill profile for the selected career. The application produces a professional summary, a skill-gap report, learning recommendations, and interview practice questions. The current implementation runs locally using Python and Streamlit and does not require a paid API.

## 2\. Problem Statement

Students may find it difficult to connect their current skills with the requirements of a target career and to prepare a focused learning plan. The project provides a simple tool to organize this information and highlight skills that may need further development.

## 3\. Objectives

* Collect student profile information through a simple web interface.
* Generate a customized professional summary from the supplied information.
* Compare entered skills with predefined career skill requirements.
* Recommend learning activities and interview practice questions.
* Allow the generated profile data to be downloaded.

## 4\. Existing System

Students often gather career information manually from different websites and documents. This can make it difficult to organize skill gaps and interview preparation in one place.

## 5\. Proposed System

The proposed prototype combines a profile form, career-specific rule sets, skill matching, and report generation in one interface. It supports AI Engineer, Data Analyst, Software Developer, and Web Developer career paths.

## 6\. System Requirements

**Software:** Python 3.11/3.12, Streamlit, Pandas, web browser, Windows.  
**Hardware:** A laptop/desktop capable of running Python; internet is needed to install packages but not for normal local use afterward.

## 7\. Methodology / Algorithm

1. Read the student's profile and target career.
2. Split the entered skills using commas.
3. Load the predefined required skills for the selected career.
4. Compare the entered skills against required skills using case-insensitive exact matching.
5. List matched skills and missing target skills.
6. Display a generated summary, learning recommendations, and interview questions.
7. Offer CSV and TXT downloads.

## 8\. Architecture

Student input → Streamlit interface → Career rules and skill matching → Summary and skill-gap report → Downloadable output.

## 9\. Testing

Record your actual test results after running the app.

|Test|Input|Expected result|Actual result|
|-|-|-|-|
|T1|Goal AI Engineer; skills Python, Java|Python matched; missing required skills shown|Passed – Python matched; missing skills displayed correctly.|
|T2|Goal Data Analyst; skills SQL, Excel|SQL and Excel matched; remaining gaps shown|Passed – SQL and Excel matched; remaining skill gaps displayed correctly|
|T3|Empty skills|All required skills shown as gaps|Passed – All required skills displayed as missing.|
|T4|Enter profile and download|CSV/TXT download is available|Passed – Profile entered successfully and CSV/TXT download available.|

## 10\. Results and Discussion

Insert screenshots of the input form, generated profile, skill-gap report, and download buttons. Discuss how the recommendations change for different target careers.

## 11\. Limitations

The current version uses predefined rules and exact skill-name matching. It does not infer synonyms, measure skill proficiency, verify employment-market demand, or use a large language model. Recommendations should be reviewed by the student.

## 12\. Future Enhancements

* Add synonym-aware skill matching and proficiency ratings.
* Add a local open-source language model if hardware permits.
* Add user accounts and persistent profile storage.
* Add verified links to learning resources.
* Evaluate recommendation quality with a larger test set.

## 13\. Conclusion

The project demonstrates how a web application can organize career profiles, compare skills with predefined career requirements, and produce structured learning and interview-preparation guidance.

## 14\. References

* Python documentation: https://docs.python.org/3/
* Streamlit documentation: https://docs.streamlit.io/
* Pandas documentation: https://pandas.pydata.org/docs/

**Before submission:** replace placeholders, add your own screenshots, and record real test results. Do not claim features that you have not implemented.

