def get_result_context(form):
    gewicht = float(form.get('gewicht'))
    groesse_cm = float(form.get('groesse'))
    alter = int(form.get('alter'))
    geschlecht = form.get('geschlecht')
    aktivitaet = form.get('aktivitaet')
    ziel = form.get('ziel')

    return _calculate_results(gewicht, groesse_cm, alter, geschlecht, aktivitaet, ziel)


def build_export_text(form):
    result = get_result_context(form)

    return f"""FitCheck Ergebnis

Eingaben
Geschlecht: {result["geschlecht_name"]}
Alter: {result["alter"]} Jahre
Gewicht: {result["gewicht"]} kg
Größe: {result["groesse_cm"]} cm
Aktivitätslevel: {result["aktivitaet_name"]}
Ziel: {result["ziel_name"]}

Ergebnis
BMI: {result["bmi"]}
Bewertung: {result["bewertung"]}
Wasserbedarf: {result["wasser_liter"]} L
Proteinbedarf: {result["protein"]} g
Gesamtumsatz: {result["gesamtumsatz"]} kcal
Kalorienziel ({result["ziel_name"]}): {result["kalorienziel"]} kcal
"""


def _calculate_results(gewicht, groesse_cm, alter, geschlecht, aktivitaet, ziel):
    groesse_m = groesse_cm / 100
    bmi = gewicht / (groesse_m ** 2)
    bmi_gerundet = round(bmi, 2)

    if geschlecht == "maennlich":
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter + 5
    else:
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter - 161

    aktivitaet_faktoren = {
        "wenig": 1.2,
        "moderat": 1.55,
        "hoch": 1.75
    }

    gesamtumsatz = grundumsatz * aktivitaet_faktoren[aktivitaet]

    if ziel == "abnehmen":
        kalorienziel = gesamtumsatz - 500
    elif ziel == "muskelaufbau":
        kalorienziel = gesamtumsatz + 300
    else:
        kalorienziel = gesamtumsatz

    ziel_namen = {
        "abnehmen": "Abnehmen",
        "halten": " Halten",
        "muskelaufbau": "Aufbauen"
    }
    geschlecht_namen = {
        "maennlich": "Männlich",
        "weiblich": "Weiblich"
    }
    aktivitaet_namen = {
        "wenig": "Niedrig",
        "moderat": "Mittel",
        "hoch": "Hoch"
    }

    if bmi < 18.5:
        bewertung = "Unter"
        bmi_klasse = "bmi-orange"
    elif bmi < 25:
        bewertung = "Normal"
        bmi_klasse = "bmi-green"
    elif bmi < 30:
        bewertung = "Über"
        bmi_klasse = "bmi-orange"
    else:
        bewertung = "Adipositas"
        bmi_klasse = "bmi-red"

    wasser_ml = gewicht * 35
    wasser_liter = round(wasser_ml / 1000, 2)
    protein_faktoren = {
        "abnehmen": 2.0,
        "muskelaufbau": 1.8,
        "halten": 1.4
    }
    protein = round(gewicht * protein_faktoren[ziel], 1)

    result = {
        "bmi": bmi_gerundet,
        "bewertung": bewertung,
        "bmi_klasse": bmi_klasse,
        "wasser_liter": wasser_liter,
        "protein": protein,
        "gesamtumsatz": round(gesamtumsatz),
        "kalorienziel": round(kalorienziel),
        "ziel_name": ziel_namen[ziel],
        "geschlecht": geschlecht,
        "geschlecht_name": geschlecht_namen[geschlecht],
        "alter": alter,
        "gewicht": gewicht,
        "groesse_cm": groesse_cm,
        "aktivitaet": aktivitaet,
        "aktivitaet_name": aktivitaet_namen[aktivitaet],
        "ziel": ziel,
    }
    result["metrics"] = [
        ("BMI", result["bmi"], "⚖️", "Der BMI bewertet dein Gewicht im Verhältnis zu deiner Körpergröße.", bmi_klasse),
        ("Bewertung", bewertung, "✅", "Diese Kategorie zeigt, wie dein BMI grob eingeordnet wird.", bmi_klasse),
        ("Wasserbedarf", f'{wasser_liter} L', "💧", "Das ist eine grobe Empfehlung für deine tägliche Trinkmenge.", ""),
        ("Proteinbedarf", f'{protein} g', "🥚", "Protein unterstützt Muskeln, Sättigung und Regeneration.", ""),
        ("Gesamtumsatz", f'{round(gesamtumsatz)} kcal', "🔥", "Dein geschätzter täglicher Kalorienverbrauch mit Aktivitätslevel.", ""),
        (f'Kalorienziel ({ziel_namen[ziel]})', f'{round(kalorienziel)} kcal', "🎯", "Dieses Ziel passt den Gesamtumsatz an dein ausgewähltes Ziel an.", ""),
    ]
    result["export_fields"] = [(name, result[name]) for name in ("geschlecht", "alter", "gewicht", "groesse_cm", "aktivitaet", "ziel")]
    result["export_fields"][3] = ("groesse", groesse_cm)
    return result
