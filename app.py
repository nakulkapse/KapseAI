from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)


def kapseAI(question):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<www.kapseai.com>",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<KapseAI>",  # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "user", "content": f"{question}"}],
    )
    return completion.choices[0].message.content


@app.route("/", methods=["GET", "POST"])
def helloWorld():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = kapseAI(question)
    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)