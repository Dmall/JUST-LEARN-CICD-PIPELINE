# JUST-LEARN-CICD-PIPELINE

![CI/CD Pipeline](https://img.shields.io/badge/GitHub-Actions-blue?logo=github-actions)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A hands-on learning project for understanding and practicing **CI/CD pipelines** using **GitHub Actions**.  
This repository contains a simple Python app, automated tests, workflow configurations, and learning notes.

---

## 📌 Features

- Automated CI pipeline (build + test)
- GitHub Actions workflow  
- Simple Python application & unit tests  
- Notes and documentation for CI/CD learning  
- MIT-licensed, open to contributions

---

## ⚙️ How the CI/CD Pipeline Works

```mermaid
flowchart LR
    A[Push to GitHub] --> B[GitHub Actions Trigger]
    B --> C[Install Dependencies]
    C --> D[Run Unit Tests]
    D --> E{Tests Passed?}
    E -- Yes --> F[Build Success ✔]
    E -- No --> G[Build Fails ❌]
