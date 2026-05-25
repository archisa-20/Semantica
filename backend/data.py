# data.py — Semantica Movie Database
# 200+ movies with rich descriptions, themes, and mood tags
# Themes + mood are used to build richer embeddings for more accurate semantic search

movies = [

    # ── ACTION / THRILLER ──────────────────────────────────────────────
    {
        "title": "The Dark Knight",
        "description": "Batman faces the Joker, a psychopathic criminal who wants to unleash chaos and anarchy upon Gotham City. A battle of ideals between order and chaos, the film examines what it takes to be a hero when morality is put to its ultimate test.",
        "genre": "Action/Thriller", "year": 2008,
        "themes": ["chaos vs order", "morality", "heroism", "sacrifice", "duality", "justice"],
        "mood": ["intense", "dark", "gripping", "philosophical", "tense"]
    },
    {
        "title": "Mad Max: Fury Road",
        "description": "In a post-apocalyptic wasteland, a woman named Furiosa leads a rebellion against a tyrannical warlord while a drifter named Max joins her fight for freedom. A relentless, visually breathtaking chase through the desert that rarely stops for breath.",
        "genre": "Action", "year": 2015,
        "themes": ["survival", "freedom", "oppression", "female empowerment", "redemption", "hope"],
        "mood": ["intense", "adrenaline", "chaotic", "epic", "relentless"]
    },
    {
        "title": "John Wick",
        "description": "A retired hitman seeks vengeance against the gangsters who killed his dog and stole his car — a final gift from his late wife. Set in a hidden criminal underworld of assassins with its own rules and economy.",
        "genre": "Action", "year": 2014,
        "themes": ["revenge", "grief", "loyalty", "honor", "violence", "loss"],
        "mood": ["intense", "stylish", "relentless", "dark", "cool"]
    },
    {
        "title": "Heat",
        "description": "A veteran detective and a meticulous career criminal are locked in a tense cat-and-mouse game across Los Angeles. Both men are defined by their work to the point that their personal lives crumble around them.",
        "genre": "Crime/Thriller", "year": 1995,
        "themes": ["obsession", "duality", "crime", "identity", "loneliness", "professionalism"],
        "mood": ["tense", "cold", "methodical", "dark", "gripping"]
    },
    {
        "title": "No Country for Old Men",
        "description": "A hunter stumbles upon drug money in the Texas desert and is pursued by a relentless and philosophically terrifying killer. A meditation on fate, evil, and the helplessness of men against the forces of the world.",
        "genre": "Crime/Thriller", "year": 2007,
        "themes": ["fate", "evil", "mortality", "violence", "morality", "hopelessness"],
        "mood": ["bleak", "tense", "unsettling", "slow-burn", "existential"]
    },
    {
        "title": "Sicario",
        "description": "An idealistic FBI agent is enlisted by a government task force to aid in the fight against a powerful Mexican drug cartel. The deeper she goes, the more the moral lines blur between law enforcement and the criminals they pursue.",
        "genre": "Thriller", "year": 2015,
        "themes": ["moral ambiguity", "war on drugs", "corruption", "idealism vs reality", "violence"],
        "mood": ["tense", "dark", "bleak", "claustrophobic", "unsettling"]
    },
    {
        "title": "Se7en",
        "description": "Two detectives hunt a serial killer who uses the seven deadly sins as his motives in a perpetually dark and rainy city. A deeply unsettling thriller about the nature of evil, obsession, and the cost of confronting true darkness.",
        "genre": "Crime/Thriller", "year": 1995,
        "themes": ["evil", "sin", "obsession", "justice", "nihilism", "darkness"],
        "mood": ["dark", "disturbing", "bleak", "tense", "unsettling"]
    },
    {
        "title": "Zodiac",
        "description": "A cartoonist, a reporter, and a detective become obsessed with tracking down the Zodiac killer in San Francisco. A methodical, haunting procedural about how an unsolved mystery can consume an entire life.",
        "genre": "Crime/Thriller", "year": 2007,
        "themes": ["obsession", "mystery", "identity", "truth", "paranoia", "crime"],
        "mood": ["slow-burn", "tense", "paranoid", "haunting", "methodical"]
    },
    {
        "title": "The Bourne Identity",
        "description": "A man with no memory is rescued from the ocean with bullet wounds and must piece together who he is while being hunted by the CIA. A grounded, intelligent spy thriller about identity, memory, and institutional betrayal.",
        "genre": "Action/Thriller", "year": 2002,
        "themes": ["identity", "amnesia", "survival", "betrayal", "government conspiracy"],
        "mood": ["tense", "gripping", "paranoid", "fast-paced", "cool"]
    },
    {
        "title": "Casino Royale",
        "description": "James Bond earns his 00 status and faces a financier of terrorism in a high-stakes poker game in Montenegro. A gritty, emotionally grounded reimagining of the spy genre that strips Bond down to his vulnerable core.",
        "genre": "Action/Thriller", "year": 2006,
        "themes": ["espionage", "trust", "vulnerability", "betrayal", "love", "identity"],
        "mood": ["stylish", "tense", "cool", "emotional", "gripping"]
    },
    {
        "title": "The Raid",
        "description": "A SWAT team becomes trapped in a tenement building controlled by a ruthless crime lord and must fight their way through floor by floor. A relentless, perfectly choreographed action film that redefines the genre.",
        "genre": "Action", "year": 2011,
        "themes": ["survival", "corruption", "brotherhood", "violence", "loyalty"],
        "mood": ["intense", "relentless", "adrenaline", "visceral", "claustrophobic"]
    },
    {
        "title": "Oldboy",
        "description": "A man is mysteriously imprisoned for fifteen years without explanation, then released and given five days to find out why. A visceral, shocking South Korean thriller about revenge, secrets, and the crushing weight of the past.",
        "genre": "Thriller", "year": 2003,
        "themes": ["revenge", "identity", "secrets", "trauma", "guilt", "obsession"],
        "mood": ["dark", "disturbing", "intense", "shocking", "bleak"]
    },
    {
        "title": "Prisoners",
        "description": "A desperate father takes justice into his own hands when his daughter is kidnapped and the police suspect is released. A moral thriller that forces you to question how far a parent would go and at what cost to their own humanity.",
        "genre": "Crime/Thriller", "year": 2013,
        "themes": ["parenthood", "justice vs vigilantism", "faith", "desperation", "morality", "grief"],
        "mood": ["tense", "dark", "haunting", "agonizing", "slow-burn"]
    },
    {
        "title": "Taken",
        "description": "A retired CIA operative uses his lethal skills to track down human traffickers who have kidnapped his daughter in Paris. A lean, efficient revenge thriller built entirely around a father's love.",
        "genre": "Action/Thriller", "year": 2008,
        "themes": ["parenthood", "revenge", "human trafficking", "protection", "family"],
        "mood": ["intense", "tense", "fast-paced", "relentless", "gripping"]
    },
    {
        "title": "Parasite",
        "description": "A poor family cleverly infiltrates the lives of a wealthy household, leading to a shocking and darkly comedic chain of events. A biting satire of class inequality that transforms from comedy to thriller to horror with breathtaking precision.",
        "genre": "Thriller/Drama", "year": 2019,
        "themes": ["class inequality", "deception", "poverty", "wealth", "ambition", "social satire"],
        "mood": ["darkly comic", "tense", "shocking", "satirical", "claustrophobic"]
    },
    {
        "title": "Gone Girl",
        "description": "On the morning of their fifth anniversary, Amy Dunne goes missing and her husband Nick becomes the prime suspect as dark secrets about their marriage surface. A razor-sharp psychological thriller about marriage, media, and manipulation.",
        "genre": "Thriller", "year": 2014,
        "themes": ["marriage", "deception", "media obsession", "identity", "manipulation", "secrets"],
        "mood": ["cold", "twisty", "dark", "unsettling", "tense"]
    },
    {
        "title": "Knives Out",
        "description": "When a famous crime novelist is found dead, a master detective investigates the eccentric and greedy family. A joyful, subversive whodunit that flips genre conventions while delivering sharp commentary on class and privilege.",
        "genre": "Mystery/Comedy", "year": 2019,
        "themes": ["inheritance", "class", "family dysfunction", "deception", "privilege", "immigration"],
        "mood": ["witty", "playful", "tense", "surprising", "warm"]
    },
    {
        "title": "Collateral",
        "description": "A taxi driver is taken hostage and forced to drive a contract killer around Los Angeles on a series of assassinations. A nocturnal thriller about ordinary men thrust into extraordinary violence across a dazzling neon city.",
        "genre": "Thriller", "year": 2004,
        "themes": ["fate", "survival", "moral awakening", "urban loneliness", "identity", "violence"],
        "mood": ["tense", "slick", "nocturnal", "cool", "philosophical"]
    },
    {
        "title": "Drive",
        "description": "A quiet Hollywood stunt driver moonlights as a getaway driver and falls for his neighbor, only to be pulled into a deadly criminal underworld. A hypnotic, violent fairy tale about a man defined entirely by silence and sudden brutality.",
        "genre": "Thriller", "year": 2011,
        "themes": ["violence", "loneliness", "love", "identity", "protection", "crime"],
        "mood": ["atmospheric", "slow-burn", "tense", "dreamy", "violent"]
    },

    # ── DRAMA ─────────────────────────────────────────────────────────
    {
        "title": "The Shawshank Redemption",
        "description": "A banker wrongly convicted of murder builds an unlikely friendship and maintains hope through decades in a brutal prison. A deeply moving story about the indestructibility of the human spirit and the power of friendship.",
        "genre": "Drama", "year": 1994,
        "themes": ["hope", "friendship", "freedom", "injustice", "resilience", "redemption"],
        "mood": ["uplifting", "emotional", "inspiring", "hopeful", "melancholic"]
    },
    {
        "title": "Good Will Hunting",
        "description": "A genius janitor at MIT with a troubled past reluctantly works with a therapist to unlock his potential and confront deep emotional wounds. A story about the courage it takes to accept love, help, and your own worth.",
        "genre": "Drama", "year": 1997,
        "themes": ["trauma", "potential", "therapy", "self-worth", "belonging", "mentorship", "love"],
        "mood": ["emotional", "warm", "inspiring", "tender", "melancholic"]
    },
    {
        "title": "A Beautiful Mind",
        "description": "The story of Nobel Prize-winning mathematician John Nash, who battled paranoid schizophrenia while making groundbreaking contributions to game theory. A moving portrait of genius, love, and the struggle to distinguish reality from delusion.",
        "genre": "Drama/Biopic", "year": 2001,
        "themes": ["mental illness", "genius", "love", "paranoia", "reality", "perseverance"],
        "mood": ["inspiring", "emotional", "tense", "melancholic", "uplifting"]
    },
    {
        "title": "Whiplash",
        "description": "An ambitious young drummer at a prestigious conservatory is pushed to his psychological and physical limits by a ruthless instructor. A brutal exploration of obsession, greatness, and the price of perfection.",
        "genre": "Drama", "year": 2014,
        "themes": ["obsession", "ambition", "perfectionism", "abuse", "greatness", "music", "sacrifice"],
        "mood": ["intense", "agonizing", "exhilarating", "dark", "thrilling"]
    },
    {
        "title": "Birdman",
        "description": "A faded Hollywood superhero actor attempts to mount a serious Broadway play while battling his ego, delusions, and a desperate need for relevance. A dazzling, tragicomic portrait of artistic insecurity and the hunger for recognition.",
        "genre": "Drama/Comedy", "year": 2014,
        "themes": ["ego", "artistic relevance", "identity", "mental illness", "fame", "theater"],
        "mood": ["manic", "darkly comic", "surreal", "intense", "melancholic"]
    },
    {
        "title": "Spotlight",
        "description": "The Boston Globe's investigative team exposes the systematic cover-up of child abuse by the Catholic Church. A restrained, powerful journalism procedural about institutions, complicity, and the courage to expose the truth.",
        "genre": "Drama", "year": 2015,
        "themes": ["journalism", "institutional corruption", "abuse", "truth", "accountability", "complicity"],
        "mood": ["serious", "restrained", "gripping", "important", "tense"]
    },
    {
        "title": "The Social Network",
        "description": "A Harvard student betrays his best friend to build one of the most powerful companies in the world, only to find himself alone with his billions. A brilliant dissection of ambition, betrayal, and the loneliness behind success.",
        "genre": "Drama", "year": 2010,
        "themes": ["ambition", "betrayal", "loneliness", "success", "friendship", "obsession", "technology"],
        "mood": ["cold", "sharp", "brilliant", "melancholic", "intense"]
    },
    {
        "title": "American History X",
        "description": "A former neo-Nazi skinhead tries to prevent his younger brother from going down the same destructive path after serving time in prison for a brutal hate crime. A searing examination of racism, radicalization, and the possibility of change.",
        "genre": "Drama", "year": 1998,
        "themes": ["racism", "redemption", "radicalization", "family", "violence", "change"],
        "mood": ["intense", "disturbing", "emotional", "powerful", "dark"]
    },
    {
        "title": "Forrest Gump",
        "description": "A kind-hearted man from Alabama with a low IQ accidentally influences many of the defining moments of American history while searching for the girl he loves. A bittersweet fable about innocence, love, and the randomness of life.",
        "genre": "Drama", "year": 1994,
        "themes": ["innocence", "love", "destiny", "historical events", "perseverance", "loss"],
        "mood": ["bittersweet", "warm", "uplifting", "melancholic", "heartfelt"]
    },
    {
        "title": "Requiem for a Dream",
        "description": "Four people in Brooklyn become consumed by their obsessions and drug addictions, each descending into their own private hell. A harrowing, visceral portrait of addiction that treats it with unflinching honesty and visual poetry.",
        "genre": "Drama", "year": 2000,
        "themes": ["addiction", "despair", "dreams vs reality", "loneliness", "self-destruction"],
        "mood": ["harrowing", "dark", "visceral", "disturbing", "tragic"]
    },
    {
        "title": "Black Swan",
        "description": "A ballerina wins the lead in Swan Lake only to be consumed by a psychological breakdown as she attempts to achieve perfection. A dark psychological thriller about obsession, duality, and the destruction that comes from demanding perfection of yourself.",
        "genre": "Drama/Thriller", "year": 2010,
        "themes": ["obsession", "perfection", "identity", "duality", "mental breakdown", "art"],
        "mood": ["intense", "dark", "psychological", "unsettling", "haunting"]
    },
    {
        "title": "Boyhood",
        "description": "Filmed over twelve years with the same cast, the movie follows a boy from age six to eighteen, capturing the ordinary moments that shape a life. A profound, quietly radical cinematic experiment about growing up in real time.",
        "genre": "Drama", "year": 2014,
        "themes": ["growing up", "family", "time", "identity", "childhood", "adulthood"],
        "mood": ["nostalgic", "tender", "melancholic", "quiet", "emotional"]
    },
    {
        "title": "Manchester by the Sea",
        "description": "A man is forced to return to his hometown after his brother's death to become guardian of his teenage nephew, confronting unimaginable grief. A devastating, unsentimental portrait of a man broken by tragedy who cannot forgive himself.",
        "genre": "Drama", "year": 2016,
        "themes": ["grief", "guilt", "loss", "family", "forgiveness", "trauma"],
        "mood": ["devastating", "bleak", "honest", "quiet", "heartbreaking"]
    },
    {
        "title": "Marriage Story",
        "description": "A stage director and his actor wife struggle through a coast-to-coast divorce that pushes them both to their emotional limits. An intimate, devastatingly honest portrait of how love and resentment coexist in a crumbling marriage.",
        "genre": "Drama/Romance", "year": 2019,
        "themes": ["divorce", "love", "identity", "communication", "family", "ambition", "resentment"],
        "mood": ["heartbreaking", "intimate", "honest", "emotional", "bittersweet"]
    },
    {
        "title": "Moonlight",
        "description": "A young Black man grows up in Miami, navigating poverty, a drug-addicted mother, and his own sexuality across three defining chapters of his life. A tender, lyrical masterpiece about identity, love, and the search for belonging.",
        "genre": "Drama", "year": 2016,
        "themes": ["identity", "sexuality", "poverty", "love", "belonging", "masculinity", "loneliness"],
        "mood": ["tender", "lyrical", "melancholic", "beautiful", "quiet"]
    },
    {
        "title": "The Pianist",
        "description": "A Polish-Jewish musician survives the destruction of the Warsaw Ghetto with help from a German officer. A devastating, intimate account of survival, loss, and the sustaining power of art amidst the worst of human history.",
        "genre": "Drama/War", "year": 2002,
        "themes": ["survival", "Holocaust", "war", "music", "humanity", "loss"],
        "mood": ["devastating", "emotional", "haunting", "somber", "powerful"]
    },
    {
        "title": "12 Years a Slave",
        "description": "A free Black man from New York is kidnapped and sold into slavery in 1841, spending twelve brutal years in the antebellum South. An unflinching, necessary portrait of one of history's greatest atrocities told with gut-wrenching humanity.",
        "genre": "Drama/Historical", "year": 2013,
        "themes": ["slavery", "survival", "humanity", "injustice", "dignity", "freedom"],
        "mood": ["harrowing", "powerful", "devastating", "important", "visceral"]
    },
    {
        "title": "Her",
        "description": "A lonely writer in the near future develops a deep emotional and romantic relationship with an AI operating system. A melancholic meditation on connection, loneliness, and what it means to love in a technologically mediated world.",
        "genre": "Drama/Sci-Fi", "year": 2013,
        "themes": ["loneliness", "connection", "AI", "love", "technology", "identity", "loss"],
        "mood": ["melancholic", "warm", "tender", "bittersweet", "contemplative"]
    },
    {
        "title": "The Pursuit of Happyness",
        "description": "A homeless father struggles to build a future for himself and his young son while completing an unpaid stockbroker internship in 1980s San Francisco. An emotionally exhausting true story about perseverance and the cost of the American Dream.",
        "genre": "Drama/Biopic", "year": 2006,
        "themes": ["perseverance", "fatherhood", "poverty", "ambition", "hope", "survival"],
        "mood": ["inspiring", "emotional", "heartbreaking", "uplifting", "tense"]
    },
    {
        "title": "Schindler's List",
        "description": "A German businessman saves the lives of more than a thousand Jewish refugees during the Holocaust by employing them in his factories. Spielberg's towering masterpiece about moral transformation in the face of industrial genocide.",
        "genre": "Drama/Historical", "year": 1993,
        "themes": ["Holocaust", "moral awakening", "survival", "humanity", "war", "redemption"],
        "mood": ["devastating", "powerful", "haunting", "important", "somber"]
    },
    {
        "title": "Cast Away",
        "description": "A FedEx executive must transform himself physically and emotionally to survive after his plane crashes on a deserted island. A profound meditation on solitude, will to survive, and what it means to return to the world after profound isolation.",
        "genre": "Drama", "year": 2000,
        "themes": ["survival", "solitude", "isolation", "resilience", "identity", "loss"],
        "mood": ["quiet", "tense", "emotional", "contemplative", "uplifting"]
    },
    {
        "title": "The Green Mile",
        "description": "A death row corrections officer witnesses supernatural events involving a gentle giant with an unusual gift on death row during the Great Depression. A deeply moving fantasy drama about compassion, injustice, and the miraculous.",
        "genre": "Drama/Fantasy", "year": 1999,
        "themes": ["injustice", "compassion", "death", "miracles", "race", "redemption"],
        "mood": ["emotional", "melancholic", "powerful", "heartbreaking", "uplifting"]
    },
    {
        "title": "Three Billboards Outside Ebbing, Missouri",
        "description": "A grieving mother erects provocative billboards to challenge the local police chief after her daughter's murder goes unsolved. A dark, compassionate, deeply funny portrait of grief, anger, and the complicated mess of human beings.",
        "genre": "Drama/Dark Comedy", "year": 2017,
        "themes": ["grief", "anger", "justice", "redemption", "community", "forgiveness"],
        "mood": ["darkly comic", "angry", "compassionate", "bittersweet", "powerful"]
    },
    {
        "title": "Soul",
        "description": "A jazz musician accidentally falls into the afterlife and must find his way back to Earth before his big break. A profound Pixar meditation on what makes life worth living and the danger of letting your passion consume your presence.",
        "genre": "Animation/Drama", "year": 2020,
        "themes": ["purpose", "life", "death", "passion", "mindfulness", "identity"],
        "mood": ["heartfelt", "philosophical", "warm", "bittersweet", "uplifting"]
    },

    # ── SCI-FI ────────────────────────────────────────────────────────
    {
        "title": "Inception",
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into a CEO's mind. A dazzling puzzle-box thriller about the architecture of the unconscious mind and the nature of reality.",
        "genre": "Sci-Fi/Thriller", "year": 2010,
        "themes": ["reality vs illusion", "dreams", "guilt", "identity", "subconscious", "heist"],
        "mood": ["mind-bending", "tense", "spectacular", "emotional", "complex"]
    },
    {
        "title": "Interstellar",
        "description": "A former NASA pilot travels through a wormhole near Saturn to find a new home for humanity as Earth faces extinction. A grand, emotional sci-fi epic about love transcending the dimensions of space and time.",
        "genre": "Sci-Fi", "year": 2014,
        "themes": ["love", "time", "space", "sacrifice", "parenthood", "survival", "science"],
        "mood": ["epic", "emotional", "awe-inspiring", "melancholic", "tense"]
    },
    {
        "title": "The Matrix",
        "description": "A hacker discovers that the world he knows is a simulation and joins a rebellion against the machine overlords running it. A visionary sci-fi action film that blends philosophy, bullet-time action, and a genuine sense of awakening.",
        "genre": "Sci-Fi/Action", "year": 1999,
        "themes": ["reality vs simulation", "free will", "identity", "rebellion", "technology", "awakening"],
        "mood": ["mind-bending", "cool", "intense", "philosophical", "exhilarating"]
    },
    {
        "title": "Arrival",
        "description": "A linguist is recruited by the military to help communicate with alien spacecraft that have appeared around the world. A deeply moving, non-linear sci-fi film about language, grief, and the choice to love knowing that loss is inevitable.",
        "genre": "Sci-Fi/Drama", "year": 2016,
        "themes": ["language", "time", "grief", "love", "first contact", "choice", "motherhood"],
        "mood": ["contemplative", "emotional", "awe-inspiring", "melancholic", "quiet"]
    },
    {
        "title": "Ex Machina",
        "description": "A programmer is invited to administer the Turing Test to a humanoid AI at a secluded estate, only to find the lines between observer and subject rapidly blurring. A taut, glacially cool thriller about consciousness, manipulation, and what makes us human.",
        "genre": "Sci-Fi/Thriller", "year": 2014,
        "themes": ["AI consciousness", "manipulation", "identity", "gender", "power", "creation"],
        "mood": ["cold", "tense", "unsettling", "cerebral", "atmospheric"]
    },
    {
        "title": "Blade Runner 2049",
        "description": "A young blade runner discovers a long-buried secret that could plunge society into chaos and goes in search of Rick Deckard, who has been missing for thirty years. A visually stunning meditation on memory, identity, and what it means to be human.",
        "genre": "Sci-Fi", "year": 2017,
        "themes": ["identity", "memory", "humanity", "loneliness", "AI", "existence"],
        "mood": ["atmospheric", "melancholic", "beautiful", "slow-burn", "contemplative"]
    },
    {
        "title": "Moon",
        "description": "An astronaut nearing the end of his three-year solo contract on the moon makes a discovery that challenges everything he thought he knew about his mission. A haunting, intimate sci-fi film about loneliness, identity, and corporate exploitation.",
        "genre": "Sci-Fi", "year": 2009,
        "themes": ["identity", "loneliness", "cloning", "corporate ethics", "isolation", "memory"],
        "mood": ["quiet", "haunting", "melancholic", "unsettling", "contemplative"]
    },
    {
        "title": "Gravity",
        "description": "A medical engineer and an astronaut work together to survive after a catastrophic accident destroys their space shuttle. A visually staggering, emotionally raw survival film set against the terrifying beauty of outer space.",
        "genre": "Sci-Fi/Thriller", "year": 2013,
        "themes": ["survival", "grief", "rebirth", "isolation", "will to live"],
        "mood": ["tense", "awe-inspiring", "emotional", "intense", "visceral"]
    },
    {
        "title": "2001: A Space Odyssey",
        "description": "Humanity discovers a mysterious monolith that may hold the key to evolution, leading a crew to Jupiter where a supercomputer begins acting strangely. A transcendent, glacially paced masterpiece about human evolution and the terror of artificial intelligence.",
        "genre": "Sci-Fi", "year": 1968,
        "themes": ["evolution", "AI", "existentialism", "space", "humanity", "transcendence"],
        "mood": ["awe-inspiring", "mysterious", "cerebral", "slow", "transcendent"]
    },
    {
        "title": "Alien",
        "description": "The crew of a commercial spaceship encounters a deadly extraterrestrial organism after responding to a distress signal from a desolate moon. The original haunted house in space — a masterpiece of dread, isolation, and creature design.",
        "genre": "Sci-Fi/Horror", "year": 1979,
        "themes": ["survival", "isolation", "body horror", "corporate greed", "fear", "space"],
        "mood": ["terrifying", "claustrophobic", "tense", "atmospheric", "dark"]
    },
    {
        "title": "The Martian",
        "description": "An astronaut is stranded alone on Mars and must use his wits and botanical skills to survive while NASA devises a rescue mission. An optimistic, problem-solving sci-fi film that celebrates science, ingenuity, and the refusal to give up.",
        "genre": "Sci-Fi/Drama", "year": 2015,
        "themes": ["survival", "ingenuity", "isolation", "optimism", "teamwork", "science"],
        "mood": ["uplifting", "tense", "funny", "inspiring", "warm"]
    },
    {
        "title": "Annihilation",
        "description": "A biologist leads a team of scientists into a mysterious environmental disaster zone where the laws of nature no longer apply. A hypnotic, deeply unsettling horror-inflected sci-fi film about self-destruction, identity, and the unknowable.",
        "genre": "Sci-Fi/Horror", "year": 2018,
        "themes": ["self-destruction", "identity", "nature", "the unknown", "transformation", "grief"],
        "mood": ["disturbing", "dreamlike", "haunting", "tense", "cerebral"]
    },
    {
        "title": "District 9",
        "description": "An alien species forced to live in slums in South Africa are subject to brutal government control, seen through the eyes of a bureaucrat who begins to transform. A visceral sci-fi allegory for apartheid, xenophobia, and what defines humanity.",
        "genre": "Sci-Fi/Action", "year": 2009,
        "themes": ["xenophobia", "apartheid", "identity", "humanity", "discrimination", "transformation"],
        "mood": ["intense", "gritty", "thought-provoking", "tense", "visceral"]
    },
    {
        "title": "Contact",
        "description": "A scientist receives a message from extraterrestrials that contains plans for a machine, triggering a global debate about science, faith, and first contact. A thoughtful, patient sci-fi film about the relationship between science and belief.",
        "genre": "Sci-Fi/Drama", "year": 1997,
        "themes": ["science vs faith", "first contact", "truth", "loneliness", "wonder", "discovery"],
        "mood": ["contemplative", "awe-inspiring", "emotional", "philosophical", "quiet"]
    },
    {
        "title": "Looper",
        "description": "In the future, a hitman must confront his older self sent back in time to be killed — and must decide whether to change the future or preserve it. A clever, emotionally complex time-travel thriller about consequence and the desire for change.",
        "genre": "Sci-Fi/Action", "year": 2012,
        "themes": ["time travel", "identity", "consequence", "sacrifice", "free will", "violence"],
        "mood": ["tense", "clever", "emotional", "dark", "gripping"]
    },
    {
        "title": "Edge of Tomorrow",
        "description": "A military officer caught in a time loop must relive the same battle against alien invaders over and over until he can find a way to win. A brilliantly executed sci-fi action thriller that uses its concept to build genuine emotional stakes.",
        "genre": "Sci-Fi/Action", "year": 2014,
        "themes": ["time loop", "perseverance", "war", "growth", "courage", "sacrifice"],
        "mood": ["thrilling", "funny", "tense", "exhilarating", "clever"]
    },
    {
        "title": "Eternal Sunshine of the Spotless Mind",
        "description": "A couple undergoes a procedure to erase each other from their memories after their relationship falls apart, only to rediscover their love in the process. A non-linear, deeply romantic film about the pain of love and why we choose to remember.",
        "genre": "Sci-Fi/Romance", "year": 2004,
        "themes": ["memory", "love", "loss", "identity", "regret", "relationships"],
        "mood": ["melancholic", "romantic", "dreamlike", "bittersweet", "emotional"]
    },
    {
        "title": "Children of Men",
        "description": "In a dystopian future where humanity has become infertile, a bureaucrat must escort the first pregnant woman in eighteen years to safety. A breathtaking, visceral sci-fi masterpiece about hope, sacrifice, and the fragility of civilization.",
        "genre": "Sci-Fi/Thriller", "year": 2006,
        "themes": ["hope", "fertility", "dystopia", "sacrifice", "humanity", "survival"],
        "mood": ["intense", "bleak", "hopeful", "visceral", "tense"]
    },
    {
        "title": "Minority Report",
        "description": "In a future where police arrest murderers before they commit crimes, the head of the pre-crime unit is accused of a future murder. A dazzlingly inventive sci-fi thriller about free will, surveillance, and whether the future can be changed.",
        "genre": "Sci-Fi/Thriller", "year": 2002,
        "themes": ["free will", "surveillance", "justice", "predetermination", "identity", "paranoia"],
        "mood": ["tense", "cerebral", "stylish", "intense", "paranoid"]
    },

    # ── HORROR ────────────────────────────────────────────────────────
    {
        "title": "Hereditary",
        "description": "When the Graham family's secretive grandmother dies, terrifying and inexplicable events begin unraveling the family from within. The most devastating horror film in years, built on genuine grief and dread rather than cheap scares.",
        "genre": "Horror", "year": 2018,
        "themes": ["grief", "family trauma", "inherited evil", "mental illness", "loss", "cults"],
        "mood": ["terrifying", "devastating", "disturbing", "slow-burn", "haunting"]
    },
    {
        "title": "Midsommar",
        "description": "A couple travels to a pagan midsummer festival in rural Sweden that reveals its increasingly sinister nature while their relationship crumbles. A folk horror film that doubles as a raw portrait of a toxic relationship reaching its devastating end.",
        "genre": "Horror", "year": 2019,
        "themes": ["grief", "relationships", "cults", "isolation", "community", "pagan ritual"],
        "mood": ["disturbing", "dreamlike", "unsettling", "slow-burn", "bright dread"]
    },
    {
        "title": "Get Out",
        "description": "A young Black man visits his white girlfriend's family estate and discovers a terrifying conspiracy lurking beneath the surface of liberal politeness. A sharp, terrifying horror film that uses the genre to expose the horrors of racism.",
        "genre": "Horror/Thriller", "year": 2017,
        "themes": ["racism", "exploitation", "identity", "paranoia", "social commentary", "body horror"],
        "mood": ["tense", "disturbing", "clever", "unsettling", "scary"]
    },
    {
        "title": "The Shining",
        "description": "A writer becomes the winter caretaker of an isolated mountain hotel, where supernatural forces and his own madness drive him to violence against his family. Kubrick's cold, terrifying masterpiece about isolation, madness, and domestic violence.",
        "genre": "Horror", "year": 1980,
        "themes": ["madness", "isolation", "family", "domestic violence", "supernatural", "alcoholism"],
        "mood": ["terrifying", "atmospheric", "unsettling", "claustrophobic", "cold"]
    },
    {
        "title": "A Quiet Place",
        "description": "A family struggles to survive in a post-apocalyptic world inhabited by blind monsters with an acute sense of hearing, forced to live in near-total silence. A tense, emotionally rich horror film that uses its high concept to explore parenthood and sacrifice.",
        "genre": "Horror/Thriller", "year": 2018,
        "themes": ["survival", "family", "parenthood", "sacrifice", "silence", "communication"],
        "mood": ["tense", "terrifying", "emotional", "claustrophobic", "intense"]
    },
    {
        "title": "The Witch",
        "description": "A Puritan family is banished from their plantation community in 1630s New England and begins to fall apart when they suspect their youngest child is a witch. A slow, oppressive descent into religious hysteria, paranoia, and folk horror.",
        "genre": "Horror", "year": 2015,
        "themes": ["religious hysteria", "isolation", "family breakdown", "witchcraft", "paranoia", "faith"],
        "mood": ["slow-burn", "oppressive", "unsettling", "atmospheric", "dark"]
    },
    {
        "title": "The Silence of the Lambs",
        "description": "A young FBI trainee seeks the help of imprisoned cannibal Hannibal Lecter to catch a serial killer who skins his victims. A psychologically rich thriller that creates a terrifying symbiosis between its hunter and its monster.",
        "genre": "Thriller/Horror", "year": 1991,
        "themes": ["psychology", "predator", "identity", "power", "evil", "gender"],
        "mood": ["tense", "disturbing", "brilliant", "dark", "unsettling"]
    },
    {
        "title": "It Follows",
        "description": "A teenager is pursued by an unstoppable supernatural entity after a sexual encounter passes the curse to her. A genuinely scary slow-burn horror film that uses its monster as a brilliant metaphor for anxiety, trauma, and sexual fear.",
        "genre": "Horror", "year": 2014,
        "themes": ["anxiety", "sexuality", "paranoia", "youth", "inevitability", "trauma"],
        "mood": ["atmospheric", "dread-filled", "slow-burn", "unsettling", "haunting"]
    },
    {
        "title": "Psycho",
        "description": "A secretary on the run with stolen money checks into a remote motel run by a troubled young man dominated by his mother. Hitchcock's most audacious masterpiece — the film that invented modern horror cinema.",
        "genre": "Horror/Thriller", "year": 1960,
        "themes": ["identity", "obsession", "maternal control", "violence", "guilt", "duality"],
        "mood": ["suspenseful", "shocking", "atmospheric", "tense", "dark"]
    },
    {
        "title": "Us",
        "description": "A family's beach vacation is upended when their doppelgangers appear and begin terrorizing them. A bold, allegorical horror film about the violence hidden within the American social contract and the doppelganger of privilege.",
        "genre": "Horror", "year": 2019,
        "themes": ["duality", "class", "identity", "social inequality", "family", "trauma"],
        "mood": ["terrifying", "clever", "disturbing", "unsettling", "thought-provoking"]
    },
    {
        "title": "The Conjuring",
        "description": "Paranormal investigators Ed and Lorraine Warren are called to help a family terrorized by a dark presence in their farmhouse. A masterfully crafted haunted house film that derives its terror from character and atmosphere rather than gore.",
        "genre": "Horror", "year": 2013,
        "themes": ["the supernatural", "family", "faith", "evil", "haunting", "marriage"],
        "mood": ["scary", "tense", "atmospheric", "intense", "unsettling"]
    },

    # ── CRIME / MYSTERY ───────────────────────────────────────────────
    {
        "title": "Pulp Fiction",
        "description": "Several stories of crime in Los Angeles interweave featuring hitmen, a boxer, a crime boss's wife, and others over twenty-four hours. Tarantino's genre-redefining masterpiece — a movie that made talking cool and violence lyrical.",
        "genre": "Crime/Drama", "year": 1994,
        "themes": ["crime", "fate", "redemption", "violence", "morality", "dialogue"],
        "mood": ["cool", "darkly funny", "stylish", "tense", "playful"]
    },
    {
        "title": "The Godfather",
        "description": "The aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant youngest son. A mythic, operatic portrait of power, family, loyalty, and corruption that transcends the crime genre.",
        "genre": "Crime/Drama", "year": 1972,
        "themes": ["family", "power", "corruption", "loyalty", "tradition", "violence"],
        "mood": ["epic", "somber", "powerful", "atmospheric", "tragic"]
    },
    {
        "title": "Goodfellas",
        "description": "Henry Hill and his friends work their way up through the mob hierarchy while the lifestyle of crime, drugs, and paranoia begins to destroy everything around him. Scorsese's kinetic, dazzling, and ultimately devastating portrait of the seduction of criminal life.",
        "genre": "Crime/Drama", "year": 1990,
        "themes": ["crime", "loyalty", "betrayal", "greed", "identity", "paranoia"],
        "mood": ["exhilarating", "darkly funny", "kinetic", "intense", "tragic"]
    },
    {
        "title": "Chinatown",
        "description": "A private detective hired to expose an adulterer uncovers a conspiracy involving water rights, municipal corruption, and a disturbing family secret. A perfect neo-noir about the futility of justice in a corrupt world.",
        "genre": "Mystery/Crime", "year": 1974,
        "themes": ["corruption", "power", "truth", "helplessness", "secrets", "moral failure"],
        "mood": ["atmospheric", "bleak", "tense", "mysterious", "tragic"]
    },
    {
        "title": "L.A. Confidential",
        "description": "Three very different police officers investigate a series of murders in 1950s Los Angeles that expose deep corruption within the LAPD. A beautifully crafted neo-noir about truth, justice, and the price of integrity in a corrupt system.",
        "genre": "Mystery/Crime", "year": 1997,
        "themes": ["corruption", "truth", "justice", "celebrity", "integrity", "betrayal"],
        "mood": ["atmospheric", "tense", "stylish", "complex", "gripping"]
    },
    {
        "title": "Memento",
        "description": "A man with short-term memory loss uses tattoos and photographs to hunt the man he believes killed his wife, told in reverse chronological order. A brilliantly constructed puzzle about the unreliability of memory, identity, and obsession.",
        "genre": "Mystery/Thriller", "year": 2000,
        "themes": ["memory", "identity", "revenge", "truth", "self-deception", "obsession"],
        "mood": ["mind-bending", "tense", "clever", "disorienting", "dark"]
    },
    {
        "title": "The Usual Suspects",
        "description": "The sole survivor of a massacre recounts the events that led there to a detective, building toward one of cinema's great twist endings. A supremely crafted crime mystery about the nature of truth, deception, and mythology.",
        "genre": "Mystery/Crime", "year": 1995,
        "themes": ["deception", "identity", "mythology", "crime", "truth", "manipulation"],
        "mood": ["clever", "tense", "mysterious", "gripping", "twisty"]
    },
    {
        "title": "Fargo",
        "description": "A desperate car salesman hires two criminals to kidnap his wife for ransom, leading to a series of terrible and darkly comic escalations investigated by a very pregnant local sheriff. A Coen Brothers masterpiece about evil in ordinary places.",
        "genre": "Crime/Dark Comedy", "year": 1996,
        "themes": ["greed", "evil", "decency", "crime", "small-town life", "consequences"],
        "mood": ["darkly comic", "tense", "quirky", "bleak", "warm"]
    },
    {
        "title": "City of God",
        "description": "Two boys grow up in a violent Brazilian favela — one becomes a photographer, the other a drug lord — captured over two decades of gang warfare. A kinetic, breathtaking portrait of poverty, violence, and the razor-thin line between fate and choice.",
        "genre": "Crime/Drama", "year": 2002,
        "themes": ["poverty", "violence", "crime", "fate", "survival", "coming-of-age"],
        "mood": ["intense", "kinetic", "tragic", "vital", "gripping"]
    },
    {
        "title": "The Departed",
        "description": "An undercover cop and a mole inside the police force work on opposite sides of the same investigation in Boston's criminal underworld. A furious, Shakespearean crime thriller about identity, loyalty, and betrayal.",
        "genre": "Crime/Thriller", "year": 2006,
        "themes": ["identity", "betrayal", "loyalty", "double life", "corruption", "violence"],
        "mood": ["intense", "sharp", "tense", "dark", "exhilarating"]
    },
    {
        "title": "Catch Me If You Can",
        "description": "The true story of Frank Abagnale Jr., who successfully performed cons worth millions of dollars as a pilot, doctor, and lawyer — all before his 21st birthday. A charming, elegantly crafted cat-and-mouse film about identity and the longing to belong.",
        "genre": "Crime/Drama", "year": 2002,
        "themes": ["identity", "deception", "family", "belonging", "ambition", "loneliness"],
        "mood": ["charming", "fun", "fast-paced", "nostalgic", "bittersweet"]
    },
    {
        "title": "Inside Man",
        "description": "A brilliant bank robber pulls off the perfect heist while a seasoned detective tries to figure out how he did it. A smart, cleverly constructed thriller that keeps its secrets close until the satisfying final reveal.",
        "genre": "Crime/Thriller", "year": 2006,
        "themes": ["deception", "power", "justice", "complicity", "crime", "cleverness"],
        "mood": ["clever", "tense", "stylish", "gripping", "satisfying"]
    },

    # ── COMEDY ────────────────────────────────────────────────────────
    {
        "title": "The Grand Budapest Hotel",
        "description": "A legendary hotel concierge and his young protégé are embroiled in a murder mystery and the theft of a priceless painting in a fictional European republic. A gloriously inventive, meticulously designed confection about nostalgia, decency, and the end of a world.",
        "genre": "Comedy/Drama", "year": 2014,
        "themes": ["nostalgia", "decency", "loyalty", "war", "art", "identity"],
        "mood": ["whimsical", "witty", "melancholic", "charming", "bittersweet"]
    },
    {
        "title": "The Big Lebowski",
        "description": "The Dude, a Los Angeles slacker and bowling enthusiast, is mistaken for a millionaire and drawn into a bizarre ransom scheme. A shaggy, endlessly rewatchable comedy about doing nothing in a world that demands doing everything.",
        "genre": "Comedy", "year": 1998,
        "themes": ["identity", "nihilism", "friendship", "absurdity", "laziness", "crime"],
        "mood": ["hilarious", "absurd", "laid-back", "quirky", "warm"]
    },
    {
        "title": "Superbad",
        "description": "Two socially awkward high school best friends attempt to buy alcohol for a party and end up on a series of increasingly chaotic misadventures. A brilliantly funny, surprisingly tender love letter to the intensity of teenage male friendship.",
        "genre": "Comedy", "year": 2007,
        "themes": ["friendship", "adolescence", "growing up", "awkwardness", "love"],
        "mood": ["hilarious", "raunchy", "warm", "nostalgic", "chaotic"]
    },
    {
        "title": "About a Boy",
        "description": "A shallow, self-absorbed bachelor invents a fictional son to meet single mothers and ends up forming an unlikely friendship with a troubled twelve-year-old. A charming, genuinely affecting comedy about learning to connect with other people.",
        "genre": "Comedy/Drama", "year": 2002,
        "themes": ["loneliness", "friendship", "growing up", "responsibility", "connection"],
        "mood": ["warm", "funny", "charming", "emotional", "bittersweet"]
    },
    {
        "title": "Office Space",
        "description": "A software engineer who hates his job undergoes a hypnotic transformation that makes him not care about work and accidentally impresses his bosses. A brilliantly observed satire of corporate culture and the soul-crushing mundanity of the modern office.",
        "genre": "Comedy", "year": 1999,
        "themes": ["work culture", "identity", "conformity", "rebellion", "friendship"],
        "mood": ["hilarious", "relatable", "satirical", "warm", "absurd"]
    },
    {
        "title": "Game Night",
        "description": "A couple's game night goes terrifyingly wrong when what appears to be a murder mystery game turns out to be real. A surprisingly clever and well-crafted comedy thriller that genuinely earns its laughs.",
        "genre": "Comedy/Thriller", "year": 2018,
        "themes": ["competition", "relationships", "deception", "humor", "friendship"],
        "mood": ["funny", "clever", "fast-paced", "exciting", "light-hearted"]
    },
    {
        "title": "Groundhog Day",
        "description": "A cynical TV weatherman is condemned to relive the same February day in Punxsutawney, Pennsylvania over and over until he learns to be a better person. A perfect comedy that becomes a genuine philosophical meditation on meaning and self-improvement.",
        "genre": "Comedy/Drama", "year": 1993,
        "themes": ["self-improvement", "time loop", "love", "redemption", "purpose", "change"],
        "mood": ["funny", "heartfelt", "philosophical", "warm", "clever"]
    },

    # ── ROMANCE ───────────────────────────────────────────────────────
    {
        "title": "La La Land",
        "description": "An aspiring actress and a jazz musician fall in love while pursuing their dreams in Los Angeles, ultimately forced to choose between love and ambition. A dazzling, bittersweet musical that captures both the magic of dreams and the cost of following them.",
        "genre": "Romance/Musical", "year": 2016,
        "themes": ["dreams", "ambition", "love", "sacrifice", "nostalgia", "art"],
        "mood": ["romantic", "bittersweet", "beautiful", "melancholic", "magical"]
    },
    {
        "title": "Before Sunrise",
        "description": "An American man and a French woman meet on a train and spend one magical night walking and talking through Vienna. One of cinema's most romantic films — a conversation about life, love, and connection that never grows old.",
        "genre": "Romance/Drama", "year": 1995,
        "themes": ["connection", "conversation", "love", "time", "youth", "possibility"],
        "mood": ["romantic", "warm", "intellectual", "tender", "nostalgic"]
    },
    {
        "title": "Before Sunset",
        "description": "Nine years after their Vienna night, Jesse and Céline meet again in Paris with only an hour before his flight — nine years of regret condensed into a perfect afternoon. A profound, mature sequel about what happens to love when life gets in the way.",
        "genre": "Romance/Drama", "year": 2004,
        "themes": ["regret", "love", "lost chances", "time", "marriage", "longing"],
        "mood": ["bittersweet", "intimate", "intellectual", "romantic", "melancholic"]
    },
    {
        "title": "Pride & Prejudice",
        "description": "The spirited Elizabeth Bennet navigates questions of marriage, morality, and misconceptions about a proud man named Mr. Darcy in Regency-era England. A luminously crafted adaptation of Austen's most beloved novel about the tension between pride and love.",
        "genre": "Romance/Drama", "year": 2005,
        "themes": ["love", "class", "prejudice", "pride", "marriage", "society"],
        "mood": ["romantic", "witty", "warm", "beautiful", "sweeping"]
    },
    {
        "title": "Lost in Translation",
        "description": "A fading movie star and a young woman at a crossroads form an unlikely bond during overlapping stays in a Tokyo hotel. A whisper of a film — tender, funny, and profoundly melancholic — about connection in the midst of displacement.",
        "genre": "Romance/Drama", "year": 2003,
        "themes": ["loneliness", "connection", "marriage", "identity", "displacement", "aging"],
        "mood": ["melancholic", "tender", "quiet", "bittersweet", "atmospheric"]
    },
    {
        "title": "Amélie",
        "description": "A shy Parisian waitress decides to change the lives of those around her for the better while neglecting her own happiness and longing for love. A whimsical, visually inventive French masterpiece that celebrates kindness, imagination, and the courage to connect.",
        "genre": "Romance/Comedy", "year": 2001,
        "themes": ["loneliness", "connection", "kindness", "imagination", "love", "isolation"],
        "mood": ["whimsical", "charming", "warm", "playful", "bittersweet"]
    },
    {
        "title": "500 Days of Summer",
        "description": "A hopeless romantic falls for a woman who doesn't believe in love, told in a deliberately non-linear fashion that captures the chaos of a doomed relationship. A sharp, honest deconstruction of romantic projection and the stories we tell ourselves.",
        "genre": "Romance/Comedy", "year": 2009,
        "themes": ["love", "expectation vs reality", "heartbreak", "identity", "projection"],
        "mood": ["bittersweet", "honest", "witty", "melancholic", "charming"]
    },
    {
        "title": "Carol",
        "description": "A young aspiring photographer falls for an older married woman during a chance encounter in 1950s New York. A devastating, luminously beautiful love story about desire, sacrifice, and the courage to choose who you are.",
        "genre": "Romance/Drama", "year": 2015,
        "themes": ["love", "sexuality", "identity", "sacrifice", "freedom", "1950s society"],
        "mood": ["romantic", "melancholic", "beautiful", "tense", "devastating"]
    },

    # ── ANIMATION ─────────────────────────────────────────────────────
    {
        "title": "Spirited Away",
        "description": "A ten-year-old girl wanders into a spirit world and must work in a supernatural bathhouse to save her transformed parents. Miyazaki's masterpiece — a richly imagined fantasia about identity, work, love, and finding your name.",
        "genre": "Animation/Fantasy", "year": 2001,
        "themes": ["identity", "growing up", "work", "love", "the spirit world", "courage"],
        "mood": ["magical", "adventurous", "emotional", "wondrous", "beautiful"]
    },
    {
        "title": "Up",
        "description": "An elderly widower fulfills his late wife's dream by tying thousands of balloons to his house and flying to South America, bringing an unexpected young stowaway. The most devastating first ten minutes in cinema history, followed by a joyful, touching adventure.",
        "genre": "Animation/Drama", "year": 2009,
        "themes": ["grief", "love", "adventure", "aging", "friendship", "letting go"],
        "mood": ["heartbreaking", "joyful", "warm", "emotional", "uplifting"]
    },
    {
        "title": "WALL-E",
        "description": "A lonely trash-compacting robot left on an abandoned Earth falls in love with a sleek reconnaissance robot. A nearly dialogue-free first act masterpiece about loneliness, environmental collapse, consumerism, and the transformative power of connection.",
        "genre": "Animation/Sci-Fi", "year": 2008,
        "themes": ["loneliness", "love", "environment", "consumerism", "connection", "hope"],
        "mood": ["melancholic", "romantic", "hopeful", "sweet", "profound"]
    },
    {
        "title": "Inside Out",
        "description": "The emotions inside a young girl's mind — Joy, Sadness, Fear, Disgust, and Anger — go on an adventure through her consciousness when her world is upended. A brilliant conceptual feat that teaches children and adults that sadness is not the enemy of happiness.",
        "genre": "Animation/Drama", "year": 2015,
        "themes": ["emotions", "growing up", "identity", "mental health", "childhood", "change"],
        "mood": ["emotional", "clever", "warm", "funny", "heartbreaking"]
    },
    {
        "title": "Princess Mononoke",
        "description": "A young prince becomes caught in the conflict between the gods of a forest and the humans who consume it in feudal Japan. Miyazaki's most complex film — a war epic about the impossibility of simple answers in humanity's relationship with nature.",
        "genre": "Animation/Fantasy", "year": 1997,
        "themes": ["nature vs industry", "war", "morality", "identity", "coexistence", "spirits"],
        "mood": ["epic", "dark", "complex", "beautiful", "intense"]
    },
    {
        "title": "Your Name",
        "description": "A teenage boy and girl in Japan begin switching bodies intermittently, falling in love before a catastrophic event separates them. A gorgeous, emotionally devastating anime about connection across time, distance, and memory.",
        "genre": "Animation/Romance", "year": 2016,
        "themes": ["connection", "love", "time", "identity", "memory", "fate"],
        "mood": ["romantic", "beautiful", "emotional", "bittersweet", "magical"]
    },
    {
        "title": "Coco",
        "description": "A young Mexican boy accidentally enters the Land of the Dead and must find his deceased great-great-grandfather to return home. A deeply moving celebration of family, memory, music, and what it means to be remembered.",
        "genre": "Animation/Drama", "year": 2017,
        "themes": ["family", "memory", "death", "music", "heritage", "legacy"],
        "mood": ["joyful", "emotional", "colorful", "heartbreaking", "uplifting"]
    },
    {
        "title": "The Lion King",
        "description": "A young lion prince is forced into exile after his uncle murders his father, eventually reclaiming his rightful place. A mythic, Shakespearean animated epic about responsibility, grief, identity, and the courage to face who you are.",
        "genre": "Animation/Drama", "year": 1994,
        "themes": ["responsibility", "grief", "identity", "revenge", "coming-of-age", "family"],
        "mood": ["epic", "emotional", "tragic", "uplifting", "grand"]
    },
    {
        "title": "Into the Spider-Verse",
        "description": "Miles Morales becomes Spider-Man and must team up with alternate-universe versions of the character to save New York. A revolutionary animated film that redefines what animated cinema can look like and feel like.",
        "genre": "Animation/Action", "year": 2018,
        "themes": ["identity", "belonging", "family", "self-acceptance", "heroism", "difference"],
        "mood": ["exhilarating", "emotional", "cool", "funny", "inspiring"]
    },
    {
        "title": "Grave of the Fireflies",
        "description": "Two young siblings struggle to survive in Japan during the final months of World War II after their city is firebombed. The most heartbreaking film ever made — an anti-war masterpiece told from the eyes of the most innocent victims.",
        "genre": "Animation/Drama", "year": 1988,
        "themes": ["war", "survival", "childhood", "loss", "family", "grief"],
        "mood": ["devastating", "heartbreaking", "somber", "profound", "beautiful"]
    },

    # ── WAR / HISTORICAL ──────────────────────────────────────────────
    {
        "title": "1917",
        "description": "Two young British soldiers are given an impossible mission — to cross no man's land and deliver a message that could save 1,600 lives. Presented as a single, unbroken shot, a visceral, immediate portrait of war as chaos.",
        "genre": "War/Drama", "year": 2019,
        "themes": ["war", "survival", "sacrifice", "duty", "brotherhood", "hope"],
        "mood": ["intense", "tense", "visceral", "emotional", "immersive"]
    },
    {
        "title": "Dunkirk",
        "description": "The evacuation of Allied soldiers from the beaches of France in 1940 is told across three interconnected timelines. An experiential, visceral masterpiece that puts the audience inside the terror and chaos of war with minimal dialogue.",
        "genre": "War/Thriller", "year": 2017,
        "themes": ["survival", "war", "courage", "duty", "time", "community"],
        "mood": ["tense", "immersive", "visceral", "intense", "epic"]
    },
    {
        "title": "Saving Private Ryan",
        "description": "Following the D-Day invasion, a squad of soldiers is sent behind enemy lines to retrieve a paratrooper whose three brothers have been killed in action. The first thirty minutes redefine how war is depicted in cinema — and the film never lets you forget the cost.",
        "genre": "War/Drama", "year": 1998,
        "themes": ["war", "sacrifice", "duty", "brotherhood", "loss", "leadership"],
        "mood": ["devastating", "intense", "visceral", "emotional", "harrowing"]
    },
    {
        "title": "Full Metal Jacket",
        "description": "A platoon of Marines is trained into killing machines, then sent to Vietnam where the gap between idealism and horror becomes insurmountable. Kubrick's clinical dissection of the dehumanization required to make a soldier.",
        "genre": "War/Drama", "year": 1987,
        "themes": ["dehumanization", "war", "identity", "violence", "military culture", "trauma"],
        "mood": ["dark", "disturbing", "cold", "intense", "disorienting"]
    },
    {
        "title": "Apocalypse Now",
        "description": "A U.S. Army captain is sent into the jungles of Cambodia to assassinate a rogue Special Forces colonel who commands his own private army. A hallucinatory masterpiece about the moral insanity of war and the darkness within the human heart.",
        "genre": "War/Drama", "year": 1979,
        "themes": ["madness", "war", "moral collapse", "darkness", "imperialism", "identity"],
        "mood": ["hallucinatory", "dark", "epic", "disturbing", "haunting"]
    },
    {
        "title": "Hacksaw Ridge",
        "description": "True story of Desmond Doss, a conscientious objector who served as a combat medic in World War II and saved 75 men at the Battle of Okinawa without firing a single shot. A brutal and deeply moving portrait of faith and extraordinary courage.",
        "genre": "War/Drama", "year": 2016,
        "themes": ["faith", "courage", "pacifism", "war", "sacrifice", "conviction"],
        "mood": ["intense", "inspiring", "brutal", "emotional", "powerful"]
    },

    # ── FOREIGN LANGUAGE ──────────────────────────────────────────────
    {
        "title": "A Separation",
        "description": "An Iranian couple's decision to separate cascades into a complex legal and moral battle involving their daughter, a caretaker, and questions of justice. A masterpiece of ambiguity — a film where every character is simultaneously right and wrong.",
        "genre": "Drama", "year": 2011,
        "themes": ["marriage", "morality", "justice", "class", "family", "truth"],
        "mood": ["tense", "complex", "intimate", "emotional", "thought-provoking"]
    },
    {
        "title": "The Lives of Others",
        "description": "A Stasi agent in East Germany conducting surveillance on a playwright gradually becomes emotionally entangled in his subject's life. A profound, devastating portrait of art's power to humanize even those trained to destroy it.",
        "genre": "Drama/Thriller", "year": 2006,
        "themes": ["surveillance", "art", "humanity", "freedom", "oppression", "redemption"],
        "mood": ["tense", "moving", "quiet", "powerful", "haunting"]
    },
    {
        "title": "Pan's Labyrinth",
        "description": "A young girl in post-Civil War Spain escapes into an elaborate, dark fantasy world of fauns and fairies to cope with the brutal world around her. A visually ravishing fairy tale about imagination, fascism, and the cost of defiance.",
        "genre": "Fantasy/Drama", "year": 2006,
        "themes": ["escapism", "war", "imagination", "innocence", "fascism", "courage"],
        "mood": ["dark", "beautiful", "emotional", "magical", "haunting"]
    },
    {
        "title": "Roma",
        "description": "A year in the life of a middle-class Mexico City family and their live-in housekeeper in the early 1970s. Cuarón's deeply personal, visually stunning semi-autobiographical portrait of class, love, and the women who hold families together.",
        "genre": "Drama", "year": 2018,
        "themes": ["class", "family", "love", "loss", "identity", "motherhood", "politics"],
        "mood": ["quiet", "beautiful", "melancholic", "intimate", "powerful"]
    },
    {
        "title": "Wild Strawberries",
        "description": "An elderly professor reflects on his life during a road trip with his daughter-in-law to receive an honorary degree. Bergman's most humane film — a meditation on regret, memory, and the chance to truly see your life before it ends.",
        "genre": "Drama", "year": 1957,
        "themes": ["aging", "regret", "memory", "family", "redemption", "mortality"],
        "mood": ["reflective", "melancholic", "quiet", "profound", "bittersweet"]
    },
    {
        "title": "Crouching Tiger, Hidden Dragon",
        "description": "Two masters of martial arts chase a stolen sword through ancient China while a rebellious young aristocrat follows her heart and destiny. A sweeping wuxia epic about desire, freedom, and the sacrifices of duty.",
        "genre": "Action/Drama", "year": 2000,
        "themes": ["desire", "freedom", "duty", "destiny", "honor", "love"],
        "mood": ["beautiful", "romantic", "melancholic", "epic", "lyrical"]
    },
    {
        "title": "Das Boot",
        "description": "A German submarine crew endures the claustrophobic terror of World War II patrol missions in the Atlantic. The definitive submarine film — a suffocating portrait of the ordinary men turned into instruments of war.",
        "genre": "War/Drama", "year": 1981,
        "themes": ["war", "survival", "claustrophobia", "brotherhood", "duty", "fear"],
        "mood": ["tense", "claustrophobic", "intense", "harrowing", "realistic"]
    },
    {
        "title": "Bicycle Thieves",
        "description": "A poor Italian man and his son search the streets of Rome for his stolen bicycle, which he desperately needs to keep his new job. A heartbreaking neorealist classic about poverty, dignity, and the love between a father and son.",
        "genre": "Drama", "year": 1948,
        "themes": ["poverty", "dignity", "fatherhood", "desperation", "society", "class"],
        "mood": ["heartbreaking", "intimate", "powerful", "compassionate", "quiet"]
    },

    # ── DOCUMENTARY ───────────────────────────────────────────────────
    {
        "title": "Free Solo",
        "description": "Rock climber Alex Honnold attempts to free solo climb El Capitan's 3,000-foot vertical rock face — without a rope. A terrifying, beautiful portrait of obsession, courage, and what drives someone to risk everything.",
        "genre": "Documentary", "year": 2018,
        "themes": ["obsession", "courage", "achievement", "risk", "solitude", "perfectionism"],
        "mood": ["tense", "awe-inspiring", "inspiring", "visceral", "beautiful"]
    },
    {
        "title": "Won't You Be My Neighbor?",
        "description": "An exploration of the life and work of Fred Rogers, the beloved host of Mister Rogers' Neighborhood who dedicated his life to nurturing the emotional lives of children. A profoundly moving portrait of radical kindness in a cynical world.",
        "genre": "Documentary", "year": 2018,
        "themes": ["kindness", "childhood", "empathy", "television", "love", "society"],
        "mood": ["warm", "emotional", "inspiring", "gentle", "uplifting"]
    },
    {
        "title": "Amy",
        "description": "A portrait of Amy Winehouse from her early teenage years to her death at 27, using home videos, candid footage, and personal accounts. A devastating examination of how talent is exploited and destroyed by fame, addiction, and the media.",
        "genre": "Documentary/Music", "year": 2015,
        "themes": ["addiction", "fame", "talent", "media", "love", "self-destruction"],
        "mood": ["heartbreaking", "intimate", "devastating", "powerful", "sad"]
    },
    {
        "title": "Making a Murderer",
        "description": "Documentary following Steven Avery, a man who was exonerated of a crime after 18 years in prison only to be charged with murder shortly after. A gripping, infuriating portrait of systemic injustice and the fallibility of the legal system.",
        "genre": "Documentary/Crime", "year": 2015,
        "themes": ["injustice", "legal system", "crime", "truth", "corruption", "class"],
        "mood": ["infuriating", "gripping", "disturbing", "tense", "thought-provoking"]
    },

    # ── INDIE / COMING-OF-AGE ─────────────────────────────────────────
    {
        "title": "Lady Bird",
        "description": "A wildly determined Sacramento teenager navigates her tumultuous senior year of high school, her complicated relationship with her mother, and her dream of escaping to college in New York. A perfectly observed, deeply funny and moving portrait of becoming yourself.",
        "genre": "Drama/Comedy", "year": 2017,
        "themes": ["identity", "mother-daughter relationship", "growing up", "ambition", "belonging"],
        "mood": ["funny", "emotional", "sharp", "warm", "honest"]
    },
    {
        "title": "The Perks of Being a Wallflower",
        "description": "An introverted teenager navigating trauma finds friendship in a group of charismatic misfits during his freshman year of high school. A deeply empathetic portrait of adolescence, mental health, and the saving grace of finding your people.",
        "genre": "Drama/Coming-of-Age", "year": 2012,
        "themes": ["trauma", "friendship", "mental health", "identity", "growing up", "love"],
        "mood": ["emotional", "nostalgic", "warm", "bittersweet", "tender"]
    },
    {
        "title": "Little Miss Sunshine",
        "description": "A dysfunctional family takes a road trip from New Mexico to California so their young daughter can compete in a beauty pageant. A wonderfully funny and deeply humane comedy about failure, acceptance, and the bizarre value of loving your family.",
        "genre": "Comedy/Drama", "year": 2006,
        "themes": ["family dysfunction", "failure", "acceptance", "identity", "dreams", "love"],
        "mood": ["funny", "heartfelt", "bittersweet", "warm", "quirky"]
    },
    {
        "title": "Juno",
        "description": "A sharp, witty sixteen-year-old deals with an unplanned pregnancy and her decision to give the baby up for adoption. A funny, compassionate indie that manages to be both unconventional and deeply warm-hearted.",
        "genre": "Comedy/Drama", "year": 2007,
        "themes": ["teenage pregnancy", "identity", "love", "growing up", "adoption", "relationships"],
        "mood": ["quirky", "warm", "funny", "bittersweet", "charming"]
    },
    {
        "title": "Almost Famous",
        "description": "A fifteen-year-old aspiring music journalist goes on tour with a rising band in the early 1970s. A glorious, deeply personal love letter to rock and roll, journalism, and the beautiful chaos of teenage discovery.",
        "genre": "Drama/Comedy", "year": 2000,
        "themes": ["music", "adolescence", "belonging", "journalism", "identity", "coming-of-age"],
        "mood": ["nostalgic", "warm", "joyful", "bittersweet", "romantic"]
    },
    {
        "title": "Submarine",
        "description": "A precocious Welsh teenager tries to save his parents' marriage and lose his virginity before his sixteenth birthday. A darkly funny, visually inventive coming-of-age film about the exquisite self-consciousness of early adolescence.",
        "genre": "Comedy/Drama", "year": 2010,
        "themes": ["adolescence", "love", "family", "identity", "awkwardness", "growing up"],
        "mood": ["quirky", "bittersweet", "funny", "nostalgic", "charming"]
    },

    # ── BIOPIC ────────────────────────────────────────────────────────
    {
        "title": "Bohemian Rhapsody",
        "description": "The story of the rock band Queen and lead singer Freddie Mercury's life from obscurity to global stardom, culminating in their iconic Live Aid performance. A crowd-pleasing celebration of music, identity, and the search for belonging.",
        "genre": "Biopic/Drama", "year": 2018,
        "themes": ["identity", "music", "fame", "sexuality", "belonging", "friendship"],
        "mood": ["uplifting", "emotional", "entertaining", "celebratory", "bittersweet"]
    },
    {
        "title": "Rocketman",
        "description": "A fantasy musical about the highs and lows of Elton John's breakthrough years, told through his own iconic songs. A bold, surreal, emotionally honest portrait that never lets its spectacle outweigh its humanity.",
        "genre": "Biopic/Musical", "year": 2019,
        "themes": ["identity", "loneliness", "fame", "addiction", "love", "music", "acceptance"],
        "mood": ["spectacular", "emotional", "bittersweet", "energetic", "honest"]
    },
    {
        "title": "Selma",
        "description": "The story of the 1965 voting rights marches from Selma to Montgomery, Alabama, led by Martin Luther King Jr. A powerful, urgent reminder that rights must be fought for — and the incredible personal cost of leading that fight.",
        "genre": "Biopic/Historical", "year": 2014,
        "themes": ["civil rights", "courage", "leadership", "racism", "democracy", "sacrifice"],
        "mood": ["powerful", "moving", "inspiring", "tense", "important"]
    },
    {
        "title": "The Imitation Game",
        "description": "The story of Alan Turing, the mathematical genius who cracked the Nazis' Enigma code and was later prosecuted for his homosexuality. A riveting, devastating portrait of an extraordinary mind destroyed by the society he helped to save.",
        "genre": "Biopic/Drama", "year": 2014,
        "themes": ["genius", "prejudice", "LGBTQ", "war", "secrets", "tragedy"],
        "mood": ["tense", "tragic", "inspiring", "emotional", "powerful"]
    },
    {
        "title": "Moneyball",
        "description": "The true story of how Oakland A's general manager Billy Beane revolutionized baseball through data analytics and unconventional thinking. A quietly thrilling portrait of how to change the world from inside a system that doesn't want to change.",
        "genre": "Drama/Sports", "year": 2011,
        "themes": ["innovation", "underdog", "data vs tradition", "failure", "ambition", "baseball"],
        "mood": ["gripping", "inspiring", "intelligent", "warm", "tense"]
    },

    # ── SUPERHERO / BLOCKBUSTER ───────────────────────────────────────
    {
        "title": "Avengers: Infinity War",
        "description": "The Avengers and their allies must stop Thanos from collecting all six Infinity Stones and wiping out half of all life in the universe. An unprecedented feat of franchise storytelling that earns its devastating conclusion.",
        "genre": "Action/Sci-Fi", "year": 2018,
        "themes": ["sacrifice", "power", "mortality", "teamwork", "loss", "destiny"],
        "mood": ["epic", "intense", "emotional", "thrilling", "devastating"]
    },
    {
        "title": "Black Panther",
        "description": "T'Challa returns home to the isolated technologically advanced African kingdom of Wakanda to take his place as king, only to be challenged by a powerful enemy. A groundbreaking superhero film that is also a rich political drama about identity and responsibility.",
        "genre": "Action/Drama", "year": 2018,
        "themes": ["identity", "responsibility", "heritage", "power", "colonialism", "innovation"],
        "mood": ["epic", "empowering", "political", "thrilling", "emotional"]
    },
    {
        "title": "Logan",
        "description": "An aging, ailing Logan cares for a nearly incapacitated Charles Xavier while being hunted by dark forces and reluctantly protecting a young mutant girl. A brutal, elegiac Western about legacy, aging, and the impossibility of running from who you are.",
        "genre": "Action/Drama", "year": 2017,
        "themes": ["aging", "legacy", "fatherhood", "violence", "sacrifice", "identity"],
        "mood": ["dark", "brutal", "emotional", "melancholic", "powerful"]
    },

    # ── PSYCHOLOGICAL ─────────────────────────────────────────────────
    {
        "title": "Fight Club",
        "description": "An insomniac office worker and a soap salesman form an underground fight club that evolves into something far more dangerous. A furious, dazzling critique of consumerism, masculinity, and the seductive appeal of chaos.",
        "genre": "Drama/Thriller", "year": 1999,
        "themes": ["identity", "masculinity", "consumerism", "anarchy", "duality", "self-destruction"],
        "mood": ["anarchic", "dark", "intense", "clever", "provocative"]
    },
    {
        "title": "American Psycho",
        "description": "A wealthy investment banker in 1980s Manhattan may or may not be killing people while obsessing over business cards, morning routines, and status. A viciously funny, deeply unsettling satire about capitalism, toxic masculinity, and the emptiness of status.",
        "genre": "Thriller/Dark Comedy", "year": 2000,
        "themes": ["consumerism", "toxic masculinity", "identity", "status", "violence", "capitalism"],
        "mood": ["darkly funny", "disturbing", "satirical", "cold", "stylish"]
    },
    {
        "title": "Donnie Darko",
        "description": "A troubled teenager is haunted by visions of a giant rabbit who tells him the world will end in 28 days. A cult classic that blends suburban angst, time travel, and existential dread into a genuinely unique cinematic experience.",
        "genre": "Sci-Fi/Drama", "year": 2001,
        "themes": ["time travel", "mental illness", "fate", "adolescence", "existentialism", "death"],
        "mood": ["mysterious", "dark", "atmospheric", "melancholic", "mind-bending"]
    },
    {
        "title": "Gone Girl",
        "description": "On the morning of their fifth anniversary, Amy Dunne vanishes and her husband Nick becomes the prime suspect as the investigation reveals the dark truth of their marriage. A razor-sharp psychological thriller about performance, resentment, and media complicity.",
        "genre": "Thriller", "year": 2014,
        "themes": ["marriage", "identity", "manipulation", "media", "perception", "secrets"],
        "mood": ["cold", "tense", "disturbing", "darkly funny", "twisty"]
    },

    # ── SPORTS ────────────────────────────────────────────────────────
    {
        "title": "Rocky",
        "description": "A small-time Philadelphia boxer gets a once-in-a-lifetime shot at the world heavyweight championship against the reigning champion. The definitive underdog story — a deeply human film about dignity, love, and the meaning of simply going the distance.",
        "genre": "Sports/Drama", "year": 1976,
        "themes": ["underdog", "determination", "love", "ambition", "dignity", "class"],
        "mood": ["inspiring", "emotional", "warm", "triumphant", "gritty"]
    },
    {
        "title": "Creed",
        "description": "The son of the legendary boxer Apollo Creed trains with a retired Rocky Balboa in hopes of following in his father's footsteps. A modern, emotionally rich sequel that earns the legacy of its predecessor through character rather than nostalgia.",
        "genre": "Sports/Drama", "year": 2015,
        "themes": ["legacy", "identity", "fatherhood", "ambition", "mentorship", "boxing"],
        "mood": ["inspiring", "emotional", "gritty", "triumphant", "powerful"]
    },
    {
        "title": "Hoop Dreams",
        "description": "A documentary following two Black teenagers from Chicago who dream of making it to the NBA, filmed over five years. A monumental portrait of ambition, race, family, and the American Dream's broken promises.",
        "genre": "Documentary/Sports", "year": 1994,
        "themes": ["ambition", "race", "family", "exploitation", "dreams", "poverty"],
        "mood": ["powerful", "emotional", "complex", "heartbreaking", "compelling"]
    },
]