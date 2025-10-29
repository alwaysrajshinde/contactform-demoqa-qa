Project Title: Contact Form QA Project (DemoQA)

Project Description:
This project focuses on testing the "Automation Practice Form" feature on the DemoQA website.
It includes both Manual and Automation Testing to verify form functionality, validation,
and submission workflow.

Tester: Raj Shinde
Date: 29 October 2025

--------------------------------------------------
Project Goal:
To ensure that all input fields, validations, and submission flow in the DemoQA contact form
work as expected, without functional or UI defects.

--------------------------------------------------
Folder Structure:

01_Manual_Testing
    - TestPlan_DemoQA.docx         (Detailed plan covering scope, objectives, tools)
    - TestCases_DemoQA.xlsx        (10 test cases covering positive and negative scenarios)
    - TestExecution_DemoQA.xlsx    (Execution results with pass/fail status)
    - TestSummary_DemoQA.docx      (Summary report with overall testing outcome)

02_Automation_Testing
    - Selenium automation framework using Page Object Model (POM)
    - test_contact_form_demoqa.py  (Automation script for the form)
    - config/config.json            (Contains URL and settings)
    - conftest.py and pytest.ini    (Configuration for pytest execution)

03_Reports
    - DemoQA_Bug_Report.xlsx        (List of reported bugs)
    - DemoQA_JIRA_Bug_Report.xlsx   (Formatted bug report for JIRA export)

04_Project_Screenshots
    - HTML-REPORT.png               (Pytest HTML report)
    - ALLURE-REPORT.png             (Allure summary report)
    - Jira.png                      (Screenshot of logged JIRA bugs)

--------------------------------------------------
Testing Types Covered:
1. Functional Testing
2. Negative Testing
3. UI Field Validation
4. Smoke and Regression Testing (Automation)

--------------------------------------------------
Tools and Technologies Used:
- Selenium WebDriver with Python
- Pytest Framework
- Microsoft Excel for manual documentation
- JIRA for defect tracking
- Chrome Browser for test execution

--------------------------------------------------
How to Run Automation:
1. Open the terminal inside the "02_Automation_Testing" folder.
2. Execute the following command:
       pytest 

3. The report will be generated inside the "reports" folder and screenshots (if any) will be stored automatically.
4.For Allure Report Run 
        allure serve allure-reports

--------------------------------------------------
Project Outcome:
- Total Test Cases: 10
- Passed: 9
- Failed: 1 (Invalid Email Validation Bug)
- Bug logged in JIRA with ID: CDP-1

--------------------------------------------------
Conclusion:
The DemoQA contact form is functionally stable.
A minor email validation issue has been detected and reported in JIRA.
This project demonstrates both Manual and Automation QA testing process end-to-end.
