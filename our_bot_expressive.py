#!/usr/bin/env python3
"""A simple chatbot that debates people who support capital punishment"""

from chatbot import ChatBot
import random

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

class CapPun(ChatBot):
    """A simple chatbot that debates people who support capital punishment"""

    STATES = ['gibberish', 'waiting', 'disagree_main_question', 'main_question','cheaper_argument1', 'cheaper_argument2', 'more_humane_argument1', 'more_humane_argument2','more_humane_argument3','dissuades_people_argument1', 'dissuades_people_argument2', 'eye_for_eye_argument1', 'eye_for_eye_argument2',  'cant_contribute_argument1', 'cant_contribute_argument2', 'deserves_worst_fate_argument1', 'wont_change_argument1', 'wont_change_argument2', 'positive_convo_for_another_time', 'negative_convo_for_another_time', 'annoyed_convo_for_another_time']
    

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
        'deterrant' : 'dissuade',
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
        "don't agree": 'disagree',
        #agree
        'agree' : 'agree',
        'yes' : 'agree',
        'right' : 'agree',
        'ok' : 'agree',
        'okay' : 'agree',
        'win' : 'agree',
        'fair' : 'agree',
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
        """Initialize CapPun."""

        super().__init__(default_state='waiting')
        self.agreeCounter = 0
        self.disagreeCounter = 0
        self.argumentsList = ['cheaper_argument1', 'more_humane_argument1', 'dissuades_people_argument1', 'eye_for_eye_argument1', 'cant_contribute_argument1', 'deserves_worst_fate_argument1', 'wont_change_argument1']
        self.gibberish_from = None
    
    #used to determine sentiment of opening user input
    def sentiment_analyzer_scores(self, sentence):
        score = analyser.polarity_scores(sentence)
        maxVal = 0
        for key in score:
            if score[key] > maxVal:
                maxVal = score[key]
                maxKey = key
        return maxKey

    #function used to clean up code -- called by every function when responding
    def determineNextState(self, message, tags, levelInArgument, levelsInArgument):
        #if person keeps bringing up other topics after hearing counterpoint, check if they've "disagreed" enough times to end convo
        #go through all other arguments
        if 'cheaper' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'cheaper_argument1'
        elif 'humane' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'more_humane_argument1'
        elif 'dissuade' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'dissuades_people_argument1'
        elif 'eye for eye' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'eye_for_eye_argument1'
        elif 'cant contribute' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'cant_contribute_argument1'
        elif 'deserves worst fate' in tags:
            self.disagreeCounter += 1           
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'deserves_worst_fate_argument1'
        elif 'wont change' in tags:
            self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            return 'wont_change_argument1'
        #placed before checking agree tags since disagree tags are more specific, reducing # of false positives
        elif 'disagree' in tags:
            if levelInArgument == levelsInArgument:
                self.disagreeCounter += 1
            if self.disagreeCounter == 3:
                return 'finish_disagree'
            if self.disagreeCounter < 3:
                return 'negative_convo_for_another_time'
        elif 'agree' in tags:
            self.agreeCounter += 1
            if self.agreeCounter == 3:
                return 'finish_agree'
            if self.agreeCounter < 3:  
                return 'positive_convo_for_another_time'
        else:
            return 'confused'

    def decideDiscussedState(self, nextState):
        if nextState == 'cheaper_argument1':
            return 'whether capital punishment is cheaper than prison'
        elif nextState == 'more_humane_argument1':
            return 'whether capital punishment is more humane than prison'
        elif nextState == 'dissuades_people_argument1':
            return 'whether capital punishment dissuades people from committing other haneous crimes'
        elif nextState ==  'eye_for_eye_argument1':
            return 'whether capital punishment is an eye for an eye type of thing'
        elif nextState == 'deserves_worst_fate_argument1':
            return 'whether death is a worse fate for people than prison'
        elif nextState == 'cant_contribute_argument1':
            return 'whether people can contribute to society if not sentenced to death'
        elif nextState == 'wont_change_argument1':
            return 'whether people can change after committing such haneous crimes'
    
    def on_enter_gibberish(self):
        if self.gibberish_from != 'main_question':
            self.go_to_state(self.gibberish_from)
            return "That's not relevant to the topic of capital punishment"
        else:
            return self.finish('gibberish')

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
            message = message.replace('punishment','').replace('death','').replace('penalty','')
            if self.sentiment_analyzer_scores(message) == 'pos' or self.sentiment_analyzer_scores(message) == 'neu':
                return self.go_to_state('disagree_main_question')
                
            elif self.sentiment_analyzer_scores(message) == 'neg':
                return self.finish('agree')
        else:
            self.gibberish_from = 'main_question'
            return self.go_to_state('gibberish') 

    def on_enter_disagree_main_question(self):
        """Send a message when entering the "disagree_main_question" state."""
        response = "I strongly disagree. Why do you support capital punishment?"
        return response

    def respond_from_disagree_main_question(self, message, tags):
        """Decide what state to go to from the "disagree_main_question" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        #go through all possible reasons
        if 'cheaper' in tags:
            return self.go_to_state('cheaper_argument1')
        elif 'humane' in tags:
            return self.go_to_state('more_humane_argument1')
        elif 'dissuade' in tags:
            return self.go_to_state('dissuades_people_argument1')
        elif 'eye for eye' in tags:
            return self.go_to_state('eye_for_eye_argument1')
        elif 'cant contribute' in tags:
            return self.go_to_state('cant_contribute_argument1')
        elif 'deserves worst fate' in tags:
            return self.go_to_state('deserves_worst_fate_argument1')
        elif 'wont change' in tags:
            return self.go_to_state('wont_change_argument1')
        else:
            self.gibberish_from = 'disagree_main_question'
            return self.go_to_state('gibberish')

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

        if "i don't" in message.lower() or 'i dont' in message.lower() or 'i do not' in message.lower(): 
            return self.finish('agree')
        #go through all possible reasons
        elif 'cheaper' in tags:
            return self.go_to_state('cheaper_argument1')
        elif 'humane' in tags:
            return self.go_to_state('more_humane_argument1')
        elif 'dissuade' in tags:
            return self.go_to_state('dissuades_people_argument1')
        elif 'eye for eye' in tags:
            return self.go_to_state('eye_for_eye_argument1')
        elif 'cant contribute' in tags:
            return self.go_to_state('cant_contribute_argument1')
        elif 'deserves worst fate' in tags:
            return self.go_to_state('deserves_worst_fate_argument1')
        elif 'wont change' in tags:
            return self.go_to_state('wont_change_argument1')
        else:
            self.gibberish_from = 'main_question'
            return self.go_to_state('gibberish')

    # "different arguments" state functions

    def on_enter_cheaper_argument1(self):
        """Send a message when entering the "cheaper_argument1" state."""
        return "Actually, you're wrong! Prison is cheaper"
    def respond_from_cheaper_argument1(self, message, tags):
        """Decide what state to go to from the "cheaper_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 2) #returns string
        #now that you've visited this argument for the first time, remove it from the arguments list!
        if self.gibberish_from != 'cheaper_argument1':
            index = self.argumentsList.index('cheaper_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('cheaper_argument2')
        elif nextState == 'confused':
            self.gibberish_from = 'cheaper_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.discussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)   
    
    def on_enter_cheaper_argument2(self):
        """Send a message when entering the "cheaper_argument2" state."""
        return "Well, according to Amnesty International, death penalty cases cost an average of $1.26 million while non-death penalty cases cost an average of $740,000"
    def respond_from_cheaper_argument2(self, message, tags):
        """Decide what state to go to from the "cheaper_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 2) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'cheaper_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.discussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)         
                   

    def on_enter_more_humane_argument1(self):
        """Send a message when entering the "more_humane_argument1" state."""
        return "How do you justify that?"

    def respond_from_more_humane_argument1(self, message, tags):
        """Decide what state to go to from the "more_humane_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 3) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'more_humane_argument1': 
            index = self.argumentsList.index('more_humane_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'more_humane_argument1'
            return self.go_to_state('gibberish')
        else:
            return self.go_to_state('more_humane_argument2')
   
    def on_enter_more_humane_argument2(self):
        """Send a message when entering the "more_humane_argument2" state."""
        return "That doesn't make sense, I think death is far from humane and incredibly barbaric"
                
    def respond_from_more_humane_argument2(self, message, tags):
        """Decide what state to go to from the "more_humane_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 3) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('more_humane_argument3')
        elif nextState == 'confused':
            self.gibberish_from = 'more_humane_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)     

    def on_enter_more_humane_argument3(self):
        """Send a message when entering the "more_humane_argument3" state."""
        return "Most countries in the world have completely abolished capital punishment, and I think we should do the same"

    def respond_from_more_humane_argument3(self, message, tags):
        """Decide what state to go to from the "more_humane_argument3" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 3, 3) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'more_humane_argument3'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState) 

    def on_enter_dissuades_people_argument1(self):
        """Send a message when entering the "dissuades_people_argument1" state."""
        return "Actually, data from the FBI shows that the threat of capital punishment doesnt deter offenders. States without capital punishment generally have homicde rates below the national rate"
        
    def respond_from_dissuades_people_argument1(self, message, tags):
        """Decide what state to go to from the "dissuades_people_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 2) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'dissuades_people_argument1':    
            index = self.argumentsList.index('dissuades_people_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('dissuades_people_argument2')
        elif nextState == 'confused':
            self.gibberish_from = 'dissuades_people_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)
    
    def on_enter_dissuades_people_argument2(self):
        """Send a message when entering the "dissuades_people_argument2" state."""
        return "Well, I think this conviction is also arbitrary and unfair, as nearly all death row inmates are unable to afford their own attorneys, so their lives become subject to local politics and unpredictable factors"
        
    def respond_from_dissuades_people_argument2(self, message, tags):
        """Decide what state to go to from the "dissuades_people_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 2) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'dissuades_people_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)
   
    def on_enter_eye_for_eye_argument1(self):
        """Send a message when entering the "eye_for_eye_argument1" state."""
        return 'You\'re oversimplifying it, the whole quote is "an eye for an eye makes the whole world blind"'

    def respond_from_eye_for_eye_argument1(self, message, tags):
        """Decide what state to go to from the "eye_for_eye_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 2) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'eye_for_eye_argument1':    
            index = self.argumentsList.index('eye_for_eye_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('eye_for_eye_argument2')
        elif nextState == 'confused':
            self.gibberish_from = 'eye_for_eye_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState) 

    def on_enter_eye_for_eye_argument2(self):
        """Send a message when entering the "eye_for_eye_argument2" state."""
        return "Well, as Gandhi said, if we try to solve violence with violence we become no better than the people we’re punishing"

    def respond_from_eye_for_eye_argument2(self, message, tags):
        """Decide what state to go to from the "eye_for_eye_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 2) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'eye_for_eye_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)
  
    def on_enter_cant_contribute_argument1(self):
        """Send a message when entering the "cant_contribute_argument1" state."""
        return "That’s pretty pessimistic. If the prison system works correctly, then inmates are reformed throughout their incarceration allowing them to become productive from behind bars or as members of society if they’re released"
    
    def respond_from_cant_contribute_argument1(self, message, tags):
        """Decide what state to go to from the "cant_contribute_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 2) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'cant_contribute_argument1':    
            index = self.argumentsList.index('cant_contribute_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('cant_contribute_argument2')
        elif nextState == 'confused':
            self.gibberish_from = 'cant_contribute_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)   

    def on_enter_cant_contribute_argument2(self):
        """Send a message when entering the "cant_contribute_argument2" state."""
        return "Well, numbers don't lie, and since 1973, 140 people have been taken off of death row due to new evidence or wrongful convictions. We can’t risk executing innocent people"
    
    def respond_from_cant_contribute_argument2(self, message, tags):
        """Decide what state to go to from the "cant_contribute_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 2) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'cant_contribute_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState)     

    def on_enter_deserves_worst_fate_argument1(self):
        """Send a message when entering the "deserves_worst_fate_argument1" state."""
        return "I think that life in prison is arguably a worse fate than death, and people need to be able to reflect upon their actions"

    def respond_from_deserves_worst_fate_argument1(self, message, tags):
        """Decide what state to go to from the "deserves_worst_fate_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 1) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'deserves_worst_fate_argument1':    
            index = self.argumentsList.index('deserves_worst_fate_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'deserves_worst_fate_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState) 
    
    def on_enter_wont_change_argument1(self):
        """Send a message when entering the "wont_change_argument1" state."""
        return "I don’t think that’s a fair assumption to make. The goal of prison systems should be to reform inmates, not punish or torture people indefinitely"

    def respond_from_wont_change_argument1(self, message, tags):
        """Decide what state to go to from the "wont_change_argument1" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 1, 2) #returns string
        #now that you've visited this argument, remove it from the arguments list!
        if self.gibberish_from != 'wont_change_argument1':    
            index = self.argumentsList.index('wont_change_argument1')
            self.argumentsList[index] = None

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('wont_change_argument2')
        elif nextState == 'confused':
            self.gibberish_from = 'wont_change_argument1'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
        else:
            return self.go_to_state(nextState) 

    def on_enter_wont_change_argument2(self):
        """Send a message when entering the "wont_change_argument2" state."""
        return "I don't know, I think people should be given a chance to grow. If we jump to execution, we’re no better than they are"

    def respond_from_wont_change_argument2(self, message, tags):
        """Decide what state to go to from the "wont_change_argument2" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        nextState = self.determineNextState(message, tags, 2, 2) #returns string

        if nextState == 'finish_agree':
            return self.finish('agree')
        elif nextState == 'finish_disagree':
            return self.finish('disagree')
        elif nextState == 'positive_convo_for_another_time':
            return self.go_to_state('positive_convo_for_another_time')
        elif nextState == 'negative_convo_for_another_time':
            return self.go_to_state('negative_convo_for_another_time')
        elif nextState == 'confused':
            self.gibberish_from = 'wont_change_argument2'
            return self.go_to_state('gibberish')
        #if you've already talked about what the user wants to talk about, say you've already talked about it!
        elif nextState not in self.argumentsList:
                self.discussedState = self.decideDiscussedState(nextState)
                #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
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
        #go through all possible reasons
        if 'cheaper' in tags:
            if 'cheaper_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is cheaper'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cheaper_argument1')
        elif 'humane' in tags:
            if 'more_humane_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is more humane'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('more_humane_argument1')
        elif 'dissuade' in tags:
            if 'dissuades_people_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment dissuades people from committing other heinous crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('dissuades_people_argument1')
        elif 'eye for eye' in tags:
            if 'eye_for_eye_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is an eye for an eye type of thing'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('eye_for_eye_argument1')
        elif 'cant contribute' in tags:
            if 'cant_contribute_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can contribute to society if not sentenced to death'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cant_contribute_argument1')
        elif 'deserves worst fate' in tags:
            if 'deserves_worst_fate_argument1' not in self.argumentsList:
                self.discussedState = 'whether death is a worse fate for people than prison'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('deserves_worst_fate_argument1')
        elif 'wont change' in tags:
            if 'wont_change_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can change after committing such crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('wont_change_argument1')
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
        #go through all possible reasons
        if 'cheaper' in tags:
            if 'cheaper_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is cheaper'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cheaper_argument1')
        elif 'humane' in tags:
            if 'more_humane_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is more humane'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('more_humane_argument1')
        elif 'dissuade' in tags:
            if 'dissuades_people_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment dissuades people from committing other heinous crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('dissuades_people_argument1')
        elif 'eye for eye' in tags:
            if 'eye_for_eye_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is an eye for an eye type of thing'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('eye_for_eye_argument1')
        elif 'cant contribute' in tags:
            if 'cant_contribute_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can contribute to society if not sentenced to death'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cant_contribute_argument1')
        elif 'deserves worst fate' in tags:
            if 'deserves_worst_fate_argument1' not in self.argumentsList:
                self.discussedState = 'whether death is a worse fate for people than prison'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('deserves_worst_fate_argument1')
        elif 'wont change' in tags:
            if 'wont_change_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can change after committing such crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('wont_change_argument1')
        else:
            self.gibberish_from = 'negative_convo_for_another_time'
            return self.go_to_state('gibberish')
    
    def on_enter_annoyed_convo_for_another_time(self):
        """Send a message and pose a new topic that hasn't been discussed"""
    #    randomNumber = random.randrange(0, len(self.argumentsList))
        return "We've already talked about {}. What are some of your other points?".format(self.discussedState)
    
    def respond_from_annoyed_convo_for_another_time(self, message, tags):
        """Decide what state to go to from the "annoyed_convo_for_another_time" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        #go through all possible reasons
        if 'cheaper' in tags:
            if 'cheaper_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is cheaper'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cheaper_argument1')
        elif 'humane' in tags:
            if 'more_humane_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is more humane'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('more_humane_argument1')
        elif 'dissuade' in tags:
            if 'dissuades_people_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment dissuades people from committing other heinous crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('dissuades_people_argument1')
        elif 'eye for eye' in tags:
            if 'eye_for_eye_argument1' not in self.argumentsList:
                self.discussedState = 'whether capital punishment is an eye for an eye type of thing'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('eye_for_eye_argument1')
        elif 'cant contribute' in tags:
            if 'cant_contribute_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can contribute to society if not sentenced to death'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('cant_contribute_argument1')
        elif 'deserves worst fate' in tags:
            if 'deserves_worst_fate_argument1' not in self.argumentsList:
                self.discussedState = 'whether death is a worse fate for people than prison'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('deserves_worst_fate_argument1')
        elif 'wont change' in tags:
            if 'wont_change_argument1' not in self.argumentsList:
                self.discussedState = 'whether people can change after committing such crimes'
            #we've already argued this topic before!
                return self.go_to_state('annoyed_convo_for_another_time')
            else:
                return self.go_to_state('wont_change_argument1')
        else:
            self.gibberish_from = 'positive_convo_for_another_time'
            return self.go_to_state('gibberish')

    # "finish" functions
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
    
    def finish_gibberish(self):
        """Send a message and go to the default state."""
        self.agreeCounter = 0
        self.disagreeCounter = 0
        
        return "That's not relevant to the topic of capital punishment"


if __name__ == '__main__':
    CapPun().chat()
