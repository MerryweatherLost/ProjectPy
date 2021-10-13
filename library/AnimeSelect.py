import random

from pygelbooru import Gelbooru

gelbooru = Gelbooru('7a143b6b8021d138af296847f1354d36c893132b805a213b716c32677133b9ad', '847623')

class AnimeList:
    def DokiDoki():
        dokidoki = [
            'https://media.discordapp.net/attachments/335232645044633601/895051979225702440/sample_a95c5fe38157038a7a94dbb119c6bc6bbcf23d68.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053705907408907/b6820ae5fd84f484491e7308ccf4b400.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053860463317033/doki_doki_literature_club___festival_time___gift__by_katzianxero_dbxqttd-fullview.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053926850760764/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895053980273631262/doki_doki_literature_club__light_ver___by_apricot_crown-dbyfydi.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054111383359519/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054158640599060/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054243956940830/R.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054625579859978/monika_natsuki_sayori_and_yuri_doki_doki_literature_club_drawn_by_hushabye__8b0a188cd0ee2fa8938b926f.png',
            'https://cdn.discordapp.com/attachments/862584354211364894/895054962642526279/ddlc1_by_yorieofthecastle-dbulcc1.png'
        ]
        ddlcRan = random.choice(dokidoki)
        return ddlcRan
    def Coffee():
        """Girls holding coffee. Particularly office workers."""
        coffee = [
            'https://cdn.discordapp.com/attachments/576096750331494420/895067885549019157/6dubb6nhxjr71_waifu2x_2x_png.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501307491979344/cca0af7ac2ff43951f24021750b64dd4.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501307257102376/831a570c1b2d070936f335a75e70db0c.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501307013840956/96a685b30173b1736996d67cfaaad104.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501306837684224/3d4dae0a174dbdbc15ce82d3727de7c1.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501306476957716/7e5444a98a1588af3e13e586ba7d1389.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501306154016768/317bf7b5ffd53f81062e1ad749d3c28a.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501305864593458/c7695e3cdabf4152f848acce6dc10350.jpeg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501305545818202/fe1f0e84b9266b70f402ada8bf199b7f.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501305155751997/c0b069c207ca9e5888c5c16cec7d652e.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501222255345744/a3e469698c54f1fb41f0420c0b29a58f.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501221940777031/23c7df5edc99a118666041a1f588f12e.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501221701681183/25a2aaeda9df3e76807946a54d4833bb.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501221508759612/947654ea7fb9f156b3fcd97d6c2bbaae.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501220921565224/0d5449049de3134150257ed9d454edd4.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501220640530452/11d52368e8e1446073e6ed0e3604f209.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/897501220380495872/58924ca6a0a559f01c720e3fec640ec8.jpg'
            ]
        coffeerand = random.choice(coffee)

        return coffeerand
    def AppleJuice():
        """Girls holding apple juice. - Request"""
        apple = 'https://cdn.discordapp.com/attachments/576096750331494420/896979723161337886/snapshot20061006181001.png'
        return apple
    def Dhar():
        """Dhars most famous quotes and his FACE."""
        dharquote = ['Your life doesn’t get better by chance. It gets better by change.','You can’t turn a negative mindset into positive actions.','Your past does not equal your future unless you decide to live there.',
        'Failure is an event, not a person.','Water the flowers, not the weeds.','Train your mind. Your body will follow.']

        dharrand = random.choice(dharquote)

        return dharrand
    def Renault():
        """Originally a meme."""
        renault = 'https://cdn.discordapp.com/attachments/879488846453174282/895849572033781822/renault.png'
        return renault
    def Biden():
        """Load of Malarkey."""
        biden = 'https://cdn.discordapp.com/attachments/576096750331494420/897532315666898994/P20210303AS-1901-cropped.png'
        return biden
        
class AnimeGelbooru:
    """Returns images specified through Gelbooru."""
    async def WALLPAPER() -> str:
        wallpaper = await gelbooru.random_post ( 
            tags = ['wallpaper'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','cleavage'] 
        )
        return wallpaper
    async def ZETTAI() -> str:
        """Absolute Territory, Absolute Territory..."""
        zettai = await gelbooru.random_post ( 
            tags = ['1girl','thighhighs','highres'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis','bdsm']
        )
        return zettai
    async def UNIFORM() -> str:
        """Returns uniform images through Gelbooru."""
        uniform = await gelbooru.random_post ( 
            tags = ['1girl','uniform','highres'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis','bdsm']
        )
        return uniform
    async def CAR() -> str:
        """Returns a car image through Gelbooru."""
        car = await gelbooru.random_post ( 
            tags = ['car'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis','bdsm']
        )
        return car
    async def GUN() -> str:
        """Returns a gun image through Gelbooru."""
        gun = await gelbooru.random_post ( 
            tags = ['gun'], 
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis','bdsm']
        )
        return gun
    async def CATGIRL() -> str:
        """Returns a catgirl image through Gelbooru."""    
        cat = await gelbooru.random_post ( 
            tags = ['cat_girl','highres'],
            exclude_tags = ['nude','sex','nipples','panties','anus','vaginal','comic','penis','bdsm'] 
        )
        return cat