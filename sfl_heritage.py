#!/usr/bin/env python

import random
import textwrap

import speechd
#spk = speechd.Speaker('foobar')
#spk.set_output_module('espeak')
#spk.set_rate(-1)

pays = ['Iraq', 'Nigeria', 'Afghanistan', 'Mozambique', 'Angola','Zimbabwe','Ethiopia',
	 'Cote d\'ivoire', 'Bangladesh', 'Comoros', 'Burkina Faso','Congo','Sudan']
parente = ['husband', 'father', 'cousin', 'brother', 'uncle',
		'stepfather','grandfather' ]
deathreaction = [ 'Unfortunately','Sadly','To my despair','Despite his reputation' ]
deathmethod = ['was killed','was executed','starved to death', 'was raped and killed','was poisoned','was beheaded',
		'was crucified','was eaten', 'was hanged','was shot','was beaten to death','commited suicide',
		 'was crushed with a sledgehammer','was dissolved in an acid tank','drowned in a beer tank']
cachette = ['prison', 'bunker','garbage bin','garage', 'farm','brothel','basement',
		 'Saddam\'s palace', 'cave', 'washroom', 'datacenter', 'piggery','car\'s trunk' ]
currencies = ['USD', 'GBP', 'CAD', 'Euros', 'RMB','AUD']
profession = ['judge','finance officer', 'sysadmin','CIO', 'soldier', 'officer','priest', 'warlord','sergent','journalist',
		'successful lawyer', 'general', 'minister', 'porn actor','drug dealer', 'banker','Microsoft employee', 
		'Microsoft Certified Professional','wealthy farmer','businessman','spy','Internet scammer',
		'Somali pirate','nude dancer','director of a big company', 'Romanian hacker' ]
events = ['Gulf war', 'Afghanistan war', 'September 11th attacks','Tunisian revolution',
	   'Algerian terrorist period', 'Rwandan civil war', 'Vietnam War',
	   'Haitian earthquake', 'Tamil Tiger attacks', 'riots','meteorite fall',
           'revolution', 'U S bombing', 'food shortage','elections','US invasion',
           'Israeli attack on Lebanon', 'chemical weapons testing','Intifadha',
           'terrorist act', 'Tchernobyl nuclear accident', 'tyrannosaurs attack',
           'execution of Saddam Hussein', 'flood', 'extratterrestrial invasion','collapse of the Soviet Union' ]

persons = [ 'Sir', 'Madam', 'Sir/Madam', 'Valued contact','Brother in Christ','Sister in Christ' ]
expeditorfirstname = [ 'Samira', 'Yasmina', 'Marie','Natasha','Gabriela','Alexandra','Mona',
		  'Jiang', 'Elizabeth','Grace','Lala' ]
expeditorlastname = [ 'Ben Laden', 'Hussein', 'Zulu', 'Abondis','Wong','Tang','Ballmer','de Raadt', 'Orahee','Kibaki'] 
mymood = [ 'am desperate', 'am unlucky', 'am depressed', 'almost died', 'am devastated', 'am exhausted','am very tired' ]
truthquality = ['unbelievable','awful','sad','shocking','disgusting','depressing']
qualityperson = ['a person I can trust', 'a God-fearing person','very kind','very honest','a very honourable person',
		'a respected citizen','somebody I can trust']
evil = ['Satan worshiping','diabolic','Ctulhu-worshiping','sadist','Nazi','fascist','cocaine addicted','sadist, perverted',
	'crack-addicted, Ctulhu worshiping','voodoo zombie-worshiping','Satanic followers','Satanist','incest lovers',
	'cannibal','corrupted','godawful stinking sadomasochists','EULA worshiping']
torture = ['agressed me with a meteorite','hit me with a hockey cross','hit me with a crowbar','agressed me with a rusted motherboard','beated me with hard disk platters','hit my head with Saddam portrait','threatened me with a golden kalashnikov','obliged me to configure a Nortel PBX','obliged me to rewrite Linux in brainfuck','made me seat on a hot tandoori oven','obliged me to work in a nude dancers bar','obliged me to work in a gay sex shop','obliged me to rewrite the MS Access EULA with my blood','obliged me to work with Windows Vista on a 286 computer','obliged me to rewrite the OpenBSD kernel in Visual Basic','obliged me to clean their dirty wahsroom','hit me with a guitar']
personalinformation = ['your social insurance number','your scanned signature in a JPEG file',
			'your fingerprints scanned in a high resolution BMP file', 'your private SSH key',
			'your ID','your passport','your biometric data','your DNA','your credit card number and secret code',
			'your birth certificate','your driver\'s license','your private GPG key','a sample of your hair',
			'all your bank statements','the brand of your first car','the name of the place where your parents met',
			'the name of your favorite actor','your PayPal credentials','an MDB file with all your passwords']
period = ['day','night','month','week']
admired = ['Jesus','Buddha','Gandhi','Martin Luther King','Abraham Lincoln','Steve Jobs',
		'Lenin','Stalin','Napoleon I','Alexander the Great','Pharaoh Ramses II','the Zulu King','Richard Stallman',
		'Saddam Hussein','Charles de Gaulle','the Pope','Jonh Paul II','Samuel de Champlain',
		'Haile Selassie I','the Ras Tafari','the Dalai Lama','the Queen','Mother Theresa','Che Guevara',
		'George Washington','Celine Dion','Michael Jackson','Oprah Winfrey','King David','King Solomon','Arnold Schwarzenegger',
		'Simon Bolivar','Fidel Castro','Bill Gates','Muammar Kaddhafi','our Lady Mary','Mao Zedong']
device = ['iPhone','iPad','Android device','Android smartphone','netbook','N900','BlackBerry','Palm Pre']
recompensedivine = ['health and wealth','money','children','Microsoft Access Licenses','blessings','money and biryani','inheritances',
		'rice','stuffed gnus','Microsoft Certifications','uranium','cheap nigerian oil','cheap saudi oil',
		'inodes on your harddrive','wobbly windows','pi decimal digits','AirMiles','healthy food','CPU cores']
lists = [ 'pays', 'parente', 'cachette', 'currencies','deathreaction','deathmethod','personalinformation','admired','evil','period','device','profession', 'events', 'persons','expeditorfirstname', 'expeditorlastname', 'mymood','qualityperson','truthquality','torture','recompensedivine' ]

dico = {}
for item in lists:
	dico[item] = random.choice(locals()[item])

dico["pays2"] = random.choice(pays)
dico["magot"] = random.randint(10,100)
dico["recompense"] = random.randint(15,40)
dico["annees"] = random.randint(2,10)

textbody = """
Dear %(persons)s,

My %(parente)s was a %(profession)s in %(pays)s. %(deathreaction)s, he %(deathmethod)s 
%(annees)s years ago during the %(events)s. I discovered later that he left the amount
 of %(magot)s million %(currencies)s in a bank located in %(pays2)s. I know it is %(truthquality)s,
 but I have to tell you  the truth : after my %(parente)s's horrible death, my relatives 
decided to deny me the right to my %(parente)s's inheritance. These %(evil)s 
and evil men, sequestrated me for years in a %(cachette)s, which made me unable to claim my due. 
I %(mymood)s because they raped me and %(torture)s every %(period)s. 
However, I didn't lose  my faith and prayed our Lord. He was so merciful that the last %(period)s,
 somebody lost his %(device)s in the %(cachette)s. This morning, I realized it has a working Internet connexion 
and I found your email address. 

Please send me your coordinates, %(personalinformation)s, and your bank information 
so I can transfer my inheritance to a safe place. I know you are %(qualityperson)s, so you will
receive %(recompense)s percent of the total for your unlimited helpfulness.
	 
I pray God to bless you and your family for your help. May He send you even more %(recompensedivine)s.
If my late %(parente)s  was still alive, he would be honoured to have such a great friend and he would
admire you as he admired %(admired)s.

Yours faithfully,

	  %(expeditorfirstname)s %(expeditorlastname)s
""" % dico

print textbody

#spk.speak(textbody)
#spk.close()
