#Programmer: Niko Hroncich
#Description: Gathering together football statistics for a quarterback
#Date: 9/21/2022
#Source for stats: https://www.espn.com/nfl/player/gamelog/_/id/3916387/type/nfl/year/2019

print("Hello!")
print("We will be gathering together football statistics for a quarterback that plays on either the college level or NFL!")
print("Ready? Let's begin!")

name = input("Enter the name of the quarterback: ")

#Week 1 Stats
passYards1 = input("Enter the passing yards for week 1: ")
rushYards1 = input("Enter the rushing yards for week 1: ")
passingAttempts1 = input("Enter the passing attempts for week 1: ")
passingCompletions1 = input("Enter the passing completions for week 1: ")
passTouchdown1 = input("Enter the number of passing touchdowns for week 1: ")
passInt1 = input("Enter the number of passing interceptions for week 1: ")
rushTouchdown1 = input("Enter the number of rushing touchdowns for week 1: ")
pYard1 = int(passYards1)
rYard1 = int(rushYards1)
pAtt1 = int(passingAttempts1)
pComp1 = int(passingCompletions1)
pTouchdown1 = int(passTouchdown1)
pInt1 = int(passInt1)
rTouchdown1 = int(rushTouchdown1)

#Week 2 Stats
passYards2 = input("Enter the passing yards for week 2: ")
rushYards2 = input("Enter the rushing yards for week 2: ")
passingAttempts2 = input("Enter the passing attempts for week 2: ")
passingCompletions2 = input("Enter the passing completions for week 2: ")
passTouchdown2 = input("Enter the number of passing touchdowns for week 2: ")
passInt2 = input("Enter the number of passing interceptions for week 2: ")
rushTouchdown2 = input("Enter the number of rushing touchdowns for week 2: ")
pYard2 = int(passYards2)
rYard2 = int(rushYards2)
pAtt2 = int(passingAttempts2)
pComp2 = int(passingCompletions2)
pTouchdown2 = int(passTouchdown2)
pInt2 = int(passInt2)
rTouchdown2 = int(rushTouchdown2)
                   
#Week 3 Stats
passYards3 = input("Enter the passing yards for week 3: ")
rushYards3 = input("Enter the rushing yards for week 3: ")
passingAttempts3 = input("Enter the passing attempts for week 3: ")
passingCompletions3 = input("Enter the passing completions for week 3: ")
passTouchdown3 = input("Enter the number of passing touchdowns for week 3: ")
passInt3 = input("Enter the number of passing interceptions for week 3: ")
rushTouchdown3 = input("Enter the number of rushing touchdowns for week 3: ")
pYard3 = int(passYards3)
rYard3 = int(rushYards3)
pAtt3 = int(passingAttempts3)
pComp3 = int(passingCompletions3)
pTouchdown3 = int(passTouchdown3)
pInt3 = int(passInt3)
rTouchdown3 = int(rushTouchdown3)

#Week 4 Stats
passYards4 = input("Enter the passing yards for week 4: ")
rushYards4 = input("Enter the rushing yards for week 4: ")
passingAttempts4 = input("Enter the passing attempts for week 4: ")
passingCompletions4 = input("Enter the passing completions for week 4: ")
passTouchdown4 = input("Enter the number of passing touchdowns for week 4: ")
passInt4 = input("Enter the number of passing interceptions for week 4: ")
rushTouchdown4 = input("Enter the number of rushing touchdowns for week 4: ")
pYard4 = int(passYards4)
rYard4 = int(rushYards4)
pAtt4 = int(passingAttempts4)
pComp4 = int(passingCompletions4)
pTouchdown4 = int(passTouchdown4)
pInt4 = int(passInt4)
rTouchdown4 = int(rushTouchdown4)

#Stats through the first 4 weeks of football
totalPassing = (pYard1 + pYard2 + pYard3 + pYard4)
totalRushing = (rYard1 + rYard2 + rYard3 + rYard4)
totalAttempts = (pAtt1 + pAtt2 + pAtt3 + pAtt4)
totalCompletions = (pComp1 + pComp2 + pComp3 + pComp4)
totalPassTouchdown = (pTouchdown1 + pTouchdown2 + pTouchdown3 + pTouchdown4)
totalPassInt = (pInt1 + pInt2 + pInt3 + pInt4)
totalRushTouchdown = (rTouchdown1 + rTouchdown2 + rTouchdown3 + rTouchdown4)

print("Here are the stats through the first 4 weeks of football for", name)
print("Total passing yards through the first 4 weeks =", totalPassing)
print("Total rushing yards through the first 4 weeks =", totalRushing)
print("Total passing attempts through the first 4 weeks =", totalAttempts)
print("Total passing completions through the first 4 weeks =", totalCompletions)
print("Total passing touchdowns through the first 4 weeks =", totalPassTouchdown)
print("Total passing interceptions through the first 4 weeks =", totalPassInt)
print("Total rushing touchdowns through the first 4 weeks =", totalRushTouchdown)

print("Here are the average stats per game for", name)

#Averages through the first 4 weeks
avgPassing = (totalPassing / 4)
avgRushing = (totalRushing / 4)
compPercent = (totalCompletions / totalAttempts)
avgPassTouchdown = (totalPassTouchdown / 4)
avgPassInt = (totalPassInt / 4)
avgRushTouchdown = (totalRushTouchdown / 4)

print("Average passing yards per game =", format(avgPassing,'.1f'))
print("Average rushing yards per game =", format(avgRushing,'.1f'))
print("Completion percentage per game = %", format(compPercent,'.1f'))
print("Average passing touchdowns per game =", format(avgPassTouchdown,'.1f'))
print("Average passing interceptions per game =", format(avgPassInt,'.1f'))
print("Average rushing touchdowns per game =", format(avgRushTouchdown,'.1f'))



