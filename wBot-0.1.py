# file: wBot-1.py
from ircutils import bot, format
from random import randint

class WulinBot(bot.SimpleBot):

    # IRC Message Methods
    # Method to respond to private messages
    def on_private_message(self, event):
        # Parse the message
        message = event.message.split()
        command = message[0]
        params = message[1:]

        # Interpret message
        self.options[command](self, event.source, params)
    
    # Method to respond to join messages
    def on_join(self, event):
        if event.source == self.nickname:
            #i = randint(0, len(enter_msgs) - 1)
            self.send_message(event.target, self.random_message(randint(0, len(self.enter_msgs) - 1)))

    # Method to respond to part messages
    def on_part(self, event):
        if event.source == self.nickname:
            message = "Aw. :("
            self.send_message(event.target, message)

    # Method to respond to channel messages
    def on_channel_message(self, event):
        # If the first character is a valid symbol
        if (event.message.startswith('@')) :
            # Parse Message
            message = event.message.split()
            command = message[0]
            params = message[1:]

            # Interpret Message
            if command == '@roll':
                if params[0] == 'rick':
                    self.send_message(event.target, "That joke's really old by now. Will you give it up, already?") 
                elif params[0].isdigit():
                    rolls = self.roll_lake(int(float(params[0])))
                    self.send_message(event.target, self.combine_rolls(rolls))
                    self.send_message(event.target, self.return_lake_response(rolls))
                else:
                    print "Error: Incorrect parameter on command @roll."
                    
    # Method to return a textual response of the lake roll.
    def return_lake_response(self, rolls):
        response = "Lake: ["
        i = 1
        for item in rolls:
            if i < len(rolls):
                response += str(item) + ", "
                i += 1
            else:
                response += str(item)
        response += "]"
        return response

    # Method to manage the "@join" command.
    def join(self, source, params):
        if (source in self.approved_users):
            print "Join Event: " + params[0] + " by " + source + "."
            self.join_channel(params[0])
        else:
            print "Blocked Join Attempt: " + params[0] + " by " + event.source + "."
            self.send_message(source, "Nope, sorry. You're not in the list.")
    
    # Method to manage the "@part" command.
    def part(self, source, params):
        if (source in self.approved_users):
            print "Part Event: By " + source + "."
            self.part_channel(params[0])
        else:
            print "Blocked Part Attempt: " + params[0] + " by " + source + "."
            self.send_message(source, "Nope, sorry. You're not in the list.")
    
    # Method to manage the "@leave" command.
    def leave(self, source, params):
        if (source in self.approved_users):
            print "Leave Event: By " + source + "."
            self.quit()
        else:
            print "Blocked Leave Attempt: By " + source + "."
            self.send_message(source, "Nope, sorry. You're not in the list.")
        
    # Method to manage the "@commands" command.
    def commands(self, source, params):
        if (source in self.approved_users):
            self.send_message(source, "My commands are: @join, @part, @leave, @roll #.")
            self.send_message(source, "Please don't hurt me. :(")
        else:
            self.send_message(source, "My commands are: @roll #.")
            self.send_message(source, "Please don't hurt me. :(")
    
    # Method to roll a group of dice
    def roll_lake(self, lake):
        i = 0
        diceList = []
        while i < lake:
            diceList.append(self.roll_single_die())
            i += 1
        # Sort and return
        return sorted(diceList, reverse = True)

    # Method to roll a single d10
    def roll_single_die(self):
        # Wulin dice rules stipulate a range of 0 to 9
        return randint(0,9)

    # Method to manage random enter messages
    def random_message(self, i):
        return self.enter_msgs[i]

    # Variables
    # List of approved users
    approved_users = ["Insert various names here."]
    # Dictionary of irc_command to method
    options = {'@join' : join, 
    '@part' : part, 
    '@leave' : leave, 
    '@commands' : commands
    }
    # Array of crazy entry messages!
    enter_msgs = ["I'm back~! <3", 
    "Raocow: \"Attention Great Old Ones.  When Raocow asks to join your ranks, you say YES!\"", 
    "I WILL DESTROY THE WORLD. :3", 
    "F U L L W I D T H T E X T"]

# The main method!
def main():
    # Create this bot's instance and some variables
    server = 'irc.anynet.net'   # Enter your IRC Server
    name = 'WulinBot'           # Enter a name for the bot.
    chanlist = '#GenericChannel'# Enter the channel it'll go to. 
    
    # Ready up the bot!
    wulinBot = WulinBot(name)
    print 'Bot ready.'

    # Connect
    wulinBot.connect(server, channel = chanlist)
    print 'Connection ready. Starting Bot.'

    # Start the bot
    wulinBot.start()
    
if __name__ == "__main__":
    main()

# End wBot-1.py