from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

# OpenAI API key-г орчны хувьсагчаас авна
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    # OpenAI API руу хүсэлт явуулж байна
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Чи мэргэжлийн, бизнесийн зөвлөгөө өгдөг найдвартай AI туслах байна. Хэрэглэгчийн асуултад тодорхой, үнэн зөв, бодитой, ойлгомжтой хариулт өг.",
            },
            {"role": "user", "content": incoming_msg},
        ],
    )

    reply = response.choices[0].message.content
    msg.body(reply)
    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
