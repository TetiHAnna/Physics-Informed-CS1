# Physics-Informed Scaffolding for CS1: Radiation Anomaly Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

This repository contains the reference source code and case study materials for the research paper: **"Physics-Informed Scaffolding in Computer Science Education."**

It demonstrates an **"AI-First" pedagogical approach**, where fundamental Computer Science concepts (arrays, loops, sliding windows) are taught through the lens of a real-world problem: **detecting radioactive sources in noisy environmental data.**

## 📄 Overview

This project serves as a practical demonstration of **Physics-Informed Machine Learning (PIML)** concepts adapted for undergraduate students. Instead of using "black box" libraries, students implement the core logic of signal processing from scratch to understand the algorithmic foundations of AI.

The code simulates a Geiger-Muller counter's data stream and applies a student-derived algorithm to detect weak radioactive anomalies hidden within background radiation noise.

##  Key Educational Concepts

The code connects standard CS1 topics to AI foundations:

| CS Concept | AI/Data Science Analogy | Implementation in Code |
| :--- | :--- | :--- |
| **Nested Loops** | **Convolutional Layer** | Sliding window smoothing mechanism |
| **Arrays & Indexing** | **Time-Series Analysis** | Storing and traversing CPS (Counts Per Second) data |
| **Conditionals** | **Binary Classification** | Threshold-based decision boundary (`Signal` vs `Noise`) |
| **Functions** | **Modular Architecture** | Separating data generation from processing logic |

##  How It Works

The algorithm consists of three main stages, mirroring a real-world environmental monitoring pipeline:

1.  **Data Simulation (`generate_synthetic_data`)**:
    * Generates background noise (simulating natural radiation).
    * Injects a weak Gaussian signal (anomaly) at a random or fixed location.
    * *Physics basis:* Poisson-like distribution of background noise.

2.  **Signal Processing (`find_weak_source`)**:
    * **Smoothing:** Applies a moving average filter to reduce statistical noise (Scaffold for Convolution).
    * **Calibration:** Estimates the background level from the initial data points ("clean air").
    * **Detection:** Sets a dynamic threshold (`background * factor`) to identify peaks.

3.  **Visualization & Output**:
    * Outputs the indices where the signal-to-noise ratio exceeds the safety threshold.

##  Usage

No external libraries (like NumPy or Pandas) are required. The code is written in pure Python to maximize accessibility for beginners.

### Prerequisites
* Python 3.x

### Running the Code
```bash
python main.py
Expected Output
Generated 200 data points.
--- Diagnostics ---
Background Level: 49.80
Trigger Threshold: 79.68

 Anomaly (radiation) detected at points:
[98, 99, 100, 101, 102]
This corresponds to the array center (around point 100).
Repository Structure
main.py: The complete source code (Data Generation + Student Algorithm).

README.md: Project documentation.

LICENSE: MIT License.
Citation
If you use this methodology or code in your research or teaching, please cite the original paper and the accompanying textbook:


Textbook:

Nosenko, T. I., Mashkina, I. V., & Yaskevych, V. O. (2025). Application of algorithms and data structures in artificial intelligence: A textbook. Borys Grinchenko Kyiv Metropolitan University.

Citation
If you use this methodology or code in your research or teaching, please cite the original paper and the accompanying textbook:



Textbook:

Nosenko, T. et al. (2025). Algorithms and Data Structures as the Foundation of AI [Study guide]. Borys Grinchenko Kyiv Metropolitan University.
Author: Tetiana Nosenko, Ph.D. Department of Computer Science, Borys Grinchenko Kyiv Metropolitan University

