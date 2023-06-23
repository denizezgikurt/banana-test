import banana_dev as banana

p = {
    "prompt": "Hello I am a [MASK] model."
}

api_key = ""
model_key = ""

out = banana.run(api_key, model_key, p)
print(out["modelOutputs"][0])

