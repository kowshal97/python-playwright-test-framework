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

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kowshal97/python-playwright-test-framework.git
cd python-playwright-test-framework

### 2️⃣ Create & activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate       # Windows
source .venv/bin/activate      # macOS/Linux
