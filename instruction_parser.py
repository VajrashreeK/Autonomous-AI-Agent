def parse_instruction(instruction):
    instruction = instruction.lower()

    if "smartphone" in instruction and "summary" in instruction:
        return {
            "type": "summarize_smartphones"
        }

    elif "ai news" in instruction or "ai headlines" in instruction:
        return {
            "type": "fetch_ai_news"
        }

    elif "save to file" in instruction or "save them" in instruction:
        # If it's just asking to save, assume recent task
        return {
            "type": "save_last_result"
        }

    else:
        raise ValueError("Unsupported instruction. Try a sample test case.")
