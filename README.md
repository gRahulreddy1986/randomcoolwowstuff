<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World of Warcraft Wallpapers</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        body {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to bottom, #000000, #1a1a1a);
            color: #ffd700;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem;
        }
        h1 {
            text-align: center;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        #randomImage {
            max-width: 100%;
            max-height: 70vh;
            object-fit: contain;
            border: 3px solid #ffd700;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
        }
        .btn-custom {
            background-color: #4a0e0e;
            border-color: #ffd700;
            color: #ffd700;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            background-color: #ffd700;
            color: #4a0e0e;
        }
        #viewCount {
            font-size: 1.2rem;
            font-weight: bold;
        }
    </style>


    <script>
        function refreshImage() {
            $.get('/refresh_image', function(data) {
                $('#randomImage').attr('src', data.image_url);
                $('#viewCount').text(data.view_count);
            });
        }
        function resetCount() {
            if (confirm("Are you sure you want to reset the count?")) {
                $.post('/reset_count', function(data) {
                    $('#viewCount').text(data.view_count);
                });
            }
        }
        $(document).ready(function() {
        refreshImage();
    });
    </script>



</head>
<body class="container">
    <h1 class="display-4">Beautiful World of Warcraft Wallpapers</h1>
    <button class="btn btn-custom btn-lg" onclick="refreshImage()">Generate Random Image</button>
    <h2 class="mt-3">Seen: <span id="viewCount">{{ viewCount }}</span> times</h2>
    <div class="mt-4 mb-4">
        <img id="randomImage" src="{{ image_url }}" alt="Random World of Warcraft Wallpaper" class="img-fluid">
    </div>
    <button class="btn btn-custom" onclick="resetCount()">Reset Count</button>
</body>
</html>
