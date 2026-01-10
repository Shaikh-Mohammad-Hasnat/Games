import customtkinter as ct
import random as rd
from tkinter import messagebox
from PIL import Image
root=ct.CTk()
x = [
    "Whisper", "Avalanche", "Oxygen", "Nightmare", "Pyramid", "Galaxy", "Tragedy", "Blizzard", "Labyrinth", "Quantum",
    "Eclipse", "Phoenix", "Mirage", "Harmony", "Spectrum", "Nebula", "Vortex", "Inferno", "Crystal", "Mystery",
    "Fortress", "Dragonfly", "Requiem", "Obsidian", "Equinox", "Solstice", "Cascade", "Ember", "Tempest", "Echo",
    "Tornado", "Whirlpool", "Banshee", "Enigma", "Chimera", "Fossil", "Harbinger", "Monolith", "Relic", "Crescent",
    "Oracle", "Cipher", "Oblivion", "Serenity", "Midnight", "Glacier", "Volcano", "Tundra", "Rapture", "Paradox",
    "Fragment", "Gravity", "Timeless", "Twilight", "Specter", "Comet", "Cosmos", "Radiance", "Entropy", "Wanderer",
    "Momentum", "Sanctuary", "Prism", "Cataclysm", "Ethereal", "Flicker", "Shimmer", "Thunder", "Wraith", "Zephyr",
    "Corrosion", "Ashen", "Beacon", "Nomad", "Fathom", "Obscure", "Pulse", "Reverie", "Glimmer", "Howl",
    "Talisman", "Mystic", "Horizon", "Flicker", "Storm", "Nova", "Gravity", "Echoes", "Riddle", "Static",
    "Boulder", "Silent", "Shrine", "Mythic", "Cryptic", "Omen", "Rebirth", "Hollow", "Miracle", "Shade","Hasnat"
]

root.columnconfigure((0),weight=1)
root.rowconfigure((0),weight=1)

root.title("Hang Man")

m=[]
 



def place():
   
   global choice
   choice=rd.choice(x)
   print(choice)
   for i in range(len(choice)): 
     a=ct.CTkLabel(word_guess,text="",fg_color="black",height=50,width=50)
     a.pack(padx=10,anchor="center",pady=10,side="left")
     m.append(a)


main_frame=ct.CTkFrame(root,bg_color="#e7e7e7",border_color="white",border_width=2)
main_frame.grid(row=0,column=0,sticky="nsew")

main_frame.columnconfigure((0),weight=1)
main_frame.rowconfigure((0),weight=1)

word_guess=ct.CTkFrame(main_frame,bg_color="#e7e7e7")
word_guess.pack(pady=10,padx=10)

place()


 

entery=ct.CTkLabel(main_frame,bg_color="#FFFFFF",text_color="black",height=70,text="",font=("calibri",30,"bold"))
entery.pack(pady=10,padx=10,fill="x")


image=ct.CTkImage(light_image=Image.open("replay.png"),size=(75,75))
image1=ct.CTkImage(light_image=Image.open("quit.png"),size=(60,60))


# hang_man_image=Image.open("you.png")




# Display image in a Label widget



# hang_man_frame=ct.CTkFrame(main_frame,fg_color="white",width=466,height=550)

# hang_man_frame.pack()

stick_man_images_list=["blank.jpg","stick_man1.jpg","stick_man2.jpg","stick_man3.jpg","stick_man4.jpg","stick_man5.jpg","stick_man6.jpg","stick_man7.jpg","stick_man8.jpg","stick_man9.jpg","stick_man10.jpg"]

image_stick_man=ct.CTkImage(light_image=Image.open(stick_man_images_list[0]),size=(500,550))

label = ct.CTkLabel(main_frame, image=image_stick_man,text="",corner_radius=30)
label.pack(fill="x")


hang_man_frame_options=ct.CTkFrame(main_frame,fg_color="#e7e7e7",border_color="white")
hang_man_frame_options.pack(pady=10,fill="x",padx=10)
hang_man_frame_options.columnconfigure((0,1),weight=1)



l=[]
Not_in=[]
in_in=[]
entery.configure(text="You have 10 Attempts")

def check():
    # label.configure(image=Image.open(stick_man_images_list[1]))
 
  if sum(Not_in)==0:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[0]),size=(500,550))
    
  if sum(Not_in)==1:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[1]),size=(500,550))
    entery.configure(text="You have 9 Attempts left")
  if sum(Not_in)==2:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[2]),size=(500,550))
    entery.configure(text="C'mon you can do it")

  if sum(Not_in)==3:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[3]),size=(500,550))
    entery.configure(text="Don't give up")

  if sum(Not_in)==4:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[4]),size=(500,550))
    entery.configure(text="You have 6 Attempts")
  
  if sum(Not_in)==5:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[5]),size=(500,550))
    entery.configure(text="You have 5 Attempts")
  if sum(Not_in)==6:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[6]),size=(500,550))
    entery.configure(text="You have 4 Attempts")
  if sum(Not_in)==7:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[7]),size=(500,550))
    entery.configure(text="You have 3 Attempts")
  if sum(Not_in)==8:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[8]),size=(500,550))
    entery.configure(text="You have 2 Attempts")
  if sum(Not_in)==9:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[9]),size=(500,550))
    entery.configure(text="You have 1 Attempts")
    
  if sum(Not_in)==10:
    image_stick_man.configure(light_image=Image.open(stick_man_images_list[10]),size=(500,550))


def new_game():

  for widgets in word_guess.winfo_children():
    widgets.destroy()

  Not_in.clear()
  m.clear()
  place()  
  entery.configure(text=f"")
  check()

def new_game_event(event):
    new_game()

def you_won():
    unique_letters = set(choice.lower())
    guessed_letters = set(letter.lower() for letter in in_in)

    if unique_letters.issubset(guessed_letters):

        entery.configure(text=f"You guessed it! The word was {choice}")
        messagebox.showinfo("You Won!", f"Congratulations! You guessed the word '{choice}'!")
        in_in.clear()


def get(event):
    list_choice=list(choice)
    if event.char.isalpha():
       # First, check if it's a letter
      letter=event.char.lower()
      for index,i in enumerate(list_choice):
       if letter==i.lower():
        print(i)
        m[index].configure(text=i.upper(),text_color="white",font=("halvetica",30,"bold"))
        in_in.append(i)
        check()
      # print(in_in)
      if letter not in list(choice.lower()):
        Not_in.append(1)
        # print(1)
        print("not_in",sum(Not_in))
        check() 
      if sum(Not_in)==10:
        Not_in.clear()
        
        entery.configure(text=f"Try again The word was {choice}")
        messagebox.showinfo("Failed","Try again later")
      you_won()

replay_button=ct.CTkButton(hang_man_frame_options,text="",image=image,fg_color="#e7e7e7",hover_color="white",command=new_game).grid(row=0,column=0,padx=10,sticky="e")
quit_button=ct.CTkButton(hang_man_frame_options,text="",image=image1,fg_color="#e7e7e7",hover_color="white",command=root.quit).grid(row=0,column=1,padx=10,sticky="w")

def inform(Event):
  messagebox.showinfo("Developer","Created by Hasnat\nDate:-22/05/2025\nJUST FOR FUN")


def word(Event):
    information={
    "Whisper": {
        "meaning": "A soft or confidential tone of voice.",
        "example": "She spoke in a whisper so no one else could hear."
    },
    "Avalanche": {
        "meaning": "A mass of snow, ice, and rocks falling rapidly down a mountainside.",
        "example": "The climbers were caught in an unexpected avalanche."
    },
    "Oxygen": {
        "meaning": "A chemical element essential for respiration.",
        "example": "Humans need oxygen to survive."
    },
    "Nightmare": {
        "meaning": "A frightening or unpleasant dream.",
        "example": "He woke up screaming from a nightmare."
    },
    "Pyramid": {
        "meaning": "A monumental structure with a square or triangular base and sloping sides.",
        "example": "The Great Pyramid of Giza is a marvel of ancient engineering."
    },
    "Galaxy": {
        "meaning": "A system of millions or billions of stars.",
        "example": "The Milky Way is the galaxy that contains our solar system."
    },
    "Tragedy": {
        "meaning": "An event causing great suffering, destruction, and distress.",
        "example": "The accident was a national tragedy."
    },
    "Blizzard": {
        "meaning": "A severe snowstorm with high winds and low visibility.",
        "example": "The blizzard shut down all transportation in the city."
    },
    "Labyrinth": {
        "meaning": "A complicated irregular network of passages or paths.",
        "example": "The ancient labyrinth was impossible to navigate without a map."
    },
    "Quantum": {
        "meaning": "A discrete quantity of energy proportional in magnitude.",
        "example": "Quantum mechanics changed the way we understand physics."
    },
    "Eclipse": {
        "meaning": "An event in which one celestial body moves into the shadow of another.",
        "example": "We watched the solar eclipse through special glasses."
    },
    "Phoenix": {
        "meaning": "A mythical bird that is cyclically reborn from its ashes.",
        "example": "Like a phoenix, she rose from the ashes of failure to success."
    },
    "Mirage": {
        "meaning": "An optical illusion caused by atmospheric conditions.",
        "example": "In the desert, they thought they saw water, but it was just a mirage."
    },
    "Harmony": {
        "meaning": "The combination of musical notes to produce a pleasing sound or general agreement.",
        "example": "They lived together in perfect harmony."
    },
    "Spectrum": {
        "meaning": "A range of different positions, opinions, or colors.",
        "example": "The rainbow shows the full color spectrum of visible light."
    },
    "Nebula": {
        "meaning": "A cloud of gas and dust in space, often where stars are born.",
        "example": "The Orion Nebula is visible with the naked eye on a clear night."
    },
    "Vortex": {
        "meaning": "A mass of spinning air, liquid, or other substance.",
        "example": "The water formed a vortex as it drained from the bathtub."
    },
    "Inferno": {
        "meaning": "A large fire that is dangerously out of control.",
        "example": "The building was consumed by a raging inferno."
    },
    "Crystal": {
        "meaning": "A solid material whose atoms are arranged in a highly ordered structure.",
        "example": "She collected different types of crystal formations."
    },
    "Mystery": {
        "meaning": "Something that is difficult or impossible to understand or explain.",
        "example": "The cause of the noise remained a mystery."
    },
    "Fortress": {
        "meaning": "A heavily protected and impenetrable building or place.",
        "example": "The soldiers retreated to the safety of the fortress."
    },
    "Dragonfly": {
        "meaning": "A fast-flying insect with two pairs of large wings and a long body.",
        "example": "The dragonfly hovered above the pond, wings shimmering in the sun."
    },
    "Requiem": {
        "meaning": "A mass or musical composition for the dead.",
        "example": "The choir sang a moving requiem at the memorial service."
    },
    "Obsidian": {
        "meaning": "A dark natural glass formed by the cooling of molten lava.",
        "example": "Ancient tools were often made from sharp obsidian."
    },
    "Equinox": {
        "meaning": "The time or date at which the sun crosses the celestial equator, when day and night are of equal length.",
        "example": "The spring equinox marks the start of longer days."
    },
    "Solstice": {
        "meaning": "The time or date when the sun reaches its highest or lowest point in the sky at noon.",
        "example": "The summer solstice is the longest day of the year."
    },
    "Cascade": {
        "meaning": "A small waterfall or series of waterfalls.",
        "example": "The mountain stream formed a beautiful cascade over the rocks."
    },
    "Ember": {
        "meaning": "A small glowing piece of coal or wood in a dying fire.",
        "example": "Only a few embers remained in the fireplace after midnight."
    },
    "Tempest": {
        "meaning": "A violent storm with strong winds.",
        "example": "The ship was caught in a powerful tempest at sea."
    },
    "Echo": {
        "meaning": "A sound or series of sounds caused by the reflection of sound waves.",
        "example": "Her voice echoed off the canyon walls."
    },
    "Tornado": {
        "meaning": "A rapidly rotating column of air in contact with both the surface of the Earth and a cloud.",
        "example": "The tornado tore through the town, leaving destruction in its wake."
    },
    "Whirlpool": {
        "meaning": "A rapidly rotating mass of water that pulls things into its center.",
        "example": "The boat narrowly avoided being caught in the whirlpool."
    },
    "Banshee": {
        "meaning": "A female spirit in Irish mythology, believed to wail when someone is about to die.",
        "example": "They said a banshee screamed the night before the tragedy."
    },
    "Enigma": {
        "meaning": "Something or someone that is mysterious or difficult to understand.",
        "example": "Despite years of study, the origin of the artifact remained an enigma."
    },
    "Chimera": {
        "meaning": "A mythical creature composed of parts from different animals; also a thing that is hoped for but illusory.",
        "example": "The idea of a perfect society is often seen as a chimera."
    },
    "Fossil": {
        "meaning": "The preserved remains or impression of a prehistoric organism.",
        "example": "They discovered a dinosaur fossil embedded in the rock."
    },
    "Harbinger": {
        "meaning": "A person or thing that announces or signals the approach of another.",
        "example": "Dark clouds are a harbinger of the coming storm."
    },
    "Monolith": {
        "meaning": "A large single upright block of stone, or a large and impersonal political, corporate, or social structure.",
        "example": "The ancient monolith stood tall in the deserted field."
    },
    "Relic": {
        "meaning": "An object surviving from an earlier time, especially one of historical interest.",
        "example": "The relic was displayed in the museum's ancient history section."
    },
    "Crescent": {
        "meaning": "The shape of the visible part of the moon when less than half full.",
        "example": "The crescent moon hung low in the evening sky."
    },
     "Oracle": {
        "meaning": "A person regarded as a source of wise counsel or prophetic opinions.",
        "example": "The oracle predicted the fall of the empire."
    },
    "Cipher": {
        "meaning": "A secret or disguised way of writing; a code.",
        "example": "They used a cipher to send covert messages."
    },
    "Oblivion": {
        "meaning": "The state of being unaware or unconscious of what is happening.",
        "example": "He drank himself into oblivion."
    },
    "Serenity": {
        "meaning": "The state of being calm, peaceful, and untroubled.",
        "example": "The mountain view filled her with a sense of serenity."
    },
    "Midnight": {
        "meaning": "Twelve o'clock at night.",
        "example": "The ghost was said to appear at midnight."
    },
    "Glacier": {
        "meaning": "A slowly moving mass of ice formed by the accumulation of snow.",
        "example": "The glacier carved a deep valley through the mountains."
    },
    "Volcano": {
        "meaning": "A mountain or hill that has a crater or vent through which lava erupts.",
        "example": "The volcano erupted and covered the nearby village in ash."
    },
    "Tundra": {
        "meaning": "A vast, flat, treeless Arctic region where the subsoil is permanently frozen.",
        "example": "Few plants can survive in the harsh tundra climate."
    },
    "Rapture": {
        "meaning": "A feeling of intense pleasure or joy.",
        "example": "She listened to the music with rapture."
    },
    "Paradox": {
        "meaning": "A seemingly absurd or self-contradictory statement that may be true.",
        "example": "It's a paradox that standing is more tiring than walking."
    },
    "Fragment": {
        "meaning": "A small part broken off or separated from something.",
        "example": "He found a fragment of ancient pottery buried in the soil."
    },
    "Gravity": {
        "meaning": "The force that attracts a body toward the center of the earth or toward any other physical body having mass.",
        "example": "Gravity keeps the planets in orbit around the sun."
    },
    "Timeless": {
        "meaning": "Not affected by the passage of time or changes in fashion.",
        "example": "Her beauty was timeless, untouched by age."
    },
    "Twilight": {
        "meaning": "The soft glowing light from the sky when the sun is below the horizon.",
        "example": "They walked along the beach during twilight."
    },
    "Specter": {
        "meaning": "A ghost or something widely feared as a possible unpleasant occurrence.",
        "example": "The specter of war hung over the negotiations."
    },
    "Comet": {
        "meaning": "A celestial object consisting of a nucleus of ice and dust that, when near the sun, displays a tail.",
        "example": "The comet lit up the night sky with its glowing tail."
    },
    "Cosmos": {
        "meaning": "The universe seen as a well-ordered whole.",
        "example": "She gazed at the stars, contemplating the vastness of the cosmos."
    },
    "Radiance": {
        "meaning": "Light or heat as emitted or reflected by something.",
        "example": "The bride glowed with radiance on her wedding day."
    },
    "Entropy": {
        "meaning": "A measure of disorder or randomness in a system.",
        "example": "Over time, the abandoned house fell into entropy and decay."
    },
    "Wanderer": {
        "meaning": "A person who travels aimlessly from place to place.",
        "example": "He was a wanderer, never staying in one town for long."
    },
    "Momentum": {
        "meaning": "The quantity of motion of a moving body, measured as a product of its mass and velocity; also, progress or development gaining speed.",
        "example": "The project gained momentum after the initial success."
    },
    "Sanctuary": {
        "meaning": "A place of refuge or safety.",
        "example": "The wildlife sanctuary provides a safe haven for endangered species."
    },
    "Prism": {
        "meaning": "A transparent optical element with flat, polished surfaces that refract light.",
        "example": "The glass prism split the white light into a spectrum of colors."
    },
    "Cataclysm": {
        "meaning": "A large-scale and violent event in the natural world or society.",
        "example": "The earthquake was a cataclysm that changed the region forever."
    },
    "Ethereal": {
        "meaning": "Extremely delicate and light in a way that seems not of this world.",
        "example": "She wore an ethereal gown that flowed like mist."
    },
    "Flicker": {
        "meaning": "To shine with a light that is sometimes bright and sometimes weak.",
        "example": "The candle's flame flickered in the breeze."
    },
    "Shimmer": {
        "meaning": "To shine with a soft, slightly wavering light.",
        "example": "The lake shimmered under the moonlight."
    },
    "Thunder": {
        "meaning": "A loud rumbling or crashing noise heard after a lightning flash due to the expansion of rapidly heated air.",
        "example": "The thunder shook the windows during the storm."
    },
    "Wraith": {
        "meaning": "A ghost or ghostlike image of someone, especially seen shortly before or after death.",
        "example": "The figure in the fog looked like a wraith."
    },
    "Zephyr": {
        "meaning": "A soft gentle breeze.",
        "example": "A warm zephyr swept across the fields."
    },
    "Corrosion": {
        "meaning": "The gradual destruction of materials (usually metals) by chemical reactions with their environment.",
        "example": "The pipes had weakened due to years of corrosion."
    },
    "Ashen": {
        "meaning": "Pale gray in color; often used to describe a person’s face when very shocked or ill.",
        "example": "Her face turned ashen when she heard the bad news."
    },
    "Beacon": {
        "meaning": "A light or signal that guides or warns; a source of inspiration or guidance.",
        "example": "The lighthouse served as a beacon for ships navigating the dark waters."
    },
    "Nomad": {
        "meaning": "A member of a people or group that moves from place to place without a permanent home.",
        "example": "The nomad traveled across the desert with his caravan."
    },
    "Fathom": {
        "meaning": "To understand something deeply; also a unit of depth in water.",
        "example": "He couldn't fathom why she had left so suddenly."
    },
    "Obscure": {
        "meaning": "Not clear or hard to understand; not well known.",
        "example": "The meaning of the ancient text remains obscure."
    },
    "Pulse": {
        "meaning": "A rhythmic throbbing or vibration; also refers to the heartbeat.",
        "example": "She felt the steady pulse of the music through the floor."
    },
    "Reverie": {
        "meaning": "A state of being pleasantly lost in one's thoughts; a daydream.",
        "example": "He was lost in a reverie, staring out the window."
    },
    "Glimmer": {
        "meaning": "A faint or wavering light; a small sign of hope or feeling.",
        "example": "A glimmer of light shone from the distant cabin."
    },
    "Howl": {
        "meaning": "A long, loud, doleful cry often made by animals or wind.",
        "example": "Wolves began to howl under the full moon."
    },
    "Boulder": {
        "meaning": "A large rock, typically one that has been worn smooth by erosion.",
        "example": "They had to climb over a massive boulder to continue the trail."
    },
    "Silent": {
        "meaning": "Not making or accompanied by any sound.",
        "example": "The forest was silent, save for the rustle of leaves."
    },
    "Shrine": {
        "meaning": "A place regarded as holy because of its associations with a divinity or a sacred person or event.",
        "example": "Pilgrims traveled for miles to visit the ancient shrine."
    },
    "Mythic": {
        "meaning": "Relating to or resembling myth; idealized or legendary.",
        "example": "The hero became a mythic figure in his hometown."
    },
    "Cryptic": {
        "meaning": "Having a meaning that is mysterious or obscure.",
        "example": "She left a cryptic message that no one could understand."
    },
    "Omen": {
        "meaning": "An event regarded as a sign of good or evil to come.",
        "example": "The black cat crossing his path was seen as a bad omen."
    },
    "Rebirth": {
        "meaning": "A process of being born again or renewed.",
        "example": "The spring symbolizes nature’s rebirth after winter."
    },
    "Hollow": {
        "meaning": "Having a space or cavity inside; lacking substance or value.",
        "example": "His words sounded hollow without real emotion behind them."
    },
    "Miracle": {
        "meaning": "An extraordinary and welcome event not explicable by natural or scientific laws.",
        "example": "Surviving the crash was considered a miracle."
    },
    "Shade": {
        "meaning": "A shadow or area sheltered from light; also a subtle variation in tone or meaning.",
        "example": "They rested in the cool shade of a tree."
    }
}
    try:
      messagebox.showinfo("Cheater",f"The word is - {choice}\n\nMeaning-{information[choice]["meaning"]}\n\nExample-{information[choice]["example"]}")
    
    except Exception as e:
        pass
    
root.bind("<Key>",get)

root.bind("<Control-i>",inform)

root.bind("<Control-r>",new_game_event)

root.bind("<Control-s>",word)
root.mainloop()