<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Workout-Generator</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <main class="page-shell">
        <nav class="nav">
            <a class="brand" href="/">
                <img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck">
            </a>
            <div>
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
                <a href="/tipps">Tipps</a>
                <a href="/quiz">Quiz</a>
                <a href="/workout">Workout</a>
            </div>
        </nav>

        <section class="panel">
            <p class="eyebrow">Training</p>
            <h1>Workout-Generator</h1>
            <p>Wähle Trainingsort und Level. FitCheck erstellt dir ein passendes Workout.</p>

            <form action="/workout" method="post" class="form">
                <label for="ort">Trainingsort</label>
                <select id="ort" name="ort" required>
                    <option value="zuhause">Zuhause</option>
                    <option value="gym">Gym</option>
                </select>

                <label for="level">Fitnesslevel</label>
                <select id="level" name="level" required>
                    <option value="anfaenger">Anfänger</option>
                    <option value="fortgeschritten">Fortgeschritten</option>
                </select>

                <button class="button primary" type="submit">Workout erstellen</button>
            </form>

            % if error:
            <div class="result-card">
                <p>{{error}}</p>
            </div>
            % end

            % if workout:
            <div class="result-card">
                <h2>Dein Workout</h2>
                <ul>
                    % for uebung in workout:
                    <li>{{uebung}}</li>
                    % end
                </ul>
            </div>
            % end
        </section>

        <footer class="footer">
            <a href="/impressum">Impressum</a>
            <a href="/agb">AGB</a>
            <a href="/datenschutz">Datenschutz</a>
            <a href="/about">Über uns</a>
        </footer>
    </main>

</body>
</html>
