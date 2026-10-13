# 🧵 Textile Hub — Textile Industry Dashboard

Textile Hub is a simple and interactive web application developed
using Python and Streamlit.

It provides textile production information, a production planning
calculator, and a reference guide for common textile fibers.

## Features

### 1. Overview Dashboard
- Monthly production statistics
- Sample textile production chart
- Textile manufacturing process
- Quality inspection checklist

### 2. Production Planner
- Calculate required fabric
- Estimate process waste
- Calculate gross production requirements
- Estimate production time
- Calculate hourly output
- Download production reports as CSV

### 3. Fiber Guide
- Information about cotton
- Wool and silk details
- Polyester and nylon information
- Viscose and jute details
- Searchable fiber reference table

### 4. Attractive Interface
The application uses a clean color palette:

- Deep Teal: #123C3A
- Teal: #1E7168
- Sage Green: #A8C9BD
- Soft Cream: #F4F8F7

## Technologies Used

- Python
- Streamlit
- Pandas

## Project Structure

textile_industry_streamlit/
│
├── App.py
├── requirements.txt
└── README.md

## Installation and Setup

### Step 1: Install Python

Install Python 3.10 or newer.

### Step 2: Download the Project

Download the project files and save them in one folder.

### Step 3: Install Dependencies

Open your terminal inside the project folder and run:

pip install -r requirements.txt

### Step 4: Run the Application

Run the following command:

streamlit run App.py

The application will open in your browser.

The default local address is usually:

http://localhost:8501

## Upload to GitHub

1. Sign in to GitHub.
2. Create a new repository.
3. Name it textile-industry-streamlit.
4. Upload App.py, requirements.txt, and README.md.
5. Commit your changes.

Alternatively, use Git commands:

git init
git add App.py requirements.txt README.md
git commit -m "Add Textile Hub Streamlit application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/textile-industry-streamlit.git
git push -u origin main

Replace YOUR-USERNAME with your GitHub username.

## Deploy Online

You can deploy this application using Streamlit Community Cloud.

Website:
https://share.streamlit.io/

Connect your GitHub repository and select App.py
as the main application file.

## Important Note

The dashboard uses sample production values for demonstration.
The production planner provides basic estimates and does not replace
verified factory production calculations.

## Future Improvements

- Spinning production calculator
- Yarn count calculator
- Fabric GSM calculator
- Textile quality testing
- Dyeing and finishing information
- Production cost estimation
- Real-time factory production monitoring

## License

This project is intended as a learning and development starter project.
