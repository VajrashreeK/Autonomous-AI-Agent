# Autonomous AI Agent

This project is an **Autonomous AI Agent** that can understand natural language instructions and execute them using three types of environments:

- **Browser Environment**: For web scraping or fetching online content
- **Terminal Environment**: For simulating command-line tasks like getting data
- **File System Environment**: For saving data to files (text, summary, PDF)

---

## Approach

1. **Natural Language Input**
   - The user types an instruction like:
     > Find top 5 AI news headlines and save to file

2. **Instruction Parsing** (`instruction_parser.py`)
   - Converts the instruction to a predefined `task type`
   - Example:
     - "AI news" => `fetch_ai_news`
     - "smartphone summary" => `summarize_smartphones`

3. **Task Orchestration** (`orchestrator.py`)
   - Takes the task type and decides:
     - What environment to use
     - Which functions to call
   - Calls the browser to fetch data and filesystem to save it

4. **Environment Handlers**
   - **Browser** (`env_browser.py`) – Scrapes AI news from the web (mocked)
   - **Terminal** (`env_terminal.py`) – Simulates reviews of smartphones
   - **Filesystem** (`env_filesystem.py`) – Saves output as `.txt` or `.pdf`

5. **Execution Driver** (`main.py`)
   - Accepts instruction from user (CLI input or piped)
   - Parses and runs the complete task

---

## Run

### 1. Clone the repo
```bash
https://github.com/VajrashreeK/Autonomous-AI-Agent.git
cd Autonomous-AI-Agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the agent
```bash
python main.py
```
Then enter instruction like:
```text
Find top 5 AI news headlines and save to file
```

Or pipe the instruction:
```bash
echo "Find top 5 AI news headlines and save to file" | python main.py
```

---

## Output
- Saved files like `ai_headlines.txt` or `smartphone_summary.txt` will appear in the project folder.

---



