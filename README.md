# 🎭 Python Playwright Test Automation Framework

A **scalable, cross-browser test automation framework** built using **Playwright + Pytest**, designed for **UI testing**, **data-driven execution**, and **CI/CD integration** with **GitHub Actions**.  
This framework includes structured test modules, reusable fixtures, screenshots, and HTML reporting for clear visibility into test results.

---

## 🚀 Features

✅ **Built with Pytest + Playwright (Sync API)**  
✅ **Cross-browser testing** – Chromium, Firefox, WebKit  
✅ **Custom fixtures** for browser and page management  
✅ **HTML reporting** (self-contained report for sharing)  
✅ **Parallel test execution** via `pytest-xdist`  
✅ **Automatic daily test execution** using GitHub Actions  
✅ **Integrated Allure reporting** (optional for advanced insights)  
✅ **Screenshots, videos & trace logs on failure**  

---

## 🧩 Project Structure

python-playwright-test-framework/
├── .github/
│ └── workflows/
│ └── daily-html-report.yml # Automated daily test workflow
├── test_cases/ # Organized UI test cases
│ ├── test_case1.py
│ ├── test_case2.py
│ ├── ...
│ ├── reports/
│ │ └── report.html # Pytest HTML report output
│ ├── Screenshots/ # Screenshots captured on failure
│ └── videos/ # Video recordings of failed runs
├── practice_scripts/ # Experimental Playwright scripts
├── assets/ # Static files (e.g. PDFs for upload)
├── conftest.py # Shared fixtures & hooks
├── pytest.ini # Global pytest configuration
├── requirements.txt # Project dependencies
└── README.md
