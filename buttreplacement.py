import willie, random, nltk

class Archive:
    last_message = ""
    last_butt_message= ""

    butt_sentences = []

@willie.module.rule('\\\l\s*[0-9]*')
def do_a_lenny(bot, trigger):
    if trigger.sender == '#runescape':
	tokens = trigger.bytes.split()
	if len(tokens) > 1:
	    try:
		hopefully_number = int(tokens[1])
	    except ValueError:
		hopefully_number = 0
	    bot.say('\l ' + str(hopefully_number + 1))
	else:
	    bot.say('\l 1')

@willie.module.rule('.*')
def if_rhelly_bot(bot, trigger):
    print trigger.sender
    if trigger.nick == 'rhellybot' and trigger.sender == '#runescape':
	bot.say('u suck relly')
	bot.say('\l')

def mangle_with_butts(string):

    tokens = string.split()
    tagged = nltk.pos_tag(tokens)

    words_to_buttify = random.randint(1, max(len(tokens) / 3, 1))
    buttified_words = 0
    while buttified_words < words_to_buttify:
	unflag = False
	ingflag = False
	index = random.randint(0, len(tokens) - 1)
	if word_makes_sense_to_buttify(tagged[index]):
	    pos = tagged[index][1]
	    if tokens[index][0:2] == 'un':
		unflag = True
	    if tokens[index][-3:] == 'ing':
		ingflag = True
	    if pos[-1] == 'S':
		tokens[index] = 'butts'
	    else:
		tokens[index] = 'butt'
	    if unflag:
		tokens[index] = 'un' + tokens[index]
	    if ingflag:
		tokens[index] = tokens[index] + 'ing'
	    buttified_words = buttified_words + 1
    return ' '.join(tokens)

@willie.module.rule('.*')
def replace_with_butt_or_butts(bot, trigger):
    if (len(trigger.bytes.split()) > 1 and random.randint(0, 10) == 3) or trigger.nick == 'euank':
	print trigger.bytes.encode('ascii', 'ignore')
	Archive.last_message = trigger.bytes
	new_string = mangle_with_butts(trigger.bytes)
	Archive.last_butt_message = new_string
	print new_string.encode('ascii', 'ignore')
	if not_trivia_response(trigger.bytes):
	    Archive.butt_sentences.append(new_string)
	bot.say(new_string)

def not_trivia_response(streng):
    return not (streng.startswith("Q #") or streng.startswith("A #") or streng.startswith("Giving the answer"))

def word_makes_sense_to_buttify(tagged_word):
    pos = tagged_word[1]
    wt = pos[0:2]
    if any(wt == pre for pre in ['NN', 'VB', 'JJ']):
	return True
    elif any(char.isdigit() for char in tagged_word):
	return False
    else:
	return False

@willie.module.commands('goodbye')
def testing_thing(bot, trigger):
    lines = ['euank: And I will strike down upon thee with great butt and furious anger those who attempt to poison and destroy my butts.',
	    'euank: And you will know my name is the Butt... when I lay my butt upon thee.']
    for line in lines:
	bot.msg("#interns", line)

@willie.module.commands('raw')
def send_raw(bot, trigger):
    if trigger.nick == 'grimesmg' and trigger.group(2):
	bot.say(trigger.group(2)).encode('ascii', 'ignore')

@willie.module.rule('buttbot.*\?')
def answer_question(bot, trigger):
    if len(Archive.butt_sentences) == 0:
	bot.say("swag")
    else:
	bot.say(trigger.nick  + ': ' + Archive.butt_sentences[random.randint(0, len(Archive.butt_sentences) - 1)])
