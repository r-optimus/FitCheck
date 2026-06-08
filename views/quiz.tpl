<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>FitCheck Quiz</title>
    <link rel="stylesheet" href="/static/style.css?v=3">
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

        <section class="panel content">
            <p class="eyebrow">Wissen testen</p>
            <h1>FitCheck Quiz</h1>

            % if finished:
            <div class="quiz-result">
                <span>Dein Ergebnis</span>
                <strong>{{score}} / {{total_questions}} Punkte</strong>
                <p>
                    % if score >= 8:
                    Stark! Du kennst dich schon gut aus.
                    % elif score >= 5:
                    Solide Leistung. Da ist schon gutes Basiswissen da.
                    % else:
                    Guter Start. Mit den Tipps kannst du dein Wissen weiter verbessern.
                    % end
                </p>
            </div>

            <div class="actions">
                <a class="button primary" href="/quiz">Quiz neu starten</a>
                <a class="button secondary" href="/">Startseite</a>
            </div>
            % else:
            <div class="quiz-progress">
                Frage {{question_number}} von {{total_questions}}
            </div>

            <form class="quiz-form" action="/quiz" method="post">
                <h2>{{question["question"]}}</h2>

                <input type="hidden" name="question_index" value="{{question_index}}">
                <input type="hidden" name="score" value="{{score}}">

                <div class="quiz-options">
                    % for answer in question["answers"]:
                    <label class="quiz-option">
                        <input type="radio" name="answer" value="{{answer}}" required>
                        <span>{{answer}}</span>
                    </label>
                    % end
                </div>

                <button class="primary" type="submit">
                    % if question_number == total_questions:
                    Ergebnis anzeigen
                    % else:
                    Nächste Frage
                    % end
                </button>
            </form>
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
