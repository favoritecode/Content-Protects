from flask import Flask, request, make_response, redirect
import requests

app = Flask(__name__)

SHEET_URL = "https://opensheet.elk.sh/YOUR_SHEET_ID/Sheet1"

# 🔍 check password + item
def check_password(pw, item):
    data = requests.get(SHEET_URL).json()

    for row in data:
        if row["password"] == pw and row["item"] == item:
            return True
    return False


# 🔐 HOME PAGE (password input)
@app.route("/")
def home():
    item = request.args.get("item")

    if not item:
        return "No Item ❌"

    return f"""
    <html>
    <body style="background:black;color:white;text-align:center;padding-top:50px;">

    <h2>🔒 Unlock {item}</h2>

    <input type="password" id="pw" placeholder="Enter Password">
    <button onclick="go()">Unlock</button>

    <script>
    async function go(){{
        let pw = document.getElementById("pw").value;

        let res = await fetch("/check?pass=" + encodeURIComponent(pw) + "&item={item}");
        let text = await res.text();

        if(text === "OK"){{
            document.cookie = "pw=" + pw;
            window.location.href = "/content?item={item}";
        }}else{{
            alert("Wrong Password ❌");
        }}
    }}
    </script>

    </body>
    </html>
    """


# 🔍 CHECK API
@app.route("/check")
def check():
    pw = request.args.get("pass")
    item = request.args.get("item")

    if check_password(pw, item):
        return "OK"
    return "FAIL"


# 🔥 CONTENT PAGE (LOCKED)
@app.route("/content")
def content():
    item = request.args.get("item")
    pw = request.cookies.get("pw")

    # 🔐 verify again
    if not check_password(pw, item):
        return "Access Denied ❌"

    # 🎬 CONTENT AREA (EDIT HERE 👇)

    if item == "video1":
        return """
        <h1 style="color:white;text-align:center">🎬 Video 1</h1>
        <iframe src="https://example.com/video1" width="100%" height="500"></iframe>
        """

    elif item == "video2":
        return """
        <h1 style="color:white;text-align:center">🎬 Video 2</h1>
        <iframe src="https://example.com/video2" width="100%" height="500"></iframe>
        """

    elif item == "video3":
        return """
        <h1 style="color:white;text-align:center">🎬 Video 3</h1>
        <iframe src="https://example.com/video3" width="100%" height="500"></iframe>
        """

    else:
        return "Invalid Item ❌"


app.run()
