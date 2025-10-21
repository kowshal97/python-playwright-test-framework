# 🎭 Python Playwright Test Automation Framework

[![Build Tests](https://github.com/kowshal97/python-playwright-test-framework/actions/workflows/daily-html-report.yml/badge.svg)](https://github.com/kowshal97/python-playwright-test-framework/actions/workflows/daily-html-report.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.55+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-Automated%20Daily%20Run-brightgreen)

A **scalable, cross-browser test automation framework** built using **Playwright + Pytest**, designed for **UI testing**, **data-driven execution**, and **CI/CD integration** with **GitHub Actions**.  
This framework includes structured test modules, reusable fixtures, screenshots, and HTML reporting for clear visibility into test results.

---

## 🚀 Features

✅ **Built with Pytest + Playwright (Sync API)**  
✅ **Cross-browser testing** – Chromium, Firefox, WebKit  
✅ **Custom fixtures** for browser and page management  
✅ **HTML reporting** (self-contained report for easy sharing)  
✅ **Parallel test execution** via `pytest-xdist`  
✅ **Automatic daily test execution** using GitHub Actions  
✅ **Integrated Allure reporting** *(optional for advanced insights)*  
✅ **Screenshots, videos & trace logs on failure*  

---

## 🧩 Project Structure

python-playwright-test-framework/
├── .github/
│   └── workflows/
│       └── daily-html-report.yml        # Automated daily test workflow
├── test_cases/                          # Organized UI test cases
│   ├── test_case1.py
│   ├── test_case2.py
│   ├── ...
│   ├── reports/
│   │   ├── report.html                  # Pytest HTML report (pytest-html)
│   │   ├── allure-results/              # Raw Allure JSON from last run
│   │   └── allure-report/               # (optional) Static Allure site if generated
│   ├── Screenshots/                     # Screenshots captured on failure
│   └── videos/                          # Video recordings of failed runs
├── practice_scripts/                    # Experimental Playwright scripts
├── assets/                              # Static files (e.g. PDFs for upload)
├── conftest.py                          # Shared fixtures & hooks
├── pytest.ini                           # Global pytest configuration
├── requirements.txt                     # Project dependencies
└── README.md


---


---

## ⚙️ Installation & Setup
1️⃣ **Clone the repository** to your local system  
2️⃣ **Create and activate** a virtual environment  
3️⃣ **Install dependencies** from `requirements.txt`  
4️⃣ **Install Playwright browsers** to enable Chromium, Firefox, and WebKit testing  

---

## 🧪 Running Tests
You can execute the tests using **Pytest** and view the results in the generated **HTML report**.  
All screenshots, videos, and logs are saved automatically for failed test cases.  

---

## ☁️ GitHub Actions Integration
📄 Workflow File: `.github/workflows/daily-html-report.yml`  
🔁 Automatically triggers **daily at 13:00 UTC (8 AM EST)**  
📊 Generates and uploads the **HTML report** on each run  
🔗 View all runs under the **Actions** tab on your repository  

After each run:
- Go to **Actions → Latest Run → Artifacts**  
- Download the **pytest HTML report**  
- Open the file locally to view detailed test results  

---

## 🧠 Tech Stack

| Category | Tool |
|-----------|------|
| Programming Language | Python |
| Test Framework | Pytest |
| Automation Engine | Playwright |
| Reporting | Pytest-HTML / Allure |
| CI/CD | GitHub Actions |
| Parallel Execution | Pytest-xdist |

---

## 📸 Screenshots & Videos
All failed tests automatically generate:
- **Screenshots** for visual debugging  
- **Videos** for step-by-step analysis  
- **Trace logs** for identifying root causes  

These assets can be attached to bug reports or shared with your QA team for faster issue resolution.

---

## 👨‍💻 Author

**Kowshal Sugunarajah**  
🎓 Postgraduate – Cloud Computing, Durham College    
🌐 [LinkedIn](https://linkedin.com/in/kowshal97)  
📂 [GitHub Projects](https://github.com/kowshal97)

---

## 🏁 Summary
This project showcases:
- ✅ End-to-end **UI automation** with Playwright + Pytest  
- ✅ **CI/CD integration** using GitHub Actions  
- ✅ **Daily test runs** with automated HTML reports  
- ✅ A **scalable and modular** framework structure  

Use it as a **launchpad for your own automation projects** or integrate it into enterprise CI pipelines.

---

> 💡 *“Automation isn’t just about speed — it’s about building confidence in every release.”*

