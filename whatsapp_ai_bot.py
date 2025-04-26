from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

OPENAI_API_KEY = "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"  # өөрийн API KEY-г энд тавина


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    # New OpenAI API call for v1.x
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Чи хүүхдүүдэд тусалдаг найрсаг AI туслах байна.",
            },
            {"role": "user", "content": incoming_msg},
        ],
    )
    reply = response.choices[0].message.content
    msg.body(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)
