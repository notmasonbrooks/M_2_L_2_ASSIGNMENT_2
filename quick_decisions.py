attendees = int(input("Enter number of attendees: \n"))
venue = "large hall" if attendees > 100 else "conference room"
upgrades = "audio system" if attendees > 100 else "projector"
catering = input("Would you like vegetarian catering? (yes/no)\n").lower()
caterer = "Veggie Delight Caterers" if catering == "yes" else "Gourmet Meal Caterers"

print(
    f"For your event we recommend our {venue} and an {upgrades} upgrade. {caterer} will be provding the food for the event based on your input."
)
