Here’s a clean, professional README you can paste directly into your `README.md`:

---

# 🚀 AI Slogan Generator (Azure OpenAI)

A Python-based AI-powered slogan generator built using **Azure OpenAI**.
This project dynamically generates marketing slogans using prompt engineering and configurable tone, audience, and style inputs.

---

## 📌 Overview

This application demonstrates:

* ✅ Secure API key management using `.env`
* ✅ Azure OpenAI SDK integration
* ✅ Prompt templating with variable injection
* ✅ Style-based slogan generation (Social vs Corporate)
* ✅ Structured API error handling
* ✅ Config validation before execution

The system builds reusable marketing prompts and generates AI-driven slogans based on selected style and constraints.

---

## 🧠 How It Works

The project follows a 4-step structure:

### 1️⃣ Configuration

* Loads Azure credentials from environment variables
* Validates required values before making API calls

### 2️⃣ Prompt Library

Two reusable prompt templates:

* **Social Media Style**
* **Corporate/B2B Style**

Prompts dynamically inject:

* Product name
* Target audience
* Tone

### 3️⃣ Execution

* Constructs the full prompt
* Sends it to Azure OpenAI
* Returns AI-generated slogans

### 4️⃣ Test Runs

Two sample executions:

* VoltRush Energy (Social)
* IronClad Security (Corporate)

---

## 🛠 Requirements

* Python 3.9+
* Azure OpenAI resource
* Deployed model (e.g. `gpt-4o-mini`)
* Installed dependencies

Install required packages:

```bash
pip install openai python-dotenv
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

⚠️ Important:

* The endpoint must be the base resource URL.
* Do NOT include `/openai/deployments/...`
* Never commit your `.env` file.

Make sure `.env` is in your `.gitignore`.

---

## ▶️ Running the Project

From the project directory:

```bash
python src/assignment_week3.py
```

Expected output:

```
------------------------------------------------------------
🔹 GENERATING SLOGANS FOR: VoltRush Energy (social style)
------------------------------------------------------------

[STEP 1] CONSTRUCTED PROMPT (Variable Injection):
...

[STEP 2] CONNECTING TO AZURE...

✅ SUCCESS! AI RESPONSE:
...
```

---

## 🧩 Project Structure

```
AI-Slogan_Generator/
│
├── src/
│   └── assignment_week3.py
│
├── .env
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🎯 Custom Usage

You can generate custom slogans by modifying:

```python
run_generator("social", "Your Product", "Your Audience", "Your Tone")
```

Available styles:

* `"social"`
* `"corporate"`

Example:

```python
run_generator("social", "FitFuel Protein", "Gym Enthusiasts", "Energetic")
```

---

## ⚙️ Key Features

* Dynamic prompt construction
* Style-based generation logic
* Secure credential management
* Structured API integration
* Exception handling for API failures

---

## 🔒 Security Best Practices Used

* Environment variables for credentials
* Early validation of config values
* `.gitignore` protection for `.env`
* No hardcoded API keys

---

## 🧪 Example Output

**Social Style:**

```
Power Your Play ⚡
Game On. Energy Up 🎮
Unleash the Rush 🚀
```

**Corporate Style:**

```
Enterprise-grade protection for modern infrastructure.
Built for reliability. Engineered for trust.
Security solutions that scale with confidence.
```

---

## 📚 Technologies Used

* Python
* Azure OpenAI
* python-dotenv
* Prompt Engineering

---

## 📄 License

This project is for educational and demonstration purposes.

---

If you'd like, I can also generate:

* 🔥 A more “portfolio-ready” README version
* 🎓 A submission-ready academic version
* 🏢 A production-grade README format
* 🌐 A version with badges and GitHub styling enhancements
