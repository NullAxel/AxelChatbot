import json
f = json.load(open("convert/input.json", encoding="utf-8"))
out = []
for i in f["preguntas"]:
    out.append({"tag": i["etiqueta"], "patterns": i["preguntas"], "responses": i["respuestas"]})

json.dump(out, open("convert/output.json", "w", encoding="utf-8"))