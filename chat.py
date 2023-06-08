from wit import Wit
import os
import json
from random import choice
from dotenv import load_dotenv
from wolframalpha import Client as WAClient
from translate import Translator
load_dotenv()
access_token=os.environ["WIT_ACCESS_TOKEN"]
client = Wit(access_token)
CONFIG = json.load(open("responses.json", "r", encoding="utf-8"))
ERROR_RESPONSES=CONFIG["ERROR_RESPONSES"]
INTENTS=CONFIG["RESPONSES"]
SMART=CONFIG["SMART"]
waclient = WAClient(os.environ["WA_APP_ID"])

def wolframalpha(inp: str, lang: str = "es"):
    translator_from = Translator(from_lang=lang, to_lang="en")
    translator_to = Translator(from_lang="en", to_lang=lang)
    eninp = translator_from.translate(inp)
    res = waclient.query(eninp)
    result = next(res.results).text
    esresult = translator_to.translate(result)
    return esresult
def generate(inp: str, args = {}):
    result = client.message(inp)
    if result["intents"] == []:
        intent_name = ""
        intent_conf = 0
    else:
        intent_name = result["intents"][0]["name"]
        intent_conf = result["intents"][0]["confidence"]
    print(intent_name)
    if intent_name == "" or intent_conf < 0.925:
        try:
            result = wolframalpha(inp, lang="es")
            return {"result": result, "intent": intent_name, "input": inp, "with": "wolframalpha"}
        except StopIteration:
            return {"result": choice(ERROR_RESPONSES), "intent": intent_name, "input": inp, "with": "error"}
    else:
        try:
            if str(args.get("mode")) == "smart":
                s=INTENTS
                s.update(SMART)
                response = choice(s[intent_name]).format(args=args)
            else:
                response = choice(INTENTS[intent_name])
            return {"result": response, "intent": intent_name, "input": inp, "with": "responses"}
        except KeyError:
            return {"result": choice(ERROR_RESPONSES), "intent": intent_name, "input": inp, "with": "error"}
        
