import os

def generate_invitations(template, attendees):
    # Vérification des types d’entrée
    if not isinstance(template, str):
        print(f"Error: Invalid template type {type(template).__name__}, expected str.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid attendees type {type(attendees).__name__}, expected list of dicts.")
        return

    # Vérification d’un template vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérification d’une liste d’attendees vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque invité
    for i, attendee in enumerate(attendees, start=1):
        output_text = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output_text = output_text.replace(f"{{{key}}}", str(value))
        filename = f"output_{i}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(output_text + "\n")  # Pour finir le fichier par une nouvelle ligne
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
