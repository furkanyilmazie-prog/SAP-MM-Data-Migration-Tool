# 📦 SAP MM Data Migration Tool (Legacy to ERP)

> A specialized data engineering project designed to bridge the gap between legacy Excel systems and SAP ERP (MM Module) by automating data transformation.

## 🚀 The Business Problem
During ERP implementation, importing massive amounts of procurement data manually is error-prone. This tool automates the extraction and transformation process to ensure data integrity before uploading to SAP via BAPI or IDocs.

## 🛠️ Key Functionalities
* **Data Transformation:** Converts flat Excel procurement records into hierarchical JSON structures compatible with SAP BAPI functions.
* **Process Automation:** Eliminates human error in manual data entry.

## ⚙️ Technical Stack
* **Language:** Python
* **Library:** Pandas (for data manipulation)
* **Output Format:** SAP-Ready JSON (BAPI_PO_CREATE structure)
