from flask import Flask, request, render_template_string
import requests
import os
import time

app = Flask(__name__)

# ✅ API ENV
API_URL = os.environ.get("API_URL")

if not API_URL:
    raise Exception("API_URL not set!")

BUY_LINK = "https://www.favoriteweb.net/2026/04/buy-premium-blogger-scripts-source-code.html"

# =========================
# 🎯 CONTENT (EDIT HERE)
# =========================

CONTENT = {
    "protectcontent-1": """
    <h2>Usage Guide</h2>
<div style="text-align:justify">এই Code গুলো ব্যাবহার করে Advance Single এবং Bulk QR কোড তৈরী করা একদম সহজ with Custom Title. কারণ নিচের Code গুলো আপনার পোস্ট/পেইজে Copy করে Past করলে‘ই আপনার QR Code Generator Tools Ready. এরপর শুধু Title থেকে নাম পরিবর্তন এবং JS Code থেকে Zip এর নাম পরিবর্তন করলেই নিজস্ব Branding এ আপনার QR Code Generator Tools সম্পূর্ণ প্রস্তুত।</div>

<h2>HTML Code</h2>

<div style="position:relative;background:#0f172a;color:#fff;padding:15px;border-radius:12px;margin-top:10px;">

<button onclick="(function(btn){
  var text = document.getElementById('box_xv08iw').innerText;
  navigator.clipboard.writeText(text);

  btn.innerText = 'Copied!';
  btn.style.background = '#16a34a';

  setTimeout(function(){
    btn.innerText = 'Copy';
    btn.style.background = '#22c55e';
  }, 5000);

})(this)"
style="position:absolute;top:10px;right:10px;background:#22c55e;border:none;padding:5px 10px;border-radius:6px;color:#fff;cursor:pointer;">
Copy
</button>

<pre id="box_xv08iw" style="white-space:pre-wrap;margin:0;">&lt;div class="qrcontainer"&gt;
  &lt;h2&gt;Favorite Web QR Generator&lt;/h2&gt;

  &lt;textarea id="bulk" placeholder="Favorite-Web https://favoriteweb.net" 
  style="width:100%;height:120px;padding:10px;"&gt;&lt;/textarea&gt;

  &lt;br&gt;&lt;br&gt;

  &lt;input type="file" id="csvFile" accept=".csv"&gt;

  &lt;br&gt;&lt;br&gt;

  &lt;button onclick="generateQRs()" style="padding:10px 20px;"&gt;Generate QR&lt;/button&gt;
  &lt;button onclick="downloadZip()" style="padding:10px 20px;"&gt;Download&lt;/button&gt;
  &lt;div id="errorMsg" style="display:none;background:#ef4444;color:#fff;padding:10px;border-radius:8px;margin-top:10px;"&gt;&lt;/div&gt;
  &lt;div id="output" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin-top:20px;"&gt;&lt;/div&gt;
&lt;/div&gt;

&lt;script src="https://cdn.jsdelivr.net/npm/qrcode/build/qrcode.min.js"&gt;&lt;/script&gt;
&lt;script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.7.1/jszip.min.js"&gt;&lt;/script&gt;</pre>

</div>

<br/><br/>
<h2>CSS Code</h2>

<div style="position:relative;background:#0f172a;color:#fff;padding:15px;border-radius:12px;margin-top:10px;">

<button onclick="(function(btn){
  var text = document.getElementById('box_8k112a').innerText;
  navigator.clipboard.writeText(text);

  btn.innerText = 'Copied!';
  btn.style.background = '#16a34a';

  setTimeout(function(){
    btn.innerText = 'Copy';
    btn.style.background = '#22c55e';
  }, 5000);

})(this)"
style="position:absolute;top:10px;right:10px;background:#22c55e;border:none;padding:5px 10px;border-radius:6px;color:#fff;cursor:pointer;">
Copy
</button>

<pre id="box_8k112a" style="white-space:pre-wrap;margin:0;">&lt;style&gt;
/* Container */
.qrcontainer {
  max-width: 900px;
  margin: auto;
  padding: 20px;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #0f172a, #1e293b);
  color: #fff;
}

/* Glass Card */
.qrcontainer .card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border-radius: 20px;
  padding: 20px;
  margin-top: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

/* Title */
.qrcontainer h2 {
  font-size: 28px;
  margin-bottom: 10px;
}

/* Textarea */
.qrcontainer textarea {
  width: 100%;
  height: 130px;
  padding: 12px;
  border-radius: 12px;
  border: none;
  outline: none;
  background: rgba(255,255,255,0.08);
  color: #fff;
}

/* File Input */
.qrcontainer input[type="file"] {
  margin-top: 10px;
  color: #fff;
}

/* Buttons */
.qrcontainer button {
  background: linear-gradient(135deg, #6366f1, #22c55e);
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 10px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
}

.qrcontainer button:hover {
  transform: scale(1.05);
  box-shadow: 0 5px 20px rgba(0,0,0,0.4);
}

/* QR Grid */
.qrcontainer #output {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 15px;
  margin-top: 20px;
}

/* QR Card */
.qrcontainer #output div {
  background: rgba(255,255,255,0.06);
  padding: 10px;
  border-radius: 15px;
  text-align: center;
  transition: 0.3s;
}

.qrcontainer #output div:hover {
  transform: translateY(-5px);
}

/* QR Name */
.qrcontainer #output p {
  font-size: 12px;
  margin-top: 5px;
  word-break: break-word;
}
.qrcontainer #errorMsg {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  font-weight: 500;
  text-align: center;
}
&lt;/style&gt;</pre>

</div>


<br/><br/>
<h2>JS Code</h2>

<div style="position:relative;background:#0f172a;color:#fff;padding:15px;border-radius:12px;margin-top:10px;">

<button onclick="(function(btn){
  var text = document.getElementById('box_85f8py').innerText;
  navigator.clipboard.writeText(text);

  btn.innerText = 'Copied!';
  btn.style.background = '#16a34a';

  setTimeout(function(){
    btn.innerText = 'Copy';
    btn.style.background = '#22c55e';
  }, 5000);

})(this)"
style="position:absolute;top:10px;right:10px;background:#22c55e;border:none;padding:5px 10px;border-radius:6px;color:#fff;cursor:pointer;">
Copy
</button>

<pre id="box_85f8py" style="white-space:pre-wrap;margin:0;">&lt;script&gt;
let qrData = [];
let nameCount = {};

function getUniqueName(name){
  if(nameCount[name]){
    nameCount[name]++;
    return name + "-" + nameCount[name];
  }else{
    nameCount[name] = 1;
    return name;
  }
}

// ✅ URL থেকে নাম বের করবে
function extractName(line){

  const urlMatch = line.match(/https?:\/\/[^\s]+/);

  if(!urlMatch) return "qr-code";

  const url = urlMatch[0];

  // URL বাদ দিয়ে name বের করা
  let name = line.replace(url, "").trim();

  // যদি কিছু না থাকে → domain থেকে নাম
  if(name.length === 0){
    try{
      let domain = new URL(url).hostname.replace("www.","");
      name = domain.split(".")[0];
    }catch{
      name = "qr-code";
    }
  }

  // 🔥 clean name (FIXED)
  name = name
    .replace(/[&lt;&gt;:"/\\|?*]+/g, "")
    .replace(/\s+/g, "-");

  if(name === "" || name === "-"){
    name = "qr-code";
  }

  return name;
}

async function generateQRs(){

  qrData = [];
  nameCount = {}; // 🔥 reset duplicate counter

  const errorBox = document.getElementById("errorMsg");
  const textArea = document.getElementById("bulk").value;

  const output = document.getElementById("output");
  output.innerHTML = "";

  if(errorBox){
    errorBox.style.display = "none";
  }

  const lines = textArea
    .replace(/,/g, "\n")
    .split(/\r?\n+/)
    .map(l =&gt; l.trim())
    .filter(Boolean);

  if(lines.length === 0){
    showError("⚠️ Please enter at least one valid URL!");
    return;
  }

  let validCount = 0;
  let invalidCount = 0;

  for(let line of lines){

    const urlMatch = line.match(/https?:\/\/[^\s]+/);

    if(!urlMatch){
      invalidCount++;
      continue;
    }

    try{

      // ✅ name extract + unique FIX
      let name = extractName(line);
      let uniqueName = getUniqueName(name);

      let canvas = document.createElement("canvas");

      await QRCode.toCanvas(canvas, line, {
        margin: 1,
        width: 200
      });

      // ✅ FIXED push
      qrData.push({canvas, name: uniqueName});
      validCount++;

      let div = document.createElement("div");
      div.appendChild(canvas);

      let p = document.createElement("p");
      p.innerText = uniqueName; // ✅ FIXED
      div.appendChild(p);

      output.appendChild(div);

    }catch(e){
      invalidCount++;
    }
  }

  if(validCount === 0){
    showError("❌ No valid URLs found!");
    return;
  }

  if(invalidCount &gt; 0){
    showError(`⚠️ ${invalidCount} invalid input ignored!`, "warning");
  }
}

// ✅ error function
function showError(msg, type="error"){
  const box = document.getElementById("errorMsg");
  if(!box) return;

  box.innerText = msg;
  box.style.display = "block";

  if(type === "warning"){
    box.style.background = "#f59e0b";
  } else {
    box.style.background = "#ef4444";
  }
}

// ✅ CSV upload (unchanged)
document.getElementById("csvFile").addEventListener("change", async function(e){
  const file = e.target.files[0];
  if(!file) return;

  const text = await file.text();

  const lines = text.split(/\r?\n/).map(l =&gt; l.trim()).filter(Boolean);

  const dataLines = lines.slice(1);

  let formatted = "";

  for(let line of dataLines){
    const parts = line.split(",");

    if(parts.length &lt; 2) continue;

    const name = parts[0].trim();
    const url = parts[1].trim();

    if(!url) continue;

    formatted += `${name} ${url}\n`;
  }

  document.getElementById("bulk").value = formatted;
});

// ✅ download
async function downloadZip(){

  if(qrData.length === 1){
    const item = qrData[0];

    const link = document.createElement("a");
    link.href = item.canvas.toDataURL("image/png");
    link.download = item.name + ".png";
    link.click();

    return;
  }

  if(qrData.length &gt; 1){
    const zip = new JSZip();

    for(let item of qrData){
      const dataUrl = item.canvas.toDataURL("image/png");
      const base64 = dataUrl.split(",")[1];

      zip.file(item.name + ".png", base64, {base64:true});
    }

    const blob = await zip.generateAsync({type:"blob"});

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "favorite-web-qr.zip";
    link.click();
  }

  if(qrData.length === 0){
    alert("Please generate QR first!");
  }
}
&lt;/script&gt;</pre>

</div>

    """,

    "protectcontent-2": "<h2 style='padding:20px'>Content 2</h2>"
}

# =========================
# 🔐 PASSWORD PAGE (WHITE UI)
# =========================

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Protected</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
  margin:0;
  padding:0;
  font-family:'Segoe UI',sans-serif;
  display:flex;
  justify-content:center;
  align-items:center;
  height:60vh;
}

.box{
  background:#fff;
  padding:30px;
  border-radius:16px;
  width:90%;
  max-width:400px;
  text-align:center;
  box-shadow:0 10px 30px rgba(0,0,0,0.08);
}

h2{
  margin-bottom:20px;
  color:#0f172a;
}

input{
  width:93%;
  padding:12px;
  border-radius:10px;
  border:1px solid #006dff;
  outline:none;
}

input:focus{
  border-color:#6366f1;
  box-shadow:0 0 0 3px rgba(99,102,241,0.15);
}

button{
  width:100%;
  padding:12px;
  margin-top:15px;
  border:none;
  border-radius:10px;
  background:linear-gradient(135deg,#6366f1,#22c55e);
  color:#fff;
  font-weight:bold;
  cursor:pointer;
}

.buy{
  display:block;
  margin-top:15px;
  padding:10px;
  background:#ef4444;
  color:#fff;
  border-radius:10px;
  text-decoration:none;
}
@media only screen and (max-width: 600px) {
  input{
  width:90%;
  }
}
</style>

</head>

<body>

<div class="box">

<h2>🔒 Enter Password</h2>

<input type="password" id="p" placeholder="Enter password">

<button onclick="go()">Unlock</button>

<a href="{{buy}}" target="_top" class="buy">Buy Access</a>

</div>

<script>
let tries = 0;

function go(){

  let pass = document.getElementById("p").value;

  if(pass.trim() === "") return;

  fetch("?item={{item}}&pass=" + encodeURIComponent(pass))
  .then(r=>r.text())
  .then(t=>{

    if(t === "OK"){
      window.location.href = "?item={{item}}&pass="+encodeURIComponent(pass)+"&unlock=1";
    }
    else if(t === "LIMIT"){
      alert("Limit Reached!");
      window.top.location.href="{{buy}}";
    }
    else{
      tries++;
      alert("Wrong Password ("+tries+"/3)");

      if(tries>=3){
        window.top.location.href="{{buy}}";
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

    if not password:
        return render_template_string(HTML, item=item, buy=BUY_LINK)

    try:
        res = requests.get(API_URL, params={
            "pass": password,
            "url": item,
            "t": int(time.time())
        })
        result = res.text.strip()
    except:
        return "API ERROR ❌"

    if result == "WRONG":
        return "WRONG"

    if result == "LIMIT":
        return "LIMIT"

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
