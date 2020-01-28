import random
import time
from time import sleep

character_data = {
    "current_scene": "scene_1",
    "name": "Errenwulf",
    "dead": False,
    "base_health": 20,
    "base_attack": 20,
    "base_defence": 20,
    "has_ring": False,
    "ring_health": 1,
    "has_necklace": False,
    "necklace_health": 0,
    "has_shield": False,
    "shield_health": 0,
    "has_sword1": False,
    "sword_1_attack": 0,
    "has_sword2": False,
    "sword_2_attack": 0,
    "has_sword3": False,
    "sword_3_attack": 0,
    "max_sword_attack": 0,
    "has_key": False,
    "current_health": 20,
    "current_attack": 20,
    "current_defence": 20
}

scene_1 = {
    "scene_title":"Prison Cell",
    "scene_description": "You awaken in a dark cell, head throbbing and body aching from the battle earlier that day. \n You hear soft footsteps outside, a short silence before a click as the lock is turned. The door opens to reveal your mother, the queen in a dark robe. She stealthily moves towards you and whispers, Errenwulf Thank god you are OK! Come with me quickly, we don't have much time.",
    "option_1_text": "Immediately exit the cell with her",
    "option_1_outcome_text": "You leave the cell with your mother",
    "option_1_display": True,
    "option_2_text": "Ask, 'We lost? Is Jennifer safe?",
    "option_2_outcome_text": "We did... I'm sorry Errenwulf... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
    "option_2_display": True,
    "option_3_text": "Do Nothing",
    "option_3_outcome_text":"Not so clever... The guards come in and run you and your mother through with swords. You definitely deserved that...",
    "option_3_display": True,
    "option_4_text": "",
    "option_4_outcome_text": "",
    "option_4_display": False,
}

scene_2 = {
    "scene_title":"The Tunnel",
    "scene_description": "Your mother, Queen Xenia, leads you quietly to a secret passage in the basement of the castle. You pass through and come across 2 dead guards at the feet of Queen Xenia's bodyguard. Their weapons lay loose in their death grip: \n Do you:",
    "option_1_text": "Exclaim loudly, 'Godwin, you old rascal. You could have left some for me?'",
    "option_1_display": True,
    "option_1_outcome_text": "Your excessively loud greeting results in an army of guards being alerted. You put up a decent fight but they outnumber you 10 - 1. You watch as your mother and friend are cut to pieces and then you lose your head...",
    "option_2_text": "Quickly take a sword and head along the forest path to the cross-roads",
    "option_2_display": True,
    "option_2_outcome_text": "You reach down and take one of the guard's sword then move - it's standard issue but it is well balanced and feels good in your hand. (att increased by 2).",
    "option_3_text": "Head along the forest path immediately",
    "option_3_display": True,
    "option_3_outcome_text": "You flee down the forest path with your mother and Godric close by",
    "option_4_text": "Take armour and sword from the dead men",
    "option_4_display": True,
    "option_4_outcome_text": "You start to remove a dead guards armour... Just as you pull it over your head, 2 guards come through the passage. Unarmed and outnumbered, your life flashes before your eyes as your head is cleaved from your neck.",
    }

scene_3 = {
    "scene_title":"Forest Path",
    "scene_description": "As you travel further in to the woods, your mother asks you to halt. 'Errenwulf, I strongly advise we stop at the inn to speak to the bar keep. He is a valuable source of information and can help you understand the adventure that awaits you.'",
    "option_1_text": "Ignore your mother and head straight to the cross-roads (don't receive game overview)",
    "option_1_display": True,
    "option_1_outcome_text": "You rush towards the crossroads",
    "option_2_text": "Go to the inn with your mother (receive game overview)",
    "option_2_display": True,
    "option_2_outcome_text": "'You're right, mother, a helping hand is always welcome",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }

scene_4 = {
    "scene_title":"The Inn",
    "scene_description": "You enter the inn. Amazingly, despite recent events, it appears completely in tact with the inn keep entertaining customers. The inn keep spies you, shepherds you in to a quiet side room and gives you the following information: \n \n 'You must travel to Archibald's Castle in the deep south, to avenge your father and rescue your princess.' \n \n 'I'm not certain that you are strong enough right now and you are ill equipped.' \n \n 'You're direct route to Archibald is South but I would encourage you to consider paths to the west or east as well to speak to your allies and gain some equipment and experience along the way.'",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }

scene_5 = {
    "scene_title":"ambush at the Crossroads",
    "scene_description": "A small band of guards ambush you as you reach the Cross-Roads. You face your first test in battle. Godric and the Queen act fast and you follow them into the fray:",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    "enemy_health": 15,
    "enemy_attack": 15,
    "enemy_defence": 15,
    }

scene_6 = {
    "scene_title":"Home Crossroads",
    "scene_description": "'Well fought Errenwulf, we must move quickly! Will you...:",
    "option_1_text": "...head back to the inn to have a few pints before you head on your way?",
    "option_1_display": True,
    "option_1_outcome_text": "What a ridiculous notion! Your Alcoholism has cost you more than ever; Before you make it back to the inn, you are attacked by an army of guards and they enjoy giving you an agonisingly slow death.",
    "option_2_text": "...travel west with us for a little while to help keep us safe?",
    "option_2_display": True,
    "option_2_outcome_text": "You head West in the hope of keeping your mother safe",
    "option_3_text": "...Head East to the Mountains, to seek help from wise friends",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "or head south in quick pursuit of your vengeance?",
    "option_4_display": True,
    "option_4_outcome_text": "In your haste to find head South, you find yourself on the edge of a dark forest",
    }

scene_7 = {
    "scene_title":"Mountains",
    "scene_description": "The snowy, ice cold mountains, where few dare to go block the majority of your view to the North and East. You've heard tell of mystical creatures in the mountains to your South East where you spy a mountain pass. To the south is a deep ravine that looks a little slippy...",
    "option_1_text": "Begin the trek up the mountain pass",
    "option_1_display": True,
    "option_1_outcome_text": "You brace yourself for wind and cold, heading up the mountain pass",
    "option_2_text": "Try to scale the sheer rock face to the North",
    "option_2_display": True,
    "option_2_outcome_text": "For some reason you choose to do a bit of mountain climbing instead of continuing your adventure. You're pretty good at it!! \n \nSadly, as you make it halfway up the sheer cliff face, you realise you have no equipment and in the panic, lose your grip and fall to your death... Splat!",
    "option_3_text": "Try your luck in the ravine",
    "option_3_display": True,
    "option_3_outcome_text": "You really weren't prepared for the ravine! \n \nYou slip and you bounce off rock after rock, leaving you with barely enough breath to cry out... \n \nIt takes a while but you eventually expire...",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }

scene_8 = {
    "scene_title":"Forest",
    "scene_description": "The dense dark forest looms all around you. You continue cautiously, sticking to the overgrown path. n/ n/The forest is so dense to the East and West that it makes South your only option. \n \nOut of the silence comes a 'Hoooooowwwwl'! It's followed by many more... \n You guess a pack of Wolves or worse has picked up your scent.",
    "option_1_text": "Head North and face the multiple beasts?",
    "option_1_display": True,
    "option_1_outcome_text": "You were right, they had your scent and it doesn't take long until you are surrounded on all sides. \n \nYou barely have a chance to realise as a dozen Wargs spring at you and enjoy an evening snack...",
    "option_2_text": "Rush South and get out of this hostile environment as quickly as possible",
    "option_2_display": True,
    "option_2_outcome_text": "You head West in the hope of keeping your mother safe",
    "option_3_text": "...Head East to the Mountains, to seek help from wise friends",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": ""
    }
# a - outcome death.
# b - outcome crossroads

scene_9 = {
    "scene_title":"The barrow part 1",
    "scene_description": "After a some time with little encounter, you reach a fork in the road. 'Thanks for your help, Errenwulf! We should be safe from here until I reach your aunt. \n \nYour grandmother always used to talk of hidden treasure in the barrows to the south, perhaps you could find something of interest? \n \n It's time we part ways, you have much to do! Where will you go from here?'",
    "option_1_text": "'I intend to follow you to the North, Mother'",
    "option_1_display": True,
    "option_1_outcome_text": "Your mother gives you a stern look that says it all. \n \n'I thought you cared about your father and Jennifer? Why would you be such a strange child?' \n \n'You will head south!'",
    "option_2_text": "'I always liked Grandmother's stories' (head south)",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
}

# scene 10 ?? 

scene_11 = {
    "scene_title":"The Crossroads2",
    "scene_description": "You arrive at another crossroads! \n \n The signposts read: \n \n North: Forest - Enter at your peril! \n \n South: The dark castle",
    "option_1_text": "Head North into the forest...",
    "option_1_display": True,
    "option_1_outcome_text": "It's a challenge to make your way into the forest let alone through it. \n You make it 50 metres in...\n\n You hear multiple snarls... Before you can do anything to protect yourself, you feel powerful jaws around your calf... \n \n It's the first of many as a dozen Wargs leap from cover and overwhelm you! Nom Nom...",
    "option_2_text": "Head South and face your destiny!",
    "option_2_display": True,
    "option_2_outcome_text": "You travel south to face Archibald...",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
# a - outcome death
# b - Tower keep.

scene_12 = {
    "scene_title":"barrow_2",
    "scene_description": "You arrive at the barrow and decide to enter. You find a torch and continue down a spiral staircase. \n \nA long corridor leads you to an atrium. As you enter you hear creaking armour... \n \nYou face a very old looking skeleton!:",
    "option_1_text": "Fight",
    "option_1_display": True,
    "option_1_outcome_text": "You wonder how well your steel will work on bone, as you fling yourself towards the enemy",
    "option_2_text": "Flee",
    "option_2_display": True,
    "option_2_outcome_text": "Sadly, the skeleton is blocking the only exit! \n \n You breath in deeply and then launch your assault",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    "enemy_health": 17,
    "enemy_attack": 17,
    "enemy_defence": 17,
}


scene_13 = {
    "scene_title":"barrow_3",
    "scene_description": "CRASH!! During your fight with the skeleton you shook something loose! Part of the roof falls away and blocks the exit. \n \n You probe the dark with your torch and notice a small passageway... ",
    "option_1_text": "Follow the passage",
    "option_1_display": True,
    "option_1_outcome_text": "You crawl through the small passageway and it leads out through some bushes...",
    "option_2_text": "Look for another way out",
    "option_2_display": True,
    "option_2_outcome_text": "Falling down old structures aren't a great place to hang around in... \n \n The roof falls in and crushes you.",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
}
# outcome one leads to cross roads 2 
# Outcome 2 - Death

scene_14 = {
    "scene_title":"Ambush_mountains",
    "scene_description": "As you Head up the mountain pass, you hear small rocks fall to your right... \n \nYou look up to see a goblin jumping down in hope of ambushing you",
    "option_1_text": "Fight",
    "option_1_display": True,
    "option_1_outcome_text": "You fancy your chances against this little green guy and react swiftly to gain the first blow",
    "option_2_text": "Run away",
    "option_2_display": True,
    "option_2_outcome_text": "Sadly, the goblin is too quick and you don't manage to get away before you are engaged in combat",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    "enemy_health": 17,
    "enemy_attack": 17,
    "enemy_defence": 17,
}

scene_15 = {
    "scene_title":"Mountain Top",
    "scene_description": "After dispatching the goblin you continue up the mountain path. \n \nThe view to the east over the ocean is beautiful... The path levels out a little as you round a corner... \n \n Your jaw drops as you come face to face with a huge Dragon... 'I'm in a good mood human! Answer this riddle for me and not only will I let you live but I will help you on your quest!'",
    "option_1_text": "'I will answer your riddle, you majestic creature'",
    "option_1_display": True,
    "option_1_outcome_text": "The dragon looks amused, 'Good choice, now answer me this...'",
    "option_2_text": "Run!",
    "option_2_display": True,
    "option_2_outcome_text": "The dragon swallows you whole",
    "option_3_text": "Fight!",
    "option_3_display": True,
    "option_3_outcome_text": "The dragon swallows you whole",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
}
#outcome 2/3 - death 
#outcome 1 - riddle

scene_20 = {
    "scene_title":"Boss fight",
    "scene_description": "Fortunately, the fighting to the north leaves the path to the castle easy using stealth. \n \nAfter besting a number of guards you reach your desired destination... You barge into the throne room full of rage and anger... \n \nYou see Archibald just sitting on his throne with a smirk on his face. He sniggers, 'You're weak just like your father!' and then pulls the princess closer to him with the chain around her neck, smirking all the while. \n \n Now is the time to avenge your father and free your love:",
    "option_1_text": "Yell, 'For my father's honour!' and attack",
    "option_1_display": True,
    "option_1_outcome_text": "You charge at Archibald with everything you have!",
    "option_2_text": "Glibly tease Archibald, 'You'll be lucky to keep your fat, ugly head today!' and attack",
    "option_2_display": True,
    "option_2_outcome_text": "Archibald chuckles as he tosses the princess to one side and unsheaths his greatsword",
    "option_3_text": "Try to talk through the error of his ways with Archibald",
    "option_3_display": True,
    "option_3_outcome_text": "It's seems there is no talking to the man... His guile and cunning are matched only by evil. He pulls a small lever next to the throne and you are crushed by a spiked trap. As your last few pints of blood ooze from your body, you have enough time to enjoy the screams of your princess and watch Archibald licking her face.",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    "enemy_health": 20,
    "enemy_attack": 20,
    "enemy_defence": 20,
    }

# functions

def display_message(message):
    print('')
    print(message)
    print('')


def riddle(riddle_text, riddle_answer):
    print(" ")
    print (riddle_text)
    success = False
    while success == False:
        answer = input("Who is it?: ")
        if answer.lower() != riddle_answer:
            print(" ")
            print("Incorrect! Try again!")
            print(" ")
        else:
            print ("'You are correct, human!' \n \nThe dragon Swoops you up on his back, dives off the cliff and flies South West. \n \nAfter some time in flight, the dragon starts to drop altitude... 'This is as far as I wish to take you human' \n \n He sets you down.")
            success = True

    # combat stuff

def calc_damage(attack, defence, text1, text2, text3, text4, text5, text6):
    attack_value = (attack + random.randint(1,10) - defence)
    time.sleep(.5)
    if attack_value < 0:
        attack_value = 0
        print("OOOOOPS!! " + text1 + "comically fumble" + text2 + text6 + " weapon!!")
    elif attack_value > 0 and attack_value < 4:
        print(text1 + " gain" + text2 + " a glancing blow") 
    elif attack_value > 3 and attack_value < 8:
        print("A clinical attack. " + text1 + "manage" + text2 + " a clean strike through " + text6 + " guard.")
    elif attack_value > 10:
        print("What a strike!! A critical hit! " + text1 + text5 + "tempted to take a bow!" )
    else:
        print("OUCH!! That was swift and strong!! " + text1 + "land " + text2 + " an extremely powerful blow!")
    print(" ")
    time.sleep(1.3)
    print(text1 + "deal" + text2 + " " + str( attack_value) + text4)
    print(" ")
    return attack_value

def calc_opponent_health (health, attack, defence):
    return (health - calc_damage(attack, defence, "You ", "", "Your attack deals ", " damage to the opponent", "are", "your"))

def calc_hero_health (health, attack, defence):
    return (health - calc_damage(attack, defence, "The enemy ", "s", "The enemy attack deals ", " damage to you.", "is", "their"))

def fight(hero_health, hero_attack, hero_defence, opponent_health, opponent_attack, opponent_defence):
    both_alive = True
    while both_alive == True:
        new_opponent_health = calc_opponent_health(opponent_health,hero_attack,opponent_defence)
        if both_alive == True:
            if new_opponent_health <= 0:
                time.sleep(3)
                sleep(1)
                print(" ")
                print('YOU VANQUISHED YOUR FOE!')
                both_alive = False
            else:
                time.sleep(1.8)
                sleep(1)
                opponent_health = new_opponent_health
                print("Your enemy has " + str(opponent_health) + " health left.")
                print(" ") 
                print(" ")                 
        if both_alive != True:
            break

        new_hero_health = calc_hero_health(hero_health, opponent_attack, hero_defence)
        if both_alive == True:
            if new_hero_health <= 0:
                time.sleep(3)
                sleep(1)
                print(" ")
                print('Your enemy bested you...')
                print(" ")
                both_alive = False
            else:
                time.sleep(1.5)
                sleep(1)
                hero_health = new_hero_health
                print("Errenwulf, you now have " + str(new_hero_health) + " health remaining")
                print(" ")
                print(" ")
                

def option_display():
    # print(character_data['current_scene'])
    print('')
    print('Your Options are')
    option_string = ''
    if current_scene["option_1_display"]:
        print ('a: ' + current_scene["option_1_text"])
        option_string +='a'
    if current_scene["option_2_display"]:
        print ('b: '+ current_scene["option_2_text"])
        option_string +='b'
    if current_scene["option_3_display"]:
        print ('c: '+ current_scene["option_3_text"])
        option_string +='c'
    if current_scene["option_4_display"]:
        print ('d: '+ current_scene["option_4_text"])
        option_string +='d'
    option_chosen = False
    while option_chosen != True:
        option_choice = input('Choose an option - Enter a letter:')
        if option_choice.lower() in option_string:
            option_chosen = True
            return option_choice.lower()
        else:
            print('try again')

def you_are_dead():
    character_data['dead'] = True
    print('')
    print('Oh No...')
    print('Death comes to us all eventually')
    print('Unfortunately for you, it is happened to you now ')
    print('')

    
# add art here

print('''       (      (               )                     (      (     
       )\ )   )\ )         ( /(   (  (              )\ )   )\ )  
 (    (()/(  (()/(   (     )\())  )\))(   '    (   (()/(  (()/(  
 )\    /(_))  /(_))  )\   ((_)\  ((_)()\ )     )\   /(_))  /(_)) 
((_)  (_))   (_))   ((_)   _((_) _(())\_)() _ ((_) (_))   (_))_| 
| __| | _ \  | _ \  | __| | \| | \ \((_)/ /| | | | | |    | |_   
| _|  |   /  |   /  | _|  | .` |  \ \/\/ / | |_| | | |__  | __|  
|___| |_|_\  |_|_\  |___| |_|\_|   \_/\_/   \___/  |____| |_|   ''')


# intro_text = "This is a fantasy tale of a fearless young bull who is on a mission to avenge the death of his father and retrieve his kidnapped princess. \nArchibald, the dark lord, is holding the princess hostage in his dungeon! \nYou wake up in a cold, dirty prison cell clinging onto a thin sheet of fabric that the guards call a duvet."
# display_message(intro_text)

# main game
current_scene = scene_1
# current_scene = character_data['current_scene']

# main loop
while character_data['dead'] == False:

    # scene 1
    if character_data['current_scene'] == 'scene_1':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            character_data['current_scene'] = 'scene_2'
            current_scene = scene_2
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            you_are_dead()
            break
        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            you_are_dead()
            break

    # scene 2
    if character_data['current_scene'] == 'scene_2':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            you_are_dead()
            break
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            character_data['current_scene'] = "scene_3"
            current_scene = scene_3
            character_data['max_sword_attack']=2 #update character
        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            character_data['current_scene'] = "scene_3"
            current_scene = scene_3

        if option == 'd':
            display_message(current_scene['option_4_outcome_text'])
            you_are_dead()
            break

    # scene 3
    if character_data['current_scene'] == 'scene_3':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            character_data['current_scene'] = "scene_5"
            current_scene = scene_5
            #goto forest path scene 5
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            # goto inn scene 4
            character_data['current_scene'] = "scene_4"
            current_scene = scene_4
    
    # scene 4
    if character_data['current_scene'] == 'scene_4':
        inn_text = 'You enter the inn. Amazingly, despite recent events, it appears completely intact with the inn keep entertaining customers. \nThe inn keep spies you, shepherds you in to a quiet side room and gives you the following information: \n \n \'You must travel to Archibald\'s Castle in the deep south, to avenge your father and rescue your princess.\' \n \n \'I\'m not certain that you are strong enough right now and you are ill equipped.\' \n \n \'You\'re direct route to Archibald is South but I would encourage you to consider paths to the west or east as well to speak to your allies and gain some equipment and experience along the way.'        
        display_message(inn_text)
        character_data['current_scene'] = "scene_5"
        current_scene = scene_5
        time.sleep(4)

    # scene 5
    if character_data['current_scene'] == 'scene_5':
        display_message(current_scene['scene_description'])
        # print('we are in scene 5 the fight')
        fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
        character_data['current_scene'] = "scene_6"
        current_scene = scene_6
        
    # scene 6  - the crossroads
    if character_data['current_scene'] == 'scene_6':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            you_are_dead()
            break

        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            character_data['current_scene'] = "scene_9"
            current_scene = scene_9
            # barrow  - not written yet

        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            character_data['current_scene'] = "scene_7"
            current_scene = scene_7
            # mountain - not written yet

        if option == 'd':
            display_message(current_scene['option_4_outcome_text'])
            character_data['current_scene'] = "scene_8"
            current_scene = scene_8
            #forest

    # scene 7 - mountains
    if character_data['current_scene'] == 'scene_7':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            character_data['current_scene'] = "scene_14"
            current_scene = scene_14

        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            you_are_dead()

        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            you_are_dead()
        
    # scene 8 - forest
    if character_data['current_scene'] == 'scene_8':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            you_are_dead()
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            character_data['current_scene'] = "scene_11"
            current_scene = scene_11
# goto crossroads2 scene 11

    # scene 9 - barrow
    if character_data['current_scene'] == 'scene_9':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            character_data['current_scene'] = "scene_12"
            current_scene = scene_12
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            character_data['current_scene'] = "scene_12"
            current_scene = scene_12
        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])

    # scene 11 - second crossroads
    if character_data['current_scene'] == 'scene_11':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            you_are_dead

        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            character_data['current_scene'] = "scene_20"
            current_scene = scene_20

    # scene 12 - barrow 2nd part
    if character_data['current_scene'] == 'scene_12':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            character_data['current_scene'] = "scene_13"
            current_scene = scene_13
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            character_data['current_scene'] = "scene_13"
            current_scene = scene_13

    # scene 13 - barrow 3rd part
    if character_data['current_scene'] == 'scene_13':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            character_data['current_scene'] = "scene_11"
            current_scene = scene_11
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            you_are_dead()

    # scene 14 - mountain ambush
    if character_data['current_scene'] == 'scene_14':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            character_data['current_scene'] = "scene_15"
            current_scene = scene_15
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            character_data['current_scene'] = "scene_15"
            current_scene = scene_15

    # scene 15 - mountain top
    if character_data['current_scene'] == 'scene_15':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d
        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            my_riddle_text = "Forwards and backwards it reads the same. \n \nHe is called something else by others but is known to you by another name. \n"
            my_riddle_answer = "dad"
            riddle(my_riddle_text, my_riddle_answer)
            # crossoads 2
            character_data['current_scene'] = "scene_11"
            current_scene = scene_11

        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            you_are_dead()
        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            you_are_dead()

    # scene 20 - boss
    if character_data['current_scene'] == 'scene_20':
        display_message(current_scene['scene_description'])
        option = option_display() # get selected option a b c d

        win_text = "Archibald lies in a bloody mess on the floor. You have rid the world of a tyrant and rescued your true love! \n \nHearing that their tyrant lord is dead, Archibald's former armies throw down their swords and opt for peace, helping to rebuild the lands they reluctantly despoiled. \n \nHarmony in the land exists... At least for a while..."

        # options
        if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            display_message(win_text)
            character_data['dead'] = True
        if option == 'b':
            display_message(current_scene['option_2_outcome_text'])
            fight(character_data['current_health'], character_data['current_attack'], character_data['current_defence'], current_scene['enemy_health'], current_scene['enemy_attack'], current_scene['enemy_defence'] )
            display_message(win_text)
            character_data['dead'] = True
        if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            you_are_dead()



print('Game Over!')

