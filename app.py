from flask import Flask, request, render_template_string
import requests
import os
import time

app = Flask(__name__)

# 🔐 API (Render ENV)
API_URL = os.environ.get("API_URL")

if not API_URL:
    raise Exception("API not set!")

BUY_LINK = "https://yourdomain.com/buy.html"

# =========================
# 🎯 CONTENT (PASTE HERE)
# =========================

CONTENT = {
    "protectcontent-1": """
    <div style="color:white;font-family:sans-serif;padding:20px">
        <h2>🔓 Premium Content 1</h2>
        <p>এই জায়গায় তোর আসল HTML / CSS / JS content paste করবি</p>

        <div style="background:#020617;padding:15px;border-radius:10px;">
        <pre>
&lt;div&gt;Your Code Here&lt;/div&gt;
        </pre>
        </div>
    </div>
    """,

    "protectcontent-2": """
    <div style="color:white;padding:20px">
        <h2>🔓 Premium Content 2</h2>
    </div>
    """
}

# =========================
# 🔐 PASSWORD PAGE
# =========================

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Protected</title>
<style>
body{
  background:#0f172a;
  color:#fff;
  text-align:center;
  padding:50px;
  font-family:sans-serif;
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

<input type="password" id="p" placeholder="Enter password">
<br><br>
<button onclick="go()">Unlock</button>

<br><br>
<a href="{{buy}}" style="background:red;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;">
Buy Access
</a>

<script>
let tries = 0;

function go(){

  let pass = document.getElementById("p").value;

  if(pass.trim() === "") return;

  fetch("?item={{item}}&pass=" + encodeURIComponent(pass))
  .then(r=>r.text())
  .then(t=>{

    if(t === "OK"){
      location.href = "?item={{item}}&pass="+encodeURIComponent(pass)+"&unlock=1";
    }
    else if(t === "LIMIT"){
      alert("Limit Reached!");
      location.href="{{buy}}";
    }
    else{
      tries++;
      alert("Wrong Password ("+tries+"/3)");

      if(tries>=3){
        location.href="{{buy}}";
      }
    }

  });

}
</script>

</body>
</html>
"""

# =========================
# 🚀 MAIN ROUTE
# =========================

@app.route("/")
def home():

    item = request.args.get("item", "").strip()
    password = request.args.get("pass", "").strip()
    unlock = request.args.get("unlock")

    if not item:
        return "No item ❌"

    # 🔒 password page
    if not password:
        return render_template_string(HTML, item=item, buy=BUY_LINK)

    # 🔥 API CALL (FIXED + SAFE)
    try:
        res = requests.get(API_URL, params={
            "pass": password,
            "url": item,
            "t": int(time.time())   # cache bypass
        })

        result = res.text.strip()

    except Exception as e:
        return "API ERROR ❌"

    # ❌ WRONG
    if result == "WRONG":
        return "WRONG"

    # ❌ LIMIT
    if result == "LIMIT":
        return "LIMIT"

    # ✅ OK
    if result == "OK":

        if unlock == "1":
            return CONTENT.get(item, "No content ❌")

        return "OK"

    return "ERROR ❌"

# =========================
# 🚀 RUN
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
