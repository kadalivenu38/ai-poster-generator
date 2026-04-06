# 🎨 AI Poster & Meme Generator

An AI-powered web application that automatically generates event posters using Generative AI.
Users provide a topic, tone, and style — the system produces a headline, tagline, and a downloadable poster image instantly.

Live-URL : https://ai-poster-generator-9wzuvpeychuqnhldbvh7s2.streamlit.app/

---

## 📌 Problem Statement

Students and college clubs frequently need posters for events, hackathons, workshops, and social media promotions.
However, many students lack graphic design skills or access to professional tools such as Photoshop or Canva Pro.
Creating posters manually takes time and requires design knowledge.

This project provides an automated solution that generates creative posters using Artificial Intelligence.

---

## 💡 Proposed Solution

The system accepts event details from the user and uses a Generative AI model to:

* Generate a poster headline
* Generate a catchy tagline
* Create a styled poster image
* Allow the user to download the final poster

This eliminates the need for design experience and significantly reduces the time required to create promotional material.

---

## ⚙️ Tech Stack

**Frontend & Interface**

* Streamlit

**Backend**

* Python

**AI Model**

* Google Gemini API (gemini-3-flash-preview)

**Libraries Used**

* Pillow (Image processing)
* python-dotenv (Environment variables)
* Requests (Image fetching)

---

## 🧠 System Workflow

1. User enters event topic, tone, and style.
2. The system sends a prompt to the Gemini AI model.
3. AI generates a short caption and tagline.
4. A background image is fetched.
5. Text is styled and rendered onto the image using Pillow.
6. Poster is displayed and available for download.

---

## 📂 Project Structure

```
ai-poster-generator/
│
├── app.py              # Streamlit UI
├── ai_caption.py       # AI text generation using Gemini
├── poster.py           # Poster image creation
├── requirements.txt
├── .env                # API key (not uploaded to GitHub)
│
├── Montserrat-Bold.ttf             # Typography assets
├── Montserrat-Regular.ttf
│
└── README.md
```

---

## 🚀 Installation & Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-poster-generator.git
cd ai-poster-generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Add the API key inside Streamlit → App Settings → Secrets:

```
GEMINI_API_KEY="your_api_key_here"
```

---

## 🖼️ Features

* AI caption generation
* AI tagline creation
* Styled typography poster
* Automatic background image
* Downloadable poster
* Simple user interface

---

## 📈 Future Scope

* Custom poster size selection
* Multiple templates
* Logo upload option
* Social media auto-format (Instagram, WhatsApp)
* Meme template generator
* User accounts and saved posters

---

## 👨‍💻 Author

**Venu**
B.Tech Student – Computer Science - (AI)

---

## 📜 License

This project is for educational and internship demonstration purposes.
