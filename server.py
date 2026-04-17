from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# 👇 APNA NVIDIA API KEY YAHA DAL
client = OpenAI(
    api_key="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",  # 👈 apna real key daal
    base_url="https://integrate.api.nvidia.com/v1"
)

# ✅ HOME ROUTE (404 FIX)
@app.route("/")
def home():
    return "Jarvis server is running 🚀"

# ✅ AI ROUTE
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")

    try:
        response = client.chat.completions.create(
            model="meta/llama3-8b-instruct",
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart AI assistant."},
                {"role": "user", "content": query}
            ]
        )

        return jsonify({
            "response": response.choices[0].message.content
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "response": "Error connecting to AI"
        })

# ✅ RUN SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)