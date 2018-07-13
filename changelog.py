ending = "\nTo see other versions, just type that version's number.\nTo see a list of all of the version's numbers, type \"list\".\nTo keep up the current screen you are seeing without being able to change the screen via inputs, type \"keepup\"\nTo exit, type \"exit\"\n```"

a = "```\nv1.0.0\nInitial release.\n" + ending

b = "```\nv1.0.1\nAdded admin to the permission checking code and fixed co-captains and captains\nChanged !hello to !pzhello to make sure other bots don't get in the way.\nAdded !pzhelp and !pzchangelog (again with pz to make sure other bots don't get in the way)\n" + ending

c = "```\nv1.1.0\nCompressed a lot of code via functions. Sadly this is backend, so you won't see many of the changes, but it still warrants a x.1.x instead of a x.x.1 due to how much was changed.\nAdded !pzbotcode, which shows you the GitHub page to the code.\n" + ending

d = "```\nv1.1.1\nAdded !pzproteccdenpa because Aurora wanted it. Knock yourself out.\n" + ending

e = "```\nv1.1.2\nRemoved v1.1.1 feature and made the bot automatically run !run at startup... I hope.\n" + ending

f = "```\nv1.1.3\nMainly bugfixes:\nMade sure things like !run (commands with no parameters) can't also be triggered by doing things like !runningtopineapples.\nMade sure to get information for all of the roles only once. This should make it more stable.\nThe Omega, Infinite, and Alpha roles are also done only once, but now are checked alongside with the other roles instead of doing it during !omepassed and such.\n" + ending

g = "```\nv1.1.4\n!canprac has been fixed; how it handled canceling the bot's messages was not made correctly.\n" + ending

h = "```\nv1.2.0\nThe merge update:\nMerged !omepassed, !infpassed, and !alppassed into one, complete with a prompt.\nNow automatically announces the next practice is canceled when !canprac is run.\nBugfix: Talking to the bot in a DM won't crash it now (thankfully, nobody has done that yet except me once) and instead make it do nothing.\n" + ending

i = "```\nv1.2.1\nBugfix: Made sure the bot doesn't ping Omega on repeat for a whole minute.\nAdded an easter egg that has a one of 49,999 chance of happening.\n" + ending

j = "```\nv1.2.2\nRemoved !pzsorry, as it was only meant for one use.\nAdded the pass to \"Practice is starting now!\"\nBugfix: Cleaned up the code to how the bot reacts with emojis to certain messages.\n" + ending

k = "```\nv1.2.3\nAdded an exception to when you run !passed with nobody mentioned.\nMade a changelog screen for !pzchangelog, allowing you to see all of the changelogs without going to pastebin. Will be adding a similar feature to !pzhelp soon.\n" + ending

l = "```\nv1.2.4\nAdded an option to keep the current changelog screen up but also make the bot not respond to new inputs (an exit without deleting the program, one may say).\nBugfix: Made sure the pass shown at \"Practice starts now\" is accurate and not \"1111\".\n```"