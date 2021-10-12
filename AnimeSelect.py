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
        coffee = 'https://cdn.discordapp.com/attachments/576096750331494420/895067885549019157/6dubb6nhxjr71_waifu2x_2x_png.png'
        return coffee
    def AppleJuice():
        apple = 'https://cdn.discordapp.com/attachments/576096750331494420/896979723161337886/snapshot20061006181001.png'
        return apple
    def Dhar():
        dharquote = ['Your life doesn’t get better by chance. It gets better by change.','You can’t turn a negative mindset into positive actions.','Your past does not equal your future unless you decide to live there.',
        'Failure is an event, not a person.','Water the flowers, not the weeds.','Train your mind. Your body will follow.']

        dharrand = random.choice(dharquote)

        return dharrand
    def Renault():
        renault = 'https://cdn.discordapp.com/attachments/879488846453174282/895849572033781822/renault.png'
        return renault
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