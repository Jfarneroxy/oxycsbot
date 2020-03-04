#!/usr/bin/env python3
"""A simple chatbot that directs students to office hours of CS professors."""

from chatbot import ChatBot
import random
import indicoio

indicoio.config.api_key = 'cbd8b7b9fff405463abda7d325a40890'

class OxyCSBot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""

    STATES = ['gibberish', 'waiting', 'main_question','cheaper_argument', 'more_humane_argument', 'dissuades_people_argument', 'eye_for_eye_argument', 'deserves_worst_fate_argument', 'cant_contribute_argument', 'wont_change_argument', 'positive_convo_for_another_time', 'negative_convo_for_another_time', 'annoyed_convo_for_another_time']
    

    TAGS = {
        #cheaper response
        'cheap' : 'cheaper',
        'cost' : 'cheaper',
        'price' : 'cheaper',
        'cheaper' : 'cheaper',
        'expense' : 'cheaper',
        'expensive' : 'cheaper',
        'money' : 'cheaper',
        'economic' : 'cheaper',
        'high-price' : 'cheaper',
        'costly' : 'cheaper',
        'extortionate' : 'cheaper',
        'overpriced' : 'cheaper',
        'valuable' : 'cheaper',
        'taxpayer' : 'cheaper',
        'taxpayers' : 'cheaper',
        #humane argument
        'humane' : 'humane',
        'not right' : 'humane',
        'unjust' : 'humane',
        'civil' : 'humane',
        'uncivil' : 'humane',
        'compassionate' : 'humane',
        'civilized' : 'humane',
        'humanitarian' : 'humane',
        'unsympathetic' : 'humane',
        #Dissuade argument
        'dissuade' : 'dissuade' ,
        'dissuades' : 'dissuade' ,
        'deter' : 'dissuade' ,
        'deters' : 'dissuade' ,
        'crime' : 'dissuade' ,
        'lower' : 'dissuade' ,
        'rate' : 'dissuade' ,
        'discourage' : 'dissuade' ,
        'prevent' : 'dissuade' ,
        'preemptive' : 'dissuade' ,
        'put off' : 'dissuade' ,
        'stop' : 'dissuade' ,
        'preventative' : 'dissuade' ,
        'offense' : 'dissuade' ,
        'offender' : 'dissuade' ,
        'offenders' : 'dissuade' ,
        'felon' : 'dissuade' ,
        'felons' : 'dissuade' ,
        'delinquency' : 'dissuade' ,
        'delinquent' : 'dissuade' ,
        'wrongdoing' : 'dissuade' ,
        'sin' : 'dissuade' ,
        'sins' : 'dissuade' ,
        'sinner' : 'dissuade' ,
        'sinners' : 'dissuade' ,
        #eye for an eye argument
        'justice' : 'eye for eye',
        'karma' : 'eye for eye',
        'legal' : 'eye for eye',
        'fair' : 'eye for eye',
        'fairness' : 'eye for eye',
        'judge' : 'eye for eye',
        'eye for eye' : 'eye for eye',
        'eye for an eye' : 'eye for eye',
        'hammurabi' : 'eye for eye',
        'punish' : 'eye for eye',
        'punishment' : 'eye for eye',
        'objectively' : 'eye for eye',
        'ethics' : 'eye for eye',
        'morals' : 'eye for eye',
        'morality' : 'eye for eye',
        'principle' : 'eye for eye',
        #cant contribute argument
        'contribute' : 'cant contribute',
        'worthless' : 'cant contribute',
        'alive' : 'cant contribute',
        'vital' : 'cant contribute',
        'functioning' : 'cant contribute',
        'society' : 'cant contribute',
        'wasted' : 'cant contribute',
        'valueless' : 'cant contribute',
        'unproductive' : 'cant contribute',
        'productive' : 'cant contribute',
        'meaningless' : 'cant contribute',
        'empty' : 'cant contribute',
        'pathetic' : 'cant contribute',
        'lame' : 'cant contribute',
        #deserve worst fate argument
        'deserve' : 'deserves worst fate',
        'deserves' : 'deserves worst fate',
        'worst fate' : 'deserves worst fate',
        'suffer' : 'deserves worst fate',
        'warrants' : 'deserves worst fate',
        'merits' : 'deserves worst fate',
        'earned' : 'deserves worst fate',
        'justified' : 'deserves worst fate',
        'rightful' : 'deserves worst fate',
        'reasonable' : 'deserves worst fate',
        'fitting' : 'deserves worst fate',
        'fits' : 'deserves worst fate',
        'appropriate' : 'deserves worst fate',
        'hardship' : 'deserves worst fate',
        'distress' : 'deserves worst fate',
        'pain' : 'deserves worst fate',
        'torment' : 'deserves worst fate',
        'tormented' : 'deserves worst fate',
        'trauma' : 'deserves worst fate',
        'traumatic' : 'deserves worst fate',
        'misery' : 'deserves worst fate',
        'miserable' : 'deserves worst fate',
        #won't change
        'change' : 'wont change',
        'inherently' : 'wont change',
        'bad' : 'wont change',
        'intrinsically' : 'wont change',
        'no hope' : 'wont change',
        'destructive' : 'wont change',
        'hateful' : 'wont change',
        'heinous' : 'wont change',
        'wired' : 'wont change',
        #disagree
        'disagree' : 'disagree',
        'wrong' : 'disagree',
        'no' : 'disagree',
        'nah' : 'disagree',
        'nope' : 'disagree',
        #agree
        'agree' : 'agree',
        'yes' : 'agree',
        'right' : 'agree',
        'ok' : 'agree',
        'okay' : 'agree',
        'win' : 'agree',
        "don't" : 'agree',
        #greetings
        'hi' : 'greeting',
        'hello' : 'greeting',
        'howdy' : 'greeting',
        'hey' : 'greeting',
        'morning' : 'greeting',
        'afternoon' : 'greeting',
        
        #generic
        'capital punishment' : 'capital punishment',
        'death penalty' : 'death penalty',
        'Capital punishment' : 'capital punishment',
        'Death penalty' : 'death penalty',

    }

    def __init__(self):
        """Initialize the OxyCSBot.

        The `professor` member variable stores whether the target professor has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.agreeCounter = 0
        self.disagreeCounter = 0
        self.argumentsList = ['cheaper_argument', 'more_humane_argument', 'dissuades_people_argument', 'eye_for_eye_argument', 'cant_contribute_argument', 'deserves_worst_fate_argument', 'wont_change_argument']


    #function used to clean up code -- called by every function when responding
    def determineNextState(self, message, tags):
        if 'agree' in tags:
            self.agreeCounter += 1
            if self.agreeCounter == 3:
                return 'finish_agree'
            if self.agreeCounter < 3:  
            # randomNumber = random.randrange(0, len(self.argumentsList))
            # return randomself.argumentsList[randomNumber] #return the name of a random argument (.pop() when going to it first ensures that there will only be undiscussed arguments in array)
                return 'positive_convo_for_another_time'
        if 'disagree' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                print(self.disagreeCounter)
                return 'finish_disagree'
            if self.disagreeCounter < 3:
                return 'negative_convo_for_another_time'
        else:
            return 'confused'
    
    def on_enter_gibberish(self):
        self.go_to_state(self.gibberish_from)
        # print(self.state)
        #return "that is gibberish"
        return "That's not relevant to the topic of capital punishment"
            
    # def respond_from_gibberish_function(self, message, tags):
    #     if message not gibberish
    #         return message, tags
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
            return self.finish('confused')        ###gibberish doesnt work!!!!!!!

    # "specific_faculty" state functions

    def on_enter_main_question(self):
        """Send a message when entering the "main_question" state."""
        response = "Hi. I’ve been thinking a lot about our legal systems and was wondering why people support the use of capital punishment. Why do you support capital punishment?"
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
            self.gibberish_from = 'main_question'
            return self.go_to_state('gibberish')

    # "different arguments" state functions

    def on_enter_cheaper_argument(self):
        """Send a message when entering the "cheaper_argument" state."""
        return "I thought that too at first, but it turns out that prison is actually cheaper! I was reading up on Amnesty International’s website and they estimate that death penalty cases cost an average of $1.26 million, while non-death penalty cases cost an average of $740,000"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'cheaper_argument'
            return self.go_to_state('gibberish')
        else:
            # if nextState not in self.argumentsList:
            #     self.discussedState = 'whether capital punishment is cheaper'
            # #we've already argued this topic before!
            #     return self.go_to_state('annoyed_convo_for_another_time')
            return self.go_to_state(nextState)

    def on_enter_more_humane_argument(self):
        """Send a message when entering the "more_humane_argument" state."""
        return "I would argue that methods of execution are far from humane. Most countries in the world have completely abolished capital punishment, as it’s considered to be inhumane and well below human rights standards"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'more_humane_argument'
            return self.go_to_state('gibberish')
        else:
            if nextState not in self.argumentsList:
                self.discussedState = 'whether capital punishment is more humane'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            return self.go_to_state(nextState)
        
    def on_enter_dissuades_people_argument(self):
        """Send a message when entering the "dissuades_people_argument" state."""
        return "Actually, data from the FBI shows that the threat of capital punishment doesnt deter offenders. States without capital punishment generally have homicde rates below the national rate. This conviction is also arbitrary and unfair, as nearly all death row inmates are unable to afford their own attorneys, so their lives become subject to local politics and unpredictable factors"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'dissuades_people_argument'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state(nextState)
    def on_enter_eye_for_eye_argument(self):
        """Send a message when entering the "eye_for_eye_argument" state."""
        return "I think that sort of oversimplifies the issue. And while some might consider it ‘fair’, an eye for an eye makes the whole world blind. As Gandhi said, if we try to solve violence with violence we become no better than the people we’re punishing"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'eye_for_eye_argument'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state(nextState)
    def on_enter_cant_contribute_argument(self):
        """Send a message when entering the "cant_contribute_argument" state."""
        return "If the prison system works correctly, then inmates are reformed throughout their incarceration allowing them to become productive from behind bars or as members of society if they’re released. Also, since 1973 140 people have been taken off of death row due to new evidence or wrongful convictions. Wrongful convictions ending in the death penalty can cause a serious strain on society"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'cant_contribute_argument'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state(nextState)

    def on_enter_deserves_worst_fate_argument(self):
        """Send a message when entering the "deserves_worst_fate_argument" state."""
        return "I think that life in prison is arguably a worse fate than death, and people need to be able to reflect upon their actions"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'deserves_worst_fate_argument'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state(nextState)
    
    def on_enter_wont_change_argument(self):
        """Send a message when entering the "wont_change_argument" state."""
        return "I don’t think that’s a fair assumption to make. The goal of prison systems should be to reform inmates, not punish or torture people indefinitely. People should be given a chance to grow. If we jump to execution, we’re no better than they are"

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
        if nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        if nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        if nextState == 'confused':
            self.gibberish_from = 'wont_change_argument'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state(nextState)

    # temp functions

    def on_enter_positive_convo_for_another_time(self):
        """Send a message and pose a new topic that hasn't been discussed"""
    #    randomNumber = random.randrange(0, len(self.argumentsList))
        return "Yay! We agree! What are some of your other points?"
    
    def respond_from_positive_convo_for_another_time(self, message, tags):
        """Decide what state to go to from the "positive_convo_for_another_time" state.

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
            self.gibberish_from = 'positive_convo_for_another_time'
            return self.go_to_state('gibberish')

    def on_enter_negative_convo_for_another_time(self):
        """Send a message and pose a new topic that hasn't been discussed"""
    #    randomNumber = random.randrange(0, len(self.argumentsList))
        return "That's a conversation for another time. What other points do you have?"
    
    def respond_from_negative_convo_for_another_time(self, message, tags):
        """Decide what state to go to from the "negative_convo_for_another_time" state.

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
            self.gibberish_from = 'negative_convo_for_another_time'
            return self.go_to_state('gibberish')

    def on_enter_annoyed_convo_for_another_time(self):
        """Send a message and pose a new topic that hasn't been discussed"""
    #    randomNumber = random.randrange(0, len(self.argumentsList))
        return "We've already talked about {} before! What other points do you have?".format(self.discussedState)
    
    def respond_from_annoyed_convo_for_another_time(self, message, tags):
        """Decide what state to go to from the "annoyed_convo_for_another_time" state.

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
            self.gibberish_from = 'negative_convo_for_another_time'
            return self.go_to_state('gibberish')

    # "finish" functions
    def finish_confused(self):
        """Send a message and go to the default state."""
        self.agreeCounter = 0
        self.disagreeCounter = 0
        
        return "Sorry, I'm just a simple bot that can't understand much. You can ask me about office hours though!"

    def finish_agree(self):
        """Send a message and go to the default state."""
        self.agreeCounter = 0
        self.disagreeCounter = 0
        
        return "Looks like we agree then. Yay!"

    def finish_disagree(self):
        """Send a message and go to the default state."""
        self.agreeCounter = 0
        self.disagreeCounter = 0
        
        return "Agree to disagree, I'm done debating with you for now"


if __name__ == '__main__':
    OxyCSBot().chat()
