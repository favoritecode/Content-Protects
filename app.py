from flask import Flask, request, make_response
import requests
import os

app = Flask(__name__)

API = os.environ.get("API_URL")

if not API:
    raise Exception("API_URL not set!")

# 🏠 HOME
@app.route("/")
def home():
    item = request.args.get("item")

    if not item:
        return "No item provided ❌"

    return f"""
    <html>
    <body style="background:#0f172a;color:#fff;text-align:center;padding-top:80px;font-family:sans-serif;">

    <h2>🔒 Unlock {item}</h2>

    <input type="password" id="pw" placeholder="Enter Password"
    style="padding:10px;border-radius:8px;border:none;margin:10px;">
    
    <br>

    <button onclick="go()" style="padding:10px 20px;border:none;border-radius:8px;
    background:#22c55e;color:#fff;cursor:pointer;">
    Unlock
    </button>

    <script>
    async function go(){{
        let pw = document.getElementById("pw").value;

        let res = await fetch("/check?pass=" + encodeURIComponent(pw) + "&item={item}");
        let text = await res.text();

        if(text === "OK"){{
            document.cookie = "pw=" + pw;
            window.location.href = "/content?item={item}";
        }}
        else if(text === "LIMIT"){{
            alert("❌ Limit reached!");
        }}
        else if(text === "WRONG"){{
            alert("Wrong Password ❌");
        }}
        else{{
            alert("Error ❌");
        }}
    }}
    </script>

    </body>
    </html>
    """


# 🔍 CHECK PASSWORD
@app.route("/check")
def check():
    pw = request.args.get("pass")
    item = request.args.get("item")

    try:
        # 🔥 IMPORTANT: item → url
        res = requests.get(API + f"?pass={pw}&url={item}")
        return res.text.strip()
    except:
        return "ERROR"


# 🔒 CONTENT
@app.route("/content")
def content():
    item = request.args.get("item")
    pw = request.cookies.get("pw")

    if not pw:
        return "Access Denied ❌"

    try:
        res = requests.get(API + f"?pass={pw}&url={item}")
        result = res.text.strip()
    except:
        return "Server Error ❌"

    if result != "OK":
        return "Access Denied ❌"

    # 🎬 CONTENT
    if item == "video1":
        return """
        <html style="background:black;color:white;">
        <h1 style="text-align:center;">🎬 Video 1</h1>
        <iframe src="https://example.com/video1"
        width="100%" height="500" style="border:none;"></iframe>
        </html>
        """

    elif item == "video2":
        return """
        <html style="background:black;color:white;">
        <h1 style="text-align:center;">🎬 Video 2</h1>
        <iframe src="https://example.com/video2"
        width="100%" height="500" style="border:none;"></iframe>
        </html>
        """

    else:
        return "Invalid Item ❌"


# 🔥 Render fix
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
