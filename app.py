from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

API_URL = os.environ.get("API")
BUY_LINK = "https://yourdomain.com/buy.html"

# 🔥 Content map
CONTENT = {
    "protectcontent-1": "<h2>Unlocked Content 1 ✅</h2><p>Premium Data 1</p>",
    "protectcontent-2": "<h2>Unlocked Content 2 ✅</h2><p>Premium Data 2</p>"
}

# 🔐 Password page
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Protected</title>
<style>
body{background:#0f172a;color:#fff;text-align:center;padding:50px;font-family:sans-serif;}
input{padding:10px;border-radius:8px;border:none;}
button{padding:10px 20px;background:#22c55e;border:none;border-radius:8px;color:#fff;}
</style>
</head>

<body>

<h2>🔒 Enter Password</h2>

<input type="password" id="p">
<br><br>
<button onclick="go()">Unlock</button>

<br><br>
<a href="{{buy}}" style="color:#fff;background:red;padding:10px 20px;border-radius:8px;text-decoration:none;">
Buy Access
</a>

<script>
let tries = 0;

function go(){
  let pass = document.getElementById("p").value;

  fetch("?item={{item}}&pass=" + encodeURIComponent(pass))
  .then(r=>r.text())
  .then(t=>{

    if(t === "OK"){
      location.href = "?item={{item}}&pass="+pass+"&unlock=1";
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

@app.route("/")
def home():

    item = request.args.get("item", "").strip()
    password = request.args.get("pass", "").strip()
    unlock = request.args.get("unlock")

    if not item:
        return "No item ❌"

    # 🔒 show password page
    if not password:
        return render_template_string(HTML, item=item, buy=BUY_LINK)

    # 🔗 API call
    try:
        res = requests.get(API_URL, params={
            "pass": password,
            "url": item
        })
        result = res.text.strip()
    except:
        return "API ERROR ❌"

    # ❌ wrong
    if result == "WRONG":
        return "WRONG"

    # ❌ limit
    if result == "LIMIT":
        return "LIMIT"

    # ✅ correct
    if result == "OK":

        if unlock == "1":
            return CONTENT.get(item, "No content ❌")

        return "OK"

    return "ERROR ❌"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
