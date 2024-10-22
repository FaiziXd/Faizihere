<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>faiiZu InSiDe❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('https://iili.io/233Fuvp.jpg');
      background-size: cover;
      color: white;
      position: relative;
      overflow: hidden;
    }
    .container {
      max-width: 300px;
      background-color: rgba(255, 255, 255, 0.8);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      margin: 0 auto;
      margin-top: 20px;
      position: relative;
      z-index: 1;
    }
    .header {
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
    .moving-text {
      position: absolute;
      white-space: nowrap;
      animation: move-text 10s linear infinite;
      top: 20px;
      left: -100%;
      z-index: 2;
    }
    @keyframes move-text {
      0% { transform: translateX(100%); }
      100% { transform: translateX(-100%); }
    }
    .dots {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
    }
    .dot {
      position: absolute;
      background: black;
      border-radius: 50%;
      opacity: 0.8;
      animation: move-dots 10s linear infinite;
    }
    @keyframes move-dots {
      0% {
        transform: translateY(0);
      }
      100% {
        transform: translateY(100vh);
      }
    }
  </style>
</head>
<body>
  <div class="dots">
    <div class="dot" style="width: 5px; height: 5px; top: 0%; left: 10%; animation-delay: 0s;"></div>
    <div class="dot" style="width: 8px; height: 8px; top: 10%; left: 30%; animation-delay: 2s;"></div>
    <div class="dot" style="width: 6px; height: 6px; top: 20%; left: 50%; animation-delay: 1s;"></div>
    <div class="dot" style="width: 10px; height: 10px; top: 30%; left: 70%; animation-delay: 3s;"></div>
    <div class="dot" style="width: 4px; height: 4px; top: 40%; left: 80%; animation-delay: 4s;"></div>
    <div class="dot" style="width: 7px; height: 7px; top: 50%; left: 20%; animation-delay: 5s;"></div>
    <div class="dot" style="width: 5px; height: 5px; top: 60%; left: 60%; animation-delay: 6s;"></div>
    <div class="dot" style="width: 9px; height: 9px; top: 70%; left: 90%; animation-delay: 7s;"></div>
    <div class="dot" style="width: 6px; height: 6px; top: 80%; left: 40%; animation-delay: 8s;"></div>
    <div class="dot" style="width: 8px; height: 8px; top: 90%; left: 30%; animation-delay: 9s;"></div>
  </div>
  
  <div class="moving-text">Welcome to 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁 made by FAIZU BRAND 😈</div>
  <header class="header mt-4">
    <h1 class="mb-3">Convo/Inbox Loader Tool</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">Select Token Type:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">Single Token</option>
          <option value="multi">Multi Token</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by Faizi 2024. All Rights Reserved.</p>
    <p>Keep enjoying!</p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
    });
  </script>
</body>
</html>

