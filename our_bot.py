#!/usr/bin/env python3
"""A simple chatbot that directs students to office hours of CS professors."""

from chatbot import ChatBot
import random
import indicoio

indicoio.config.api_key = 'cbd8b7b9fff405463abda7d325a40890'

class OxyCSBot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""

    STATES = ['waiting','main_question','cheaper_argument', 'more_humane_argument', 'dissuades_people_argument', 'eye_for_eye_argument', 'deserves_worst_fate_argument', 'cant_contribute_argument', 'wont_change_argument']
    

    TAGS = {
        # cheaper argument
        'cheap' : 'cheaper',
        'cost' : 'cheaper',
        'price' : 'cheaper',
        'cheaper' : 'cheaper',

        #more humane argument
        'humane' : 'humane',
        'not right' : 'humane',
        'unjust' : 'humane',
        'civil' : 'humane',

        #dissuades people argument
        'dissuade' : 'dissuade' ,
        'dissuades' : 'dissuade',
        'deter' : 'dissuade',
        'deters' : 'dissuade',

        #eye for eye/justice argument
        'justice' : 'eye for eye',
        'karma' : 'eye for eye',
        'legal' : 'eye for eye',
        'fair' : 'eye for eye',
        'eye for eye' : 'eye for eye',

        #why keep alive? Argument
        'contribute' : 'cant contribute',
        'alive' : 'cant contribute',

        #deserve worst fate possible argument
        'deserve' : 'deserves worst fate',
        'deserves' : 'deserves worst fate',
        'worst fate' : 'deserves worst fate',
        'suffer' : 'deserves worst fate',

        #people are inherently bad/won't change argument
        'change' : 'wont change',
        'inherently bad' : 'wont change',

        # #new evidence argument
        # 'Evidence' :  'evidence'
        # 'Changes' :  'changes'
        # 'Reasonable doubt' : 'reasonable doubt'
        # 'New' : 'new'
        # 'Information' : 'information'

        #disagree

        'disagree': 'disagree',
        "don't agree" : "disagree",
        'wrong' : 'disagree',
        'no' : 'disagree',
        'nah' : 'disagree',
        'nope' : 'disagree',
        'false' : 'false',

        #agree
        'agree' : 'agree',
        'yes' : 'agree',
        'right' : 'agree',
        'ok' : 'agree',
        'okay' : 'agree',
        'true' : 'agree',

        #generic tags
        'hello' : 'greeting',
        'hi' : 'greeting',
        'greetings' : 'greeting',

        # 'Capital punishment' : 'Capital punishment',
        # 'capital punishment' : 'capital punishment',
        # 'Death penalty' : 'Death Penalty',
        # 'death penalty' : 'death Penalty'
        'Capital punishment' : 'capital punishment',
        'capital punishment' : 'capital punishment',
        'Death penalty' : 'death penalty',
        'death penalty' : 'death penalty'

    }

    argumentsList = ['cheaper_argument', 'more_humane_argument', 'dissuades_people_argument', 'eye_for_eye_argument', 'cant_contribute_argument', 'deserves_worst_fate_argument', 'wont_change_argument']

    def __init__(self):
        """Initialize the OxyCSBot.

        The `professor` member variable stores whether the target professor has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.agreeCounter = 0
        self.disagreeCounter = 0

    #function used to clean up code -- called by every function when responding
    def determineNextState(self, message, tags):
        if 'agree' in tags and self.agreeCounter == 3:
            return 'finish_agree'
        elif 'agree' in tags and self.agreeCounter < 3:  #TODO how do we pose a new topic?
            # randomNumber = random.randrange(0, len(self.argumentsList))
            # return randomself.argumentsList[randomNumber] #return the name of a random argument (.pop() when going to it first ensures that there will only be undiscussed arguments in array)
            return 'finish_agree'
        elif 'disagree' in tags and self.disagreeCounter == 3:
            return 'finish_disagree'
        elif 'disagree' in tags and self.disagreeCounter < 3:
            return 'finish_disagree' #TODO how do we pose a new topic?
        else:
            return 'confused'
    
    # def on_enter_gibberish_function(self):
    #     return "That's not relevant to cp"
            
    # def respond_from_gibberish_function(self, message, tags):
    #     if message not gibberish
    #         return message
    #     else:
    #         go_to_state(gibberish_function(message, tags)
    
    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        if 'greeting' in tags:
            return self.go_to_state('main_question')
        elif 'capital punishment' in tags or 'death penalty' in tags and 'hello' not in tags:
            if indicoio.sentiment(message) >= .5:
                return self.go_to_state('pose_topic') ############## cant pose topic yet--not a function!
            elif indicoio.sentiment(message) < .5:
                return self.finish('agree')
        else:
            return self.finish('confused')

    # "specific_faculty" state functions

    def on_enter_main_question(self):
        """Send a message when entering the "main_question" state."""
        response = "Hello. Why do you support the use of capital punishment?"
        return response

    def respond_from_main_question(self, message, tags):
        """Decide what state to go to from the "main_question" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        
        if "I don't" in message:  #####doesnt work ATM!!!
            return self.finish('agree')
        #go through all possible reasons
        elif 'cheaper' in tags:
            return self.go_to_state('cheaper_argument')
        elif 'humane' in tags:
            return self.go_to_state('more_humane_argument')
        elif 'dissuade' in tags:
            return self.go_to_state('dissuades_people_argument')
        elif 'eye for eye' in tags:
            return self.go_to_state('eye_for_eye_argument')
        elif 'cant contribute' in tags:
            return self.go_to_state('cant_contribute_argument')
        elif 'deserves worst fate' in tags:
            return self.go_to_state('deserves_worst_fate_argument')
        elif 'wont change' in tags:
            return self.go_to_state('wont_change_argument')
        else:
            return self.finish('confused')
            # message, tags = self.go_to_state('gibberish_function')
            # return respond_from_main_question(self, message, tags)

    # "different arguments" state functions

    def on_enter_cheaper_argument(self):
        """Send a message when entering the "cheaper_argument" state."""
        return "Prison is actually cheaper! Court appeals can last upwards of 20+ years"

    def respond_from_cheaper_argument(self, message, tags):
        """Decide what state to go to from the "cheaper_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        
        ####TODO add if statement that checks if argument counter has reached three to prevent circular arguments

        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)

    def on_enter_more_humane_argument(self):
        """Send a message when entering the "more_humane_argument" state."""
        return "Death via electrocution, firing squad, or poison doesn't sound very humane to me"

    def respond_from_more_humane_argument(self, message, tags):
        """Decide what state to go to from the "more_humane_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)
        
    def on_enter_dissuades_people_argument(self):
        """Send a message when entering the "dissuades_people_argument" state."""
        return "This is actually false. Provide stat?????????????"

    def respond_from_dissuades_people_argument(self, message, tags):
        """Decide what state to go to from the "dissuades_people_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)
    def on_enter_eye_for_eye_argument(self):
        """Send a message when entering the "eye_for_eye_argument" state."""
        return "If multiple people were affected, then one death is not justice (fix??????????)"

    def respond_from_eye_for_eye_argument(self, message, tags):
        """Decide what state to go to from the "eye_for_eye_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)
    def on_enter_cant_contribute_argument(self):
        """Send a message when entering the "cant_contribute_argument" state."""
        return "The average time for a capital punishment case is ____________. They might as well be in prison during this time, no?"

    def respond_from_cant_contribute_argument(self, message, tags):
        """Decide what state to go to from the "cant_contribute_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)

    def on_enter_deserves_worst_fate_argument(self):
        """Send a message when entering the "deserves_worst_fate_argument" state."""
        return "Thinking about what your actions in prison for the rest of your life sounds pretty bad to me!"

    def respond_from_deserves_worst_fate_argument(self, message, tags):
        """Decide what state to go to from the "deserves_worst_fate_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)
    
    def on_enter_wont_change_argument(self):
        """Send a message when entering the "wont_change_argument" state."""
        return "You don't know that"

    def respond_from_wont_change_argument(self, message, tags):
        """Decide what state to go to from the "wont_change_argument" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags) #returns string
        if nextState == 'finish_agree':
            return self.finish('agree')
        if nextState == 'finish_disagree':
            return self.finish('disagree')
        if nextState == 'confused':
            return self.finish('confused')
        else:
            return self.go_to_state(nextState)

    # temp functions

    #make one for gibberish!!! -- left it out initially

    # def on_enter_convo_for_another_time(self):
    #     """Send a message and pose a new topic that hasn't been discussed""""
    #     randomNumber = random.randrange(0, len(self.argumentsList))
    #     return "That's a conversation for another time. Whatrandomself.argumentsList[randomNumber]


    # "finish" functions
    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. You can ask me about office hours though!"

    def finish_agree(self):
        """Send a message and go to the default state."""
        return "Looks like we agree then. Yay!"

    def finish_disagree(self):
        """Send a message and go to the default state."""
        return "Agree to disagree, I'm done debating with you for now"


if __name__ == '__main__':
    OxyCSBot().chat()
