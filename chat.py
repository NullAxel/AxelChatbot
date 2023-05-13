from random import choice
import os
import json
CONFIG = json.load(open("config.json", "r"))
ERROR_RESPONSES=CONFIG["ERROR_RESPONSES"]
INTENTS=CONFIG["INTENTS"]


def debug(result: str):
    print(f"DEBUG: {result}")

def telemetry_send_input(result: str):
    print(f"TELEM: {result}")

def generate(inp: str):
    telemetry_send_input(str)
    intent = [intent for intent in INTENTS if inp in intent["patterns"]]
    if intent == []:
        out = choice(ERROR_RESPONSES)
        debug(f"{inp};unknown;{out}")
        return out
    else:
        out = choice(intent[0]["responses"])
        debug(f"{inp};{intent[0]['tag']};{out}")
        return out