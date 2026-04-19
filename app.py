from flask import Flask, request
import requests
import os

app = Flask(__name__)

API = os.environ.get("API_URL")

if not API:
    raise Exception("API_URL not set!")

# 🔥 =========================
# 🎯 CONTENT 1
# 🔥 =========================

CONTENT_1 = """ hi

"""

# 🔥 =========================
# 🎯 CONTENT 2
# 🔥 =========================

CONTENT_2 = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Protected Content 2</title>
</head>

<body style="background:#020617;color:#fff;font-family:sans-serif;padding:20px;">

<h2>🔓 Premium Content 2</h2>
<p>এটা দ্বিতীয় content।</p>

</body>
</html>
"""

# 🔥 =========================
# 🏠 HOME
# 🔥 =========================

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

<br><br>

<button id="buyBtn" style="display:none;padding:10px 20px;border:none;border-radius:8px;
background:#ef4444;color:#fff;cursor:pointer;">
Buy Now 💰
</button>

<script>
let attempts = 0;

async function go(){{
    let pw = document.getElementById("pw").value;

    let res = await fetch("/check?pass=" + encodeURIComponent(pw) + "&item={item}");
    let text = await res.text();

    if(text === "OK"){{
        window.location.href = "/content?item={item}&pass=" + encodeURIComponent(pw);
    }}
    else if(text === "LIMIT"){{
        alert("Limit reached ❌");
    }}
    else{{
        attempts++;
        alert("Wrong Password ❌ (" + attempts + "/3)");

        if(attempts >= 3){{
            document.getElementById("buyBtn").style.display = "inline-block";

            setTimeout(()=>{{
                window.location.href = "/buy";
            }}, 1500);
        }}
    }}
}}
</script>

</body>
</html>
"""

# 🔍 =========================
# CHECK PASSWORD
# =========================

@app.route("/check")
def check():
    pw = request.args.get("pass")
    item = request.args.get("item")

    try:
        res = requests.get(API + f"?pass={pw}&url={item}")
        return res.text.strip()
    except:
        return "ERROR"

# 🔒 =========================
# CONTENT ROUTE
# =========================

@app.route("/content")
def content():
    item = request.args.get("item")
    pw = request.args.get("pass")

    if not pw:
        return "Access Denied ❌"

    try:
        res = requests.get(API + f"?pass={pw}&url={item}")
        result = res.text.strip()
    except:
        return "Server Error ❌"

    if result != "OK":
        return "Access Denied ❌"

    if item == "protectcontent-1":
        return CONTENT_1

    elif item == "protectcontent-2":
        return CONTENT_2

    return "Invalid Item ❌"

# 💰 =========================
# BUY PAGE
# =========================

@app.route("/buy")
def buy():
    return """
<html style="background:#0f172a;color:white;text-align:center;padding-top:100px;">
<h1>🔓 Unlock Full Access</h1>

<a href="https://your-payment-link.com"
style="padding:12px 25px;background:#22c55e;color:white;border-radius:8px;text-decoration:none;">
Buy Now 💰
</a>

</html>
"""

# 🚀 =========================
# RUN
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
