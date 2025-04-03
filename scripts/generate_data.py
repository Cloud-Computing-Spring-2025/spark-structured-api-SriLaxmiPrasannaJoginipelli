import pandas as pd
import random
from datetime import datetime, timedelta

# Generate songs metadata
genres = ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip-Hop', 'Electronic']
moods = ['Happy', 'Sad', 'Energetic', 'Chill']
num_songs = 1000

songs = []
for i in range(1, num_songs + 1):
    songs.append([
        f"song_{i}",
        f"Title {i}",
        f"Artist {random.randint(1, 50)}",
        random.choice(genres),
        random.choice(moods)
    ])

songs_df = pd.DataFrame(songs, columns=['song_id', 'title', 'artist', 'genre', 'mood'])
songs_df.to_csv('data/songs_metadata.csv', index=False)

# Generate listening logs
num_users = 200
num_logs = 5000
start_date = datetime(2025, 3, 1)

logs = []
for _ in range(num_logs):
    user_id = f"user_{random.randint(1, num_users)}"
    song_id = f"song_{random.randint(1, num_songs)}"
    timestamp = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    duration_sec = random.randint(30, 300)
    logs.append([user_id, song_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), duration_sec])

logs_df = pd.DataFrame(logs, columns=['user_id', 'song_id', 'timestamp', 'duration_sec'])
logs_df.to_csv('data/listening_logs.csv', index=False)

print("Data generated successfully!")
