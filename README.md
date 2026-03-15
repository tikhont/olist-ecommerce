# Olist E-Commerce Performance Analysis (2016-2018)

### Project Overview

This is a **technical case study** of the Brazilian marketplace **Olist** (2016-2018), focused on building a reproducible analytical environment to investigate the friction between operational logistics and customer loyalty. 

Instead of taking data at face value, this project demonstrates an **engineering-first approach** to Data Analytics: from containerized infrastructure to auditing data integrity.

**The analysis targets two high-stakes business dimensions:**
* **Operational Friction:** Mapping delivery delays and logistical bottlenecks across 27 states.
* **Retention Reality:** Measuring true Customer Lifetime Value (LTV) while accounting for data noise and structural churn.

---

### 📊 Key Business Insights & Strategic Analysis

#### 1. [Critically Low Customer Retention & Data Limitations](https://github.com/tikhont/olist-ecommerce/blob/main/notebooks/02_Cohort_Analysis.ipynb)
* **Finding:** Average Month 1 retention is **0.48%**. This represents a "lower-bound" estimate, as the current model includes all order statuses (including `canceled` and `unavailable`).
* **Analytical Insight:** Even with data noise, the platform operates as a **pure-acquisition engine**. The product mix (infrequent purchases like furniture) prevents natural organic retention.
* **Business Implication:** Extremely high dependency on new customer acquisition. The business model is unsustainable if CAC (Customer Acquisition Cost) is not offset by very high margins on single transactions.
* **Action Plan:** * **Data QA:** Filter analysis by `order_status = 'delivered'` to isolate successful transactions from technical churn.
    * **Strategic Pivot:** Investigate high-frequency categories (FMCG) to build a "habitual" layer on top of the existing marketplace.

#### 2. [Logistics Bottlenecks in the Northeast (Nordeste)](https://github.com/tikhont/olist-ecommerce/blob/main/notebooks/03_Delivery_Analysis.ipynb)
* **Finding:** Identified a systemic delay in the **AL (Alagoas) state**, with a delay rate of **23.9%**.
* **Specifics:** Deliveries to the North and Northeast regions suffer from a **13–16 day lag** beyond the estimated date. 
* **Business Risk:** These delays directly correlate with poor review scores and the "one-and-done" customer behavior. Logistical failure is likely a primary driver of the low retention rate.
* **Recommendation:** Establish regional distribution centers or strategic "last-mile" partnerships in the Nordeste region. Improving delivery speed is a more effective retention tool than any loyalty program in this context.

#### 3. [Realistic RFM Segmentation (The "One-Timer" Problem)](https://github.com/tikhont/olist-ecommerce/blob/main/notebooks/04_RFM_Segmentation.ipynb)
*Standard RFM models struggle here because ~97% of the database are one-time buyers. The strategy must be adjusted:*

* **HIGH PRIORITY: "Promising" Segment (~19%)**
    * *Who:* Recent one-time buyers. They are the only "warm" leads.
    * *Action:* **Aggressive Cross-Sell.** Trigger automated recommendations based on their first purchase within the first 7 days.
* **CRITICAL AUDIT: "New Customers" (~38%)**
    * *Who:* Users with their first and only purchase.
    * *Action:* **Experience Survey.** Instead of selling, ask *why* they haven't returned. Was it the delivery delay? Use this data to fix the product-market fit.
* **LOW PRIORITY: "Hibernating" (~37%)**
    * *Who:* Historical one-time buyers who haven't engaged in 12+ months.
    * *Action:* **Data Archiving.** Do not waste marketing budget. Their LTV is effectively zero; focus resources on the "Promising" segment instead.

---

### 🛠 Technical Implementation & Engineering Standards

The project is built as a **production-ready local environment**, moving beyond simple script execution to a reproducible data engineering workflow.

| Requirement | Implementation & Rationale |
| :--- | :--- |
| **Reproducible Environment** | Deployed **PostgreSQL within Docker** to eliminate "works on my machine" issues. This ensures consistent schema behavior and environment isolation. |
| **Data Pipeline (ETL)** | Developed an automated ingestion flow using **Kaggle API** and **Pandas**. Unlike manual CSV loading, this allows for one-click updates of the entire 100k+ record dataset. |
| **Architectural DRYness** | Abstracted all database logic into `db_utils.py`. This reduces technical debt and ensures that connection pooling and credentials are managed centrally. |
| **Advanced Analytical SQL** | Leveraged **CTEs and Window Functions** to handle complex temporal logic (Month Lag, First Purchase Minima). This approach prioritizes query modularity and auditability over nested subqueries. |
| **Schema Integrity** | Integrated **SQL data type casting** during ingestion to ensure that timestamps and IDs are treated as primary objects, not strings, preventing calculation errors in later stages. |

---

### 🚀 Future Roadmap & Scalability

While the current version demonstrates core technical competency, the following steps are planned to bring the project closer to an enterprise-grade analytical framework:

1. **Data Transformation Layer (dbt):** Transition from raw SQL in notebooks to **dbt (Data Build Tool)**. This will allow for better version control of data models, automated documentation, and lineage tracking.
2. **Automated Data Quality Testing:** Implement **Great Expectations** or dbt-tests to validate data integrity (e.g., ensuring no negative prices, verifying unique customer keys).
3. **Advanced Predictive Modeling:** Develop a **Churn Prediction Model** using Scikit-Learn to identify "Promising" customers with a high probability of churn based on their initial delivery experience.
4. **Interactive BI Dashboard:** Connecting the PostgreSQL container to **Looker Studio** or **Tableau** for real-time stakeholder visibility.
5. **Security & Secrets Management:** Moving Kaggle API credentials from scripts to a protected `.env` environment to follow security best practices.

***

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

### ⚙️ How to Run Locally (Reproducibility)

Follow these steps to reproduce the environment and analysis. 

**Prerequisites:**
* **Docker** installed and running.
* **Python 3.10+**.
* **Kaggle API Token** (ensure `kaggle.json` is in `~/.kaggle/` or your project root).

#### 1. Setup Environment

1. Clone and enter the repository
```bash
git clone https://github.com/tikhont/olist-ecommerce
cd olist-ecommerce
```

2. Create a CLEAN virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 2. Launch PostgreSQL Container

We use Docker to maintain a production-like database environment without polluting the host OS.

```bash
# Start Postgres container
docker run --name olist-db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres

# Create the target database
docker exec -it olist-db psql -U postgres -c "CREATE DATABASE olist;"
```

#### 3. Run Analysis
Launch Jupyter and execute notebooks in sequential order (**01 -> 02 -> 03 -> 04**).

```bash
jupyter-lab
```

*Note:* Notebook **01_ETL_Ingest.ipynb** will automatically fetch data via Kaggle API and populate your PostgreSQL instance.
