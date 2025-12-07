# Olist E-Commerce Performance Analysis (2016-2018)

### Project Overview

This project is a comprehensive analysis of the Brazilian e-commerce giant **Olist** (customer orders from 2016 to 2018). It serves as a portfolio piece demonstrating end-to-end Data Analytics capabilities, from **ETL Pipeline construction** and **PostgreSQL integration** to **advanced business intelligence** reporting.

The analysis focuses on two critical areas for e-commerce growth: **Customer Retention** (Cohort Analysis) and **Operational Efficiency** (Delivery Logistics).

### Key Technical Achievements

The project is structured to demonstrate best practices in a local development environment, emphasizing reproducibility and code maintainability (**DRY principle**).

| Skill Demonstrated | Implementation |
| :--- | :--- |
| **Data Engineering (ETL)** | Automated data ingestion pipeline using **Kaggle API** and **Pandas** to load 9 separate CSV files directly into PostgreSQL. |
| **Database Management** | Utilized **PostgreSQL** running in a **Docker** container for a local, production-like data warehouse environment. |
| **Code Structure** | Full code unification using the **DRY principle**: all database configurations and connection logic are isolated into a shared `db_utils.py` module. |
| **Advanced SQL** | **CTE** (Common Table Expressions) and **Window Functions** were used extensively for complex calculations like Monthly Cohort Period Lag. |
| **Data Analysis** | Implemented **Cohort Analysis** and **Time Series/Interval** calculations to identify customer behavior and operational bottlenecks. |

***

### Key Analytical Findings (Insights)

The analysis reveals critical insights into Olist's business model, particularly regarding customer behavior and regional logistics performance.

#### 1. Critically Low Customer Retention
* **Finding:** The monthly retention rate is critically low, consistently falling below **1.0%** after the first month of purchase. This suggests that the Olist platform relies heavily on **Customer Acquisition** rather than Customer Lifetime Value (LTV).
* **Business Implication:** The model appears optimized for single, high-value purchases (e.g., furniture, electronics) rather than repeat commodity sales. This indicates a high dependency on marketing spend.

#### 2. Systemic Logistics Failure in the Northeast
* **Finding:** Delivery performance is highly inconsistent across Brazilian states, with a clear systemic failure pattern in the **North and Northeast (Nordeste) regions**.
* **Specifics:**
    * **Alagoas (AL)** has the worst delay rate, with nearly **24%** of orders delivered late.
    * States like **Ceará (CE)** and **Sergipe (SE)** experience average delays ranging from **13 to 16 days** past the estimated delivery date for late orders.
* **Recommendation:** Prioritize investment in warehousing or logistics partnerships in the Nordeste region to reduce customer friction and mitigate the negative impact of long delays on customer satisfaction and review scores.

#### 3. Strategic Segmentation (RFM Action Plan)
Based on Recency and Frequency analysis, the customer base has been segmented to optimize marketing spend:

* **HIGH PRIORITY (Growth): "Promising" Segment (~19%)**
    * *Who:* Users who bought once but relatively recently.
    * *Action:* **Targeted Cross-Sell.** They are still "warm." This is the highest ROI segment for converting one-time buyers into loyalists.
* **HIGH PRIORITY (Retention): "New Customers" (~38%)**
    * *Who:* Just acquired customers.
    * *Action:* **Onboarding Sequence.** Implement an automated "Welcome" email chain to build trust and secure a second purchase immediately.
* **LOW PRIORITY: "Hibernating" (~37%)**
    * *Who:* Old, inactive users.
    * *Action:* **Minimize Spend.** Only use low-cost automated win-back campaigns to protect sender reputation.***

### Project Structure

```bash
olist-ecommerce/
├── notebooks/
│   ├── 01_ETL_Ingest.ipynb         # Data ingestion from Kaggle API to PostgreSQL
│   ├── 02_Cohort_Retention.ipynb   # Advanced SQL Cohort Analysis & Heatmap
│   ├── 03_Delivery_Logistics.ipynb # Analysis of delays by state and region
│   ├── 04_RFM_Segmentation.ipynb   # Customer segmentation and strategic planning
│   └── db_utils.py                 # Shared utility module (DRY principle implementation)
├── data/                           # CSV files (excluded from GitHub via .gitignore)
└── requirements.txt                # List of required Python packages
```
***

### How to Run Locally (Reproducibility)

Follow these steps to reproduce the entire analysis from scratch:

**Prerequisites:**
1.  **Docker** (to run PostgreSQL).
2.  **Python 3.10+** (with `python3-venv` installed).
3.  **Kaggle API Token** (must be saved to `~/.kaggle/kaggle.json`).

**Setup Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/tikhont/olist-ecommerce
    cd olist-ecommerce
    ```
2.  **Create and Activate Virtual Environment:**
    *(Uses `--system-site-packages` to leverage system-installed libraries)*
    ```bash
    python3 -m venv .venv --system-site-packages
    source .venv/bin/activate
    ```
3.  **Install Project Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Start PostgreSQL Container:**
    ```bash
    docker run --name olist-db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres
    docker exec -it olist-db psql -U postgres -c "CREATE DATABASE olist;"
    ```
5.  **Run JupyterLab:**
    ```bash
    jupyter-lab
    ```
6.  **Execute Analysis:**
    Open and run the notebooks in **sequential order (01 -> 02 -> 03 -> 04)** to complete the ETL, Cohort, Logistics, and RFM analyses.