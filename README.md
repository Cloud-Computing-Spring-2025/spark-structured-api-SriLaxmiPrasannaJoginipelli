# Spark Structured API

## Overview
This project analyzes user listening behavior and music trends using PySpark Structured Streaming. It processes structured data from a fictional music streaming platform to gain insights into genre preferences, song popularity, and listener engagement.

## Dataset Details
- **listening_logs.csv**: Contains log data of user listening activity.
- **songs_metadata.csv**: Contains metadata about the songs, including genre and mood.

## Tasks Implemented
1. Find each user’s favorite genre.
2. Calculate the average listen time per song.
3. List the top 10 most played songs this week.
4. Recommend “Happy” songs to users who mostly listen to “Sad” songs.
5. Compute the genre loyalty score for each user.
6. Identify users who listen to music between 12 AM and 5 AM.
7. Enrich logs by joining listening data with song metadata.

## Running the Scripts
### Step 1: Generate Data
```bash
python scripts/generate_data.py
```
### Step 2: Run Spark Analysis
```bash
python scripts/spark_analysis.py
```

## Output Directory Structure
```
output/
├── user_favorite_genres/
├── avg_listen_time_per_song/
├── top_songs_this_week/
├── happy_recommendations/
├── genre_loyalty_scores/
├── night_owl_users/
├── enriched_logs/
```

## Errors Faced & Resolutions
- **Issue: SparkSession not initializing**
  - Fixed by installing PySpark: `pip install pyspark`
- **Issue: FileNotFoundError for data files**
  - Fixed by ensuring `data/` directory exists before running scripts.



