
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monster Token Checker</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 500px;
            margin: 50px auto;
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        h1 {
            font-weight: 600;
        }
        input, button {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        input {
            background: rgba(255, 255, 255, 0.2);
            color: white;
        }
        input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        button {
            background: #ff7eb3;
            cursor: pointer;
            font-weight: 600;
            color: white;
            transition: 0.3s;
        }
        button:hover {
            background: #ff4e91;
        }
        .stats-box {
            margin-top: 20px;
            background: rgba(0, 0, 0, 0.3);
            padding: 15px;
            border-radius: 5px;
        }
        .stats-box p {
            font-size: 18px;
            font-weight: 600;
        }
        .result-box {
            margin-top: 20px;
            background: rgba(0, 0, 0, 0.2);
            padding: 15px;
            border-radius: 5px;
        }
        .profile {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            background: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .profile img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 2px solid white;
        }
        .profile div {
            text-align: left;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Checker 2.0</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="token_file" accept=".txt"><br>
        <input type="text" name="manual_token" placeholder="Enter Token Manually">
        <button type="submit">Check Tokens</button>
    </form>

    

     
</div>
</body>
</html>
