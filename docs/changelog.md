## [ *Project Py* ]

## [LEGACY] - ~ 2021-10-09

- Added gitignore
  
- Laid framework for the bot itself. `(init.py)`

- Added cogs and a command handler.

- Added ConsoleLib along with `Time (class)` and `Essentials (class)`, clearing up some clutter.

## [0.5.0] - 2021-10-09

- **NSFW** Gelbooru and **SFW** Gelbooru commands have been split. See `booru` and `nsfwbooru`.
  
- Fun commands have `message: discord.Message` designation for deletion and editing.
  
- New `catgirl`, and `nsfwcatgirl` command, Nya! See `booru` and `nsfwbooru` respectively.
  
- New Help Command with assistance from `PrettyHelp`, more easy to read on the eyes.
  
- New profile picture for the project.
  
- AnimeSelect along with a `AnimeList (class)`, which currently contains `coffee` and `ddlc` methods.
  
- `renault` command. What else is there to say?
  
- Fixed typos in the `booru` section.
  
## [0.6.0] - 2021-10-09

- New `avatar` command, which pulls the avatar from a person. Found in the `Fun (class)` category.
  
- Added timestamps to embeds.
  
- New `ballImage` def to pull a thumbnail image for `8ball`.
  
- New NSFW commands for nekomini in `waifu.py`.
  
- `waifu.py` changes added, many new constructs for each command to make things cleaner.
  
- Refractor nearly completed.

## [0.7.0] - 2021-10-10

- New commands coming out of the woodwork!

  - `toprole` command to return highest role of yourself.
  
  - `roles` command to get the number of roles for a person.
  
  - `.` command.

- Multiple Roundtrips added to `waifu.py`
  
- `Admin (class)` altered so that permissions are the parameters required instead of roles.

## [0.8.0] - 2021-10-11 - 2021-10-13

- More refractoring.

- New class `AnimeGelbooru (class)` to serve to call methods from Gelbooru imageboard.

- More roundtrip additions to keep code clean.

- New descriptions to the AnimeSelect library. `using """..."""`

## [0.9.0] - 2021-10-14

- More refractoring.

- Biden Command (*What a Load of Malarkey Jack!*)

- Trump Command (*Wrong!*)

- Positivity Quote Command in `Anime (class)`, trigger by using `positivity`.

- Also, note that you can now trigger commands with whitespace. EX: `: rundir`

- `AnimeSelect (Library)` now has more content to facilitate new commands.

- New `coffee` image of another business image.

- More `ROUNDTRIP (CONSTANT)`

- Added `waifuspecial` command that adds handpicked images from myself.

## [1.0.0] - RELEASE - 2021-10-15

- 24/7 Release.

- Let the stable build commence! Hayate!

- Configuration set in private folder.

- New token for Tachibana, protected and secured.

- `tachibana` command exclusive to Tachibana.

- New `Color (class)` to handle specific color requests.

- Private folder config updated for prefixes and status updates.

- Seperated Development build 'Project PY' and 'Tachibana'. They operate independently now.

- From now on, pull requests will be used for new changes.

## [1.1.0] - 2021-10-15 - 2021-10-19

- New `Roundtrip (class)` to facilitate latency and make code cleaner.

- `Color (class)` additions.

- New `akaneko` Commands.

  - `nsfwschool` command, which returns schoolgirls.
  
  - `nsfwmaid` command, which returns maids.
  
  - `nsfwgif`, command, which returns gifs.

- This ones a big one. Added `states and territories (classes)` and all state flags and territory flags of the United States of America.
  
- Added PoliticalSelect to suppliment the afformentioned.
  
- Refractor, and forced "tachi" color.

- Refractor in `AnimeSelect (library)`, and new defs and new `AnimeNSFWGel (class)` to handle requests in `nsfwbooru`.
  
- Amazing progress bar.

- Music added on startup.

- Major shortening of words and a large refractor for stuff to make sense.

- New `math` and `mathround` commands added. Arithmetic only (for now.)

- New `weather` command. Advanced weather command achieved.

- Visualizes the way initialization is done.

- Weather and Math refractor.

## [1.2.0] - 2021-10-19 - 2021-10-31

- Added version to keep track of version.

- New `genshin` command to return genshin characters.

- Added `mute` command to mute people with.

- `SauceSelect (library)` `SauceNow (class)`, and three saucenao commands, Pixiv, Booru, and Anime respectively.

- Wildcard Refractor (*I'm dumb for not using them. (kinda).*)

- `roles` and `rolecount` work as intended now.

- `whois` command.

- `track` command, and `Spotify (class)`

- Event Handiling Changes, and listeners to fix other stuff.

## [1.3.0] - 2021-10-31 - 2021-11-17

- `spotify` command replacing the `track` command.

- ??? These things. cool... ???

- Better music library to run multiple audio files without problem. (still need an asynchronous one without C++).

- Spotify UI and image return.

- Avatar circle image, which will be used as a greeting tool when I read over guild and channel docs.

- `Console (class)` and `log (function)` to handle my console logs from now on, and no more printing. `async` for all!

- Cache folder to hold all my images that are not assets. They are temp files and will be refreshed routinely.

- Changed the way time works so that way it timestamps from other peoples time to prevent confusion.

- Akaneko was refractored and given way more commands.

- New `Neko (library)` and many neko commands incoming.

- Group command features.