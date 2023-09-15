import requests

from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


def serach_location(post_code):
    url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={post_code}"
    response = requests.get(url)
    data: map = response.json()
    if data["status"] == 200:
        if "results" in data and (results := data["results"]):
            return results[0]
        return {"error": "うまくデータを取得できませんでしたもう一回試してみてください"}
    return {"error": data["message"]}


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        result = serach_location(request.form["code"])
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
