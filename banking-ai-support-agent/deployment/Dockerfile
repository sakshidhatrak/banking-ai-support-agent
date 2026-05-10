FROM python:3.11-slim

# =========================================
# WORK DIRECTORY
# =========================================

WORKDIR /app

# =========================================
# COPY REQUIREMENTS
# =========================================

COPY requirements.txt .

# =========================================
# INSTALL DEPENDENCIES
# =========================================

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# =========================================
# COPY PROJECT FILES
# =========================================

COPY . .

# =========================================
# STREAMLIT PORT
# =========================================

EXPOSE 8501

# =========================================
# START APPLICATION
# =========================================

CMD ["python", "-m", "streamlit", "run", "ui/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]