WulinBot
========

"Legends of the Wulin" is a tabletop RPG with a couple of interesting dice-related nuances. In it, dice pools are based on your rank (you start at 4th, which grants you 7 dice), and rolls involve combining like numbers to give you a composite total, which is modified by skills or other bonuses.

Example: I roll [7, 4, 4, 3, 2, 1, 1]. With it, I can make the following totals: 24, 21, 17, 13, 12. I can choose any of these dice as my subtotal, modify it with the skill I'm using (or my Strike, which is the combat modifier for hitting), and I'll get my total.

This bot is built for the purpose of implementing this system.

Status
=========
Beta: It's not complete, but it's well enough that it runs and doesn't explode easily. (Unless you're trying, but, in that case, you're being mean to it.)

What It Can Do
===============

This dice bot currently has the basic dice-rolling and command features. You can:

* Message it to join and part channels, as well as disconnect (leave) entirely.
* Roll dice (called "lakes" in LotW).
* Contains a small list of approved users to limit certain commands. (Currently: @leave, @join, and @part.)

What It Will Do (That Isn't Implemented Just Yet!)
================
This bot still needs a few additional features to be called released.

WulinBot should...

* Automatically combine rolls and provide all the best rolls in descending order. (See previous example.)
* Provide the option of adding a modifier to the roll. It should also add the modifier to the best roll possible.
* Come with a configuration file. This configuration file would allow an arbitrary list of allowed users for administrator commands, or even create a separate list for all users allowed to just simply use the bot.
* Be allowed to manage a few other things that LotW does, like turns, Miracles currently in play, and the like.
* Remind players of their current Chi values, and should respond with their current status.
* Remind Players and the Storyteller about the number of wounds applied at the end of a battle.
* And more!

What It Uses
==============

WulinBot is made in Python 2.7.3 (Or whatever the current Python2 version is as of 2/9/2013), and it takes advantage of IRCUtils 0.1.4, a small set of classes that wrap around and enable various IRC client and bot capabilities.

(I would have extended bot features from a pre-existing bot, but this was slightly faster, as I didn't need to learn how a bot like SupyBot worked.)