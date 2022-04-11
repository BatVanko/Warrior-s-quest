# Warrior-s-quest


First you will receive a skill that needs deciphered. Next you will be receiving commands split by a single space until you get the o	"For Azeroth" command. 
There are 5 possible commands:
o	"GladiatorStance" – replace all letters with upper case and print the result 
o	"DefensiveStance" - replace all letters with lower case and print the result 
o	"Dispel {index} {letter}" – replace the letter  at the index with the given one and print “Success”. If the index is invalid print "Dispel too weak." 
o	"Target Change {first substring} {second substring}"
Replace the first substring (all matches) with the second and print the result. If there are no matches – just print the skill
o	"Target Remove {substring}" – remove the substring from the string and print the result. If the substring is not contained in the string – skip the command 
•	If the input command is not in the list, print “Command doesn’texist”
Input
•	The possible commands are:
o	"For Azeroth"
o	"GladiatorStance"
o	"DefensiveStance"
o	"Dispel {index} {letter}"
o	"Target Change {first substring} {second substring}"
o	"Target Remove {substring}"
Output
•	The possible outputs are:
o	"Success!"
o	"Dispel too weak."
o	"Command doesn't exist!"
Input
fr1c710n
GladiatorStance
Dispel 2 I
Dispel 4 T
Target Change RICTION riction
For Azeroth
Output
FR1C710N
Success!
Success!
FRICT10N


