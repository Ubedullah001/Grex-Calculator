# 🧵 Grex Yarn Count Calculator

A simple web application made with **Python and Streamlit** to calculate yarn count in the **Grex (Tex) system**.

## 📌 About the App

This application helps textile engineering students and users calculate yarn count using the weight and length of yarn.

The user enters:

* Yarn weight in grams
* Yarn length in meters

The application calculates the yarn count in **Tex and Grex**.

## 📐 Formula

### Grex

**Grex = (Weight in grams × 10,000) ÷ Length in meters**

### Tex

**Tex = (Weight in grams × 1,000) ÷ Length in meters**

## 🧮 Example

If:

* Weight = 5 grams
* Length = 1000 meters

Then:

**Tex = (5 × 1000) ÷ 1000 = 5 Tex**

**Grex = (5 × 10,000) ÷ 1000 = 50 Grex**

## 🛠️ Technologies Used

* Python
* Streamlit

## 📁 Project Files

```text
Grex-Yarn-Count-Calculator/
│
├── App.py
├── requirements.txt
└── README.md
```

## 🚀 Run the App

Install the required package:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run App.py
```

The application will open in your web browser.

## 🌐 Deploy on Streamlit Community Cloud

1. Upload `App.py`, `requirements.txt`, and `README.md` to your GitHub repository.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select your repository.
5. Select `App.py` as the main file.
6. Click **Deploy**.

Your Grex Yarn Count Calculator will then be available as a web app.

## 🎓 For Textile Engineering

This calculator is useful for basic yarn-count calculations in textile production and yarn testing.
