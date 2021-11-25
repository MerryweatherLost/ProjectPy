import random

class _Fun:
    def coin_toss():
        """Responses handler for a randomized coinflip."""
        responses = ['Heads.', 'Tails.']
        coinflip = random.choice(responses)
        return coinflip
    
    def eight_ball(cnt:str):
        """Responses handler for a randomized eightball message, if url requested, returns an 8ball image url."""
        if cnt == 'url': 
            url = 'https://cdn.discordapp.com/attachments/576096750331494420/896414018133196800/8b.png'
            return url
        
        if cnt == 'txt':
            responses = [
                    # POSITIVES
                    'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
                    'Outlook good.', 'Signs point to yes.', 'That is correct.',
                    'Indeed.', 'Affirmative.',
                    # NEUTRALS
                    'Reply hazy, try again.',
                    'Ask again later.','Can not predict now.', 
                    'I can not find a result for that, try again.','Try again.',
                    # NEGATIVES
                    "Don't count on it.", 'My reply is no.', 'My sources say no.', 
                    'Obviously not.', 'Negative.','Absolutely false.','Decidedly not.',
                    'No.', 'That is incorrect.'
            ]
            txt = random.choice(responses)
            return txt 