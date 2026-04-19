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

VIDEO1_HTML = """<div class="separator" style="clear: both;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSFkBfiy6kta8VuX4jbziCsw8ViCiVGsooqb17T9bWhX2UkPqAZzqigyPLo0w5WeXg1riBnWPcfygoP_pXcrBOjsASqN1wmNdCr1UV5znQKoGPMx9YKxaJR9MKpUm4iv8FZWAirG0nDZcMTZQWCPej39OzCQ0Ef1XWizuGRFEzCOjVLgrLM0Yp8V-tOJA/s1600/QR%20Code%20Generator%20Script%20and%20Guide%20-%20Favorite%20Web.png" style="display: block; padding: 1em 0; text-align: center; "><img alt="" border="0" data-original-height="1024" data-original-width="1536" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSFkBfiy6kta8VuX4jbziCsw8ViCiVGsooqb17T9bWhX2UkPqAZzqigyPLo0w5WeXg1riBnWPcfygoP_pXcrBOjsASqN1wmNdCr1UV5znQKoGPMx9YKxaJR9MKpUm4iv8FZWAirG0nDZcMTZQWCPej39OzCQ0Ef1XWizuGRFEzCOjVLgrLM0Yp8V-tOJA/s1600/QR%20Code%20Generator%20Script%20and%20Guide%20-%20Favorite%20Web.png"/></a></div>

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
