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
        </div>
    </nav>

    <section class="panel">
        <p class="eyebrow">Deine Werte</p>
        <h1>Eingabe</h1>

        <form action="/ergebnis" method="post">
            <label for="geschlecht">Geschlecht</label>
            <select id="geschlecht" name="geschlecht" required>
                <option value="">Bitte auswählen</option>
                <option value="maennlich">Männlich</option>
                <option value="weiblich">Weiblich</option>
            </select>

            <label for="alter">Alter</label>
            <input id="alter" type="number" name="alter" step="1" min="1" max="130" placeholder="in Jahren" required
            oninvalid="this.setCustomValidity('Bitte gib ein realistisches Alter ein.')"
             oninput="this.setCustomValidity('')" >  
            
            <label for="gewicht">Gewicht</label>
            <input id="gewicht" type="number" name="gewicht" step="0.1" min="1" max="600" placeholder="in kg" required
            oninvalid="this.setCustomValidity('Bitte gib ein realistisches Gewicht ein.')"
             oninput="this.setCustomValidity('')" >  

            <label for="groesse">Größe</label>
            <input id="groesse" type="number" name="groesse" step="1" min="1" max="300" placeholder="in cm" required
            oninvalid="this.setCustomValidity('Bitte gib eine realistische Größe ein.')"
             oninput="this.setCustomValidity('')" >  
            

            <label for="aktivitaet">Aktivitätslevel</label>
            <select id="aktivitaet" name="aktivitaet" required>
                <option value="">Bitte auswählen</option>
                <option value="niedrig">Niedrig</option>
                <option value="mittel">Mittel</option>
                <option value="hoch">Hoch</option>
            </select>

            <label for="ziel">Ziel</label>
            <select id="ziel" name="ziel" required>
                <option value="">Bitte auswählen</option>
                <option value="abnehmen">Abnehmen</option>
                <option value="halten">Gewicht halten</option>
                <option value="muskelaufbau">Muskelaufbau</option>
            </select>

            <button type="submit">Absenden</button>
        </form>
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
