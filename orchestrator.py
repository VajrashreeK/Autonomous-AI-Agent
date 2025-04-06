from env_browser import fetch_ai_headlines
from env_terminal import get_smartphone_reviews
from env_filesystem import save_summary, save_text

def run_task(plan):
    task_type = plan["type"]

    if task_type == "summarize_smartphones":
        reviews = get_smartphone_reviews()
        save_summary(reviews)

    elif task_type == "fetch_ai_news":
        headlines = fetch_ai_headlines()
        save_text("ai_headlines.txt", "\n".join(headlines))

    elif task_type == "save_last_result":
        save_text("last_result.txt", "No previous result to save in this mock version.")

    else:
        raise ValueError("Unknown task type")
