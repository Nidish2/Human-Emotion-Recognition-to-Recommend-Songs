import pandas as pd
import numpy as np
import random
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define the number of songs for each mood
n_songs_per_mood = 150
total_songs = n_songs_per_mood * 4  # 4 moods: Happy, Sad, Calm, Energetic

# Lists of popular Indian artists from various languages and genres
artists = [
    # Bollywood/Hindi
    'Arijit Singh', 'Neha Kakkar', 'Badshah', 'Jubin Nautiyal', 'Shreya Ghoshal',
    'A.R. Rahman', 'Amit Trivedi', 'Armaan Malik', 'Atif Aslam', 'Darshan Raval',
    'Guru Randhawa', 'Yo Yo Honey Singh', 'Sunidhi Chauhan', 'Vishal-Shekhar', 'Sonu Nigam',
    'Pritam', 'Shankar-Ehsaan-Loy', 'Sachet-Parampara', 'Tanishk Bagchi', 'B Praak',
    'Jasleen Royal', 'Diljit Dosanjh', 'Nucleya', 'Ritviz', 'Divine',
    
    # Tamil
    'Anirudh Ravichander', 'G.V. Prakash Kumar', 'Yuvan Shankar Raja', 'D. Imman', 'Sid Sriram',
    'Hariharan', 'Benny Dayal', 'Pradeep Kumar', 'Chinmayi Sripada', 'Hip Hop Tamizha',
    
    # Telugu
    'S. Thaman', 'Devi Sri Prasad', 'M.M. Keeravani', 'Hiphop Tamizha',
    
    # Malayalam
    'Vidyasagar', 'Gopi Sundar', 'Sushin Shyam', 'Prithviraj Sukumaran',
    
    # Punjabi
    'AP Dhillon', 'Diljit Dosanjh', 'Harrdy Sandhu', 'Karan Aujla', 'Sidhu Moose Wala',
    'Parmish Verma', 'Ammy Virk', 'Maninder Buttar', 'Jassie Gill', 'Shubh',
    
    # Independent/Indie
    'Prateek Kuhad', 'The Local Train', 'Ritviz', 'Divine', 'When Chai Met Toast',
    'Papon', 'Raghu Dixit', 'Taba Chake', 'Indian Ocean', 'Parvaaz',
    'Agnee', 'Ankur Tewari', 'Lifafa', 'Madboy/Mink', 'Seedhe Maut'
]

# Create lists of song names for each mood
# Happy songs
happy_songs = [
    'Balam Pichkari', 'London Thumakda', 'Badtameez Dil', 'The Breakup Song', 'Cutiepie',
    'Kamariya', 'Kar Gayi Chull', 'Ghungroo', 'Swag Se Swagat', 'Gallan Goodiyaan',
    'Malhari', 'Baar Baar Dekho', 'Nachde Ne Saare', 'Ainvayi Ainvayi', 'Desi Girl',
    'Dhinka Chika', 'Chittiyaan Kalaiyaan', 'Senorita', 'Tune Maari Entriyaan', 'Kala Chashma',
    'Punjabi Wedding Song', 'Banno Tera Swagger', 'Ghar More Pardesiya', 'Dilbaro', 'Coca Cola',
    'Aaj Ki Raat', 'Navrai Majhi', 'Ik Junoon', 'Thodi Si Daru', 'Chamak Challo',
    'Nachdi Phira', 'Rangtaari', 'High Heels', 'Radha', 'Dil Dhadakne Do',
    'Hawan Karenge', 'Saturday Saturday', 'Gal Ban Gayi', 'Kaala Chashma', 'Humma Humma (2017)',
    'Naach Meri Jaan', 'Mind Na Kariyo', 'Kudiye Ni', 'Proper Patola', 'Morni Banke',
    'Cheap Thrills (Hindi)', 'Brown Rang', 'Blue Eyes', 'Bijlee Bijlee', 'Koka',
    'No Competition', 'Sauda Khara Khara', 'Hauli Hauli', 'Slowly Slowly', 'Wakhra Swag',
    'Vaathi Coming', 'Arabic Kuthu', 'Saranga Dariya', 'Kutti Story', 'Master the Blaster',
    'Naanga Vera Maari', 'Ranjithame', 'Oo Antava', 'Butta Bomma', 'Ramuloo Ramulaa',
    'Bottal Khol', 'Tunak Tunak Tun', 'High Rated Gabru', 'Lehenga', 'Laembadgini',
    'Prada', 'Naagin', 'Kamariya', 'Leke Pehla Pehla Pyaar', 'Chaiyya Chaiyya',
    'Desi', '8 Parche', 'Amplifier', 'Daru Badnaam', 'Ankhiyon Se Goli Mare',
    'The Disco Song', 'Main Tera Boyfriend', 'Love Dose', 'Genda Phool', 'Chandigarh Mein',
    'Chogada', 'Kamariya', 'Jhinghat', 'Ek Diamond Da Haar', 'Thumka',
    'Sajan Bendre', 'Coka 2.0', 'Nikle Currant', 'Ankh Lad Jave', 'First Class',
    'Zingaat Hindi', 'Zingaat Marathi', 'Paagal', 'Garmi', 'Ghagra',
    'Fevicol Se', 'Chikni Chameli', 'Sheila Ki Jawani', 'Jai Jai Shivshankar', 'Ghungroo',
    'Besharam Rang', 'Jhoome Jo Pathaan', 'What Jhumka?', 'Janam Janam', 'Tauba Tauba',
    'Taare Gin Gin', 'Nehu Da Vyah', 'Akhiyaan Gulaab', 'Do You Know', 'Naja',
    'Kala Chasma', 'Dil Diyan Gallan', 'Veham', 'Habibi', 'Temporary Pyar',
    'Laung Laachi', 'Naah', 'Kaun Nachdi', 'Lamborghini', 'Taare'
]

# Sad songs
sad_songs = [
    'Channa Mereya', 'Agar Tum Saath Ho', 'Tum Hi Ho', 'Ae Dil Hai Mushkil', 'Kalank Title Track',
    'Naina', 'Luka Chuppi (Rang De Basanti)', 'Rozana', 'Aaoge Jab Tum', 'Tujhe Kitna Chahne Lage',
    'Phir Le Aya Dil', 'Kun Faya Kun', 'Hasi', 'Soch Na Sake', 'Khamoshiyan',
    'Zara Zara (RHTDM)', 'Sooraj Dooba Hai', 'Main Dhoondne Ko Zamaane Mein', 'Humdard', 'Ghar',
    'Lo Maan Liya', 'Judaai', 'Hawayein', 'Sanu Ek Pal Chain', 'Muskurane',
    'Zehnaseeb', 'Tum Saath Ho', 'Jeena Jeena', 'Mann Bharryaa', 'Jaan Nisaar',
    'Bekhayali', 'Mehrama', 'Thodi Jagah', 'Tujhe Kitna Chahein Aur', 'Raataan Lambiyan',
    'Dil Na Jaaneya', 'Khairiyat', 'Kaise Hua', 'Tujhe Kitna Chahein Aur Hum', 'Taaron Ke Shehar',
    'Phir Mulaaqat', 'Tu Laung Main Elaachi', 'Pachtaoge', 'Thodi Jagah', 'Mera Pyaar Tera Pyaar',
    'Lut Gaye', 'Wafa Na Raas Aayee', 'Taaron Ke Shehar', 'Dil Tod Ke', 'Aise Na Chhoro',
    'Aaj Bhi', 'Tere Naal', 'Bhula Dunga', 'Jinke Liye', 'Meri Tarah',
    'Baarish', 'Dhadkanein Meri', 'Tu Hi Yaar Mera', 'Mere Liye Tum Kaafi Ho', 'Haan Main Galat',
    'Shayad', 'Thoda Thoda Pyaar', 'Bepanah Pyaar', 'Chhor Denge', 'Dariyaganj',
    'Dil Tod Ke', 'Bepanah Pyaar', 'Tu Mila To Haina', 'Pal Pal Dil Ke Paas', 'Pehla Pyaar',
    'Duniyaa', 'Main Jis Din Bhulaa Du', 'Bhula Dunga', 'Woh Din', 'Qismat',
    'Filhaal', 'Filhaal 2 Mohabbat', 'Koi Vi Nahi', 'Kinna Sona', 'Main Jis Din Bhulaa Du',
    'Tu Banja Gali Benaras Ki', 'Jaan Nisaar', 'Dil Jaaniye', 'Yaad Piya Ki Aane Lagi', 'Kaun Tujhe',
    'Kabira', 'Qaafirana', 'Bulleya', 'Bekhayali', 'Raabta Title Track',
    'Mere Sohneya', 'Enna Sona', 'Humsafar', 'Jaan Nisaar', 'Dil Diyan Gallan',
    'Rehna Tu', 'Sajdaa', 'Abhi Mujh Mein Kahin', 'Kabhi Alvida Naa Kehna', 'Aye Khuda',
    'Tum Mile', 'Te Amo', 'O Saathi', 'Maula Mere', 'Tere Bina (Guru)',
    'Judaai', 'Laal Ishq', 'Aayat', 'Tu Hai Ki Nahi', 'Meri Aashiqui',
    'Hamari Adhuri Kahani', 'Rozana', 'Soch Na Sake', 'Hamdard', 'Chahun Main Ya Naa',
    'Phir Kabhi', 'Mast Magan', 'Sawan Aaya Hai', 'Tu Jo Mila', 'Sapna Jahan',
    'Tu Zaroori', 'Sanam Re', 'Humnava', 'Mar Jaayen', 'Tujhe Bhula Diya',
    'Mileya Mileya', 'Bhula Dena', 'Baatein Ye Kabhi Na', 'Dard Dilo Ke', 'Jeena Jeena'
]

# Calm songs
calm_songs = [
    'Tum Se Hi', 'Sau Aasmaan', 'Main Rang Sharbaton Ka', 'Sooraj Dooba Hai', 'Kho Gaye Hum Kahan',
    'Iktara', 'Kabira (Encore)', 'Tum Ho', 'Tujhe Sochta Hoon', 'Patakha Guddi (Female)',
    'Shaam Shaandaar', 'Kaun Tujhe', 'Samjhawan', 'Khulke Jeene Ka', 'Agar Tum Saath Ho (Acoustic)',
    'Nazm Nazm', 'Thodi Der', 'Afreen Afreen (Coke Studio)', 'Sooha Saaha', 'Qaafirana',
    'Ilahi', 'Safarnama', 'Meet', 'Humsafar', 'Hawayein (Acoustic)',
    'Phir Se Ud Chala', 'Rasiya', 'Kesariya', 'Tu Jhoom', 'Heeriye',
    'Pasoori', 'Phir Aur Kya Chahiye', 'Waqt Ki Baatein', 'Dil Mere', 'Maahi Ve',
    'Nadaan Parinde', 'Tu Hai', 'Khaabon Ke Parinday', 'Tu Koi Aur Hai', 'O Rangrez',
    'Tu Aaja', 'Agar Tum Saath Ho', 'Love You Zindagi', 'Moh Moh Ke Dhaage', 'Daryaa',
    'Ranjha', 'Mann Bharryaa 2.0', 'Shauq', 'Kahaani', 'Rait Zara Si',
    'Raatan Lambiyan (Acoustic)', 'Kabhii Tumhhe', 'Lut Gaye (Acoustic)', 'Tujh Mein', 'Suna Hai',
    'Kaash', 'Baarishein', 'Jaan Ban Gaye', 'Zaroori Tha', 'Phir Le Aaya Dil',
    'Tere Liye', 'Bol Do Na Zara', 'Saiyaara', 'Tere Bina', 'Dildaara',
    'Zara Sa', 'Pehli Dafa', 'O Saathiya', 'Naina Da Kya Kasoor', 'Sun Raha Hai Na Tu',
    'Tum Hi Aana', 'Tera Yaar Hoon Main', 'Jeena Marna', 'Kabhii Tumhhe', 'Thodi Jagah',
    'Kasoor', 'Phir Kabhi', 'Dil Ibaadat', 'Tu Jo Mila', 'Tum Tak',
    'Jag Ghoomeya', 'Tere Sang Yaara', 'Thodi Der', 'Kaun Hoyega', 'Channa Mereya (Unplugged)',
    'Cold/Mess', 'Hum Jee Lenge', 'Khushi', 'Pehla Nasha', 'Lag Ja Gale',
    'Tere Jeya Hor Disda', 'Ve Maahi', 'Sanu Ek Pal Chain (Acoustic)', 'Baatein Kuch Ankahee Si', 'Zara Zara Bahekta Hai',
    'Janib', 'Bol Na Halke Halke', 'Main Tenu Samjhawan Ki', 'Abhi Na Jao Chhod Kar', 'Manwa Laage',
    'Sawan Aaya Hai', 'Jeena Jeena (Acoustic)', 'Mast Magan', 'Chhod Diya', 'Enna Sona',
    'Mere Naam Tu', 'Dil Ibaadat', 'Soch Na Sake (Acoustic)', 'Maula Mere Maula', 'Kho Gaye Hum Kahan',
    'Piya Aaye Na', 'Bin Tere', 'Dekhte Dekhte', 'Tum Hi Ho (Acoustic)', 'Main Agar Kahoon',
    'Tu Har Lamha', 'Main Jahan Rahoon', 'Bakhuda Tumhi Ho', 'Tu Mileya', 'Mera Mann',
    'Choo Lo', 'Dhuaan Dhuaan', 'Manjha', 'Tafreeh', 'Taare Ginn',
    'Jogi', 'Aahista', 'Laapata', 'Tota Maina', 'Sawayaan'
]

# Energetic songs
energetic_songs = [
    'Naatu Naatu', 'Kaavaalaa', 'Jhoome Jo Pathaan', 'Halamithi Habibo', 'Srivalli',
    'Oo Antava', 'Arabic Kuthu', 'Current Laga Re', 'Saami Saami', 'RRR Mass Anthem',
    'Pushpa: The Rise - Title Track', 'Toofan', 'Dhakka Laga Bukka', 'Ra Ra Reddy', 'Jigelu Rani',
    'Butta Bomma', 'Mind Block', 'Ramuloo Ramulaa', 'Vaathi Coming', 'Master the Blaster',
    'Kutti Story', 'Verithanam', 'Machi Open the Bottle', 'Kadhal Psycho', 'Monster',
    'Ullaallaa', 'Rowdy Baby', 'Marana Mass', 'The Monster Song', 'Enjoy Enjaami',
    'Jalabulajangu', 'Thee Thalapathy', 'Jigelu Rani', 'Dhummu Dholi', 'Pasoori',
    'Amplifier', 'Kala Chashma', 'Aaj Ki Raat', 'Aankh Marey', 'Taare Gin Gin',
    'Desi Kalakaar', 'Mercy', 'Genda Phool', 'Proper Patola', 'Naah',
    'Downtown', 'G.O.A.T.', 'Satisfya', 'Koka', 'Lamborghini',
    'Dil Chori', 'Illegal Weapon 2.0', 'Laung Laachi', 'Sakhiyaan', 'Sip Sip',
    'Prada', 'Buzz', 'Lahore', 'She Move It Like', 'Morni Banke',
    'Coka', 'Nikle Currant', 'Car Nachdi', 'Suit Suit', 'Kaun Nachdi',
    'Machayenge', 'Slowly Slowly', 'Aankh Marey', 'Saki Saki', 'O Saki Saki',
    'Ek Toh Kum Zindagani', 'Muqabla', 'Sauda Khara Khara', 'Chandigarh Mein', 'Simmba Title Track',
    'Psycho Saiyaan', 'The Jawani Song', 'Ghungroo', 'Jai Jai Shivshankar', 'Yaalai Kadhal',
    'Malang', 'Badtameez Dil', 'Selfie Le Le Re', 'Tum Todo Na', 'Bezubaan Phir Se',
    'Dhol Bajne Laga', 'Party All Night', 'Lungi Dance', 'Balam Pichkari', 'Badri Ki Dulhania',
    'Kar Gayi Chull', 'The Breakup Song', 'Desi Girl', 'Dhinka Chika', 'Munni Badnaam Hui',
    'Sooraj Dooba Hai Yaaron', 'Raat Baaki', 'Laila Main Laila', 'Tip Tip Barsa Paani (2021)', 'Chittiyaan Kalaiyaan',
    'Lat Lag Gayee', 'Malhari', 'Chokra Jawaan', 'Tattad Tattad', 'Tu Meri',
    'Saturday Saturday', 'Hook Up Song', 'Naagin', 'Kaala Chasma', 'Tauba Tauba',
    'Naah Goriye', 'Psycho', 'Lovely', 'First Class', 'The Disco Song',
    'Mauja Hi Mauja', 'Aal Izz Well', 'Kun Faya Kun (Dance)', 'Nagada Sang Dhol', 'Ram Chahe Leela',
    'Garmi', 'Illegal Weapon', 'Wakhra Swag', 'Blue Eyes', 'ABCD',
    'Kalaastar', 'Soorma', 'Aafat Waapas', 'Takkar', 'Mirchi',
    'Garmi', 'Paagal', 'Makhna', 'Genda Phool', 'Loca',
    'Bharat: The Soul of India', 'Swag Mera Desi', 'Nazar Na Lag Jaaye', 'Channa Mereya (Dance)', 'Bolna'
]

# Create dataframe with columns: name, artist, mood, popularity, year
data = []

# Helper function to generate random popularity scores
def generate_popularity(base_value):
    # Generate a value between base_value-10 and base_value+10, capped at 100
    return min(100, max(1, base_value + random.randint(-10, 10)))

# Function to assign a release year between 2003 and 2023
def assign_year():
    return random.randint(2003, 2023)

# Add Happy songs
for song in happy_songs[:n_songs_per_mood]:
    artist = random.choice(artists)
    popularity = generate_popularity(80)  # Base popularity around 80
    year = assign_year()
    data.append({
        'name': song,
        'artist': artist,
        'mood': 'Happy',
        'popularity': popularity,
        'year': year
    })

# Add Sad songs
for song in sad_songs[:n_songs_per_mood]:
    artist = random.choice(artists)
    popularity = generate_popularity(75)  # Base popularity around 75
    year = assign_year()
    data.append({
        'name': song,
        'artist': artist,
        'mood': 'Sad',
        'popularity': popularity,
        'year': year
    })

# Add Calm songs
for song in calm_songs[:n_songs_per_mood]:
    artist = random.choice(artists)
    popularity = generate_popularity(70)  # Base popularity around 70
    year = assign_year()
    data.append({
        'name': song,
        'artist': artist,
        'mood': 'Calm',
        'popularity': popularity,
        'year': year
    })

# Add Energetic songs
for song in energetic_songs[:n_songs_per_mood]:
    artist = random.choice(artists)
    popularity = generate_popularity(85)  # Base popularity around 85
    year = assign_year()
    data.append({
        'name': song,
        'artist': artist,
        'mood': 'Energetic',
        'popularity': popularity,
        'year': year
    })

# Create DataFrame
music_df = pd.DataFrame(data)

# Shuffle the dataframe
music_df = music_df.sample(frac=1).reset_index(drop=True)

# Save to CSV
music_df.to_csv('data_moods.csv', index=False)

print(f"Dataset created with {len(music_df)} songs.")
print(f"Mood distribution:")
print(music_df['mood'].value_counts())
print("\nSample of the dataset:")
print(music_df.head())
