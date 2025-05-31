# 🌾 Crop Yield Prediction App
This project predicts crop productivity (hg/ha) using environmental inputs like rainfall, temperature, and pesticide usage — built using machine learning and deployed with Streamlit.

## 🔧 Technologies Used

- 🧠 *Random Forest Regressor* for prediction
- ⚙️ *MinMaxScaler* for normalization
- 🌐 *Streamlit* for live UI app
- 📊 *Jupyter Notebook* for data cleaning, EDA & model training
---

## 📁 Project Files

| File | Description |
|------|-------------|
| Capstone_project.ipynb | Complete EDA, preprocessing, model training & evaluation |
| crop_yield_predictor.py | Streamlit web app to input variables & get yield predictions |
| CROP YIELD PREDICTION USING MACHINE LEARNING.pptx | Final project presentation with visualizations & results |

---
## 🚀 Sample Prediction

📌 For the following inputs:
- Rainfall: 657 mm/year  
- Temperature: 21°C  
- Pesticides Used: 3305 tonnes  
- Crop: *Potatoes*

🟢 *Predicted Yield:* 164,312 hg/ha

---

## 📦 How to Run the Streamlit App Locally
```bash
git clone https://github.com/MustafaMah2003/Crop-Yield-Prediction.git
cd Crop-Yield-Prediction
streamlit run crop_yield_predictor.py
