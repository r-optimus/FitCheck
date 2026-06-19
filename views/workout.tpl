% import random
% workouts = {
%     ("zuhause", "anfaenger"): [
%         ["10 Kniebeugen", "8 Liegestütze", "20 Sekunden Plank", "10 Ausfallschritte"],
%         ["15 Kniebeugen", "10 Sit-ups", "30 Sekunden Plank", "20 Hampelmänner"],
%         ["20 Kniebeugen", "10 Liegestütze", "15 Ausfallschritte", "30 Sekunden Plank"],
%     ],
%     ("zuhause", "fortgeschritten"): [
%         ["25 Kniebeugen", "20 Liegestütze", "45 Sekunden Plank", "20 Ausfallschritte"],
%         ["30 Kniebeugen", "15 Burpees", "60 Sekunden Plank", "30 Hampelmänner"],
%         ["20 Burpees", "25 Liegestütze", "60 Sekunden Plank", "30 Kniebeugen"],
%     ],
%     ("zuhause", "profi"): [
%         ["40 Kniebeugen", "20 Liegestütze", "90 Sekunden Plank", "40 Ausfallschritte"],
%         ["50 Kniebeugen", "25 Burpees", "120 Sekunden Plank", "50 Hampelmänner"],
%         ["30 Burpees", "30 Liegestütze", "2 Minuten Plank", "60 Kniebeugen"],
%     ],
%     ("gym", "anfaenger"): [
%         ["Beinpresse 3x10", "Brustpresse 3x10", "Latzug 3x10", "Plank 3x30 Sekunden"],
%         ["Rudern 3x10", "Schulterpresse 3x10", "Beinbeuger 3x10", "10 Minuten Fahrrad"],
%         ["Beinstrecker 3x12", "Brustpresse 3x12", "Latzug 3x12", "Bauchmaschine 3x15"],
%     ],
%     ("gym", "fortgeschritten"): [
%         ["Kniebeugen 4x8", "Bankdrücken 4x8", "Rudern 4x10", "Schulterdrücken 3x10"],
%         ["Kreuzheben 4x6", "Latzug 4x10", "Beinpresse 4x10", "Bizepscurls 3x12"],
%         ["Schrägbankdrücken 4x8", "Rudern Kabelzug 4x10", "Beinstrecker 3x12", "Trizepsdrücken 3x12"],
%     ],
%     ("gym", "profi"): [
%         ["Kniebeugen 5x5", "Bankdrücken 5x5", "Kreuzheben 5x5", "Klimmzüge 4xMax"],
%         ["Schrägbankdrücken 4x8", "Rudern 4x10", "Beinpresse 4x10", "Schulterdrücken 4x10"],
%         ["Kreuzheben 4x6", "Klimmzüge 4xMax", "Bulgarian Split Squats 3x12", "Bizepscurls 3x12"],
%         ["Bankdrücken 4x8", "Latzug 4x10", "Beinstrecker 3x12", "Trizepsdrücken 3x12"],
%         ["Frontkniebeugen 4x6", "Kurzhantel-Bankdrücken 4x10", "Rudern Kabelzug 4x10", "Seitheben 3x15"],
%     ],
%     ("outdoor", "anfaenger"): [
%         ["15 Minuten Spaziergang", "10 Kniebeugen", "10 Ausfallschritte", "5 Minuten Dehnen"],
%         ["20 Minuten zügiges Gehen", "15 Kniebeugen", "10 Liegestütze", "5 Minuten Dehnen"],
%         ["2 km Spaziergang", "15 Kniebeugen", "15 Ausfallschritte", "30 Sekunden Plank"],
%     ],
%     ("outdoor", "fortgeschritten"): [
%         ["3 km Joggen", "20 Kniebeugen", "15 Liegestütze", "10 Ausfallschritte"],
%         ["20 Minuten Intervalllauf", "25 Kniebeugen", "20 Liegestütze", "60 Sekunden Plank"],
%         ["4 km Lauf", "20 Ausfallschritte", "20 Liegestütze", "45 Sekunden Plank"],
%     ],
%     ("outdoor", "profi"): [
%         ["5 km Lauf", "30 Liegestütze", "50 Kniebeugen", "90 Sekunden Plank"],
%         ["10 Sprintintervalle", "40 Ausfallschritte", "30 Liegestütze", "2 Minuten Plank"],
%         ["8 km Lauf", "50 Kniebeugen", "40 Liegestütze", "2 Minuten Plank"],
%     ],
% }
% workout = None
% error = None
% if submitted:
%     workout_options = workouts.get((ort, level))
%     if workout_options is None:
%         error = "Bitte wähle Trainingsort und Fitnesslevel aus."
%     else:
%         workout = random.choice(workout_options)
%     end
% end

<section class="panel">
    <p class="eyebrow">Training</p>
    <h1>Workout-Generator</h1>
    <p>Wähle Trainingsort und Level. FitCheck erstellt dir ein passendes Workout.</p>
    <form action="/workout" method="post" class="form">
        <label for="ort">Trainingsort</label>
        <select id="ort" name="ort" required>
            <option value="zuhause" {{'selected' if ort == 'zuhause' else ''}}>Zuhause</option>
            <option value="outdoor" {{'selected' if ort == 'outdoor' else ''}}>Outdoor</option>
            <option value="gym" {{'selected' if ort == 'gym' else ''}}>Gym</option>
        </select>

        <label for="level">Fitnesslevel</label>
        <select id="level" name="level" required>
            <option value="anfaenger" {{'selected' if level == 'anfaenger' else ''}}>Anfänger</option>
            <option value="fortgeschritten" {{'selected' if level == 'fortgeschritten' else ''}}>Fortgeschritten</option>
            <option value="profi" {{'selected' if level == 'profi' else ''}}>Profi</option>
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
