from env_browser import fetch_news, fetch_reviews, fetch_data
from env_terminal import analyze_data
from env_filesystem import save_text, save_summary, save_pdf

def run_task(plan):
    data = None

    if "browser" in plan:
        task = plan["browser"]
        if task["action"] == "fetch_news":
            data = fetch_news(task["topic"], task["limit"])
        elif task["action"] == "fetch_reviews":
            data = fetch_reviews(task["product"])
        elif task["action"] == "fetch_data":
            data = fetch_data(task["topic"])

    if "terminal" in plan:
        task = plan["terminal"]
        if task["action"] == "analyze_data":
            data = analyze_data(data)

    if "file" in plan:
        task = plan["file"]
        if task["action"] == "save_text":
            save_text(data, task["filename"])
        elif task["action"] == "save_summary":
            save_summary(data, task["filename"])
        elif task["action"] == "save_pdf":
            save_pdf(data, task["filename"])

    print("Task complete.")
