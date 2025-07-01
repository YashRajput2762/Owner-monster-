from flask import Flask, render_template_string, request

app = Flask(__name__)

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MADE BY MONSTER</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
  <style>
    body {
      background-image: url('https://i.ibb.co/QFmNQvFH/a6897a8162196ae12a2680fef41c487d.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      color: white;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 350px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px white;
      border: none;
      resize: none;
      margin-top: 20px;
    }
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
    }
    .header { text-align: center; padding-top: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 30px; color: #888; }
    .instagram-link { color: #e1306c; text-decoration: none; }
    .instagram-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header"><h1>👑 BLACK PANTHER RULEX 💀👑</h1></header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3"><label for="tokenFile">Token File</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required />
      </div>
      <div class="mb-3"><label for="threadId">Thread ID</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required />
      </div>
      <div class="mb-3"><label for="kidx">Hather Name</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required />
      </div>
      <div class="mb-3"><label for="time">Delay (s)</label>
        <input type="number" class="form-control" id="time" name="time" required />
      </div>
      <div class="mb-3"><label for="txtFile">Text File</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required />
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Start Sending</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Sending</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; MADE BY MONSTER 💀👑</p>
    <p><a href="https://www.facebook.com/blackpantherrulexkaownerkamena" target="_blank">Facebook</a></p>
    <a href="https://www.instagram.com/kameena_hu_yrr" class="instagram-link" target="_blank">
      <i class="fab fa-instagram"></i> Instagram
    </a>
  </footer>
</body>
</html>'''

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template_string(html_code)

@app.route("/stop", methods=["POST"])
def stop():
    return "Stopped sending messages!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
