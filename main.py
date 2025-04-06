from instruction_parser import parse_instruction
from orchestrator import run_task
import sys

def main():

    print("Enter your instruction:")
    instruction = sys.stdin.read().strip()


    try:
        plan = parse_instruction(instruction)
        run_task(plan)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
