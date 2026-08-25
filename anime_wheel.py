import random
import tkinter as tk


BG = "#0f1117"
PANEL = "#171b26"
PANEL_LIGHT = "#222839"
HOVER = "#2c3547"
BORDER = "#303a4e"
INK = "#f4f1ea"
MUTED = "#8b93a7"
CORAL = "#ff715b"
GOLD = "#f4c95d"
MINT = "#67d8b0"
BLUE = "#7da7ff"
DARK_INK = "#141721"

TEAM_COLORS = [CORAL, BLUE, MINT, GOLD]
DEFAULT_TEAMS = ["TEAM SUN", "TEAM MOON", "TEAM STAR", "TEAM COMET"]
MIN_ROUNDS = 3
MAX_ROUNDS = 25

TIERS = {
	"normal": ("NORMAL", BLUE, 1),
	"medium": ("MEDIUM", GOLD, 2),
	"deep": ("DEEP CUT", CORAL, 3),
	"vet": ("VETERAN", "#b18cff", 4),
	"boss": ("FINAL BOSS", "#ff5d8f", 5),
}


STYLES = {
	"One Piece": ("☠", "#e85d4a", "#ffd166"),
	"Naruto": ("渦", "#ef8f3a", "#f7d488"),
	"Naruto Shippuden": ("九", "#b03a2e", "#f5cba7"),
	"Dragon Ball": ("亀", "#3478c9", "#81d4fa"),
	"Dragon Ball Z": ("龍", "#f19a1a", "#ffe08a"),
	"Demon Slayer": ("炎", "#2374ab", "#6fe7db"),
	"The Eminence in Shadow": ("影", "#3a3f58", "#9aa7ff"),
	"Fist of the North Star": ("北斗", "#7a2f2f", "#ffd9a0"),
	"JoJo's Bizarre Adventure": ("★", "#c44569", "#f8c291"),
	"Vinland Saga": ("船", "#3f6b4f", "#bcd9a0"),
	"Attack on Titan": ("翼", "#34495e", "#9ad1d4"),
	"Fullmetal Alchemist": ("⚗", "#7b4f9c", "#e0b1cb"),
	"Fullmetal Alchemist: Brotherhood": ("⚗", "#7b4f9c", "#e0b1cb"),
	"Fate/stay night": ("剣", "#8a6d1f", "#f0d68a"),
	"The Melancholy of Haruhi Suzumiya": ("S", "#5b8dd9", "#a8d8ff"),
	"Steins;Gate": ("Ω", "#37465b", "#7fd4c1"),
	"Code Geass": ("♞", "#4b2e63", "#d1b3ff"),
	"Neon Genesis Evangelion": ("01", "#6d3ca8", "#79c267"),
	"Black Butler": ("♟", "#2b2b3d", "#c9a227"),
	"Death Note": ("N", "#222831", "#a7bbc7"),
	"One Punch Man": ("拳", "#d8a012", "#fff0a8"),
	"Berserk": ("蝕", "#5a1f1f", "#e08a8a"),
	"Hunter x Hunter": ("♣", "#2e7d54", "#9ce8b8"),
	"My Hero Academia": ("+", "#d64550", "#f7d354"),
	"Rurouni Kenshin": ("刃", "#8a2f2f", "#f0c987"),
	"Sailor Moon": ("☾", "#6c5ce7", "#f8a5c2"),
	"Pokémon": ("⚡", "#f1b514", "#fff3a3"),
	"Bleach": ("斬", "#252a34", "#f38181"),
	"Haikyuu!!": ("●", "#f28f3b", "#fff1c1"),
	"Jujutsu Kaisen": ("∞", "#4c5bd4", "#b8c0ff"),
	"Solo Leveling": ("君", "#3b2f63", "#a88cff"),
	"Puella Magi Madoka Magica": ("契", "#d4699e", "#ffd1e0"),
	"Monster": ("怪", "#3d4653", "#aab7c4"),
	"Kaguya-sama: Love Is War": ("戦", "#c94f6d", "#ffb3c1"),
	"Gintama": ("銀", "#9aa5b1", "#dbe4ee"),
	"Detective Conan": ("真", "#b03a48", "#f2b3bb"),
	"Trigun": ("銃", "#c96f3a", "#ffd9a8"),
	"Cowboy Bebop": ("♪", "#3a4668", "#8fa7ff"),
	"Yu-Gi-Oh!": ("遊", "#7a4fc9", "#cdb0ff"),
	"Fairy Tail": ("妖", "#e0641f", "#ffc98a"),
	"Spy × Family": ("家", "#c23b4e", "#f5a3ad"),
	"Dr. Stone": ("石", "#2f9e6e", "#9fe8c5"),
	"Inuyasha": ("犬", "#8a5a2b", "#e8c39a"),
	"Love Live! School Idol Project": ("虹", "#e06aa8", "#ffc3dd"),
	"Higurashi: When They Cry": ("綺", "#7a4a6a", "#d8b3c9"),
	"Katanagatari": ("刀", "#c9a227", "#f5ebc0"),
	"A Certain Magical Index": ("禁", "#8a9ab0", "#dce4ee"),
	"Hyouka": ("氷", "#8fa8b8", "#dfeef2"),
	"The Prince of Tennis": ("球", "#3f8f5f", "#a8e0bf"),
	"Slam Dunk": ("桜", "#c94f3d", "#ffb09f"),
	"The World God Only Knows": ("攻", "#7a5fc9", "#cdb0ff"),
	"Monogatari Series": ("猫", "#4a3f5f", "#c9bcd8"),
	"Tengen Toppa Gurren Lagann": ("天", "#ff8f3a", "#ffe08a"),
	"The Seven Deadly Sins": ("罪", "#c9a227", "#f5e08a"),
	"Black Clover": ("黒", "#33383f", "#9aa3b5"),
	"Frieren: Beyond Journey's End": ("葬", "#5a7d9a", "#cfe3f0"),
	"Dragon Ball Super": ("神", "#c96f1e", "#ffe08a"),
	"Sword Art Online": ("檻", "#2b6f8f", "#9fdcf0"),
	"Yu Yu Hakusho": ("霊", "#2f7d4f", "#a8e6c3"),
	"KonoSuba": ("爆", "#c98f1e", "#ffe08a"),
	"Slayers": ("紅", "#c2452d", "#ffb0a3"),
	"Magical Girl Lyrical Nanoha": ("星", "#b05fd4", "#e6c9ff"),
	"Mobile Fighter G Gundam": ("G", "#2f5fa0", "#a8c8ff"),
	"That Time I Got Reincarnated as a Slime": ("覇", "#2f6f8f", "#a8dcf0"),
	"Tokyo Ghoul": ("喰", "#2b2b3d", "#c0394b"),
	"Re:Zero": ("死", "#5f5fa8", "#c9c9ff"),
	"Chainsaw Man": ("鋸", "#c9611e", "#ffd9b0"),
	"Food Wars!": ("食", "#e07b39", "#ffe0a8"),
	"Serial Experiments Lain": ("繋", "#3d4653", "#9fb8c9"),
	"Made in Abyss": ("淵", "#7a5a2f", "#e8d0a0"),
	"Kill la Kill": ("鮮", "#c92f4a", "#ff9fb0"),
	"Psycho-Pass": ("犯", "#2f4858", "#9fd4e8"),
	"Mobile Suit Gundam": ("赤", "#a83a3a", "#ffb0b0"),
}

QUESTIONS = [
	{
		"anime": "One Piece", "prompt": "Which pirate captain wears a straw hat?",
		"answer": "Monkey D. Luffy", "choices": ["Monkey D. Luffy", "Portgas D. Ace", "Trafalgar Law", "Shanks"],
		"kind": "character", "symbol": "☠", "colors": ("#e85d4a", "#ffd166"),
	},
	{
		"anime": "Naruto", "prompt": "Complete the iconic line: 'Believe it!' is said by...",
		"answer": "Naruto Uzumaki", "choices": ["Naruto Uzumaki", "Sasuke Uchiha", "Kakashi Hatake", "Rock Lee"],
		"kind": "line", "symbol": "!", "colors": ("#ef8f3a", "#f7d488"),
	},
	{
		"anime": "Dragon Ball", "prompt": "What is Goku's signature energy attack?",
		"answer": "Kamehameha", "choices": ["Kamehameha", "Rasengan", "Getsuga Tensho", "Bankai"],
		"kind": "symbol", "symbol": "亀", "colors": ("#3478c9", "#81d4fa"),
	},
	{
		"anime": "Attack on Titan", "prompt": "Who is known as humanity's strongest soldier?",
		"answer": "Levi Ackerman", "choices": ["Levi Ackerman", "Erwin Smith", "Eren Yeager", "Reiner Braun"],
		"kind": "character", "symbol": "⚔", "colors": ("#34495e", "#9ad1d4"),
	},
	{
		"anime": "Sailor Moon", "prompt": "Which phrase begins the famous transformation?",
		"answer": "Moon Prism Power, Make Up!", "choices": ["Moon Prism Power, Make Up!", "In the name of the moon!", "Tuxedo La Smokin'!", "Silver Crystal Shine!"],
		"kind": "line", "symbol": "☾", "colors": ("#6c5ce7", "#f8a5c2"),
	},
	{
		"anime": "Demon Slayer", "prompt": "Which breathing style does Tanjiro first master?",
		"answer": "Water Breathing", "choices": ["Water Breathing", "Flame Breathing", "Thunder Breathing", "Mist Breathing"],
		"kind": "symbol", "symbol": "水", "colors": ("#2374ab", "#6fe7db"),
	},
	{
		"anime": "Death Note", "prompt": "What does Light Yagami find in the human world?",
		"answer": "A Death Note", "choices": ["A Death Note", "A cursed sword", "A magic mirror", "A demon mask"],
		"kind": "symbol", "symbol": "N", "colors": ("#222831", "#a7bbc7"),
	},
	{
		"anime": "My Hero Academia", "prompt": "Who shouts 'Plus Ultra!'?",
		"answer": "All Might", "choices": ["All Might", "Deku", "Bakugo", "Endeavor"],
		"kind": "line", "symbol": "+", "colors": ("#d64550", "#f7d354"),
	},
	{
		"anime": "Jujutsu Kaisen", "prompt": "Who is the teacher with the blindfold?",
		"answer": "Satoru Gojo", "choices": ["Satoru Gojo", "Yuji Itadori", "Megumi Fushiguro", "Suguru Geto"],
		"kind": "character", "symbol": "∞", "colors": ("#4c5bd4", "#b8c0ff"),
	},
	{
		"anime": "Pokémon", "prompt": "What does Pikachu say?",
		"answer": "Pika Pika!", "choices": ["Pika Pika!", "Gotta go fast!", "Digivolve!", "Believe it!"],
		"kind": "line", "symbol": "⚡", "colors": ("#f1b514", "#fff3a3"),
	},
	{
		"anime": "Bleach", "prompt": "What does Ichigo wield?",
		"answer": "Zangetsu", "choices": ["Zangetsu", "Samehada", "Nichirin", "Excalibur"],
		"kind": "symbol", "symbol": "斬", "colors": ("#252a34", "#f38181"),
	},
	{
		"anime": "Fullmetal Alchemist", "prompt": "What is the first rule of alchemy?",
		"answer": "Equivalent Exchange", "choices": ["Equivalent Exchange", "The law of gravity", "Never look back", "Truth is beauty"],
		"kind": "line", "symbol": "⚗", "colors": ("#7b4f9c", "#e0b1cb"),
	},
	{
		"anime": "Neon Genesis Evangelion", "prompt": "What is Unit-01's main color?",
		"answer": "Purple and green", "choices": ["Purple and green", "Red and white", "Blue and gold", "Black and silver"],
		"kind": "symbol", "symbol": "01", "colors": ("#6d3ca8", "#79c267"),
	},
	{
		"anime": "Haikyuu!!", "prompt": "What sport do the Karasuno players love?",
		"answer": "Volleyball", "choices": ["Volleyball", "Basketball", "Tennis", "Baseball"],
		"kind": "symbol", "symbol": "●", "colors": ("#f28f3b", "#fff1c1"),
	},
	{
		"anime": "JoJo's Bizarre Adventure", "prompt": "Finish the battle cry: 'Oh, you're approaching me?'",
		"answer": "I can't beat you without getting closer.", "choices": ["I can't beat you without getting closer.", "You cannot escape destiny.", "The world is mine.", "Good grief, what a mess."],
		"kind": "line", "symbol": "★", "colors": ("#c44569", "#f8c291"),
	},
]


QUOTE_BANK = [
	("“I’m gonna be King of the Pirates!”", "Monkey D. Luffy", "One Piece", "normal",
	 ["Roronoa Zoro", "Marshall D. Teach", "Portgas D. Ace"]),
	("“Believe it!” — “Dattebayo!”", "Naruto Uzumaki", "Naruto", "normal",
	 ["Sasuke Uchiha", "Kakashi Hatake", "Jiraiya"]),
	("“I am Atomic.”", "Cid Kagenou", "The Eminence in Shadow", "normal",
	 ["Alexia Midgar", "Alpha", "Rose Oriana"]),
	("“Set your heart ablaze.”", "Kyojuro Rengoku", "Demon Slayer", "normal",
	 ["Tanjiro Kamado", "Giyu Tomioka", "Zenitsu Agatsuma"]),
	("“Omae wa mou shindeiru.”", "Kenshiro", "Fist of the North Star", "normal",
	 ["Raoh", "Jotaro Kujo", "Guts"]),
	("“It’s over 9000!”", "Vegeta", "Dragon Ball Z", "normal",
	 ["Goku", "Frieza", "Piccolo"]),
	("“Bankai.”", "A Soul Reaper", "Bleach", "normal",
	 ["A Hokage", "A Pirate Captain", "A Titan Shifter"]),
	("“Yare yare daze.”", "Jotaro Kujo", "JoJo's Bizarre Adventure", "normal",
	 ["Joseph Joestar", "Dio Brando", "Josuke Higashikata"]),

	("“Those who break the rules are scum, that's true. But those who abandon their friends are worse than scum.”",
	 "Kakashi Hatake", "Naruto", "medium",
	 ["Obito Uchiha", "Itachi Uchiha", "Might Guy"]),
	("“I never go back on my word. That's my ninja way!”", "Naruto Uzumaki", "Naruto", "medium",
	 ["Minato Namikaze", "Jiraiya", "Hashirama Senju"]),
	("“A lesson without pain is meaningless. That's because you can't gain something without sacrificing something in return.”",
	 "Edward Elric", "Fullmetal Alchemist: Brotherhood", "medium",
	 ["Roy Mustang", "Alphonse Elric", "Father"]),
	("“The world isn't perfect. But it's there for us, doing the best it can. And that's what makes it so damn beautiful.”",
	 "Roy Mustang", "Fullmetal Alchemist: Brotherhood", "medium",
	 ["Edward Elric", "Scar", "Maes Hughes"]),
	("“People die when they are killed.”", "Shirou Emiya", "Fate/stay night", "medium",
	 ["Archer", "Rin Tohsaka", "Gilgamesh"]),
	("“You have no enemies. No one has any enemies.”", "Thors", "Vinland Saga", "medium",
	 ["Thorfinn", "Askeladd", "Canute"]),
	("“Tatakae.”", "Eren Yeager", "Attack on Titan", "medium",
	 ["Reiner Braun", "Zeke Yeager", "Armin Arlert"]),
	("“Give up on your dreams and die.”", "Levi Ackerman", "Attack on Titan", "medium",
	 ["Erwin Smith", "Kenny Ackerman", "Eren Yeager"]),
	("“If we don't fight, we can't win. If we fight, we might lose. But if we don't fight, we have no chance of winning.”",
	 "Mikasa Ackerman", "Attack on Titan", "medium",
	 ["Historia Reiss", "Annie Leonhart", "Sasha Blouse"]),
	("“The world is cruel. But also very beautiful.”", "Mikasa Ackerman", "Attack on Titan", "medium",
	 ["Erwin Smith", "Hange Zoë", "Jean Kirstein"]),
	("“Wake up to reality! Nothing ever goes as planned in this accursed world.”",
	 "Madara Uchiha", "Naruto Shippuden", "medium",
	 ["Pain", "Obito Uchiha", "Hashirama Senju"]),
	("“How can you call yourself Hokage when you can't even save one friend?”",
	 "Sasuke Uchiha", "Naruto Shippuden", "medium",
	 ["Naruto Uzumaki", "Itachi Uchiha", "Tobirama Senju"]),
	("“The moment people come to know love, they run the risk of carrying hate.”",
	 "Obito Uchiha", "Naruto Shippuden", "medium",
	 ["Madara Uchiha", "Kakashi Hatake", "Pain"]),

	("“Those who cannot acknowledge themselves will eventually fail.”",
	 "Itachi Uchiha", "Naruto Shippuden", "deep",
	 ["Sasuke Uchiha", "Kisame Hoshigaki", "Obito Uchiha"]),
	("“The longer you live, the more you realize that reality is just made of pain, suffering and emptiness.”",
	 "Madara Uchiha", "Naruto Shippuden", "deep",
	 ["Nagato", "Obito Uchiha", "Orochimaru"]),
	("“A man's dream will never die!”", "Marshall D. Teach", "One Piece", "deep",
	 ["Monkey D. Luffy", "Portgas D. Ace", "Shanks"]),
	("“Nothing happened.”", "Roronoa Zoro", "One Piece", "deep",
	 ["Sanji", "Monkey D. Luffy", "Nico Robin"]),
	("“I want to live! Take me with you to the sea!”", "Nico Robin", "One Piece", "deep",
	 ["Nami", "Nefertari Vivi", "Franky"]),
	("“Thank you for loving me.”", "Portgas D. Ace", "One Piece", "deep",
	 ["Monkey D. Luffy", "Sabo", "Edward Newgate"]),
	("“He laughed.”", "Gol D. Roger", "One Piece", "deep",
	 ["Edward Newgate", "Shanks", "Silvers Rayleigh"]),
	("“I have no interest in ordinary humans.”", "Haruhi Suzumiya", "The Melancholy of Haruhi Suzumiya", "deep",
	 ["Kyon", "Mikuru Asahina", "Yuki Nagato"]),
	("“El Psy Kongroo.”", "Rintarou Okabe", "Steins;Gate", "deep",
	 ["Kurisu Makise", "Itaru Daru", "Mayuri Shiina"]),
	("“I'm mad scientist! It's so cool! Sonuvabitch!”", "Rintarou Okabe", "Steins;Gate", "deep",
	 ["Kurisu Makise", "Suzuha Amane", "Moeka Kiryu"]),
	("“The only ones who should kill are those prepared to be killed.”",
	 "Lelouch vi Britannia", "Code Geass", "deep",
	 ["Suzaku Kururugi", "Schneizel el Britannia", "C.C."]),
	("“If the king doesn't lead, how can he expect his subordinates to follow?”",
	 "Lelouch vi Britannia", "Code Geass", "deep",
	 ["Suzaku Kururugi", "Charles zi Britannia", "Jeremiah Gottwald"]),
	("“What do you mean by ‘people’?”", "Rei Ayanami", "Neon Genesis Evangelion", "deep",
	 ["Shinji Ikari", "Asuka Langley", "Gendo Ikari"]),
	("“I mustn't run away.”", "Shinji Ikari", "Neon Genesis Evangelion", "deep",
	 ["Misato Katsuragi", "Kaworu Nagisa", "Toji Suzuhara"]),
	("“Congratulations!”", "The entire cast", "Neon Genesis Evangelion", "deep",
	 ["Rei Ayanami", "Misato Katsuragi", "Gendo Ikari"]),
	("“Get in the robot, Shinji!”", "Misato Katsuragi", "Neon Genesis Evangelion", "deep",
	 ["Gendo Ikari", "Asuka Langley", "Ritsuko Akagi"]),
	("“Daga, kotowaru!”", "Rohan Kishibe", "JoJo's Bizarre Adventure", "deep",
	 ["Jotaro Kujo", "Josuke Higashikata", "Yoshikage Kira"]),
	("“I reject my humanity, JoJo!”", "Dio Brando", "JoJo's Bizarre Adventure", "deep",
	 ["Jonathan Joestar", "Speedwagon", "Enrico Pucci"]),
	("“WRYYYYYYYY!”", "Dio Brando", "JoJo's Bizarre Adventure", "deep",
	 ["Jonathan Joestar", "Kars", "Funny Valentine"]),
	("“You thought it was a normal attack, but it was me, Dio!”",
	 "Dio Brando", "JoJo's Bizarre Adventure", "deep",
	 ["Jonathan Joestar", "Noriaki Kakyoin", "Joseph Joestar"]),
	("“I am the bone of my sword. Steel is my body and fire is my blood. I have created over a thousand blades. Unknown to Death, nor known to Life. So as I pray, Unlimited Blade Works.”",
	 "Archer", "Fate/stay night", "deep",
	 ["Shirou Emiya", "Gilgamesh", "Kirei Kotomine"]),
	("“I am simply one hell of a butler.”", "Sebastian Michaelis", "Black Butler", "deep",
	 ["Ciel Phantomhive", "Grell Sutcliff", "Undertaker"]),
	("“Humans are so interesting.”", "Ryuk", "Death Note", "deep",
	 ["Light Yagami", "Rem", "Misa Amane"]),
	("“I am justice!”", "Light Yagami", "Death Note", "deep",
	 ["L", "Near", "Misa Amane"]),
	("“I am not a hero. I am just a guy who loves playing games.”", "Saitama", "One Punch Man", "deep",
	 ["Genos", "King", "Blast"]),

	("“I don't want to kill anyone. But if I must, I will.”", "Kenshin Himura", "Rurouni Kenshin", "vet",
	 ["Hajime Saito", "Sanosuke Sagara", "Makoto Shishio"]),
	("“The weak don't get to decide how they die.”", "Griffith", "Berserk", "vet",
	 ["Guts", "Casca", "Zodd"]),
	("“If you are always concerned about what others think of you, you'll never be stronger than you are now.”",
	 "Guts", "Berserk", "vet",
	 ["Griffith", "Puck", "Skull Knight"]),
	("“What do you think is the meaning of life?”", "Meruem", "Hunter x Hunter", "vet",
	 ["Isaac Netero", "Komugi", "Gon Freecss"]),
	("“Komugi… are you there?”", "Meruem", "Hunter x Hunter", "vet",
	 ["Isaac Netero", "Gon Freecss", "Killua Zoldyck"]),
	("“You should enjoy the little detours to the fullest.”", "Ging Freecss", "Hunter x Hunter", "vet",
	 ["Gon Freecss", "Killua Zoldyck", "Leorio Paradinight"]),
	("“When do you think people die? When they are shot through the heart by a bullet? No. When they are struck by an incurable disease? No. A man dies when he is forgotten!”",
	 "Dr. Hiriluk", "One Piece", "vet",
	 ["Dr. Kureha", "Tony Tony Chopper", "Wapol"]),

	("“This is the story of how I became the greatest hero.”", "Izuku Midoriya", "My Hero Academia", "boss",
	 ["All Might", "Katsuki Bakugo", "Stain"]),
	("“I am here!”", "All Might", "My Hero Academia", "boss",
	 ["Izuku Midoriya", "Sir Nighteye", "Gran Torino"]),
	("“Young Midoriya, you too can become a hero.”", "All Might", "My Hero Academia", "boss",
	 ["Izuku Midoriya", "Endeavor", "Shota Aizawa"]),
	("“Throughout heaven and earth, I alone am the honored one.”", "Satoru Gojo", "Jujutsu Kaisen", "boss",
	 ["Suguru Geto", "Kento Nanami", "Ryomen Sukuna"]),
	("“My soldiers, rage! My soldiers, scream! My soldiers, fight!”", "Erwin Smith", "Attack on Titan", "boss",
	 ["Levi Ackerman", "Hange Zoë", "Dot Pixis"]),
	("“Dedicate your heart!”", "The Survey Corps", "Attack on Titan", "boss",
	 ["The Military Police", "The Garrison", "The Marines"]),
	("“You are free.”", "Grisha Yeager", "Attack on Titan", "boss",
	 ["Eren Yeager", "Zeke Yeager", "Eren Kruger"]),

	("“Sometimes, you must hurt in order to know… life’s greatest lessons are learned through pain.”", "Pain", "Naruto Shippuden", "medium",
	 ["Jiraiya", "Obito Uchiha", "Madara Uchiha"]),
	("“There is no such thing as truth or lies in this world. There is only facts.”", "Aizen Sosuke", "Bleach", "medium",
	 ["Byakuya Kuchiki", "Grimmjow Jaegerjaquez", "Urahara Kisuke"]),
	("“Love and peace!”", "Vash the Stampede", "Trigun", "medium",
	 ["Nicholas D. Wolfwood", "Millions Knives", "Meryl Stryfe"]),
	("“Whatever happens, happens.”", "Spike Spiegel", "Cowboy Bebop", "medium",
	 ["Jet Black", "Faye Valentine", "Vicious"]),
	("“Who decided that?”", "Escanor", "The Seven Deadly Sins", "medium",
	 ["Meliodas", "Ban", "King"]),
	("“O kawaii koto.” (“How cute.”)", "Kaguya Shinomiya", "Kaguya-sama: Love Is War", "medium",
	 ["Chika Fujiwara", "Yu Ishigami", "Miko Iino"]),
	("“Surpass your limits. Right here, right now.”", "Yami Sukehiro", "Black Clover", "medium",
	 ["Asta", "Yuno", "Julius Novachrono"]),
	("“There is always only one truth.”", "Conan Edogawa", "Detective Conan", "medium",
	 ["Heiji Hattori", "Kaito Kid", "Ai Haibara"]),
	("“Zura janai, Katsura da!” (“It’s not Zura, it’s Katsura!”)", "Kotaro Katsura", "Gintama", "medium",
	 ["Gintoki Sakata", "Shinsuke Takasugi", "Sakamoto Tatsuma"]),
	("“I’m going to surpass you, Kakarot!”", "Vegeta", "Dragon Ball Z", "medium",
	 ["Son Goku", "Nappa", "Raditz"]),
	("“This isn’t even my final form.”", "Frieza", "Dragon Ball Z", "medium",
	 ["Cell", "Majin Buu", "King Cold"]),
	("“Your next line is…”", "Joseph Joestar", "JoJo's Bizarre Adventure", "medium",
	 ["Jotaro Kujo", "Caesar Zeppeli", "Lisa Lisa"]),
	("“I just want to live a quiet life.”", "Yoshikage Kira", "JoJo's Bizarre Adventure", "medium",
	 ["Josuke Higashikata", "Noriaki Kakyoin", "Jean Pierre Polnareff"]),
	("“I ask of you: are you my Master?”", "Saber", "Fate/stay night", "medium",
	 ["Archer", "Gilgamesh", "Lancer"]),
	("“Want to make a contract with me and become a magical girl?”", "Kyubey", "Puella Magi Madoka Magica", "medium",
	 ["Mami Tomoe", "Homura Akemi", "Sayaka Miki"]),
	("“Don’t worry. I am the strongest.”", "Satoru Gojo", "Jujutsu Kaisen", "medium",
	 ["Suguru Geto", "Kento Nanami", "Ryomen Sukuna"]),
	("“It’s a terrible day for rain.”", "Roy Mustang", "Fullmetal Alchemist: Brotherhood", "medium",
	 ["Edward Elric", "Alphonse Elric", "Maes Hughes"]),

	("“Aku Soku Zan.” (“Slay evil immediately.”)", "Saito Hajime", "Rurouni Kenshin", "deep",
	 ["Himura Kenshin", "Shishio Makoto", "Sanosuke Sagara"]),
	("“What did you just say about my hair?!”", "Josuke Higashikata", "JoJo's Bizarre Adventure", "deep",
	 ["Jotaro Kujo", "Okuyasu Nijimura", "Koichi Hirose"]),
	("“Arrivederci.”", "Bruno Bucciarati", "JoJo's Bizarre Adventure", "deep",
	 ["Giorno Giovanna", "Guido Mista", "Narancia Ghirga"]),
	("“Who the hell do you think I am?!”", "Kamina", "Tengen Toppa Gurren Lagann", "deep",
	 ["Simon", "Yoko Littner", "Rossiu Adai"]),
	("“Nico Nico Nii!”", "Nico Yazawa", "Love Live! School Idol Project", "deep",
	 ["Honoka Kosaka", "Rin Hoshizora", "Hanayo Koizumi"]),
	("“Nipah~!”", "Rika Furude", "Higurashi: When They Cry", "deep",
	 ["Keiichi Maebara", "Mion Sonozaki", "Hanyuu"]),
	("“Cheerio!”", "Togame", "Katanagatari", "deep",
	 ["Shichika Yasuri", "Hitei-hime", "Emonzaemon"]),
	("“I’m curious!” (Watashi, ki ni narimasu!)", "Chitanda Eru", "Hyouka", "deep",
	 ["Oreki Houtarou", "Fukube Satoshi", "Ibara Mayaka"]),
	("“Such misfortune!” (Fukou da!)", "Touma Kamijou", "A Certain Magical Index", "deep",
	 ["Accelerator", "Mikoto Misaka", "Index"]),
	("“Mada mada dane.” (“You still have lots more to work on.”)", "Echizen Ryoma", "The Prince of Tennis", "deep",
	 ["Tezuka Kunimitsu", "Fuji Syusuke", "Momoshiro Takeshi"]),
	("“Because I am a genius!”", "Hanamichi Sakuragi", "Slam Dunk", "deep",
	 ["Kaede Rukawa", "Takenori Akagi", "Ryota Miyagi"]),
	("“I can see the ending!”", "Keima Katsuragi", "The World God Only Knows", "deep",
	 ["Elsie", "Haqua", "Chihiro Kosaka"]),
	("“I don’t know everything. I just know what I know.”", "Tsubasa Hanekawa", "Monogatari Series", "deep",
	 ["Hitagi Senjougahara", "Koyomi Araragi", "Mayoi Hachikuji"]),

	("“If I tear open your chest, will I see it? If I crack open your skull, will I find it there?”", "Ulquiorra Cifer", "Bleach", "vet",
	 ["Grimmjow Jaegerjaquez", "Byakuya Kuchiki", "Orihime Inoue"]),
	("“The only thing all humans are equal in… is death.”", "Johan Liebert", "Monster", "vet",
	 ["Kenzo Tenma", "Nina Fortner", "Inspector Lunge"]),

	("“I, Giorno Giovanna, have a dream.”", "Giorno Giovanna", "JoJo's Bizarre Adventure", "boss",
	 ["Dio Brando", "Bruno Bucciarati", "Jotaro Kujo"]),
	("“ONE PIECE… does exist!”", "Whitebeard", "One Piece", "boss",
	 ["Gol D. Roger", "Monkey D. Luffy", "Shanks"]),
	("“I am the hope of the universe. I am the answer to all living things that cry out for peace. Ally to good… nightmare to you!”", "Son Goku", "Dragon Ball Z", "boss",
	 ["Vegeta", "Frieza", "Piccolo"]),
]


# (technique / move, character, anime, tier, [3 wrong characters])
TECH_BANK = [
	("Kamehameha", "Son Goku", "Dragon Ball", "normal",
	 ["Vegeta", "Piccolo", "Yamcha"]),
	("Shadow Clone Jutsu", "Naruto Uzumaki", "Naruto", "normal",
	 ["Sasuke Uchiha", "Kakashi Hatake", "Rock Lee"]),
	("Spirit Gun", "Yusuke Urameshi", "Yu Yu Hakusho", "normal",
	 ["Kazuma Kuwabara", "Hiei", "Kurama"]),
	("Arise", "Sung Jinwoo", "Solo Leveling", "normal",
	 ["Cha Hae-In", "Igris", "Baek Yoonho"]),
	("Transmutation Clap", "Edward Elric", "Fullmetal Alchemist: Brotherhood", "normal",
	 ["Roy Mustang", "Scar", "Alex Louis Armstrong"]),
	("Gear Second", "Monkey D. Luffy", "One Piece", "normal",
	 ["Roronoa Zoro", "Sanji", "Portgas D. Ace"]),

	("Spirit Bomb", "Son Goku", "Dragon Ball Z", "medium",
	 ["Vegeta", "Gohan", "Krillin"]),
	("Gear Fifth", "Monkey D. Luffy", "One Piece", "medium",
	 ["Roronoa Zoro", "Sanji", "Marshall D. Teach"]),
	("Ultra Instinct", "Son Goku", "Dragon Ball Super", "medium",
	 ["Vegeta", "Jiren", "Beerus"]),
	("Final Getsuga Tensho", "Ichigo Kurosaki", "Bleach", "medium",
	 ["Byakuya Kuchiki", "Kenpachi Zaraki", "Uryu Ishida"]),
	("Explosion", "Megumin", "KonoSuba", "medium",
	 ["Kazuma Satou", "Aqua", "Darkness"]),
	("Detroit Smash", "All Might", "My Hero Academia", "medium",
	 ["Izuku Midoriya", "Endeavor", "Shoto Todoroki"]),
	("Thunderclap and Flash", "Zenitsu Agatsuma", "Demon Slayer", "medium",
	 ["Tanjiro Kamado", "Inosuke Hashibira", "Kyojuro Rengoku"]),
	("Jajanken", "Gon Freecss", "Hunter x Hunter", "medium",
	 ["Killua Zoldyck", "Hisoka Morow", "Kurapika"]),
	("Demon-Slayer Sword", "Asta", "Black Clover", "medium",
	 ["Yuno", "Yami Sukehiro", "Noelle Silva"]),
	("Starburst Stream", "Kirito", "Sword Art Online", "medium",
	 ["Asuna Yuuki", "Heathcliff", "Eugeo"]),
	("Rasenshuriken", "Naruto Uzumaki", "Naruto Shippuden", "medium",
	 ["Sasuke Uchiha", "Minato Namikaze", "Jiraiya"]),
	("Full Counter", "Meliodas", "The Seven Deadly Sins", "medium",
	 ["Ban", "King", "Diane"]),

	("Kyoka Suigetsu's Complete Hypnosis", "Aizen Sosuke", "Bleach", "deep",
	 ["Byakuya Kuchiki", "Toshiro Hitsugaya", "Grimmjow Jaegerjaquez"]),
	("ZA WARUDO! (The World)", "Dio Brando", "JoJo's Bizarre Adventure", "deep",
	 ["Jotaro Kujo", "Josuke Higashikata", "Kars"]),
	("Unlimited Void", "Satoru Gojo", "Jujutsu Kaisen", "deep",
	 ["Ryomen Sukuna", "Suguru Geto", "Mahito"]),
	("Senbonzakura Kageyoshi", "Byakuya Kuchiki", "Bleach", "deep",
	 ["Renji Abarai", "Kenpachi Zaraki", "Rukia Kuchiki"]),
	("Zoltraak", "Frieren", "Frieren: Beyond Journey's End", "deep",
	 ["Fern", "Stark", "Himmel"]),
	("Berserker Armor", "Guts", "Berserk", "deep",
	 ["Griffith", "Casca", "Zodd Nosferatu"]),
	("Hinokami Kagura", "Tanjiro Kamado", "Demon Slayer", "deep",
	 ["Zenitsu Agatsuma", "Nezuko Kamado", "Giyu Tomioka"]),
	("Giga Drill Breaker", "Simon", "Tengen Toppa Gurren Lagann", "deep",
	 ["Kamina", "Viral", "Lordgenome"]),
	("ORA ORA ORA!", "Jotaro Kujo", "JoJo's Bizarre Adventure", "deep",
	 ["Dio Brando", "Josuke Higashikata", "Giorno Giovanna"]),
	("Moon Spiral Heart Attack", "Sailor Moon", "Sailor Moon", "deep",
	 ["Sailor Mars", "Sailor Mercury", "Tuxedo Mask"]),
	("Starlight Breaker", "Nanoha Takamachi", "Magical Girl Lyrical Nanoha", "deep",
	 ["Fate Testarossa", "Hayate Yagami", "Vita"]),
	("Dragon Slave", "Lina Inverse", "Slayers", "deep",
	 ["Gourry Gabriev", "Zelgadis Greywords", "Amelia Wil Tesla Saillune"]),
	("Burning Finger", "Domon Kasshu", "Mobile Fighter G Gundam", "deep",
	 ["Rain Mikamura", "Master Asia", "Schwarz Bruder"]),
	("Wind Scar (Kaze no Kizu)", "Inuyasha", "Inuyasha", "deep",
	 ["Sesshomaru", "Kagome Higurashi", "Miroku"]),
	("Steal", "Kazuma Satou", "KonoSuba", "deep",
	 ["Megumin", "Aqua", "Darkness"]),
	("Eight Inner Gates", "Might Guy", "Naruto Shippuden", "deep",
	 ["Kakashi Hatake", "Rock Lee", "Neji Hyuga"]),

	("Gate of Babylon", "Gilgamesh", "Fate/stay night", "vet",
	 ["Archer", "Saber", "Lancer"]),
	("Emperor Time", "Kurapika", "Hunter x Hunter", "vet",
	 ["Chrollo Lucilfer", "Hisoka Morow", "Feitan Portor"]),
	("Malevolent Shrine", "Ryomen Sukuna", "Jujutsu Kaisen", "vet",
	 ["Satoru Gojo", "Mahito", "Toji Fushiguro"]),
	("Bungee Gum", "Killua Zoldyck", "Hunter x Hunter", "vet",
	 ["Gon Freecss", "Hisoka Morow", "Meruem"]),
	("Final Flash", "Vegeta", "Dragon Ball Z", "vet",
	 ["Son Goku", "Cell", "Trunks"]),
	("Dragon of the Darkness Flame", "Hiei", "Yu Yu Hakusho", "vet",
	 ["Yusuke Urameshi", "Kurama", "Kazuma Kuwabara"]),

	("Serious Punch", "Saitama", "One Punch Man", "boss",
	 ["Genos", "Lord Boros", "Garou"]),
	("Made in Heaven", "Enrico Pucci", "JoJo's Bizarre Adventure", "boss",
	 ["Jolyne Cujoh", "Dio Brando", "Emporio Alnino"]),
	("Founding Titan", "Eren Yeager", "Attack on Titan", "boss",
	 ["Reiner Braun", "Zeke Yeager", "Erwin Smith"]),
	("United States of Smash", "All Might", "My Hero Academia", "boss",
	 ["Izuku Midoriya", "Endeavor", "All For One"]),
]


# (clue, answer series, tier, [3 wrong series])
ANIME_BANK = [
	("Bankai — the second release of a zanpakuto", "Bleach", "normal",
	 ["Naruto", "Inuyasha", "Yu Yu Hakusho"]),
	("Devil Fruits that grant powers but steal your ability to swim", "One Piece", "normal",
	 ["Naruto", "My Hero Academia", "Fairy Tail"]),
	("Chakra, hand signs, and hidden ninja villages", "Naruto", "normal",
	 ["One Piece", "Bleach", "Black Clover"]),
	("Man-eating Titans behind towering walls", "Attack on Titan", "normal",
	 ["Chainsaw Man", "Tokyo Ghoul", "Vinland Saga"]),
	("Breathing Styles that turn swordsmanship into elemental art", "Demon Slayer", "normal",
	 ["Jujutsu Kaisen", "Bleach", "Rurouni Kenshin"]),
	("The Heart of the Cards", "Yu-Gi-Oh!", "normal",
	 ["Pokémon", "Digimon", "One Piece"]),
	("Poké Balls and a trainer who wants to catch 'em all", "Pokémon", "normal",
	 ["Digimon", "Yu-Gi-Oh!", "One Piece"]),
	("PLUS ULTRA!", "My Hero Academia", "normal",
	 ["One Punch Man", "Black Clover", "Haikyuu!!"]),

	("Domain Expansions fueled by cursed energy", "Jujutsu Kaisen", "medium",
	 ["Demon Slayer", "Chainsaw Man", "Bleach"]),
	("Nen categories like Transmuter, Emitter, and Specialist", "Hunter x Hunter", "medium",
	 ["Naruto Shippuden", "Jujutsu Kaisen", "One Piece"]),
	("Haki — Conqueror's, Armament, or Observation", "One Piece", "medium",
	 ["Naruto", "Bleach", "Fairy Tail"]),
	("Equivalent Exchange alchemy", "Fullmetal Alchemist", "medium",
	 ["Black Clover", "Re:Zero", "The Seven Deadly Sins"]),
	("Stands named after rock bands and tarot arcana", "JoJo's Bizarre Adventure", "medium",
	 ["Hunter x Hunter", "Jujutsu Kaisen", "Chainsaw Man"]),
	("An episode-ending sign-off: 'See you, space cowboy…'", "Cowboy Bebop", "medium",
	 ["Trigun", "Monster", "Gintama"]),
	("Kagune — predatory organs made of Rc cells", "Tokyo Ghoul", "medium",
	 ["Chainsaw Man", "Attack on Titan", "Jujutsu Kaisen"]),
	("Return by Death", "Re:Zero", "medium",
	 ["Steins;Gate", "That Time I Got Reincarnated as a Slime", "The Eminence in Shadow"]),
	("Geass — a power of absolute obedience granted by eye contact", "Code Geass", "medium",
	 ["Death Note", "Monster", "Psycho-Pass"]),
	("Reading Steiner — keeping memories across worldlines", "Steins;Gate", "medium",
	 ["Re:Zero", "Monogatari Series", "Serial Experiments Lain"]),
	("Foodgasms after nearly every dish", "Food Wars!", "medium",
	 ["Dr. Stone", "Spy × Family", "Kaguya-sama: Love Is War"]),
	("Guild marks stamped onto members' skin", "Fairy Tail", "medium",
	 ["One Piece", "Black Clover", "The Seven Deadly Sins"]),
	("Grimoires wielded by squads of magic knights", "Black Clover", "medium",
	 ["Fairy Tail", "Re:Zero", "Magical Girl Lyrical Nanoha"]),
	("The Akatsuki hunting tailed beasts", "Naruto Shippuden", "medium",
	 ["Bleach", "Hunter x Hunter", "One Piece"]),
	("Hero rankings kept by a Hero Association hotline", "One Punch Man", "medium",
	 ["My Hero Academia", "Jujutsu Kaisen", "Dr. Stone"]),

	("A.T. Fields — absolute terror barriers around bio-machines", "Neon Genesis Evangelion", "deep",
	 ["Mobile Suit Gundam", "Tengen Toppa Gurren Lagann", "Mobile Fighter G Gundam"]),
	("Newtypes sensing each other across the void of space", "Mobile Suit Gundam", "deep",
	 ["Neon Genesis Evangelion", "Code Geass", "Cowboy Bebop"]),
	("Behelits that summon the God Hand's apostles", "Berserk", "deep",
	 ["Chainsaw Man", "Made in Abyss", "Tokyo Ghoul"]),
	("Life Fibers woven into sentient clothing", "Kill la Kill", "deep",
	 ["Black Clover", "My Hero Academia", "One Punch Man"]),
	("Soul Gems that cloud into Grief Seeds", "Puella Magi Madoka Magica", "deep",
	 ["Sailor Moon", "Magical Girl Lyrical Nanoha", "Fairy Tail"]),
	("Dominators that read a target's Crime Coefficient", "Psycho-Pass", "deep",
	 ["Death Note", "Monster", "Detective Conan"]),
	("Counting down from 1,000 minus 7 to stay sane", "Tokyo Ghoul", "deep",
	 ["Attack on Titan", "Chainsaw Man", "Monster"]),
	("Exodia the Forbidden One ending duels instantly", "Yu-Gi-Oh!", "deep",
	 ["Pokémon", "Digimon", "One Piece"]),
	("'Present day. Present time. Hahaha.'", "Serial Experiments Lain", "deep",
	 ["Steins;Gate", "Psycho-Pass", "Monster"]),
	("A curse born at the bottom of a pit six layers deep", "Made in Abyss", "deep",
	 ["Dr. Stone", "Frieren: Beyond Journey's End", "KonoSuba"]),
	("Zanpakuto spirits met inside an inner world", "Bleach", "deep",
	 ["Demon Slayer", "Inuyasha", "Rurouni Kenshin"]),
	("Devil contracts paid for with body parts", "Chainsaw Man", "deep",
	 ["Jujutsu Kaisen", "Tokyo Ghoul", "Berserk"]),

	("Unlimited Blade Works — 'I am the bone of my sword…'", "Fate/stay night", "boss",
	 ["Bleach", "Rurouni Kenshin", "Demon Slayer"]),
]


QUESTION_HEADERS = {
	"line": "WHO SAYS IT?",
	"tech": "NAME THAT MOVE",
	"anime": "NAME THAT SERIES",
}


def _expand_quotes():
	for text, speaker, anime, tier, distractors in QUOTE_BANK:
		symbol, c1, c2 = STYLES[anime]
		QUESTIONS.append({
			"anime": anime, "prompt": text, "answer": speaker,
			"choices": [speaker] + list(distractors[:3]),
			"kind": "line", "symbol": symbol, "colors": (c1, c2), "tier": tier,
		})


_expand_quotes()


def _expand_techs():
	for move, who, anime, tier, distractors in TECH_BANK:
		symbol, c1, c2 = STYLES[anime]
		QUESTIONS.append({
			"anime": anime, "prompt": f"Which character unleashes \u201c{move}\u201d?",
			"answer": who, "choices": [who] + list(distractors[:3]),
			"kind": "tech", "symbol": symbol, "colors": (c1, c2), "tier": tier,
		})


_expand_techs()


def _expand_animes():
	for clue, anime, tier, distractors in ANIME_BANK:
		symbol, c1, c2 = STYLES[anime]
		QUESTIONS.append({
			"anime": anime, "prompt": f"Which series features {clue}?",
			"answer": anime, "choices": [anime] + list(distractors[:3]),
			"kind": "anime", "symbol": symbol, "colors": (c1, c2), "tier": tier,
		})


_expand_animes()
for entry in QUESTIONS:
	entry.setdefault("tier", "normal")


def shade(color, factor):
	color = color.lstrip("#")
	r, g, b = (int(color[i:i + 2], 16) for i in (0, 2, 4))
	rgb = tuple(max(0, min(255, int(c * factor))) for c in (r, g, b))
	return "#{:02x}{:02x}{:02x}".format(*rgb)


class AnimeWheel:
	def __init__(self, root):
		self.root = root
		self.root.title("ANIME WHEEL")
		self.root.geometry("1160x780")
		self.root.minsize(1000, 700)
		self.root.configure(bg=BG)
		self.rounds = 10
		self.team_count = 2
		self.teams = DEFAULT_TEAMS[:2]
		self.scores = {}
		self.current_team = 0
		self.round_number = 0
		self.question = None
		self.deck = []
		self.phase = "idle"
		self.selected = None
		self.art_text = ""
		self.show_setup()

	def clear(self):
		for child in self.root.winfo_children():
			child.destroy()
		for seq in ("<Return>", "1", "2", "3", "4"):
			try:
				self.root.unbind(seq)
			except KeyError:
				pass

	def label(self, parent, text, size=12, color=INK, **kwargs):
		return tk.Label(parent, text=text, bg=kwargs.pop("bg", parent.cget("bg")), fg=color,
						font=("Segoe UI", size, kwargs.pop("weight", "normal")), **kwargs)

	def button(self, parent, text, command, bg, fg, size=12, **kwargs):
		return tk.Button(parent, text=text, command=command, bg=bg, fg=fg,
						 disabledforeground=fg, activebackground=shade(bg, .82),
						 activeforeground=fg, relief="flat", bd=0, cursor="hand2",
						 font=("Segoe UI", size, "bold"),
						 padx=kwargs.pop("padx", 18), pady=kwargs.pop("pady", 10), **kwargs)

	def hover(self, btn, normal_bg, hover_bg):
		btn.bind("<Enter>", lambda e: btn.configure(bg=hover_bg) if str(btn.cget("state")) == "normal" else None)
		btn.bind("<Leave>", lambda e: btn.configure(bg=normal_bg))

	def show_setup(self):
		self.clear()
		self.phase = "setup"
		wrap = tk.Frame(self.root, bg=BG)
		wrap.pack(fill="both", expand=True, padx=70, pady=40)
		self.label(wrap, "ANIME WHEEL", 44, CORAL, weight="bold").pack(anchor="w")
		self.label(wrap, f"SPIN  •  GUESS  •  SCORE      {len(QUESTIONS)} CHALLENGES ACROSS {len(STYLES)} SHOWS",
				   13, GOLD, weight="bold").pack(anchor="w", pady=(2, 26))

		card = tk.Frame(wrap, bg=PANEL, padx=32, pady=26, highlightbackground=BORDER, highlightthickness=1)
		card.pack(fill="x")

		left = tk.Frame(card, bg=PANEL)
		left.pack(side="left", fill="both", expand=True, padx=(0, 44))

		self.label(left, "TEAMS", 13, MINT, weight="bold").pack(anchor="w")
		count_row = tk.Frame(left, bg=PANEL)
		count_row.pack(anchor="w", pady=(10, 16))
		self.label(count_row, "How many teams?", 13, INK).pack(side="left", padx=(0, 16))
		self.count_buttons = []
		for count in (2, 3, 4):
			btn = self.button(count_row, str(count), lambda c=count: self.set_team_count(c),
							  bg=PANEL_LIGHT, fg=INK, size=12, width=3, pady=6)
			btn.pack(side="left", padx=(0, 8))
			self.count_buttons.append(btn)
		self.style_count_buttons()

		self.label(left, "Team names", 13, INK).pack(anchor="w", pady=(4, 8))
		self.rows_frame = tk.Frame(left, bg=PANEL)
		self.rows_frame.pack(anchor="w")
		self.entries = []
		self.build_team_rows()

		right = tk.Frame(card, bg=PANEL, width=270)
		right.pack(side="right", fill="y")
		right.pack_propagate(False)
		self.label(right, "ROUNDS", 13, MINT, weight="bold").pack(anchor="w")
		stepper = tk.Frame(right, bg=PANEL)
		stepper.pack(anchor="w", pady=(10, 0))
		minus = self.button(stepper, "−", lambda: self.step_rounds(-1), bg=PANEL_LIGHT, fg=INK, size=15, width=3, pady=8)
		minus.pack(side="left")
		self.rounds_value = self.label(stepper, str(self.rounds), 22, GOLD, bg=PANEL_LIGHT, weight="bold", width=4)
		self.rounds_value.pack(side="left", padx=8, ipady=5)
		plus = self.button(stepper, "+", lambda: self.step_rounds(1), bg=PANEL_LIGHT, fg=INK, size=15, width=3, pady=8)
		plus.pack(side="left")
		self.label(right, f"{MIN_ROUNDS} to {MAX_ROUNDS} rounds", 10, MUTED).pack(anchor="w", pady=(8, 0))

		tiers_box = tk.Frame(right, bg=PANEL)
		tiers_box.pack(anchor="w", pady=(18, 0))
		self.label(tiers_box, "POINTS BY TIER", 11, MINT, weight="bold").pack(anchor="w")
		for key in ("normal", "medium", "deep", "vet", "boss"):
			name, color, pts = TIERS[key]
			row = tk.Frame(tiers_box, bg=PANEL)
			row.pack(anchor="w", pady=1)
			self.label(row, f"{name}", 10, color, weight="bold").pack(side="left")
			self.label(row, f"   +{pts}", 10, MUTED).pack(side="left")

		start = self.button(right, "START GAME  →", self.start_game, bg=CORAL, fg="white", size=14, pady=14)
		start.pack(side="bottom", fill="x")
		self.hover(start, CORAL, shade(CORAL, .82))

		self.error = self.label(wrap, "", 12, CORAL, weight="bold")
		self.error.pack(anchor="w", pady=(12, 0))

	def style_count_buttons(self):
		for count, btn in zip((2, 3, 4), self.count_buttons):
			active = count == self.team_count
			btn.configure(bg=CORAL if active else PANEL_LIGHT, fg="white" if active else MUTED)

	def build_team_rows(self):
		for child in self.rows_frame.winfo_children():
			child.destroy()
		self.entries = []
		for index in range(self.team_count):
			row = tk.Frame(self.rows_frame, bg=PANEL)
			row.pack(anchor="w", pady=3)
			dot = tk.Canvas(row, width=12, height=12, bg=PANEL, highlightthickness=0)
			dot.pack(side="left", padx=(0, 10))
			dot.create_oval(1, 1, 11, 11, fill=TEAM_COLORS[index], outline="")
			entry = tk.Entry(row, width=18, bg=PANEL_LIGHT, fg=INK, insertbackground=INK,
							 relief="flat", font=("Segoe UI", 12), justify="center")
			entry.insert(0, DEFAULT_TEAMS[index])
			entry.pack(side="left", ipady=5)
			self.entries.append(entry)

	def set_team_count(self, count):
		self.team_count = count
		self.style_count_buttons()
		self.build_team_rows()

	def step_rounds(self, direction):
		self.rounds = max(MIN_ROUNDS, min(MAX_ROUNDS, self.rounds + direction))
		self.rounds_value.configure(text=str(self.rounds))

	def start_game(self):
		names = []
		for index, entry in enumerate(self.entries):
			name = entry.get().strip().upper()
			if not name:
				self.error.configure(text=f"Team {index + 1} needs a name!")
				return
			if name in names:
				self.error.configure(text=f"'{name}' is used more than once — give every team its own name.")
				return
			names.append(name)
		self.error.configure(text="")
		self.teams = names
		self.scores = {name: 0 for name in self.teams}
		self.current_team = 0
		self.round_number = 0
		self.deck = []
		self.show_game()

	def show_game(self):
		self.clear()
		header = tk.Frame(self.root, bg=BG)
		header.pack(fill="x", padx=36, pady=(22, 8))
		self.label(header, "ANIME WHEEL", 22, CORAL, weight="bold").pack(side="left")
		self.status = self.label(header, "", 12, GOLD, weight="bold")
		self.status.pack(side="right")
		tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x", padx=36)

		self.score_frame = tk.Frame(self.root, bg=BG)
		self.score_frame.pack(fill="x", padx=36, pady=(12, 14))
		self.render_scores()

		body = tk.Frame(self.root, bg=BG)
		body.pack(fill="both", expand=True, padx=36, pady=(0, 26))
		left = tk.Frame(body, bg=PANEL, width=420, highlightbackground=BORDER, highlightthickness=1)
		left.pack(side="left", fill="both", expand=True, padx=(0, 22))
		left.pack_propagate(False)
		self.art = tk.Canvas(left, bg=PANEL, highlightthickness=0)
		self.art.pack(fill="both", expand=True, padx=14, pady=14)
		self.art.bind("<Button-1>", self.reveal_answer)
		self.art.bind("<Configure>", lambda e: self.draw_art())

		right = tk.Frame(body, bg=BG, width=540)
		right.pack(side="right", fill="both")
		right.pack_propagate(False)
		self.tier_chip = self.label(right, "", 11, GOLD, weight="bold")
		self.tier_chip.pack(anchor="w", pady=(0, 4))
		self.prompt = self.label(right, "", 15, INK, weight="bold", wraplength=520, justify="left")
		self.prompt.pack(anchor="w", pady=(0, 6))
		self.subtitle = self.label(right, "", 12, MUTED, justify="left")
		self.subtitle.pack(anchor="w", pady=(0, 14))
		self.choices_frame = tk.Frame(right, bg=BG)
		self.choices_frame.pack(fill="x")
		self.feedback = self.label(right, "", 12, MUTED, wraplength=520, justify="left", height=2)
		self.feedback.pack(anchor="w", pady=(12, 6))
		self.action_button = self.button(right, "SPINNING...", self.on_action, bg=BORDER, fg=MUTED, size=13, pady=12)
		self.action_button.pack(anchor="w", fill="x", pady=(4, 0))

		self.root.bind("<Return>", lambda e: self.on_action())
		for key in "1234":
			self.root.bind(key, lambda e, i=int(key) - 1: self.pick_index(i))
		self.next_round()

	def pick_index(self, index):
		if self.phase == "pick" and index < len(self.choice_values):
			self.choose(self.choice_values[index])

	def render_scores(self):
		for child in self.score_frame.winfo_children():
			child.destroy()
		for index, team in enumerate(self.teams):
			active = index == self.current_team
			item = tk.Frame(self.score_frame, bg=PANEL, padx=16, pady=9,
							highlightbackground=CORAL if active else BORDER,
							highlightthickness=2 if active else 1)
			item.pack(side="left", fill="x", expand=True, padx=(0 if index == 0 else 10, 0))
			dot = tk.Canvas(item, width=10, height=10, bg=PANEL, highlightthickness=0)
			dot.pack(side="left")
			dot.create_oval(1, 1, 9, 9, fill=TEAM_COLORS[index], outline="")
			self.label(item, team, 11, INK if active else MUTED, weight="bold").pack(side="left", padx=(9, 0))
			self.label(item, str(self.scores[team]), 17, TEAM_COLORS[index] if active else MUTED, weight="bold").pack(side="right")

	def draw_question(self):
		if not self.deck:
			self.deck = QUESTIONS[:]
			random.shuffle(self.deck)
		return self.deck.pop()

	def next_round(self):
		if self.round_number >= self.rounds:
			self.show_winner()
			return
		self.round_number += 1
		self.question = self.draw_question()
		self.phase = "spin"
		self.selected = None
		name, _, _ = TIERS[self.question["tier"]]
		self.status.configure(text=f"ROUND {self.round_number:02d} / {self.rounds}   •   {self.teams[self.current_team]}")
		self.tier_chip.configure(text="", fg=GOLD)
		self.prompt.configure(text="Spinning the wheel...")
		self.subtitle.configure(text="")
		self.feedback.configure(text="", fg=MUTED)
		for child in self.choices_frame.winfo_children():
			child.destroy()
		self.set_action("SPINNING...", False)
		self.spin_steps = 0
		self.animate_spin()

	def animate_spin(self):
		if self.spin_steps < 14:
			flash = random.choice(QUESTIONS)
			self.art_text = flash["symbol"]
			self.flash_colors = flash["colors"]
			self.draw_art()
			self.spin_steps += 1
			self.root.after(70 + self.spin_steps * 9, self.animate_spin)
			return
		self.start_question()

	def start_question(self):
		self.phase = "pick"
		question = self.question
		tier_name, tier_color, pts = TIERS[question["tier"]]
		if question["kind"] == "anime":
			self.art_text = "?"
			self.flash_colors = ("#2b2b3d", "#8f97b5")
			self.draw_art()
		else:
			self.art_text = question["symbol"]
			self.draw_art()
		self.tier_chip.configure(text=f"{tier_name}  •  +{pts} POINT{'S' if pts != 1 else ''}", fg=tier_color)
		header = QUESTION_HEADERS.get(question["kind"], "SYMBOL ROUND")
		self.prompt.configure(text=f"{header}\n{question['prompt']}")
		if question["kind"] in ("line", "character"):
			self.subtitle.configure(text=f"🎬  {question['anime']}")
		choices = question["choices"][:]
		random.shuffle(choices)
		self.choice_values = choices
		self.choice_buttons = []
		for index, choice in enumerate(choices):
			btn = self.button(self.choices_frame, f"  {chr(65 + index)}    {choice}",
							  lambda value=choice: self.choose(value),
							  bg=PANEL_LIGHT, fg=INK, size=11, pady=11, anchor="w", justify="left")
			btn.pack(fill="x", pady=4)
			self.hover(btn, PANEL_LIGHT, HOVER)
			self.choice_buttons.append(btn)
		self.feedback.configure(text="Pick an answer, then reveal.", fg=MUTED)
		self.set_action("REVEAL ANSWER", False)

	def choose(self, choice):
		if self.phase != "pick":
			return
		self.selected = choice
		for btn, value in zip(self.choice_buttons, self.choice_values):
			picked = value == choice
			btn.configure(bg=GOLD if picked else PANEL_LIGHT, fg=DARK_INK if picked else INK)
		self.feedback.configure(text=f"Locked in: {choice}", fg=GOLD)
		self.set_action("REVEAL ANSWER", True)

	def set_action(self, text, enabled):
		self.action_button.configure(
			text=text, state="normal" if enabled else "disabled",
			bg=GOLD if enabled else BORDER, fg=DARK_INK if enabled else MUTED,
			disabledforeground=MUTED, activebackground=shade(GOLD, .82) if enabled else BORDER)

	def on_action(self):
		if self.phase == "pick" and self.selected is not None:
			self.reveal_answer()
		elif self.phase == "revealed":
			self.next_round()

	def reveal_answer(self, _event=None):
		if self.phase != "pick" or self.selected is None:
			return
		self.phase = "revealed"
		answer = self.question["answer"]
		correct = self.selected == answer
		for btn, value in zip(self.choice_buttons, self.choice_values):
			if value == answer:
				btn.configure(bg=MINT, fg=DARK_INK, state="disabled", disabledforeground=DARK_INK)
			elif value == self.selected:
				btn.configure(bg=CORAL, fg="white", state="disabled", disabledforeground="white")
			else:
				btn.configure(bg=PANEL, fg=MUTED, state="disabled", disabledforeground=MUTED)
		team = self.teams[self.current_team]
		_, _, pts = TIERS[self.question["tier"]]
		if correct:
			self.scores[team] += pts
			self.feedback.configure(text=f"CORRECT!  +{pts} point{'s' if pts != 1 else ''} for {team}", fg=MINT)
		else:
			self.feedback.configure(text=f"Not quite — the answer is: {answer}", fg=CORAL)
		self.draw_art()
		self.set_action("NEXT ROUND  →", True)
		self.render_scores()
		self.current_team = (self.current_team + 1) % len(self.teams)
		self.render_scores()

	def draw_art(self):
		if not hasattr(self, "art"):
			return
		canvas = self.art
		canvas.delete("all")
		width = max(canvas.winfo_width(), 320)
		height = max(canvas.winfo_height(), 300)
		if self.phase == "spin":
			colors = getattr(self, "flash_colors", (CORAL, GOLD))
		elif self.question and self.question["kind"] == "anime" and self.phase != "revealed":
			colors = ("#2b2b3d", "#8f97b5")
		elif self.question:
			colors = self.question["colors"]
		else:
			colors = (CORAL, GOLD)
		c1, c2 = colors
		for offset in range(-height, width, 42):
			canvas.create_line(offset, 0, offset + height, height, fill=shade(c1, .45), width=2, stipple="gray25")

		if self.phase == "spin":
			size = min(width, height)
			cx, cy = width / 2, height / 2
			r = size * .42
			pulse = .34 if self.spin_steps % 2 == 0 else .37
			canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=shade(c1, .55), outline=c2, width=4)
			canvas.create_oval(cx - r * pulse, cy - r * pulse, cx + r * pulse, cy + r * pulse,
							   fill=PANEL, outline=shade(c2, .75), width=2)
			canvas.create_text(cx, cy, text=self.art_text, fill=c2,
							   font=("Segoe UI Symbol", max(24, int(size * .22)), "bold"))
			return

		mode = "emblem" if self.question and self.question["kind"] in ("symbol", "anime") else "avatar"
		correct = self.phase == "revealed" and self.selected == self.question["answer"]
		wrong = self.phase == "revealed" and not correct
		ring = MINT if correct else CORAL if wrong else None
		if mode == "emblem":
			self._draw_emblem(canvas, width, height, c1, c2)
		else:
			self._draw_avatar(canvas, width, height, c1, c2)
		if ring:
			size = min(width, height)
			cx, cy = width / 2, height / 2
			r = size * .47
			canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline=ring, width=4)
		if self.phase == "pick":
			canvas.create_text(width - 14, height - 14, text="CLICK TO REVEAL", anchor="se",
							   fill=MUTED, font=("Segoe UI", 9, "bold"))

	def _draw_emblem(self, canvas, width, height, c1, c2):
		size = min(width, height)
		cx, cy = width / 2, height / 2
		outer = size * .44
		canvas.create_oval(cx - outer, cy - outer, cx + outer, cy + outer,
						   fill=shade(c1, .55), outline=c2, width=3)
		import math
		for i in range(24):
			angle = math.radians(i * 15)
			x1 = cx + math.cos(angle) * outer * .92
			y1 = cy + math.sin(angle) * outer * .92
			x2 = cx + math.cos(angle) * outer
			y2 = cy + math.sin(angle) * outer
			canvas.create_line(x1, y1, x2, y2, fill=c2, width=2)
		mid = outer * .78
		canvas.create_oval(cx - mid, cy - mid, cx + mid, cy + mid, fill=PANEL, outline=shade(c2, .7), width=2)
		for i in range(4):
			angle = math.radians(45 + i * 90)
			dx = cx + math.cos(angle) * (outer + 14)
			dy = cy + math.sin(angle) * (outer + 14)
			d = 7
			canvas.create_polygon(dx, dy - d, dx + d, dy, dx, dy + d, dx - d, dy,
								  fill=c2, outline="")
		canvas.create_text(cx, cy, text=self.art_text, fill=c2,
						   font=("Segoe UI Symbol", max(28, int(mid * .95)), "bold"))
		if self.phase == "pick":
			caption = "MYSTERY SERIES — NO HINTS HIDDEN IN THE ART!" \
				if self.question and self.question["kind"] == "anime" \
				else "WHAT DOES THIS EMBLEM BELONG TO?"
			canvas.create_text(cx, cy + mid + 24, text=caption,
							   fill=MUTED, font=("Segoe UI", 9, "bold"))

	def _draw_avatar(self, canvas, width, height, c1, c2):
		import math
		u = min(width, height)
		cx = width / 2
		head_cy = height / 2 - u * .14
		hrx, hry = u * .155, u * .175
		figure = shade(c1, .34)
		shoulder_top = head_cy + hry * 1.15
		canvas.create_arc(cx - u * .40, shoulder_top - u * .04, cx + u * .40, shoulder_top + u * .52,
						  start=0, extent=180, style="chord", fill=figure, outline=c2, width=3)
		canvas.create_rectangle(cx - u * .07, head_cy + hry * .55, cx + u * .07, shoulder_top + u * .08,
								fill=figure, outline="")
		canvas.create_oval(cx - hrx, head_cy - hry, cx + hrx, head_cy + hry,
						   fill=figure, outline=c2, width=3)

		seed_text = (self.question["anime"] + self.question["answer"]) if self.question else "wheel"
		rng = random.Random(seed_text)
		spikes = rng.randint(5, 9)
		base_len = rng.uniform(.10, .16)
		for i in range(spikes):
			frac = (i + .5) / spikes
			angle = math.radians(200 - frac * 220)
			ax = cx + math.cos(angle) * hrx * .96
			ay = head_cy + math.sin(angle) * hry * .96
			tip_r = hrx + u * (base_len + rng.uniform(0, .07))
			tx = cx + math.cos(angle) * tip_r
			ty = head_cy + math.sin(angle) * tip_r * 1.15
			left = angle - math.radians(90 / spikes)
			right = angle + math.radians(90 / spikes)
			lx = cx + math.cos(left) * hrx * .9
			ly = head_cy + math.sin(left) * hry * .9
			rx = cx + math.cos(right) * hrx * .9
			ry = head_cy + math.sin(right) * hry * .9
			canvas.create_polygon(ax, ay, tx, ty, rx, ry, fill=figure, outline="")
			canvas.create_polygon(ax, ay, lx, ly, tx, ty, fill=figure, outline="")

		eye_dx = hrx * rng.uniform(.38, .5)
		eye_dy = head_cy - hry * rng.uniform(.05, .25)
		eye_w, eye_h = u * .022, u * .009
		eye_color = c2 if self.phase != "revealed" else (MINT if self.selected == self.question["answer"] else CORAL)
		for sign in (-1, 1):
			canvas.create_oval(cx + sign * eye_dx - eye_w, eye_dy - eye_h,
							   cx + sign * eye_dx + eye_w, eye_dy + eye_h,
							   fill=eye_color, outline="")
		badge_x, badge_y, badge_r = cx + u * .27, shoulder_top + u * .22, u * .055
		canvas.create_oval(badge_x - badge_r, badge_y - badge_r, badge_x + badge_r, badge_y + badge_r,
						   fill=PANEL, outline=c2, width=2)
		glyph = self.art_text if self.question else "?"
		canvas.create_text(badge_x, badge_y, text=glyph, fill=c2,
						   font=("Segoe UI Symbol", max(10, int(badge_r * 1.15)), "bold"))

		if self.phase == "pick":
			canvas.create_text(width - 18, 22, text="?", anchor="ne", fill=c2, stipple="gray25",
							   font=("Segoe UI", int(u * .3), "bold"))
			canvas.create_text(18, height - 40, text="MYSTERY SPEAKER", anchor="sw",
							   fill=MUTED, font=("Segoe UI", 9, "bold"))
		elif self.phase == "revealed":
			label = self.question["answer"]
			canvas.create_text(cx, height - 26, text=label.upper(), fill=c2,
							   font=("Segoe UI", 12, "bold"))

	def show_winner(self):
		self.clear()
		self.phase = "done"
		top = max(self.scores.values())
		winners = [team for team, score in self.scores.items() if score == top]
		if len(winners) > 1:
			title, subtitle = "IT'S A TIE!", "  vs  ".join(winners) + " share the crown!"
		else:
			title, subtitle = winners[0], f"wins with {top} point{'s' if top != 1 else ''}!"
		wrap = tk.Frame(self.root, bg=BG)
		wrap.pack(fill="both", expand=True, padx=90, pady=60)
		self.label(wrap, "FINAL SCORE", 15, GOLD, weight="bold").pack(anchor="w")
		self.label(wrap, title, 42, CORAL, weight="bold").pack(anchor="w", pady=(8, 0))
		self.label(wrap, subtitle, 20, INK).pack(anchor="w")
		board = tk.Frame(wrap, bg=PANEL, padx=26, pady=16, highlightbackground=BORDER, highlightthickness=1)
		board.pack(fill="x", pady=26)
		for rank, (team, score) in enumerate(sorted(self.scores.items(), key=lambda kv: kv[1], reverse=True), 1):
			row = tk.Frame(board, bg=PANEL)
			row.pack(fill="x", pady=4)
			self.label(row, f"{rank}.   {team}", 13, INK if score == top else MUTED, weight="bold").pack(side="left")
			self.label(row, str(score), 16, MINT, weight="bold").pack(side="right")
		again = self.button(wrap, "PLAY AGAIN", self.show_setup, bg=CORAL, fg="white", size=13, pady=13)
		again.pack(anchor="w", pady=(8, 0))
		self.hover(again, CORAL, shade(CORAL, .82))


if __name__ == "__main__":
	root = tk.Tk()
	AnimeWheel(root)
	root.mainloop()
