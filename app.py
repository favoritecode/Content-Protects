from flask import Flask, request
import requests
import os

app = Flask(__name__)

API = os.environ.get("API_URL")

if not API:
    raise Exception("API_URL not set!")

# 🔥 =========================
# 🎯 LOCKED CONTENT (VIDEO1)
# 🔥 =========================

VIDEO1_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>QR Generator</title>
</head>

<body style="background:#0f172a;color:#fff;font-family:sans-serif;padding:20px;">

<h2>Usage Guide</h2>
<p>এই Code ব্যবহার করে QR Generator বানাতে পারবেন।</p>

<!-- 🔥 CODE BOX -->
<div style="position:relative;background:#020617;color:#fff;padding:15px;border-radius:12px;margin-top:20px;">

<button onclick="copyCode(this)" 
style="position:absolute;top:10px;right:10px;background:#22c55e;border:none;padding:5px 10px;border-radius:6px;color:#fff;cursor:pointer;">
Copy
</button>

<pre id="codeBox" style="white-space:pre-wrap;margin:0;">
&lt;div class="qrcontainer"&gt;
  &lt;h2&gt;Favorite Web QR Generator&lt;/h2&gt;
  &lt;textarea&gt;&lt;/textarea&gt;
&lt;/div&gt;
</pre>

</div>

<script>
function copyCode(btn){
  var text = document.getElementById("codeBox").innerText;
  navigator.clipboard.writeText(text);

  btn.innerText = "Copied!";
  btn.style.background = "#16a34a";

  setTimeout(()=>{
    btn.innerText = "Copy";
    btn.style.background = "#22c55e";
  }, 3000);
}
</script>

</body>
</html>
"""

# 🔥 =========================
# 🏠 HOME (PASSWORD PAGE)
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
        document.cookie = "pw=" + pw;
        window.location.href = "/content?item={item}";
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
# CHECK PASSWORD (API)
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
# CONTENT PAGE
# =========================

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

    if item == "video1":
        return VIDEO1_HTML

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
# RUN APP
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
