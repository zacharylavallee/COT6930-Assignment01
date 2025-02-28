import requests
import json
import os
import time
import csv

def load_config():
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

def create_payload(model, prompt, target="ollama", **kwargs):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    if kwargs:
        payload["options"] = {key: value for key, value in kwargs.items()}
    return payload

def model_req(payload=None):
    try:
        load_config()
    except:
        return -1, "!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, "!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    if response is None:
        return -1, "!!ERROR!! There was no response (?)"
    elif response.status_code == 200:
        delta = round(delta, 3)
        response_json = response.json()
        result = response_json.get("response") or response_json.get("choices", [{}])[0].get("message", {}).get("content", "")
        return delta, result
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"

PROMPT = ("Step 1: Define personal privacy. Step 2: Define national security. "
          "Step 3: Identify conflicts. Step 4: Suggest a balance.\n\nNow, answer: "
          "What is the ideal balance between personal privacy and national security in the digital age?")
MODEL = "llama3.2:latest"

temperature_values = [0.5, 1.0, 1.5]
num_ctx_values = [500, 5000, 50000]
num_predict_values = [200, 1000, 5000]

baseline_temperature = 1.0
baseline_num_ctx = 100
baseline_num_predict = 100

results = []

def run_experiment():
    global results

    payload = create_payload(MODEL, PROMPT, temperature=baseline_temperature, num_ctx=baseline_num_ctx, num_predict=baseline_num_predict)
    response_time, response_text = model_req(payload)
    results.append(["Baseline", baseline_temperature, baseline_num_ctx, baseline_num_predict, response_time, response_text])

    for temp in temperature_values:
        payload = create_payload(MODEL, PROMPT, temperature=temp, num_ctx=baseline_num_ctx, num_predict=baseline_num_predict)
        response_time, response_text = model_req(payload)
        results.append(["Temperature", temp, baseline_num_ctx, baseline_num_predict, response_time, response_text])

    for ctx in num_ctx_values:
        payload = create_payload(MODEL, PROMPT, temperature=baseline_temperature, num_ctx=ctx, num_predict=baseline_num_predict)
        response_time, response_text = model_req(payload)
        results.append(["Context Size", baseline_temperature, ctx, baseline_num_predict, response_time, response_text])

    for predict in num_predict_values:
        payload = create_payload(MODEL, PROMPT, temperature=baseline_temperature, num_ctx=baseline_num_ctx, num_predict=predict)
        response_time, response_text = model_req(payload)
        results.append(["Prediction Length", baseline_temperature, baseline_num_ctx, predict, response_time, response_text])

    for i in range(3):
        payload = create_payload(MODEL, PROMPT, temperature=temperature_values[i], num_ctx=num_ctx_values[i], num_predict=baseline_num_predict)
        response_time, response_text = model_req(payload)
        results.append(["Two Variables", temperature_values[i], num_ctx_values[i], baseline_num_predict, response_time, response_text])

    for i in range(3):
        payload = create_payload(MODEL, PROMPT, temperature=temperature_values[i], num_ctx=num_ctx_values[i], num_predict=num_predict_values[i])
        response_time, response_text = model_req(payload)
        results.append(["Three Variables", temperature_values[i], num_ctx_values[i], num_predict_values[i], response_time, response_text])

    save_results()

def save_results():
    filename = "experiment_results.csv"
    headers = ["Variation Type", "Temperature", "Context Size", "Prediction Length", "Response Time", "Generated Response"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(results)
    
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    run_experiment()
