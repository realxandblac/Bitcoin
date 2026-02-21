<!DOCTYPE html>
<html>
<head>
  <title>Bitcoin Tracker</title>
  <style>
    body {
      background: #0d1117;
      color: white;
      text-align: center;
      font-family: Arial;
    }
    h1 {
      margin-top: 60px;
      font-size: 40px;
    }
    .price {
      font-size: 32px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Bitcoin Price</h1>
  <div class="price" id="btc">Loading...</div>

  <script>
    fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
      .then(response => response.json())
      .then(data => {
        document.getElementById("btc").innerHTML =
          "$" + data.bitcoin.usd;
      })
      .catch(() => {
        document.getElementById("btc").innerHTML =
          "Unable to load price.";
      });
  </script>
</body>
</html>
