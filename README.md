# BattleNotes
HackDartmouth 2021 

**YouTube Demo: https://youtu.be/YzIAeII5IEU**

BattleNotes is a web-based game. The player creates/joins a room and selects the character they wanna play - Musician, FitFreak, or TypeMaster. They wait until another player (opponent) joins the room.

Each character has their way of attacking/defending against the opponent. For example, FitFreak would attack a Musician by doing a few jumping jacks or push-ups, and the Musician could choose to defend by playing a tune given by the game engine. (​Similarly, TypeMaster would attack/defend by typing a sequence of words in a time constraint and achieving a fast typing score) As the game goes on, the difficulty level gets harder and the competition intensifies- the Musician gets increasingly challenging and long melodies, and the FitFreak has to do more reps!

Attacks make opponents lose points whereas your defenses recover your points. When one of the players' HP gets to zero, they lose and the game is over.

## Musician
The melodies are taken from the EsAC (Essen Associate Code and Folksong) Database, which contains over 7000 musical tunes, as well as the Weimar Jazz Database (nearly 500 jazz lead sheets). We categorize these into different “difficulty” levels based on their musical density and length, and extract the musical features. We use an obscure MIT Python library, in conjunction with a music engraving engine, to typeset the music and display it as an image for the musician to read. The recording of the musician’s playing is analyzed using FFT/spectrogram to detect beats and pitches and check them against the known correct sequence of notes they were supposed to play.

## Typemaster
The typing interface is based off of cheetoise, a typing tutor for python based on pygame. We get a corpus of words and sentences from various texts and joke sources and display them to the user to type out. The score is calculated as a function of accuracy, words per minute and length of sentence. This is then applied as an attack value or defense buff for incoming attacks.

## Pushups
The pushup detector interface is based off of an OpenCV and optical flow based pushup detection engine originaly authored by VNOpenAI. We take this engine and gameify it by using a retrained model to detect number of pushups and the detection threshold is dictated by the difficulty level. The number of pushups performed is the basis of the attack and defense values in the game.

## Game Engine
The basic game state is stored on mongodb and the engine itself is written as serverless functions.

# Select Screenshots

![image](https://user-images.githubusercontent.com/21221668/115465238-4ff1a880-a1fc-11eb-9c43-637bd4612bb0.png)
![image](https://user-images.githubusercontent.com/21221668/115465269-5aac3d80-a1fc-11eb-864a-426aabb0cab5.png)
![image](https://user-images.githubusercontent.com/21221668/115465289-5ed85b00-a1fc-11eb-98d9-e9081ee27667.png)
