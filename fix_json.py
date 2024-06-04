import json

# Läs in den felaktiga JSON-filen
with open('Data.json', 'r') as file:
    content = file.read()

# Försök att fixa JSON-strukturen
try:
    # Radera eventuell tomt JSON-objekt och försök att ladda JSON-data
    if '{}' in content:
        content = content.replace('{}', '')
    if '[]' in content:
        content = content.replace('[]', '')
    
    # Lägg till slutliga hakparenteser om de saknas
    if not content.strip().startswith('['):
        content = '[' + content.strip()
    if not content.strip().endswith(']'):
        content = content.strip() + ']'

    # Ladda JSON för att säkerställa att det är korrekt format
    data = json.loads(content)
    
    # Skriv ut den fixade JSON-strukturen till filen
    with open('Data_fixed.json', 'w') as fixed_file:
        json.dump(data, fixed_file, indent=4)
    
    print("JSON-filen har fixats och sparats som 'Data_fixed.json'.")

except json.JSONDecodeError as e:
    print(f"Misslyckades med att fixa JSON-filen: {e}")
