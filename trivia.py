from random import randint
from urllib2 import urlopen
import willie

class Trivia:
    url = "http://dl.dropbox.com/u/8248281/trivia/qa/"
    print "this is called"
    q = ""
    a = ""

@willie.module.commands('trivia')
def trivia(bot, trigger):
    if trigger.sender == '#buttbottrivia':
	if trigger.group(2):
	    n = str(int(trigger.group(2)) - 1).zfill(4)
	else:
	    n = "{0:04d}".format(randint(0,9999))
	try:
	    Trivia.q = urlopen(Trivia.url + "q" + n).read().strip()
	    Trivia.a = urlopen(Trivia.url + "a" + n).read().strip()
	    print "Trivia question: " + Trivia.q
	    print "Trivia answer: " + Trivia.a
	    bot.say("#" + str(int(n) + 1) + ": " + Trivia.q)
	except urllib2.URLError, e:
	    bot.say("I'm unable to reach the trivia endpoint url: " + Trivia.url)
	    raise

@willie.module.commands('answer')
def answer(bot, trigger):
    if trigger.sender == '#buttbottrivia':
	if trigger.group(2):
	    try:
		n = str(int(trigger.group(2)) - 1).zfill(4)
		answer = urlopen(Trivia.url + "a" + n).read().strip()
	    except TypeError:
		bot.say(".trivia argument must be a number between 1 - 10000")
	else:
	    answer = Trivia.a
        bot.say("Answer: " + answer)
