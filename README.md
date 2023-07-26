# Let's teach an AI to catch exploiters (LTAATCE)

This is the repo for the Python & ML half of the tutorial. Make sure you have...
- Python 3
- An ML library of your choice (in this case we are using Tensorflow & Keras)
- Git (to clone this repo)

Full tutorial: [not published yet]

Directory:
- `/data/`
    - `data.csv`, houses the CSV version of the raw data
    - `lerped-data.csv`, houses the lerped version of the CSV data
    - `rawdata.txt`, houses the direct data, straight from ROBLOX via Github Gists
- `data-lerp.py`, converts `data.csv` -> `lerped-data.csv`
- `data-parser.py`, converts `rawdata.txt` -> `data.csv`