from random import choice
import os
import json
CONFIG = json.load(open("intents.json", "r", encoding="utf-8"))
ERROR_RESPONSES=CONFIG["ERROR_RESPONSES"]
INTENTS=CONFIG["INTENTS"]


def debug(result: str):
    print(f"DEBUG: {result}")

def telemetry_send_input(result: str):
    print(f"TELEM: {result}")

def generate(inp: str):
    inp = inp.lower()
    inp = inp.replace("á", "a")
    inp = inp.replace("é", "e")
    inp = inp.replace("í", "i")
    inp = inp.replace("ó", "o")
    inp = inp.replace("ú", "u")
    telemetry_send_input(inp)
    intent = [intent for intent in INTENTS if inp in [j.lower() for j in intent["patterns"]]]
    if intent == []:
        out = choice(ERROR_RESPONSES)
        debug(f"{inp};unknown;{out}")
        return out
    else:
        out = choice(intent[0]["responses"])
        debug(f"{inp};{intent[0]['tag']};{out}")
        return out