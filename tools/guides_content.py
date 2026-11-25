# TAB guidance sheets. Each guide: slug, title, cat, mins, summary, body (mini-markdown:
# "## " heading, "- " bullet, "1. " numbered, "> " tip box, "!! " warning box, blank line = new paragraph)

GUIDES = [
dict(slug='how-to-send-stems', title='How to send stems', cat='Mixing', mins=4,
summary='Exactly what to export and how to package it so your mix starts right first time.',
body='''
Stems are the separate audio files that make up your song: the beat, each vocal, each instrument. Send them right and your engineer spends the session mixing, not fixing.

## What to send
- Every track as its own WAV file, all starting at the very beginning of the song (bar 1, 0:00), even if the part comes in later.
- The same length for every file, so they line up perfectly when dropped into a new session.
- The beat as stems (drums, bass, melodies, FX) if you have them. A single two-track beat is fine if that's all you've got.
- A rough mix or demo bounce of the whole song, so we can hear what you're going for.
- One or two reference tracks: songs whose sound you love.

## Format
- WAV, 24-bit, at the session's sample rate (usually 44.1 kHz or 48 kHz). Don't convert it.
- No MP3s for stems. MP3 throws away detail you can't get back.
- Mono sources (a single vocal, a kick) can be mono files. Stereo sources (pads, beats, doubles panned wide) stay stereo.

## Effects: on or off?
- Send vocals dry (no effects) as the main version.
- If an effect is part of the sound (a tape stop, a vocal chop, a distorted ad-lib), send a second "wet" version too and label it.
- Turn off anything on the master/stereo bus: limiters, maximisers, mastering presets.

## Label everything
Name files so anyone can understand them without asking:

1. 01_Kick.wav
2. 05_LeadVox_Verse.wav
3. 06_LeadVox_Hook.wav
4. 07_Adlibs_L.wav
5. 12_808.wav

Put the song name, BPM and key in the folder name, for example: SongName_140bpm_Fmin_Stems.

## How to send
- Zip the folder and send it through WeTransfer, Google Drive or Dropbox.
- Check the link works and the files open before you send it.
- Message us on WhatsApp with the link, the BPM and anything specific you want (louder ad-libs, darker vocal, more space).

> Quick check: drag every stem into a fresh, empty project at bar 1. If it plays back sounding like your song, you've done it right.
'''),

dict(slug='bouncing-and-export-settings', title='Bouncing & export settings', cat='Mixing', mins=4,
summary='The right sample rate, bit depth and file type for every stage, from demo to master.',
body='''
"Bouncing" means exporting audio out of your DAW. The settings you choose decide the quality we get to work with.

## The settings that matter
- File type: WAV (or AIFF). Lossless, full quality.
- Bit depth: 24-bit for stems and mixes. 32-bit float is fine too if your DAW offers it.
- Sample rate: keep it the same as your project, usually 44.1 kHz or 48 kHz. Don't upsample.
- Normalise: off. It changes your levels.
- Dither: off for stems and mixes. Only the final master gets dither, once.

## For each stage
- Stems for mixing: WAV, 24-bit, project sample rate, master bus effects off, everything starting at bar 1.
- Mix for mastering: one stereo WAV, 24-bit, no limiter on the master bus, peaks around -6 dB to -3 dB.
- Rough mix to share: MP3 at 320 kbps is fine for listening only, never for working files.

## Tails and silence
- Leave a couple of bars at the end so reverbs and delays can ring out instead of cutting off.
- Don't trim the start. Everything should line up from 0:00.

!! Avoid clipping: if the red light on your master or any channel is flashing, pull the faders down before you bounce. Distortion you didn't mean to make can't be removed later.

> Not sure of your project sample rate? Look in your DAW's project or audio settings. Use the same number on export.
'''),

dict(slug='exporting-stems-in-your-daw', title='Exporting stems in your DAW', cat='Mixing', mins=5,
summary='Step-by-step stem exports in Logic Pro, FL Studio, Ableton Live and Pro Tools.',
body='''
Every DAW can export all your tracks in one go. Before you start, set your loop or selection from the very start of the song to a couple of bars past the end.

## Logic Pro
1. Go to File, Export, All Tracks as Audio Files (Shift + Cmd + E).
2. Format WAV, resolution 24-bit, sample rate: same as the project.
3. Untick Normalise. Tick Include Volume/Pan Automation.
4. Choose whether to bypass effect plug-ins: send one dry set, and a wet set too if the effects are part of the sound.
5. Pick a folder and export.

## FL Studio
1. Route each sound to its own mixer insert and name the inserts.
2. Go to File, Export, WAV file (Ctrl + R).
3. Set the mode to Song, bit depth 24-bit.
4. Tick Split mixer tracks.
5. Render. FL saves one file per mixer track.

## Ableton Live
1. Go to File, Export Audio/Video (Cmd/Ctrl + Shift + R).
2. Set Rendered Track to All Individual Tracks.
3. File type WAV, bit depth 24, sample rate: same as the project.
4. Turn Normalise off.
5. Export.

## Pro Tools
1. Select the tracks you want to export.
2. Right-click a track name and choose Bounce (Track Bounce).
3. File type WAV, bit depth 24-bit, interleaved stereo for stereo tracks.
4. Untick any options that add effects you don't want, and export to a new folder.

> After exporting, open the folder and check the number of files matches the number of tracks. Missing a file is the most common hold-up.
'''),

dict(slug='using-plug-ins-the-right-way', title='Using plug-ins the right way', cat='Production', mins=5,
summary='Inserts vs sends, the order of your chain and how to avoid the mistakes that wreck a mix.',
body='''
Plug-ins are the effects and processors inside your DAW: EQ, compressors, reverb, delay, saturation, tuning. Used well they shape your sound. Used blindly they make it smaller.

## Inserts vs sends
- Inserts sit directly on a channel and process the whole signal: EQ, compression, saturation, tuning.
- Sends split a copy of the signal off to a shared effect channel (an aux or return): reverb and delay usually live here.
- Using sends for reverb and delay means one reverb can glue several parts together, and you keep control over how much each part gets.

## A common vocal chain (in order)
1. Tuning (if needed), set gently first.
2. Subtractive EQ: roll off rumble below roughly 80 to 100 Hz and cut harsh or boxy spots.
3. Compression to even out the level.
4. De-esser to tame harsh S and T sounds.
5. Tone EQ or saturation for character.
6. Reverb and delay on sends, not inserts.

The order changes the sound. Compressing before EQ reacts to the bass you're about to cut, so cut first.

## Habits that help
- Level-match: when you add a plug-in, check it isn't just making things louder. Louder always sounds "better" for a second.
- Bypass and compare often. If you can't hear what a plug-in is doing, remove it.
- Fewer plug-ins, used with purpose, beats ten presets stacked on top of each other.
- Keep the master bus clean while you're writing. Limiters on the master hide problems.

## Sending a session with plug-ins
- Third-party plug-ins won't open on someone else's computer unless they own them too.
- If a plug-in is part of your sound, print it: bounce that track with the effect on, as well as a dry version.
- List the plug-ins and settings you used in a note with your stems.
'''),

dict(slug='gain-staging-basics', title='Gain staging basics', cat='Recording', mins=4,
summary='Keep your levels healthy from the mic to the master so nothing clips and plug-ins behave.',
body='''
Gain staging means keeping a healthy level at every step of the signal, from the microphone to the master fader. Get it right and your recordings are clean, your plug-ins respond properly and your mix has room to breathe.

## When recording
- Set your interface gain so the loudest parts peak around -12 dB to -6 dB on the meter.
- Never let it hit 0 dB. Digital clipping is permanent.
- Too quiet is better than too loud, but very low levels bring up noise when boosted later. Aim for the middle.

## In your session
- Keep individual tracks peaking roughly around -18 dB to -10 dB before effects.
- Use clip or region gain to even out loud and quiet takes before they hit plug-ins.
- Leave the master fader at 0 and turn the channels down instead if the master is too hot.

## Before you bounce a mix
- Aim for peaks between -6 dB and -3 dB on the master, with no limiter.
- That leaves headroom for mastering, where the final loudness is set.

> Many analogue-style plug-ins are designed around a level near -18 dBFS. Feeding them much hotter than that can add distortion you didn't ask for.
'''),

dict(slug='recording-vocals-at-home', title='Recording vocals at home', cat='Recording', mins=5,
summary='Get clean, usable vocal takes from a bedroom setup before your mix session.',
body='''
A great mix starts with a clean recording. You don't need an expensive studio to capture a vocal we can work with, just a few good habits.

## The room
- Pick the quietest, softest room you have. Bedrooms with carpets, curtains and a bed are better than kitchens and bathrooms.
- Stand away from walls, especially corners. Hanging duvets or a clothes rail behind you cuts reflections a lot.
- Turn off fans, fridges, heaters and notifications.

## Mic technique
- Use a pop filter about 5 to 10 cm from the mic.
- Stand roughly a hand's width or two from the mic. Stay at the same distance for every take.
- For loud parts, lean back a little rather than turning the gain down mid-song.

## Levels and settings
- Peak around -12 dB to -6 dB on your interface. Never into the red.
- Record at 24-bit, 44.1 kHz or 48 kHz.
- Record dry: no reverb or autotune printed into the file. Monitor with effects if you like, but record clean.

## Takes
- Record several full takes of each section so there are options to comp from.
- Record doubles and ad-libs on separate tracks, and label them.
- Listen back on headphones for clicks, breaths, phones buzzing and clothes rustling.

> Wear closed-back headphones so the beat doesn't bleed into the mic.
'''),

dict(slug='before-your-studio-session', title='Before your studio session', cat='Sessions', mins=3,
summary='What to bring, how to prepare and what happens on the day, so you get the most from your time.',
body='''
Studio time goes fast. A little preparation means more of it is spent creating.

## A few days before
- Send us your beat and lyrics, and any references, on WhatsApp.
- Tell us the BPM and key of the beat.
- Practise your parts so you're recording, not writing, in the room.
- Confirm the time, address and who's coming.

## What to bring
- Your beat as a WAV (and stems if you have them) on a USB stick or ready to download.
- Lyrics on your phone or printed.
- Your own headphones if you prefer them.
- Water. Avoid dairy and fizzy drinks right before singing.

## On the day
- Arrive on time. Your session time starts at the booked time.
- We'll set up and soundcheck, then get straight into recording.
- Keep the room to the people who need to be there. Too many guests slow things down.

## After the session
- You'll get your recorded files, labelled and ready to mix.
- Book your mix and master, or the next session, straight away while the song is fresh.

> Booking regular sessions? Artist development gives you two 4-hour studio blocks every month.
'''),

dict(slug='preparing-your-mix-for-mastering', title='Preparing your mix for mastering', cat='Mastering', mins=4,
summary='How to bounce a mix that gives the mastering engineer room to make it shine.',
body='''
Mastering is the final stage: it sets the loudness, balances the tone and makes your track translate on every system. It works best on a mix that's been prepared for it.

## The checklist
- Export one stereo WAV, 24-bit, at the project sample rate.
- Remove the limiter or maximiser from your master bus.
- Peaks between -6 dB and -3 dB. No clipping anywhere.
- Leave a little silence at the start and let the end ring out fully. Don't fade it yourself unless the fade is part of the song.
- Name it clearly: Artist_SongTitle_Mix_v3.wav.

## Send with it
- One or two reference tracks you'd like it to sit next to.
- Notes on the vibe or anything you want changed.
- Your release format: streaming only, or vinyl/CD too.

## What mastering can't fix
- A vocal that's too quiet or too loud in the mix.
- A harsh instrument or a muddy low end that's built into the mix.
Fix those in the mix first. Mastering polishes, it doesn't rebuild.
'''),

dict(slug='loudness-for-streaming', title='Loudness for streaming', cat='Mastering', mins=3,
summary='LUFS, true peak and why louder isn\'t always better on Spotify, Apple Music and YouTube.',
body='''
Streaming platforms turn tracks up or down so everything plays at a similar volume. That's called loudness normalisation, and it's measured in LUFS.

## The numbers
- Spotify and YouTube normalise to around -14 LUFS integrated.
- Apple Music normalises to around -16 LUFS.
- Keep true peak at or below -1 dBTP so the track doesn't distort when it's converted for streaming.

## What this means for you
- A track mastered much louder than -14 LUFS just gets turned down, and you lose punch and dynamics for nothing.
- A track mastered quieter may get turned up, as long as there's headroom.
- Modern rap, drill and pop are often mastered louder than -14 LUFS for impact. That's a creative choice, not a rule, and the platforms will still turn it down.

> We master to sound great after normalisation, not just loud in your DAW.
'''),

dict(slug='naming-and-organising-files', title='Naming & organising files', cat='Workflow', mins=3,
summary='A simple folder and file system that saves you hours and keeps every version safe.',
body='''
Lost files and confusing names cost more studio time than anything else. Use the same system for every song.

## Folder structure
1. SongName (main folder)
2. 01_Session (your DAW project)
3. 02_Stems
4. 03_Mixes
5. 04_Masters
6. 05_Artwork_and_Info

## File names
- Artist_SongTitle_Mix_v1.wav, then v2, v3. Never "final", "final final" or "NEW".
- Put the BPM and key in the stems folder name.
- Use underscores, not spaces or symbols.

## Back it up
- Keep everything in at least two places: your computer and a cloud drive or external hard drive.
- Back up after every session.

> When you send us a new version, tell us which version number you're sending and what changed.
'''),

dict(slug='using-reference-tracks', title='Using reference tracks', cat='Mixing', mins=3,
summary='How to pick references that get you the sound you\'re hearing in your head.',
body='''
A reference track is a released song you love the sound of. It's the fastest way to show us what you want.

## Choosing references
- Pick songs in a similar genre and tempo to yours.
- Choose them for a specific reason: the vocal sound, the 808, the space, the energy.
- One or two is enough. Ten pulls the mix in every direction.

## Sending them
- Send streaming links or high-quality files, not screen recordings.
- Tell us what you like about each one: "the vocal sits on top like this" or "the drums hit like this".

## Listening properly
- Compare at the same volume. A louder song will always seem better.
- Listen on the systems your fans will use: phone, earphones, car, laptop.
'''),

dict(slug='release-checklist', title='Release checklist', cat='Release', mins=4,
summary='Everything to have ready before you upload, from metadata to pitching for playlists.',
body='''
Finishing the song is half the job. Plan the release so it gets heard.

## 4 to 6 weeks before
- Final master approved, and artwork at 3000 x 3000 px (JPG or PNG, no blurry text).
- Choose a distributor (for example DistroKid, TuneCore, Amuse or CD Baby) and upload with a release date at least 3 to 4 weeks away.
- Fill in the metadata carefully: song title, artist names, featured artists, writers, producers, genre, explicit tag.
- Make sure you have, or are given, an ISRC code for the track.

## 2 to 4 weeks before
- Pitch the song to Spotify's editors through Spotify for Artists. You must pitch at least 7 days before release, but earlier is better.
- Set up a pre-save link and share it.
- Plan your content: a teaser, a behind-the-scenes clip, the cover reveal.

## Release week
- Post on release day with the link in your bio.
- Send it to the people who supported you and ask them to share.
- Submit it to the TAB spotlight.

## After release
- Keep posting for at least two to three weeks. Most songs grow after day one, not on it.
- Check your stats in Spotify for Artists and Apple Music for Artists to see where listeners are coming from.
'''),

dict(slug='mix-feedback-and-revisions', title='Giving mix feedback', cat='Mixing', mins=3,
summary='How to give notes that get you the changes you want, using your included round wisely.',
body='''
Every mix includes one round of changes, and extra rounds are £25 each. Clear notes mean you get it right in one.

## Before you send notes
- Listen on at least three systems: headphones, phone speaker and a car or speaker.
- Listen at a normal volume, and take a break between listens.
- Write everything down in one message instead of sending notes one at a time.

## How to write notes
- Use timestamps: "1:24, the ad-lib is too loud."
- Describe the feeling if you don't know the technical word: "the hook feels small", "the 808 is muddy".
- Say what you like too, so it doesn't change.
- Point to a reference if you can: "I want the vocal to sit like it does in this song."

## What counts as a revision
- A round is one set of notes sent together and the updated mix that comes back.
- New parts, re-recorded vocals or a different beat count as a new mix, not a revision.
'''),
]
