import random
import akaneko
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
            'https://cdn.discordapp.com/attachments/576096750331494420/897501220380495872/58924ca6a0a559f01c720e3fec640ec8.jpg',
            'https://cdn.discordapp.com/attachments/576096750331494420/898168752061952040/f507e8e194925763c0e369652798f1d8.jpg',
            'https://i.waifu.pics/NOJicBh.png',
            ]
        coffeerand = random.choice(coffee)

        return coffeerand
    def AppleJuice():
        """Girls holding apple juice. - Request"""
        apple = 'https://cdn.discordapp.com/attachments/576096750331494420/896979723161337886/snapshot20061006181001.png'
        return apple
    def Positivity():
        quotes = [
            "It's a wonderful thing to be optimistic. It keeps you healthy and it keeps you resilient.",
            "Miracles happen to those who believe in them.",
            "One small positive thought can change your whole day.",
            "Believe you can and you’re halfway there.",
            "If you are positive, you’ll see opportunities instead of obstacles.",
            "Write it on your heart that every day is the best day in the year.",
            "Accentuate the positive, Eliminate the Negative, latch onto the affirmative.",
            "A positive atmosphere nurtures a positive attitude, which is required to take positive action.",
            ]
        randquote = random.choice(quotes)

        return randquote
    def PositivityInfo():
        desc = [
            'Here is the random quote for today!',
            'Hello, here is the random quote for today!',
            'Good day, here is the random quote.',
            'I hope you enjoy this random quote!',
            'I believe you will find inspiration in this quote!',
            'I hope you find use of this quote!'
            ]
        description = random.choice(desc)
        return description
    def PositivityImage():
        image = 'https://cdn.discordapp.com/attachments/576096750331494420/898168889949683712/aea15abed7ea5b475c484af72102f70c.jpg'
        return image
    def SpecialWaifu():
        """My best images I could find."""
        list = [
            'https://cdn.discordapp.com/attachments/576096750331494420/898346718024843304/7d0955b149e32b04539819597df91a7a.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898348448745664534/66922995_p0.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898348469406814248/55093576_p13.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898348516219441172/93407491_p0.jpeg',
            'https://cdn.discordapp.com/attachments/576096750331494420/898348712894550026/fi6.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898348984924512266/54ad5dd82190c943106fcf677307bada.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898349934003257384/261d4f78a3ac357e819480d8f99dade0.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898350804505866300/08d3dfaae342ce58c2da475a160438e4.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898351323836215336/c524ea6162e47e221f0b0b808717dd8d.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898351550542536734/01a3fe9b0be78ac93636510e8779e75c.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898351973013798982/32ad0eef353ef7c429ce17295b6c9970.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898352427261120512/unknown.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898352854748770344/806095565d6bb77d942b07d291ccf99b.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898354151019405342/unknown.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898354623566479390/unknown.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898356735360782366/14f5b7c6591f126b35fed3ef2753e81b.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361536555397140/2xcan3_waifu2x_2x_2n_png.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361537486520330/2xcan2_waifu2x_2x_2n_jpg.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361539684352000/2xcan_waifu2x_2x_2n_jpg.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361541898956850/2xcan4_waifu2x_2x_2n_jpg.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361805385109544/unknown.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898361933135245392/unknown.png',
            'https://cdn.discordapp.com/attachments/576096750331494420/898407034842656808/ac4ad612e6958cf5403d17a6b4e00cca.png',
            ''
            ]
        waifuspecial = random.choice(list)
        return waifuspecial

class AnimeGel:
    """Returns images specified through Gelbooru.
    This inherits from: :exc:`Gelbooru`"""
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
class AnimeNSFWGel:
    """Imports not safe for work images.\n
    This inherits from: :exc:`Gelbooru`"""
    async def nsfwzettai() -> str:
        """Imports NSFW thighhighs."""
        zettairyo = await gelbooru.random_post ( 
            tags = ['1girl','zettai_ryouiki','highres'],
            exclude_tags = ['comic']
        )
        return zettairyo
    async def nsfwuniform() -> str:
        """Returns NSFW uniform types. School, nurses, military..."""
        uniform = await gelbooru.random_post ( 
            tags = ['1girl','uniform','highres'],
            exclude_tags = ['comic']
        )
        return uniform
    async def ahegao() -> str:
        """Ahegao images, mainly facial."""
        ahegao = await gelbooru.random_post ( 
            tags = ['ahegao','highres'],
            exclude_tags = ['comic']
        )
        return ahegao
    async def nsfwgif() -> str:
        """Not safe for work gif images."""
        gif = await gelbooru.random_post ( 
            tags = ['animated_gif','highres']
        )
        return gif
    async def doujinshi() -> str:
        """Not safe for work comics."""
        doujin = await gelbooru.random_post ( 
            tags = ['comic','highres']
        )
        return doujin
    async def nsfwcatgirl() -> str:
        """Not safe for work catgirls."""
        catgirl = await gelbooru.random_post ( 
            tags = ['cat_girl','highres'],
            exclude_tags = ['comic']
        )
        return catgirl
class AkaNSFW:
    def school():
        """NSFW Schoolgirls."""
        school = akaneko.nsfw.school()
        return school
    def maid():
        """NSFW Maid."""
        maid = akaneko.nsfw.maid()
        return maid
    def gif():
        """NSFW gifs."""
        gif = akaneko.nsfw.gif()
        return gif

class DharMann:
    def DharQuote():
        """Dhars most famous quotes."""
        dharquote = [
            'Your life doesn’t get better by chance. It gets better by change.',
            'You can’t turn a negative mindset into positive actions.',
            'Your past does not equal your future unless you decide to live there.',
            'Failure is an event, not a person.',
            'Water the flowers, not the weeds.',
            'Train your mind. Your body will follow.'
        ]
        dharrand = random.choice(dharquote)
        return dharrand
    def DharImage():
        """Dhar Collage."""
        dharimg = [
            'https://cdn.discordapp.com/attachments/576096750331494420/896981047848353812/unknown.png',
            'https://cdn.discordapp.com/attachments/895302028375490596/899660726740865055/EtbPOwSVEAA9uUC.jpg',
        ]
        imgrand = random.choice(dharimg)
        return imgrand