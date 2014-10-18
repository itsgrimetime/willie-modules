import willie, random

def mangle_with_butts(string):
    words = string.split()
    words_to_buttify = random.randint(1, max(len(words) / 2, 1))
    for i in range(words_to_buttify):
	index = random.randint(0, len(words) - 1)
	if words[index][-1] == 's' or words[index][-1] == 'S':
	    words[index] = 'butts'
	else:
	    words[index] = 'butt'
    return ' '.join(words)

@willie.module.rule('.*')
def replace_with_butt_or_butts(bot, trigger):
    if random.randint(1, 6) == 3:
	print trigger.bytes
	new_string = mangle_with_butts(trigger.bytes)
	print new_string
	bot.say(new_string)
