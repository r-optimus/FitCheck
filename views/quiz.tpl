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
    <div class="quiz-progress">Frage {{question_number}} von {{total_questions}}</div>
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
        <button class="primary" type="submit">{{'Ergebnis anzeigen' if question_number == total_questions else 'Nächste Frage'}}</button>
    </form>
    % end
</section>

% rebase('layout', title='FitCheck Quiz', stylesheet='/static/style.css?v=3', page_class='')
