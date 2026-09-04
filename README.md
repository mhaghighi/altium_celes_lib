# Celestial Altium Library (SQLite / DBLib Edition)

This repository provides an easy setup for using the open-source **Celestial Altium Library** as an Altium Designer Database Library (`.DbLib`) backed by a local SQLite database (`.sqlite` / `.sqlite3`).

Using SQLite removes the need for local Access/Excel setups or maintaining external SQL servers while keeping your library fast, portable, and version-control friendly.

---

## Prerequisites

### 1. SQLite ODBC Driver
Altium Designer communicates with SQLite databases via ODBC. You must install the SQLite ODBC Driver on your machine:

* **Download Link:** [SQLite ODBC Driver by Christian Werner](http://www.ch-werner.de/sqliteodbc/)
* **Important:** Ensure you download and install the **64-bit driver** (`sqliteodbc_w64.exe`) to match 64-bit Altium Designer versions (AD18 and newer). If you run an older 32-bit Altium version, install the 32-bit driver instead.

### 2. Celestial Altium Library Assets
Download the component footprints, 3D models, schematic symbols, and database files from the official Celestial project:

* **Original Repository:** [Celestial Altium Library on GitHub](https://github.com/issus/altium-library)
* Clone or download the assets (symbols, footprints, and database) to a persistent location on your storage drive (e.g., `C:\altium_library\`).

---

## Setup Instructions

### Step 1: Install the ODBC Driver
Run the installer downloaded from the link above and follow the standard installation wizard.

### Step 2: Configure the `.DbLib` File
1. Open the included `.DbLib` file in Altium Designer.
2. Under the **Source of Connection** section, choose **Use Connection String**.
3. Update the connection string with the exact absolute path to where your `.sqlite3` file is stored:

```text
Provider=MSDASQL.1;Persist Security Info=False;Extended Properties="Driver={SQLite3 ODBC Driver};Database=C:\altium_library\celestial.sqlite3;"