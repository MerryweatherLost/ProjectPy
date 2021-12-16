class USA:
    """The United States of America and its states and territories."""
    states = {
        "Alabama":        "https://cdn.discordapp.com/attachments/898666991806726175/898667677437005924/2560px-Flag_of_Alabama.png",
        "Alaska":         "https://cdn.discordapp.com/attachments/898666991806726175/898669654472544286/1280px-Flag_of_Alaska.png",
        "Arizona":        "https://cdn.discordapp.com/attachments/898666991806726175/898672683934449684/1280px-Flag_of_Arizona.png",
        "Arkansas":       "https://cdn.discordapp.com/attachments/898666991806726175/898672804793303110/1280px-Flag_of_Arkansas.png",
        "California":     "https://cdn.discordapp.com/attachments/898666991806726175/898672876939534346/1280px-Flag_of_California.png",
        "Colorado":       "https://cdn.discordapp.com/attachments/898666991806726175/898672950742515712/1280px-Flag_of_Colorado.png",
        "Connecticut":    "https://cdn.discordapp.com/attachments/898666991806726175/898673034276261929/1280px-Flag_of_Connecticut.png",
        "Delaware":       "https://cdn.discordapp.com/attachments/898666991806726175/898673103406792734/1280px-Flag_of_Delaware.png",
        "Florida":        "https://cdn.discordapp.com/attachments/898666991806726175/898673187661963294/1280px-Flag_of_Florida.png",
        "Georgia":        "https://cdn.discordapp.com/attachments/898666991806726175/898673260387000320/1280px-Flag_of_Georgia_28U.png",
        "Hawaii":         "https://cdn.discordapp.com/attachments/898666991806726175/898673337734152192/1280px-Flag_of_Hawaii.png",
        "Idaho":          "https://cdn.discordapp.com/attachments/898666991806726175/898673466960658442/1280px-Flag_of_Idaho.png",
        "Illinois":       "https://cdn.discordapp.com/attachments/898666991806726175/898673587093909504/1280px-Flag_of_Illinois.png",
        "Indiana":        "https://cdn.discordapp.com/attachments/898666991806726175/898673711480189019/1280px-Flag_of_Indiana.png",
        "Iowa":           "https://cdn.discordapp.com/attachments/898666991806726175/898673760561930280/1280px-Flag_of_Iowa.png",
        "Kansas":         "https://cdn.discordapp.com/attachments/898666991806726175/898673843583987753/1280px-Flag_of_Kansas.png",
        "Kentucky":       "https://cdn.discordapp.com/attachments/898666991806726175/898673978355372052/1280px-Flag_of_Kentucky.png",
        "Louisiana":      "https://cdn.discordapp.com/attachments/898666991806726175/898674051885715486/1280px-Flag_of_Louisiana.png",
        "Maine":          "https://cdn.discordapp.com/attachments/898666991806726175/898674109020536872/1280px-Flag_of_Maine.png",
        "Maryland":       "https://cdn.discordapp.com/attachments/898666991806726175/898674206244470824/1280px-Flag_of_Maryland.png",
        "Massachusetts":  "https://cdn.discordapp.com/attachments/898666991806726175/898674377430794260/1280px-Flag_of_Massachusetts.png",
        "Michigan":       "https://cdn.discordapp.com/attachments/898666991806726175/898674435140255774/1280px-Flag_of_Michigan.png",
        "Minnesota":      "https://cdn.discordapp.com/attachments/898666991806726175/898674503989723136/1280px-Flag_of_Minnesota.png",
        "Mississippi":    "https://cdn.discordapp.com/attachments/898666991806726175/898674592577630279/1280px-Flag_of_Mississippi.png",
        "Missouri":       "https://cdn.discordapp.com/attachments/898666991806726175/898674726308814899/1280px-Flag_of_Missouri.png",
        "Montana":        "https://cdn.discordapp.com/attachments/898666991806726175/898674796756340776/1280px-Flag_of_Montana.png",
        "Nevada":         "https://cdn.discordapp.com/attachments/898666991806726175/898674867023544420/1280px-Flag_of_Nebraska.png",
        "New Hampshire":  "https://cdn.discordapp.com/attachments/898666991806726175/898675104182054952/1280px-Flag_of_New_Hampshire.png",
        "New Jersey":     "https://cdn.discordapp.com/attachments/898666991806726175/898675188596609095/1280px-Flag_of_New_Jersey.png",
        "New Mexico":     "https://cdn.discordapp.com/attachments/898666991806726175/898675269685108756/1280px-Flag_of_New_Mexico.png",
        "New York":       "https://cdn.discordapp.com/attachments/898666991806726175/898675353512468531/1280px-Flag_of_New_York.png",
        "North Carolina": "https://cdn.discordapp.com/attachments/898666991806726175/898675434257023066/1280px-Flag_of_North_Carolina.png",
        "North Dakota":   "https://cdn.discordapp.com/attachments/898666991806726175/898675519061647390/1280px-Flag_of_North_Dakota.png",
        "Ohio":           "https://cdn.discordapp.com/attachments/898666991806726175/898675600825389146/1280px-Flag_of_Ohio.png",
        "Oklahoma":       "https://cdn.discordapp.com/attachments/898666991806726175/898675691351081040/1280px-Flag_of_Oklahoma.png",
        "Oregon":         "https://cdn.discordapp.com/attachments/898666991806726175/898675792945479700/1280px-Flag_of_Oregon.png",
        "Pennsylvania":   "https://cdn.discordapp.com/attachments/898666991806726175/898675873220268112/1280px-Flag_of_Pennsylvania.png",
        "Rhode Island":   "https://cdn.discordapp.com/attachments/898666991806726175/898675934423552010/1024px-Flag_of_Rhode_Island.png",
        "South Carolina": "https://cdn.discordapp.com/attachments/898666991806726175/898676066309259345/1280px-Flag_of_South_Carolina.png",
        "South Dakota":   "https://cdn.discordapp.com/attachments/898666991806726175/898676129521627156/1280px-Flag_of_South_Dakota.png",
        "Tennessee":      "https://cdn.discordapp.com/attachments/898666991806726175/898676243124342884/2560px-Flag_of_Tennessee.png",
        "Texas":          "https://cdn.discordapp.com/attachments/898666991806726175/898667003953418270/1200px-Flag_of_Texas.png",
        "Utah":           "https://cdn.discordapp.com/attachments/898666991806726175/898676319414521936/1280px-Flag_of_Utah.png",
        "Vermont":        "https://cdn.discordapp.com/attachments/898666991806726175/898676383339929670/1280px-Flag_of_Vermont.png",
        "Virginia":       "https://cdn.discordapp.com/attachments/898666991806726175/898676437048000532/800px-Flag_of_Virginia.png",
        "Washington":     "https://cdn.discordapp.com/attachments/898666991806726175/898676508502138910/1280px-Flag_of_Washington.png",
        "West Virginia":  "https://cdn.discordapp.com/attachments/898666991806726175/898676583286599680/1280px-Flag_of_West_Virginia.png",
        "Wisconsin":      "https://cdn.discordapp.com/attachments/898666991806726175/898676647132282890/1280px-Flag_of_Wisconsin.png",
        "Wyoming":        "https://cdn.discordapp.com/attachments/898666991806726175/898676695740067910/1280px-Flag_of_Wyoming.png",
    }
    async def territories(name):
        """All other territories official and unofficial flags within the United States of America."""
        if (name == 'puerto rico'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898684646232031232/1280px-Flag_of_Puerto_Rico.png'
        elif (name == 'guam'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898684699730407515/1280px-Flag_of_Guam.png'
        elif (name == 'us virgin islands'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898684772916793344/1280px-Flag_of_the_United_States_Virgin_Islands.png'
        elif (name == 'northern mariana islands'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898684854735110195/1280px-Flag_of_the_Northern_Mariana_Islands.png'
        elif (name == 'american samoa'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898684914415845396/1280px-Flag_of_American_Samoa.png'
        elif (name == 'midway atoll'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685087330217994/2560px-Flag_of_the_Midway_Islands_28local29.png'
        elif (name == 'palmyra atoll'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685229756203038/2560px-Flag_of_Palmyra_Atoll_28local29.png'
        elif (name == 'baker island'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685328636923974/1950px-Flag_of_Baker_island_unofficial.png'
        elif (name == 'howland island'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685514864021524/Flag_of_Howland_Island_28local29.png'
        elif (name == 'jarvis island'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685328636923974/1950px-Flag_of_Baker_island_unofficial.png'
        elif (name == 'johnston atoll'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685842132979732/2560px-Flag_of_Johnston_Atoll_28local29.png'
        elif (name == 'kingman reef'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898685975721566208/2560px-Unofficial_flag_of_Kingman_Reef.png'
        elif (name == 'wake island'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898686055933423627/2560px-Flag_of_Wake_Island.png'
        elif (name == 'navassa island'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898686137672007750/800px-Flag_of_Navassa_Island_28local29.png'
        elif (name == 'district of columbia' or name == 'washington dc' or name == 'd.c' or name == 'd.c.'):
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898687127758446602/1920px-Flag_of_the_District_of_Columbia.png'
        else:
            territory = 'https://cdn.discordapp.com/attachments/898666991806726175/898667373475811349/Feed-Test-SIC-Feed-20142_news_large.png'
        return territory