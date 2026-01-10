import customtkinter as ct
import random as rd
from tkinter import messagebox
from PIL import Image

# ---------- App/Theming ----------
ct.set_appearance_mode("dark")  # "light" | "dark" | "system"
ct.set_default_color_theme("blue")  # "blue" | "green" | "dark-blue"

root = ct.CTk()
root.title("Hang Man")
root.geometry("1000x720")
root.minsize(900, 640)


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
    "Boulder", "Silent", "Shrine", "Mythic", "Cryptic", "Omen", "Rebirth", "Hollow", "Miracle", "Shade", "Hasnat"
]

stick_man_images_list = [
    "blank.jpg","stick_man1.jpg","stick_man2.jpg","stick_man3.jpg","stick_man4.jpg",
    "stick_man5.jpg","stick_man6.jpg","stick_man7.jpg","stick_man8.jpg","stick_man9.jpg","stick_man10.jpg"
]

# ---------- Layout Root Grid ----------
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ---------- Main Container ----------
main = ct.CTkFrame(root, corner_radius=16)
main.grid(row=0, column=0, sticky="nsew", padx=16, pady=16)
main.columnconfigure(0, weight=1)
main.rowconfigure(1, weight=1)

# ---------- Header ----------
header = ct.CTkFrame(main, fg_color="transparent")
header.grid(row=0, column=0, sticky="ew", pady=(0, 10))
header.columnconfigure(0, weight=1)
title = ct.CTkLabel(
    header, text="Hang Man", font=("Segoe UI", 28, "bold")
)
subtitle = ct.CTkLabel(
    header, text="Guess the word using your keyboard or click the alphabet buttons. You have 10 attempts.",
    font=("Segoe UI", 14)
)
title.grid(row=0, column=0, sticky="w")
subtitle.grid(row=1, column=0, sticky="w")

# ---------- Content Area ----------
content = ct.CTkFrame(main, corner_radius=16)
content.grid(row=1, column=0, sticky="nsew")
content.columnconfigure((0, 1), weight=1)
content.rowconfigure(0, weight=1)

# Left: Hangman Image
image_panel = ct.CTkFrame(content, corner_radius=16)
image_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)
image_panel.columnconfigure(0, weight=1)
image_panel.rowconfigure(1, weight=1)

image_title = ct.CTkLabel(image_panel, text="Progress", font=("Segoe UI", 16, "bold"))
image_title.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 0))

# Safe load first image
def load_ctk_image(path, size):
    try:
        return ct.CTkImage(light_image=Image.open(path), size=size)
    except Exception:
        # Fallback blank image if missing
        fallback = Image.new("RGB", size, color=(30, 30, 30))
        return ct.CTkImage(light_image=fallback, size=size)

image_stick_man = load_ctk_image(stick_man_images_list[0], size=(460, 500))
image_label = ct.CTkLabel(image_panel, image=image_stick_man, text="")
image_label.grid(row=1, column=0, padx=12, pady=12)

# Attempts info + bar
attempts_frame = ct.CTkFrame(image_panel, fg_color="transparent")
attempts_frame.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))
attempts_frame.columnconfigure(1, weight=1)

attempts_text = ct.CTkLabel(attempts_frame, text="Attempts:", font=("Segoe UI", 14))
attempts_text.grid(row=0, column=0, padx=(0, 10))

attempts_bar = ct.CTkProgressBar(attempts_frame, height=10)
attempts_bar.grid(row=0, column=1, sticky="ew")
attempts_bar.set(1.0)  # start with 10/10

attempts_label = ct.CTkLabel(image_panel, text="You have 10 Attempts", font=("Segoe UI", 14))
attempts_label.grid(row=3, column=0, padx=12, pady=(0, 12), sticky="w")

# Right: Word + Controls
right_panel = ct.CTkFrame(content, corner_radius=16)
right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=10)
right_panel.columnconfigure(0, weight=1)
right_panel.rowconfigure(1, weight=1)
right_panel.rowconfigure(3, weight=2)  # Give more space to alphabet keyboard

word_title = ct.CTkLabel(right_panel, text="Word", font=("Segoe UI", 16, "bold"))
word_title.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 0))

word_guess = ct.CTkFrame(right_panel, fg_color="transparent")
word_guess.grid(row=1, column=0, sticky="n", padx=12, pady=12)

# Status
status_frame = ct.CTkFrame(right_panel, fg_color="transparent")
status_frame.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))
status_label = ct.CTkLabel(status_frame, text="", font=("Segoe UI", 14))
status_label.pack(anchor="w")

# Alphabet Keyboard
alphabet_frame = ct.CTkFrame(right_panel, corner_radius=12)
alphabet_frame.grid(row=3, column=0, sticky="nsew", padx=12, pady=(0, 12))
alphabet_frame.columnconfigure(0, weight=1)
alphabet_frame.rowconfigure(1, weight=1)

alphabet_title = ct.CTkLabel(alphabet_frame, text="Alphabet", font=("Segoe UI", 16, "bold"))
alphabet_title.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 8))

# Create alphabet buttons in a grid
alphabet_container = ct.CTkFrame(alphabet_frame, fg_color="transparent")
alphabet_container.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))

# Configure grid for alphabet buttons (6 columns)
for i in range(6):
    alphabet_container.columnconfigure(i, weight=1)
for i in range(5):  # 5 rows (26 letters / 6 columns = ~5 rows)
    alphabet_container.rowconfigure(i, weight=1)

# Toolbar
toolbar = ct.CTkFrame(main, fg_color="transparent")
toolbar.grid(row=2, column=0, sticky="ew", pady=(10, 0))
toolbar.columnconfigure((0, 1, 2, 3), weight=1)

def safe_icon(path, size):
    try:
        return ct.CTkImage(light_image=Image.open(path), size=size)
    except Exception:
        blank = Image.new("RGBA", size, (0, 0, 0, 0))
        return ct.CTkImage(light_image=blank, size=size)

replay_icon = safe_icon("replay.png", (22, 22))
quit_icon = safe_icon("quit.png", (22, 22))

# ---------- Game State ----------
m = []         # labels for letters
Not_in = []    # incorrect attempts (as 1s)
in_in = []     # correct letters
choice = ""
alphabet_buttons = {}  # dictionary to store alphabet buttons
used_letters = set()   # track used letters for visual feedback

# ---------- Functions ----------
def create_alphabet_buttons():
    """Create alphabet buttons in a grid layout"""
    global alphabet_buttons
    alphabet_buttons.clear()
    
    # Clear existing buttons
    for widget in alphabet_container.winfo_children():
        widget.destroy()
    
    # Create buttons for A-Z
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(letters):
        row = i // 6
        col = i % 6
        
        btn = ct.CTkButton(
            alphabet_container,
            text=letter,
            width=60,
            height=60,
            font=("Segoe UI", 20, "bold"),
            command=lambda l=letter: letter_clicked(l.lower())
        )
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        alphabet_buttons[letter.lower()] = btn

def letter_clicked(letter):
    """Handle alphabet button clicks"""
    if letter in used_letters:
        return  # Don't process already used letters
    
    used_letters.add(letter)
    
    # Update button appearance
    if letter in alphabet_buttons:
        alphabet_buttons[letter].configure(
            fg_color="#2b2b2b",
            hover_color="#2b2b2b",
            text_color="#666666",
            state="disabled"
        )
    
    # Process the letter
    process_letter(letter)

def process_letter(letter):
    """Process a letter guess (used by both keyboard and button input)"""
    found = False
    for index, ch in enumerate(list(choice)):
        if letter == ch.lower():
            m[index].configure(text=ch.upper())
            in_in.append(ch)
            found = True

    if not found:
        Not_in.append(1)

    check()

    if sum(Not_in) >= 10:
        Not_in.clear()
        attempts_label.configure(text=f"Try again. The word was {choice}")
        messagebox.showinfo("Failed", "Try again later")
        return

    you_won()

def reset_alphabet_buttons():
    """Reset all alphabet buttons to their original state"""
    global used_letters
    used_letters.clear()
    
    for letter, btn in alphabet_buttons.items():
        btn.configure(
            fg_color=("#3B8ED0", "#1F6AA5"),
            hover_color=("#36719F", "#144870"),
            text_color="white",
            state="normal"
        )

def place():
    global choice
    m.clear()
    choice = rd.choice(x)
    print(choice)
    letters_container = word_guess

    # remove old children
    for w in letters_container.winfo_children():
        w.destroy()

    # Centered row of rounded boxes
    row = ct.CTkFrame(letters_container, fg_color="transparent")
    row.pack(pady=10)
    for _ in range(len(choice)):
        box = ct.CTkLabel(
            row, text="", width=68, height=76,
            corner_radius=10, fg_color=("#1f1f1f", "#1f1f1f"),
            text_color="white", font=("Segoe UI", 28, "bold")
        )
        box.pack(side="left", padx=6)
        m.append(box)

def update_attempts_ui():
    attempts_left = 10 - sum(Not_in)
    attempts_left = max(0, min(10, attempts_left))
    attempts_label.configure(text=f"You have {attempts_left} Attempts")
    attempts_bar.set(attempts_left / 10)

def check():
    misses = sum(Not_in)

    # Image update
    idx = max(0, min(misses, 10))
    new_img = load_ctk_image(stick_man_images_list[idx], size=(460, 500))
    image_label.configure(image=new_img)
    image_label.image = new_img  # prevent GC

    # Status copy
    copy = {
        0: "Let's start!",
        1: "You have 9 Attempts left",
        2: "C'mon you can do it",
        3: "Don't give up",
        4: "You have 6 Attempts",
        5: "You have 5 Attempts",
        6: "You have 4 Attempts",
        7: "You have 3 Attempts",
        8: "You have 2 Attempts",
        9: "You have 1 Attempt",
        10: "No attempts left"
    }
    status_label.configure(text=copy.get(misses, ""))

    update_attempts_ui()

def new_game():
    Not_in.clear()
    in_in.clear()
    reset_alphabet_buttons()
    place()
    attempts_label.configure(text="")
    status_label.configure(text="")
    update_attempts_ui()
    check()

def new_game_event(event):
    new_game()

def you_won():
    unique_letters = set(choice.lower())
    guessed_letters = set(letter.lower() for letter in in_in)
    if unique_letters.issubset(guessed_letters):
        attempts_label.configure(text=f"You guessed it! The word was {choice}")
        messagebox.showinfo("You Won!", f"Congratulations! You guessed the word '{choice}'!")
        in_in.clear()

def get(event):
    """Handle keyboard input"""
    if not event.char or not event.char.isalpha():
        return
    letter = event.char.lower()
    
    # Check if letter was already used
    if letter in used_letters:
        return
    
    # Add to used letters and update button appearance
    used_letters.add(letter)
    if letter in alphabet_buttons:
        alphabet_buttons[letter].configure(
            fg_color="#2b2b2b",
            hover_color="#2b2b2b",
            text_color="#666666",
            state="disabled"
        )
    
    # Process the letter
    process_letter(letter)

def inform(Event=None):
    messagebox.showinfo("Developer", "Created by Hasnat\nDate: 22/05/2025\nJUST FOR FUN")

def word(Event=None):
 
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
        info = information.get(choice, None)
        if info:
            messagebox.showinfo(
                "Cheater",
                f"The word is - {choice}\n\nMeaning - {info['meaning']}\n\nExample - {info['example']}"
            )
        else:
            messagebox.showinfo("Cheater", f"The word is - {choice}")
    except Exception:
        pass

replay_button = ct.CTkButton(
    toolbar, text=" New Game", image=replay_icon, command=new_game, width=140,height=50
)
quit_button = ct.CTkButton(
    toolbar, text=" Quit", image=quit_icon, fg_color="#b3261e", hover_color="#8b1f19",
    command=root.quit, width=120,height=50
)
info_button = ct.CTkButton(
    toolbar, text=" About", command=inform, width=120,height=50
)
# hint_button = ct.CTkButton(
#     toolbar, text=" Word Info (Ctrl+S)", command=word, width=180
# )

replay_button.grid(row=0, column=0, padx=6,pady=6)
# hint_button.grid(row=0, column=1, padx=6,pady=6)
info_button.grid(row=0, column=1, padx=6,pady=6)
quit_button.grid(row=0, column=2, padx=6,pady=6)


# Initialize the game
create_alphabet_buttons()
place()
attempts_label.configure(text="You have 10 Attempts")
check()

root.bind("<Key>", get)
root.bind("<Control-i>", inform)
root.bind("<Control-r>", new_game_event)
root.bind("<Control-s>", word)

root.mainloop()