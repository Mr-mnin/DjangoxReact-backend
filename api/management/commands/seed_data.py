"""
seed_data.py

How to run this:
1. Save this file as backend/api/management/commands/seed_data.py
   (create the 'management' and 'commands' folders if they don't exist,
   each with an empty __init__.py file inside)
2. In your terminal, with DATABASE_URL still exported to your Neon connection string:
       cd backend
       python manage.py seed_data
3. This uses Django's ORM (not raw SQL), so it respects your actual model
   fields/relationships as defined in api/models.py.

Folder structure needed:
backend/
  api/
    management/
      __init__.py          <- empty file
      commands/
        __init__.py         <- empty file
        seed_data.py         <- this file
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Country, League, Characteristic, FootballClub


class Command(BaseCommand):
    help = "Seed the database with countries, leagues, characteristics, and football clubs."

    @transaction.atomic
    def handle(self, *args, **options):
        # --- Countries ---
        country_names = [
            "England", "Spain", "Germany", "France", "Brazil", "India",
            "USA", "Netherlands", "Italy", "Portugal", "Argentina", "Belgium",
        ]
        countries = {}
        for name in country_names:
            obj, created = Country.objects.get_or_create(name=name)
            countries[name] = obj
            self.stdout.write(f"{'Created' if created else 'Exists'}: Country {name}")

        # --- Leagues ---
        league_names = [
            "Premier League", "La Liga", "Bundesliga", "Ligue 1",
            "Indian Super League", "MLS", "Eredivisie", "Serie A",
            "Primeira Liga", "Liga Profesional", "Pro League", "Brasileirão",
        ]
        leagues = {}
        for name in league_names:
            obj, created = League.objects.get_or_create(name=name)
            leagues[name] = obj
            self.stdout.write(f"{'Created' if created else 'Exists'}: League {name}")

        # --- Characteristics ---
        characteristic_names = [
            "Attacking", "Defensive", "Balanced", "Tiki-Taka", "Catenaccio",
            "Total Football", "Gegenpressing", "Counter-Attacking", "Park the Bus",
            "Route One", "Possession-Based", "High Press", "Wing Play",
            "Direct Play", "Kick and Rush", "False Nine", "Long Ball", "Fluid Formation",
        ]
        characteristics = {}
        for name in characteristic_names:
            obj, created = Characteristic.objects.get_or_create(name=name)
            characteristics[name] = obj
            self.stdout.write(f"{'Created' if created else 'Exists'}: Characteristic {name}")

        # --- Football Clubs ---
        # (name, description, attendence, city, country, league, [characteristics])
        clubs = [
            ("Bayern Munich", "Dominant German football club", 75024, "Munich", "Germany", "Bundesliga", ["Attacking"]),
            ("Liverpool", "Historic English club known for attacking football", 61000, "North West England", "England", "Premier League", ["Attacking", "Defensive"]),
            ("Paris Saint Germain", "France's most dominant modern club", 47929, "Paris", "France", "Ligue 1", ["Attacking"]),

            ("Real Madrid", "One of the most successful clubs in football history, based in Madrid, competing in La Liga.", 81044, "Madrid", "Spain", "La Liga", ["Attacking", "Possession-Based", "Wing Play"]),
            ("Flamengo", "One of Brazil's most popular and successful clubs, based in Rio de Janeiro.", 78000, "Rio de Janeiro", "Brazil", "Brasileirão", ["Attacking", "Counter-Attacking"]),
            ("Mohun Bagan Super Giant", "One of India's oldest and most decorated football clubs, based in Kolkata.", 8500, "Kolkata", "India", "Indian Super League", ["Balanced", "Defensive", "Gegenpressing"]),
            ("LA Galaxy", "One of the most successful clubs in Major League Soccer, based in Los Angeles.", 27000, "Los Angeles", "USA", "MLS", ["Balanced", "Direct Play"]),
            ("Ajax", "Legendary Dutch club known for developing Total Football and world-class youth talent.", 54000, "Amsterdam", "Netherlands", "Eredivisie", ["Total Football", "Possession-Based", "High Press"]),
            ("Juventus", "Italy's most decorated football club, based in Turin, known for defensive solidity.", 41000, "Turin", "Italy", "Serie A", ["Defensive", "Catenaccio"]),
            ("Benfica", "One of Portugal's biggest clubs, based in Lisbon, with a passionate attacking style.", 65000, "Lisbon", "Portugal", "Primeira Liga", ["Attacking", "Wing Play"]),
            ("Boca Juniors", "One of Argentina's most iconic clubs, based in Buenos Aires, with a fiercely loyal fanbase.", 54000, "Buenos Aires", "Argentina", "Liga Profesional", ["Defensive", "Counter-Attacking"]),
            ("Anderlecht", "Belgium's most successful club, based in Brussels.", 21000, "Brussels", "Belgium", "Pro League", ["Balanced", "Direct Play"]),

            ("Manchester United", "One of the most widely supported football clubs in the world, based in Manchester.", 74000, "Manchester", "England", "Premier League", ["Attacking", "Wing Play"]),
            ("Barcelona", "Spanish giant renowned for its possession-based Tiki-Taka style and legendary academy, La Masia.", 99000, "Barcelona", "Spain", "La Liga", ["Tiki-Taka", "Possession-Based"]),
            ("Borussia Dortmund", "Famed for its passionate Yellow Wall support and high-intensity Gegenpressing style.", 81365, "Dortmund", "Germany", "Bundesliga", ["Gegenpressing", "Attacking"]),
            ("Marseille", "One of France's most passionately supported clubs, based on the Mediterranean coast.", 67000, "Marseille", "France", "Ligue 1", ["Attacking", "Counter-Attacking"]),
            ("Corinthians", "One of Brazil's most popular clubs, known for its massive fanbase and defensive resilience.", 49000, "São Paulo", "Brazil", "Brasileirão", ["Defensive", "Counter-Attacking"]),
            ("Bengaluru FC", "One of the most successful modern clubs in Indian football, known for a possession-oriented approach.", 24000, "Bengaluru", "India", "Indian Super League", ["Balanced", "High Press"]),
            ("Inter Miami CF", "An MLS club based in Fort Lauderdale, known for attacking, star-studded football.", 21000, "Fort Lauderdale", "USA", "MLS", ["Attacking", "Possession-Based"]),
            ("PSV Eindhoven", "One of the Netherlands' most successful clubs, known for high-pressing attacking football.", 35000, "Eindhoven", "Netherlands", "Eredivisie", ["High Press", "Attacking"]),
            ("AC Milan", "One of Italy's most decorated clubs, blending defensive discipline with clinical counter-attacks.", 75000, "Milan", "Italy", "Serie A", ["Balanced", "Counter-Attacking"]),
            ("FC Porto", "One of Portugal's biggest clubs, known for a well-organized, direct style of play.", 50000, "Porto", "Portugal", "Primeira Liga", ["Defensive", "Direct Play"]),
            ("River Plate", "One of Argentina's most successful clubs, based in Buenos Aires, with an attacking, possession-based identity.", 70000, "Buenos Aires", "Argentina", "Liga Profesional", ["Attacking", "Possession-Based"]),
            ("Club Brugge", "Belgium's most successful club, known for a balanced, direct style of play.", 29000, "Bruges", "Belgium", "Pro League", ["Balanced", "Direct Play"]),

            ("Chelsea", "West London club known for its tactical flexibility and high-intensity pressing under recent regimes.", 40000, "London", "England", "Premier League", ["Balanced", "High Press"]),
            ("Atletico Madrid", "Renowned for its disciplined, defensively resolute style under long-time manager Diego Simeone.", 68000, "Madrid", "Spain", "La Liga", ["Defensive", "Counter-Attacking"]),
            ("Bayer Leverkusen", "Play an attacking, high-pressing brand of football and won an unbeaten Bundesliga title in 2023-24.", 30000, "Leverkusen", "Germany", "Bundesliga", ["Attacking", "High Press"]),
            ("Lyon", "Historic French club known for balanced play and strong wing-based attacks.", 59000, "Lyon", "France", "Ligue 1", ["Balanced", "Wing Play"]),
            ("Palmeiras", "One of Brazil's most successful clubs, known for patient, possession-based football.", 43000, "São Paulo", "Brazil", "Brasileirão", ["Balanced", "Possession-Based"]),
            ("Kerala Blasters", "Known for one of the most passionate fanbases in Indian football and an attacking, wing-focused style.", 55000, "Kochi", "India", "Indian Super League", ["Attacking", "Wing Play"]),
            ("Seattle Sounders", "One of MLS's most consistently successful and well-supported clubs.", 32000, "Seattle", "USA", "MLS", ["Balanced", "Direct Play"]),
            ("Feyenoord", "Historic Rotterdam club known for a disciplined, counter-attacking style and passionate support.", 47000, "Rotterdam", "Netherlands", "Eredivisie", ["Defensive", "Counter-Attacking"]),
            ("Inter Milan", "One of Italy's most successful clubs, historically associated with disciplined defensive football.", 75000, "Milan", "Italy", "Serie A", ["Defensive", "Catenaccio"]),
            ("Sporting CP", "Lisbon-based club known for attacking, high-pressing football and a strong youth academy.", 50000, "Lisbon", "Portugal", "Primeira Liga", ["Attacking", "High Press"]),
            ("Independiente", "One of Argentina's most historic clubs, with a balanced tactical identity.", 48000, "Buenos Aires", "Argentina", "Liga Profesional", ["Balanced", "Defensive"]),
            ("Genk", "Leading Belgian club known for attacking football and a strong youth development pipeline.", 24000, "Genk", "Belgium", "Pro League", ["Balanced", "Attacking"]),
        ]

        for name, desc, attendence, city, country_name, league_name, char_names in clubs:
            club, created = FootballClub.objects.get_or_create(
                name=name,
                defaults={
                    "description": desc,
                    "attendence": attendence,
                    "city": city,
                    "country": countries[country_name],
                    "league": leagues[league_name],
                },
            )
            if created:
                club.characteristics.set([characteristics[c] for c in char_names])
                self.stdout.write(self.style.SUCCESS(f"Created club: {name}"))
            else:
                self.stdout.write(f"Exists, skipped: {name}")

        self.stdout.write(self.style.SUCCESS("Seeding complete."))