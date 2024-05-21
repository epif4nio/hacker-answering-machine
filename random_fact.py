import random

# List of random facts obtained from https://www.cosmopolitan.com/uk/worklife/a33367076/fun-facts-random/

RANDOM_FACTS = ["Avocados are a fruit, not a vegetable. They're technically considered a single-seeded berry, believe it or not.",
"The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space.",
"Trypophobia is the fear of closely-packed holes. Or more specifically, an aversion to the sight of irregular patterns or clusters of small holes or bumps. No crumpets for them, then.",
"Allodoxaphobia is the fear of other people's opinions. It's a rare social phobia that's characterised by an irrational and overwhelming fear of what other people think.",
"Australia is wider than the moon. The moon sits at 3400km in diameter, while Australia’s diameter from east to west is almost 4000km.",
"'Mellifluous' is a sound that is pleasingly smooth and musical to hear.",
"The Spice Girls were originally a band called Touch. When we first started [with the name Touch], we were pretty bland, Mel C told The Guardian in 2018. We felt like we had to fit into a mould.",
"Emma Bunton auditioned for the role of Bianca Butcher in Eastenders. Baby Spice already had a small part in the soap back in the 90s but tried out for a full-time role. She was pipped to the post by Patsy Palmer but ended up auditioning for the Spice Girls not long after.",
"Human teeth are the only part of the body that cannot heal themselves. Teeth are coated in enamel which is not a living tissue.",
"It's illegal to own just one guinea pig in Switzerland. It's considered animal abuse because they're social beings and get lonely.",
"The Ancient Romans used to drop a piece of toast into their wine for good health - hence why we 'raise a toast'.",
"The heart of a shrimp is located in its head. They also have an open circulatory system, which means they have no arteries and their organs float directly in blood.",
"Amy Poehler was only seven years older than Rachel McAdams when she took on the role of cool mom in Mean Girls. Rachel was 25 as Regina George - Amy was 32 as her mum.",
"People are more creative in the shower. When we take a warm shower, we experience an increased dopamine flow that makes us more creative.",
"Baby rabbits are called kits. Cute!",
"The unicorn is the national animal of Scotland. It was apparently chosen because of its connection with dominance and chivalry as well as purity and innocence in Celtic mythology.",
"The first aeroplane flew on December 17, 1903. Wilbur and Orville Wright made four brief flights at Kitty Hawk, North Carolina, with their first powered aircraft, aka the first airplane.",
"Venus is the only planet to spin clockwise. It travels around the sun once every 225 Earth days but it rotates clockwise once every 243 days.",
"Nutmeg is a hallucinogen. The spice contains myristicin, a natural compound that has mind-altering effects if ingested in large doses.",
"A 73-year-old bottle of French Burgundy became the most expensive bottle of wine ever sold at auction in 2018, going for $558,000 (approx £439,300). The bottle of 1945 Romanee-Conti sold at Sotheby for more than 17 times its original estimate of $32,000.",
"Competitive art used to be an Olympic sport. Between 1912 and 1948, the international sporting events awarded medals for music, painting, sculpture and architecture. Shame it didn't catch on, the famous pottery scene in Ghost could have won an Olympic medal as well as an Academy Award for the best screenplay.",
"A chef's hat has 100 pleats. Apparently, it's meant to represent the 100 ways you can cook an egg. Wonder if Gordon Ramsay knows that.",
"In 2014, there was a Tinder match in Antarctica. Two research scientists matched on the global dating app in the most remote part of the world - a man working at the United States Antarctic McMurdo Station and a woman camping a 45-minute helicopter ride away. What are the chances?!",
"The Spanish national anthem has no words. The 'Marcha Real' is one of only four national anthems in the world (along with those of Bosnia and Herzegovina, Kosovo, and San Marino) to have no official lyrics.",
"The Japanese word 'Kuchi zamishi' is the act of eating when you're not hungry because your mouth is lonely. We do this all the time.",
"The probability of a blue lobster existing is widely touted as being one in two million. Bright blue lobsters are so-coloured because of a genetic abnormality that causes them to produce more of a certain protein than others.",
"There’s only one letter that doesn’t appear in any American state name. There's a Z in Arizona and an X in Texas, but no Q in any of them.",
"Louboutins' iconic red soles were inspired by Andy Warhol. The 60s pop artist's drawing Flowers caught the eye of the famous designer which gave him the idea to add the infamous sole to his designs.",
"A book called 'A la recherche du temps perdu' by Marcel Proust contains an estimated 9,609,000 characters, making it the longest book in the world. The title translates to Remembrance of Things Past.",
"Google images was literally created after Jennifer Lopez wore that infamous dress at the 2000 Grammys. So many people were searching for her outfit, the search engine added an imagine function.",
"Big Ben's clock stopped at 10:07 p.m. on 27 May 2005, most likely due to an extremely hot temperature of 31.8 degrees Celsius.",
"Walt Disney currently holds the most Academy Awards. Disney won 26 Oscars over the course of his career and was nominated a grand total of 59 times.",
"There's a fruit that tastes like chocolate pudding. Can we get in on this? Apparently, there's a fruit native to Central and South America called black sapote that tastes like chocolate and sweet custard.",
"Queen Elizabeth II was a trained mechanic. When she was 16, the Queen joined the British employment agency at the Labour Exchange and learned the basics of truck repair. Apparently, she can repair tires and repair engines. Is there anything the Queen can't do?!",
"The Easter Island heads have bodies. Those iconic stone heads - you know the ones. In the 2010s, archaeologists found that two of the Pacific Island figures actually had torsos that measured as high as 33 feet.",
"M&Ms are named after the businessmen who created them. But what do the M's stand for? Forrest Mars and Bruce Murrie, who apparently didn't have the best relationship as Mars leveraged Murrie out of his 20% share of the business before it became the biggest-selling sweet in the US. Ouch.",
"Pigeons can tell the difference between Picasso and Monet. What?! A 1995 study shows that the birds can differentiate between the two artists.",
"The real name for a hashtag is an octothorpe. The 'octo' refers to the eight points in the symbol, but according to the Merriam-Webster dictionary the 'thorpe' part is a mystery.",
"The actors who voiced Mickey and Minnie mouse got married in real life. Russi Taylor (Minnie) and Wayne Allwine (Mickey) tied the knot in 1991.",
"You can hear a blue whale's heartbeat from over 2 miles away. Blue whales weigh an average of between 130,000 and 150,000kg, with their hearts weighing roughly 180kg.",
"The last letter added to the English alphabet was 'J'. The letter dates back to 1524, and before that the letter 'i' was used for both the 'i' and 'j' sounds.",
"There is actually a word for someone giving an opinion on something they know nothing about. An 'ultracrepidarian' is someone who voices thoughts beyond their expertise.",
"The Chupa Chups logo was designed by Salvador Dalí. The surrealist artist designed the logo in 1969.",
"Ketchup was once sold as medicine. The condiment was prescribed and sold to people suffering with indigestion back in 1834.",
"The world's longest walking distance is 14,000 miles. You can walk from Magadan in Russia to Cape Town in South Africa. It requires no flying or sailing - just bridges and open roads.",
"The moon has moonquakes. They happen due to tidal stresses connected to the distance between the moon and the Earth.",
"Humans are the only animals that blush. Apparently, we're also the only animals that experience embarrassment, too. This is because it's a complex emotion that involves understanding other people's opinions.",
"All the clocks in Pulp Fiction are set to 4.20. Looks like we're going to have to rewatch the film to find out.",
"Kim Kardashian has a 'glam' clause in her will. It states that if she's ever in a position where she can't get ready herself, can't communicate, or she's unconscious, someone has to make sure her hair, nails, and makeup are all perfect.",
"An ostrich's eye is bigger than its brain. This could be why the birds often run round in circles when trying to escape predators despite their fast running speed.",
"A jiffy is an actual unit of time. It's 1/100th of a second.",
"You can't hum if you hold your nose. Hands up if you just tried it!",
"Vatican City is the smallest country in the world. It's 120 times smaller than the island of Manhattan.",
"Japan has over 200 flavours of Kit Kats. They're exclusively created for different regions, cities, and seasons. There are some tasty-sounding ones like banana, blueberry cheesecake and Oreo ice cream, as well as some very questionable ones like baked potato, melon and cheese, wasabi, and vegetable juice.",
"Kris Jenner has 12 grandchildren. (Extra points if you can list them in order of age.) Kourtney Kardashianhas three children, Mason, 13, Penelope, 10, and Reign, 8. Kim has four, North, 9, Saint, 7, Chicago, 5 and Psalm, 3. Rob has one, Dream, 6. Khloé has two, True, 4 and a baby boy (a name hasn't been announced yet), born August 2022. Kylie has two, Stormi, 5 and Aire, one.",
"A crocodile cannot stick its tongue out. They have a membrane that holds their tongue in place on the roof of their mouth so it can't move.",
"Pigs can't look up into the sky. The anatomy of their spine and neck muscles limits their movement and restricts their head from being able to look upwards.",
"Kim Kardashian knows the alphabet in sign language. Apparently, she used it to cheat on tests with her friends at school.",
"In the course of an average lifetime, while sleeping you could eat around 70 different insects and 10 spiders, or more. Ew.",
"Everyone's tongue print is different. Like the fingerprint, it has unique features that differ from person to person.",
"It would take 19 minutes to fall to the centre of the Earth. Scientists have worked this out, they haven't tried it in real life.",
"The Night's Watch cloaks in Game of Thrones were made from Ikea rugs. The show bought the rugs, shaved them down and then dyed them to make the cloaks.",
"The iCarly high school set was also used for Saved by the Bell and That's So Raven. That's why it looks so familiar!",
"Harry Styles has four nipples. They stem from a common condition called polythelia.",
"People used to say prunes instead of cheese when getting their pictures taken. In the 1840s, a cheesy grin was seen as childish, so a London photographer told people to say prunes to keep their mouths tight. Now you know why people never smiled in old photos.",
"Blue whale tongues can weigh as much as an elephant. Their hearts can also weigh almost a tonne and only need to beat once every ten seconds.",
"Queen Elizabeth II had a stand-in to make sure the sun wouldn't get in her eyes. Ella Slack was a similar height to the late Queen, so she would rehearse big events beforehand to make sure everything would be comfortable for the monarch. However, she wasn't allowed to sit on the throne, so she had to squat above it.",
"There's an ant species unique to New York City. Called ManhattAnts, biologists found them in a specific 14-block strip of the city.",
"The Eiffel Tower was originally intended for Barcelona. The Spanish city thought it was too ugly, so Gustave Eiffel pitched it to Paris instead. French critics weren't too thrilled either, but it's one of the most famous landmarks in the world today.",
"There's only one Shell garage actually shaped like a Shell. There was actually eight built in the 1930s, but only one remains in North Carolina.",
"The shortest commercial flight in the world is in Scotland. Regional airline Loganair flies between the islands Westray and Papa Westray. The journey is just 1.7 miles and takes 90 seconds.",
"Dolphins have names for one another. According to National Geographic, dolphins use a unique whistle to distinguish between different members in their pod.",
"The blob of toothpaste on a toothbrush has a name. It's called a 'nurdle' and there was once a lawsuit over which toothpaste company had the right to portray it.",
"One part of Istanbul is in Europe and the other is in Asia. Part of it neighbours Greece and Bulgaria (therefore sitting in Europe) and the other part neighbours Syria, Iran, and Iraq beyond Turkey’s borders (therefore classing as Asia). The Bosphorus Strait runs between them - a narrow body of water that connects the Black Sea to the Mediterranean Sea via the Sea of Marmara.",
"There are more than 1,000 types of bananas growing in the world. These can then be divided into 50 categories"]

def get():
    return RANDOM_FACTS[random.randrange(len(RANDOM_FACTS))]