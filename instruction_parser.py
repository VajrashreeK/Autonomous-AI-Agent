def parse_instruction(instruction):
    plan = {}
    instruction = instruction.lower()

    if "headline" in instruction:
        plan["browser"] = {"action": "fetch_news", "topic": "AI", "limit": 5}
        plan["file"] = {"action": "save_text", "filename": "ai_headlines.txt"}

    elif "review" in instruction and "smartphone" in instruction:
        plan["browser"] = {"action": "fetch_reviews", "product": "smartphone"}
        plan["file"] = {"action": "save_summary", "filename": "smartphone_summary.txt"}

    elif "renewable energy" in instruction and "analyze" in instruction:
        plan["browser"] = {"action": "fetch_data", "topic": "renewable energy"}
        plan["terminal"] = {"action": "analyze_data"}
        plan["file"] = {"action": "save_pdf", "filename": "energy_report.pdf"}

    else:
        raise ValueError("Unsupported instruction. Try a sample test case.")

    return plan
