def get_result_context(form):
    gewicht = float(form.get('gewicht'))
    groesse_cm = float(form.get('groesse'))
    alter = int(form.get('alter'))
    geschlecht = form.get('geschlecht')

    return _calculate_results(gewicht, groesse_cm, alter, geschlecht)


def _calculate_results(gewicht, groesse_cm, alter, geschlecht):
    groesse_m = groesse_cm / 100
    bmi = gewicht / (groesse_m ** 2)
    bmi_gerundet = round(bmi, 2)

    if geschlecht == "maennlich":
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter + 5
    else:
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter - 161

    if bmi < 18.5:
        bewertung = "Untergewicht"
        bmi_klasse = "bmi-orange"
    elif bmi < 25:
        bewertung = "Normalgewicht"
        bmi_klasse = "bmi-green"
    elif bmi < 30:
        bewertung = "Übergewicht"
        bmi_klasse = "bmi-orange"
    else:
        bewertung = "Adipositas"
        bmi_klasse = "bmi-red"

    wasser_ml = gewicht * 35
    wasser_liter = round(wasser_ml / 1000, 2)
    protein = round(gewicht * 1.5, 1)

    return {
        "bmi": bmi_gerundet,
        "bewertung": bewertung,
        "bmi_klasse": bmi_klasse,
        "wasser_liter": wasser_liter,
        "protein": protein,
        "grundumsatz": round(grundumsatz),
    }
