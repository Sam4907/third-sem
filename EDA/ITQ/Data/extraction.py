import csv
import json

TEAM_MAPPING={
    "Mexico": "mex",
    "South Korea": "sk",
    "South Africa": "sa",
    "Czechia": "cze",
    "Switzerland": "sui",
    "Canada": "can",
    "Bosnia and Herzegovina": "bih",
    "Qatar": "qat",
    "Brazil": "bra",
    "Morocco": "mar",
    "Scotland": "sco",
    "Haiti": "hai",
    "Turkiye": "tur",
    "USA": "usa",
    "Australia": "aus",
    "Paraguay": "par",
    "Germany": "ger",
    "Ecuador": "ecu",
    "Ivory Coast": "ivo",
    "Curacao": "cur",
    "Netherlands": "ned",
    "Japan": "jap",
    "Sweden": "swe",
    "Tunisia": "tun",
    "Belgium": "bel",
    "Iran": "ira",
    "Egypt": "egy",
    "New Zealand": "nzl",
    "Spain": "esp",
    "Cape Verde": "cpv",
    "Saudi Arabia": "ksa",
    "France": "fra",
    "Norway": "nor",
    "Senegal": "sen",
    "Iraq": "irq",
    "Argentina": "arg",
    "Algeria": "alg",
    "Austria": "aut",
    "Jordan": "jor",
    "Portugal": "por",
    "Colombia": "col",
    "DR Congo": "drc",
    "Uzbekistan": "uzb",
    "England": "eng",
    "Croatia": "cro",
    "Ghana": "gha",
    "Panama": "pan",
    "Uruguay": "uru"
}

try:
    with open('fotmob_ext.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
except FileNotFoundError:
    print("Error: 'fotmob_ext.json' not found.")
    data=None

if data:
    csv_filename="xg.csv"
    headers=["country", "xg", "ga"]
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(headers)
        for group in data.get('table', [{}])[0].get('data', {}).get('tables', []):
            raw_group_name=group.get('leagueName', '')
            xg_table=group.get('table', {}).get('xg', [])
            for team in xg_table:
                full_name=team.get('teamName', '')
                short_name=TEAM_MAPPING.get(full_name, full_name)
                row=[
                    short_name,
                    round(team.get('xg', 0), 2),
                    round(team.get('xgConceded', 0), 2)
                ]
                writer.writerow(row)
    print(f"Data exported to '{csv_filename}'.")