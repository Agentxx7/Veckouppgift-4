def uppgift3():
    teamA = input("Hur många mål gjorde Tottenham? ")
    teamA = int(teamA)
    
    teamB = input("Hur många mål gjorde Liverpool? ")
    teamB = int(teamB)
    
    if teamA > teamB:
        goal_difference = teamA - teamB
        print(f"Tottenham vann matchen ({teamA} - {teamB}) med {goal_difference} mål! ")
    elif teamB > teamA:
        goal_difference = teamB - teamA
        print(f"Liverpool vann matchen med ({teamB} - {teamA}) med {goal_difference} mål!")
    else:
        print("Matchen slutade oavgjort!")