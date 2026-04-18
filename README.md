# Legal Intelligence System (LIS) ⚖️

A high-precision, multi-agent framework designed to automate complex legal research within the Indian Judicial System. This system transitions from simple AI responses to a verified, multi-stage legal discovery process.

## 🚀 Features

* **Multi-Agent Architecture:** Utilizes three distinct agents (Searcher, Writer, Corrector) to ensure a high-fidelity output.
* **Real-time Grounding:** Integrated with **Tavily Search** and **BeautifulSoup** to fetch the latest rulings from 2025-2026.
* **Local LLM Support:** Powered by **Ollama** (Gemma 31B Cloud) for secure and robust processing.
* **Professional UI:** A sleek, "Plus Jakarta Sans" inspired Streamlit dashboard for a premium user experience.
* **Strict Recency Mode:** Specifically programmed to detect queries about recent legal developments and filter for the latest data.

---

## 🏗️ Project Structure

```text
MY AGENT/
├── .env                  # API Keys (Tavily, Ollama)
├── agents.py             # Agent definitions and System Prompts
├── main.py               # Streamlit UI and Frontend logic
├── pipline.py            # CLI-based workflow execution
├── tools.py              # Custom Web Search & Scraping tools
├── requirements.txt      # Project dependencies
└── web_design.pdf        # UI/UX design references
🛠️ Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/Dipin-Parmar-001/Legal-Intelligence-System.git](https://github.com/Dipin-Parmar-001/Legal-Intelligence-System.git)
cd LexAI-Legal-Research-Agent
Install Dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file in the root directory and add your credentials:

Code snippet
TAVILY_API_KEY=your_tavily_key_here
Run the Application:

Web UI: streamlit run main.py

CLI Version: python pipline.py

🤖 The Pipeline logic
Search Agent: Breaks down the legal query into sub-questions, performs targeted web searches, and validates sources (Supreme Court, High Courts, LiveLaw).

Writer Agent: Takes the research bundle and converts it into a structured legal brief following professional drafting standards.

Corrector Agent: Acts as a legal reviewer to remove any hallucinations, ensure the law is applied correctly to the facts, and verify citations.

🤝 Developed By
Dipin Parmar

GitHub: @Dipin-Parmar-001
