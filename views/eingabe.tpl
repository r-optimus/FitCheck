<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Eingabe</title>
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
            <a href="/about">Über</a>
        </div>
    </nav>

    <section class="panel">
        <p class="eyebrow">Deine Werte</p>
        <h1>Eingabe</h1>

        <form action="/ergebnis" method="post">
            <label for="gewicht">Gewicht in kg</label>
            <input id="gewicht" type="number" name="gewicht" step="0.1" min="1" placeholder="z. B. 70" required>

            <label for="groesse">Größe in cm</label>
            <input id="groesse" type="number" name="groesse" step="0.1" min="1" placeholder="z. B. 175" required>

            <button type="submit">Absenden</button>
        </form>
    </section>
</main>

</body>
</html>
