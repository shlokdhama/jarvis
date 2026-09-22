from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")
MODEL=os.getenv("GEMINI_MODEL")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set")
if not MODEL:
    raise ValueError("GEMINI_MODEL is not set")