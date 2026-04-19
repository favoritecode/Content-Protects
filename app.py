from flask import Flask, request, make_response
import requests

app = Flask(__name__)

SHEET_URL = "https://opensheet.elk.sh/YOUR_SHEET_ID/Sheet1"

# 🔍 check password + limit
def check_password(pw, item):
    data = requests.get(SHEET_URL).json()

    for row in data:
        if row["Password"] == pw and row["Url"] == item:

            used = int(row["Used"])
            limit = int(row["Limit"])

            if used >= limit:
                return "LIMIT"   # 🔥 limit exceeded

            return "OK"

    return "FAIL"


@app.route("/")
def home():
    item = request.args.get("item")

    return f"""
    <h2>🔒 Unlock {item}</h2>
    <input type="password" id="pw">
    <button onclick="go()">Unlock</button>

    <script>
    async function go(){{
        let pw = document.getElementById("pw").value;

        let res = await fetch("/check?pass=" + pw + "&item={item}");
        let text = await res.text();

        if(text === "OK"){{
            document.cookie = "pw=" + pw;
            window.location.href = "/content?item={item}";
        }}
        else if(text === "LIMIT"){{
            alert("❌ Limit Reached!");
        }}
        else{{
            alert("Wrong Password ❌");
        }}
    }}
    </script>
    """


@app.route("/check")
def check():
    pw = request.args.get("pass")
    item = request.args.get("item")

    result = check_password(pw, item)

    return result


@app.route("/content")
def content():
    item = request.args.get("item")
    pw = request.cookies.get("pw")

    if check_password(pw, item) != "OK":
        return "Access Denied ❌"

    # 🔥 CONTENT
    if item == "video1":
        return "<h1>🎬 Video 1</h1>"
    elif item == "video2":
        return "<h1>🎬 Video 2</h1>"
    else:
        return "Invalid"


import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
