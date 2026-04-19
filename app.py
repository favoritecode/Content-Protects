from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

# 🔐 API (Render environment variable)
API_URL = os.environ.get("API")

if not API_URL:
    raise Exception("API not set!")

BUY_LINK = "https://yourdomain.com/buy.html"


# =======================
# 🔥 CONTENTS
# =======================

CONTENT = {
    "protectcontent-1": """<h2 style='color:#22c55e'>Unlocked Content 1 ✅</h2>
    <p>এটা তোমার Premium Content 1</p>""",

    "protectcontent-2": """<h2 style='color:#22c55e'>Unlocked Content 2 ✅</h2>
    <p>এটা তোমার Premium Content 2</p>"""
}


# =======================
# 🔐 PASSWORD PAGE
# =======================

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Protected</title>
<style>
body{
  background:#0f172a;
  color:#fff;
  font-family:sans-serif;
  text-align:center;
  padding:50px;
}
input{
  padding:10px;
  border-radius:8px;
  border:none;
}
button{
  padding:10px 20px;
  background:#22c55e;
  border:none;
  border-radius:8px;
  color:#fff;
  cursor:pointer;
}
</style>
</head>

<body>

<h2>🔒 Enter Password</h2>

<input type="password" id="pass" placeholder="Password">
<br><br>
<button onclick="unlock()">Unlock</button>

<script>
let attempts = 0;
const MAX = 3;

function unlock(){

  let pass = document.getElementById("pass").value;

  if(pass.trim() === "") return;

  fetch("?item={{item}}&pass=" + encodeURIComponent(pass))
  .then(res => res.text())
  .then(data => {

    if(data === "OK"){
      location.href = "?item={{item}}&unlock=1&pass=" + pass;
    }
    else if(data === "LIMIT"){
      alert("Limit Reached!");
      location.href = "{{buy}}";
    }
    else{
      attempts++;
      alert("Wrong Password (" + attempts + "/" + MAX + ")");

      if(attempts >= MAX){
        location.href = "{{buy}}";
      }
    }

  });

}
</script>

</body>
</html>
"""


# =======================
# 🚀 MAIN ROUTE
# =======================

@app.route("/")
def home():

    item = request.args.get("item")
    password = request.args.get("pass")
    unlock = request.args.get("unlock")

    # ❌ No item
    if not item:
        return "No item provided ❌"

    # 🔒 Step 1: show password page
    if not password:
        return render_template_string(HTML_PAGE, item=item, buy=BUY_LINK)

    # 🔗 API CALL (Sheet check)
    try:
        res = requests.get(API_URL, params={
            "pass": password,
            "url": item   # 🔥 IMPORTANT (protectcontent-1)
        })

        result = res.text.strip()

    except:
        return "API Error ❌"

    # ❌ Wrong password
    if result == "WRONG":
        return "WRONG"

    # ❌ Limit reached
    if result == "LIMIT":
        return "LIMIT"

    # ✅ Correct password → unlock
    if result == "OK":

        if unlock == "1":

            content = CONTENT.get(item)

            if content:
                return content
            else:
                return "No content found ❌"

        return "OK"

    return "Error ❌"


# =======================
# 🚀 RUN
# =======================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
