# Text Analysis Project

## 📖 Description:
This project extracts activities from text using a custom NLP model built with spaCy.

---

## 🛠️ Requirements:
- Python 3.7 or later

---

## 🚀 How to Run:

1. **Create Virtual Environment:**
    ```bash
    python -m venv textanalyzer
    ```

2. **Activate Virtual Environment:**
    - On **Windows:**
      ```bash
      textanalyzer\Scripts\activate
      ```
    - On **MacOS/Linux:**
      ```bash
      source textanalyzer/bin/activate
      ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm  # Optional, if needed for dependencies
    ```

4. **Start Backend:**
    ```bash
    python app.py
    ```

5. **Start Frontend (Open New Terminal):**
    ```bash
    streamlit run frontend.py
    ```

---

## 🌐 Access:
- Frontend: `http://localhost:8501`
- Backend: `http://127.0.0.1:5000`

---

