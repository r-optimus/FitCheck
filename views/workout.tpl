<section class="panel">
    <p class="eyebrow">Training</p>
    <h1>Workout-Generator</h1>
    <p>Wähle Trainingsort und Level. FitCheck erstellt dir ein passendes Workout.</p>
    <form action="/workout" method="post" class="form">
        <label for="ort">Trainingsort</label>
        <select id="ort" name="ort" required>
            <option value="zuhause">Zuhause</option>
            <option value="outdoor">Outdoor</option>
            <option value="gym">Gym</option>
        </select>

        <label for="level">Fitnesslevel</label>
        <select id="level" name="level" required>
            <option value="anfaenger">Anfänger</option>
            <option value="fortgeschritten">Fortgeschritten</option>
            <option value="profi">Profi</option>
        </select>

        <button class="button primary" type="submit">Workout erstellen</button>
    </form>

    % if error:
    <div class="result-card"><p>{{error}}</p></div>
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

% rebase('layout', title='Workout-Generator', stylesheet='/static/style.css', page_class='')
