import random


class Messages:
    MORNING = ['good morning!', 'good morning :heart_eyes:', 'good morning :monkey:', 'goodmorning :smiling_face_with_3_hearts:',
               'good morning :hatched_chick:', 'good morning :sunny:', ':sparkles: :sunny:', 'good morning :hand_with_index_finger_and_thumb_crossed:',
               'Rise and shine!', 'good morning sunshine!', 'shubho shokal!', 'good morning :kissing_heart:', 'you are stronger than you think\ndo something today that pushes you outside your comfort zone\ngood morning princess',
               'know that you have a lot of people in your corner rooting for you\ngood morning!', 'You make every day an adventure\nI never know what is going to happen, but I am always excited to find out\nGood morning!',
               ]
    DAY = ['meow meow', 'meow meow :heart_eyes:', 'meow', 'gujubabu!', 'mew mew', 'paupau\nmaumau\nhauhau\npadu!', 'paupau\nmaumau\nhauhau\ngujubabu!',
           ':heart_eyes:', ':baby:', 'pew pew pew!', 'gujumeow', 'hehe', 'awooo!', 'halo!', 'meow', 'this is a message to remind you that you are special!',
           'hello babu', 'gugugaga!', 'no matter how bad or mad you may feel, there is always someone else that is having a worse day than you\nbe thankful for what you have\nmy gujibabu!',
           'no one can tell you that you aren’t good enough\nnot even yourself\ndon’t let self-doubt hold you back\nyou got this!', 'it’s okay to feel down sometimes\nwe all have bad days\njust remember to keep pushing forward and never give up!',
           'https://tenor.com/view/emote-gif-24455800', 'https://tenor.com/view/pug-fat-dog-animal-cartoon-gif-10203243', 'https://tenor.com/view/corgi-cute-adorable-gif-15132189',
           'https://tenor.com/view/mochi-mochimochi-gif-24507378', 'https://tenor.com/view/mochi-cat-wubs-gif-21788640', 'https://tenor.com/view/sad-gif-24590413',
           'https://tenor.com/view/squish-cat-cute-animals-hugging-gif-17747528', 'https://tenor.com/view/grey-cat-lounging-gif-26310821',
           'https://tenor.com/view/cute-gif-25346669', 'https://tenor.com/view/keira-ily-keira-gif-22366972', 'https://tenor.com/view/cute-cat-cartoon-animals-cuddle-gif-17747515',
           'mushimeow!', 'yahalo!', '@Koala ping!', 'thank you for keeping up with me hehe', 'lalalala', 'peachu peachu!', 'I think you dropped this :crown:', 'is this you?\n:sloth:']
    NIGHT = ['goodnight princess!', 'goodnight!', 'sweet dreams!', 'brb gonna sleep for 2 hours', 'gujunight!', 'https://tenor.com/view/goodnight-gif-25677317',
             'don\'t stay up late\ngoodnight!', 'don\'t worry about those that don\'t believe in you\nit’s their loss for not seeing your potential\njust keep pushing forward for those that love and support you\ngoodnight!',
             'don\'t compare yourself to others\nyou have your own strengths and weaknesses\nembrace what makes you unique\ngoodnight, princess',
             'the past does not equal the future\njust because things didn\'t work out once before doesn\'t mean that they won\'t the next time\ngn my gujubabu!',
             'goodnight :night_with_stars:', 'gn princess :dizzy:', 'goodnight, my grace', 'goodnight, m\'lady :hatching_chick:', 'goodnight, my other half',
             'beep beep\nmeep meep\ngoodnight\ngo sleep!', 'zzz...\ngoodnight, princess!']

    def __init__(self):
        self.morning = Messages.MORNING.copy()
        self.day = Messages.DAY.copy()
        self.night = Messages.NIGHT.copy()

    def check_morning(self):
        if len(self.morning) == 0:
            self.morning = Messages.MORNING.copy()

    def get_morning(self):
        self.check_morning()
        choice = random.choice(self.morning)
        self.morning.remove(choice)
        return choice

    def check_day(self):
        if len(self.day) == 0:
            self.day = Messages.DAY.copy()

    def get_day(self):
        self.check_day()
        choice = random.choice(self.day)
        self.day.remove(choice)
        return choice

    def check_night(self):
        if len(self.night) == 0:
            self.night = Messages.NIGHT.copy()

    def get_night(self):
        self.check_night()
        choice = random.choice(self.night)
        self.night.remove(choice)
        return choice
