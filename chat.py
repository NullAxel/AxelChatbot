from wit import Wit
import os
import json
from random import choice
from dotenv import load_dotenv
load_dotenv()
access_token=os.environ["WIT_ACCESS_TOKEN"]
client = Wit(access_token)
CONFIG = json.load(open("responses.json", "r", encoding="utf-8"))
ERROR_RESPONSES=CONFIG["ERROR_RESPONSES"]
INTENTS=CONFIG["RESPONSES"]
logs = open("logs.txt", "a", encoding="utf-8")
def generate(inp: str):
    logs.write(inp)
    print(inp)
    result = client.message(inp)
    if result["intents"] == []:
        intent_name = ""
        intent_conf = 0
    else:
        intent_name = result["intents"][0]["name"]
        intent_conf = result["intents"][0]["confidence"]
    if intent_name == "" or intent_conf < 0.925:
        return {"result": choice(ERROR_RESPONSES), "intent": "unknown", "input": inp}
    else:
        try:
            response = choice(INTENTS[intent_name])
            return {"result": response, "intent": intent_name, "input": inp}
        except KeyError:
            return {"result": choice(ERROR_RESPONSES), "intent": intent_name, "input": inp, "error": [0, "Missing intent '" + intent_name + "' in config."]}
        
