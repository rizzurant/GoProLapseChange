# GoProLapseChange
GoPro Hero 2014 Entry Level, Change Time Lapse Script

Simple script to use multiple timelapse option from GoPro Hero 2014 Entry Level, This 129USD entry level action cam only let you using the default 0.5 second timelapse setting, means it will capture image every 0.5 second, using this simple script, we can "select" file from the 0.5 second sequence to create our new sequence file before we put into video editor

# Note
- Works with python
- Developed and tested using windows 7

# How To Use:
1. Put this script under your "Time Lapse" folder that contains for *.JPG files
2. Just double click ( make sure your python windows path is enabled )
3. The script will asked you the new variable for time lapse ( use below table as guide )

# New Lapse Variable input
- 1s --> 2
- 2s --> 4
- 5s --> 10
- 10s --> 20
- 30s --> 30

| Second | SequenceFile | 1s = 2 | 2s = 4 | 5s = 10 | 10s = 20 | 30s = 60 |
|--------|--------------|--------|--------|---------|----------|----------|
| 0      | 0            | x      | x      | x       | x        |          |
| 0.5    | 1            |        |        |         |          |          |
| 1      | 2            | x      |        |         |          |          |
| 1.5    | 3            |        |        |         |          |          |
| 2      | 4            | x      | x      |         |          |          |
| 2.5    | 5            |        |        |         |          |          |
| 3      | 6            | x      |        |         |          |          |
| 3.5    | 7            |        |        |         |          |          |
| 4      | 8            | x      | x      |         |          |          |
| 4.5    | 9            |        |        |         |          |          |
| 5      | 10           | x      |        | x       |          |          |
| 5.5    | 11           |        |        |         |          |          |
| 6      | 12           | x      | x      |         |          |          |
| 6.5    | 13           |        |        |         |          |          |
| 7      | 14           | x      |        |         |          |          |
| 7.5    | 15           |        |        |         |          |          |
| 8      | 16           | x      | x      |         |          |          |
| 8.5    | 17           |        |        |         |          |          |
| 9      | 18           | x      |        |         |          |          |
| 9.5    | 19           |        |        |         |          |          |
| 10     | 20           | x      | x      | x       | x        |          |
| 10.5   | 21           |        |        |         |          |          |
| 11     | 22           | x      |        |         |          |          |
| 11.5   | 23           |        |        |         |          |          |
| 12     | 24           | x      | x      |         |          |          |
| 12.5   | 25           |        |        |         |          |          |
| 13     | 26           | x      |        |         |          |          |
| 13.5   | 27           |        |        |         |          |          |
| 14     | 28           | x      | x      |         |          |          |
| 14.5   | 29           |        |        |         |          |          |
| 15     | 30           | x      |        | x       |          |          |
| 15.5   | 31           |        |        |         |          |          |
| 16     | 32           | x      | x      |         |          |          |
| 16.5   | 33           |        |        |         |          |          |
| 17     | 34           | x      |        |         |          |          |
| 17.5   | 35           |        |        |         |          |          |
| 18     | 36           | x      | x      |         |          |          |
| 18.5   | 37           |        |        |         |          |          |
| 19     | 38           | x      |        |         |          |          |
| 19.5   | 39           |        |        |         |          |          |
| 20     | 40           | x      | x      | x       | x        |          |
| 20.5   | 41           |        |        |         |          |          |
| 21     | 42           | x      |        |         |          |          |
| 21.5   | 43           |        |        |         |          |          |
| 22     | 44           | x      | x      |         |          |          |
| 22.5   | 45           |        |        |         |          |          |
| 23     | 46           | x      |        |         |          |          |
| 23.5   | 47           |        |        |         |          |          |
| 24     | 48           | x      | x      |         |          |          |
| 24.5   | 49           |        |        |         |          |          |
| 25     | 50           | x      |        | x       |          |          |
| 25.5   | 51           |        |        |         |          |          |
| 26     | 52           | x      | x      |         |          |          |
| 26.5   | 53           |        |        |         |          |          |
| 27     | 54           | x      |        |         |          |          |
| 27.5   | 55           |        |        |         |          |          |
| 28     | 56           | x      | x      |         |          |          |
| 28.5   | 57           |        |        |         |          |          |
| 29     | 58           | x      |        |         |          |          |
| 29.5   | 59           |        |        |         |          |          |
| 30     | 60           | x      | x      | x       | x        | x        |
