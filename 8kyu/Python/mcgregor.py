def quote(fighter):
    # Convert the input to lowercase for case-insensitive comparison
    fighter_lower = fighter.lower()
    
    # Check who the winner is and return the corresponding quote
    if fighter_lower == "george saint pierre":
        return "I am not impressed by your performance."
    elif fighter_lower == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "Invalid fighter name."
    
    #You have passed all of the tests! :)