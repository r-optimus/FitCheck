<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link rel="stylesheet" href="{{stylesheet}}">
</head>
<body>
    <main class="page-shell{{' ' + page_class if page_class else ''}}">
        <nav class="nav">
            <a class="brand" href="/"><img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck"></a>
            <div>
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
                <a href="/tipps">Tipps</a>
                <a href="/quiz">Quiz</a>
                <a href="/workout">Workout</a>
            </div>
        </nav>

        {{!base}}

        <footer class="footer">
            <a href="/impressum">Impressum</a>
            <a href="/agb">AGB</a>
            <a href="/datenschutz">Datenschutz</a>
            <a href="/about">Über uns</a>
        </footer>
    </main>
</body>
</html>
