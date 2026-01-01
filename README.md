# NovaAct Web Data Parser

**NovaAct Web Data Parser** is a simple, AI-powered Streamlit application that turns any website into structured JSON data based on your instructions and schema.

With human-like web interaction powered by NovaAct, you can extract customized data from any webpage — all through a natural instruction interface.

---

## Features
- 🌐 Navigate to any website dynamically
- ✍️ Provide human-readable instructions for extraction
- 🧩 Define your own JSON structure for the output
- ⚡ Powered by NovaAct API (automation + AI agent actions)
- 🧹 Clean and parse the extracted data reliably
- 📥 Download the extracted structured data
- 🔐 Supports API key authentication
- 🧑‍💻 Headless mode option for faster extraction

---

## How it Works
1. Enter your **NovaAct API Key**.
2. Provide the **Website URL** you want to extract data from.
3. Write simple **human instructions** about what data you want to fetch.
4. Specify the **target JSON structure** you expect.
5. Click **Extract Data** — and get neatly formatted JSON output!

Example:
- **Website URL:** `https://www.example-hotel-site.com`
- **Instructions:** "Find the cheapest hotels in London from June 10 to June 15."
- **JSON Structure:** 
    ```json
    {
      "hotel_name": "",
      "city": "",
      "from_date": "",
      "to_date": "",
      "price_per_night": ""
    }
    ```

---

## Setup and Installation

1. Clone the repository:

```bash
git clone git@ssh.gitlab.aws.dev:wwso-gtm-specialists-dev/genai-experiments/NovaAct_Web_Data_Parser.git
cd NovaAct_Web_Data_Parser
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Set your `NOVA_ACT_API_KEY` as an environment variable:

```bash
export NOVA_ACT_API_KEY=your-api-key-here
```

4. Run the Streamlit app:

```bash
streamlit run nova_act_streamlit.py
```

---

## Requirements
- Python 3.8+
- Streamlit
- NovaAct Python SDK
- Chrome or Chromium browser installed (for browser automation)

---

## Folder Structure

```
novaact-web-data-parser/
├── nova_act_streamlit.py           # Main Streamlit application
├── README.md                       # Project documentation
├── requirements.txt
```