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
        <input id="alter" type="number" name="alter" step="1" min="1" max="130" placeholder="in Jahren" required oninvalid="this.setCustomValidity('Bitte gib ein realistisches Alter ein.')" oninput="this.setCustomValidity('')">

        <label for="gewicht">Gewicht</label>
        <input id="gewicht" type="number" name="gewicht" step="0.1" min="1" max="600" placeholder="in kg" required oninvalid="this.setCustomValidity('Bitte gib ein realistisches Gewicht ein.')" oninput="this.setCustomValidity('')">

        <label for="groesse">Größe</label>
        <input id="groesse" type="number" name="groesse" step="1" min="1" max="300" placeholder="in cm" required oninvalid="this.setCustomValidity('Bitte gib eine realistische Größe ein.')" oninput="this.setCustomValidity('')">

        <label for="aktivitaet">Aktivitätslevel</label>
        <select id="aktivitaet" name="aktivitaet" required>
            <option value="">Bitte auswählen</option>
            <option value="wenig">Niedrig</option>
            <option value="moderat">Mittel</option>
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

% rebase('layout', title='Eingabe', stylesheet='/static/style.css', page_class='')
