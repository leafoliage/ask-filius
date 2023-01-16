# Ask-Filius

Search for Linux commands on the command-line right away

## Introduction

Sometimes, we forget the command we planned to use if we haven't used it in a while. For new command line users, this happens more often, as they just started learning and aren't familiar with the commands. This is where this tool, Ask-Filius, comes in handy. It allows users to search for the command by describing what the command should do, then it will recommend several candidates the user is likely looking for.

Ask-Filius relies on information on the internet. Descriptions of commands are scraped down and analyzed using TF-IDF and apriori method. The recommendation is then made according to the analysis result.

The current challenge of this project is that it lacks accuracy. This is probably because of the defective collection of data I use to analyze. Also, I wonder if there is a better way to implement this idea. If you have a better solution in mind, please feel free to raise an issue.

## Installation

1. Download archive from the [Release page](https://github.com/leafoliage/ask-filius/releases)
2. Extract the tool

```
tar -xzf ask_filius_0.1.0_linux.tar.gz -C /usr/local/bin
```

## Usage

```
ask
```

The tool will ask you to describe the command

```
$ ask
What command are you looking for?
Try describe what the command does:
```

Describe the command and get results from the tool!

## Building the Project

1. Install all packages

```
pip install -r requirements.txt
```

2. Create a programmable search engine on Google. See more on [Programmable Search Engine](https://developers.google.com/custom-search/v1/introduction)

3. Add `API_KEY` and `SE_ID` (search engin id) in `.env` file. See more on [Programmable Search Engine](https://developers.google.com/custom-search/v1/using_rest#response_data) for how to get these variables

```
API_KEY=<YOUR_API_KEY>
SE_ID=<YOUR_SEARCH_ENGINE_ID>
```

4. Run the following python scripts

```
python3 text-scrape.py
python3 tfidf.py
python3 association-scrape.py
python3 apriori.py
```

5. Start the tool by running `main.py`

```
python3 main.py
```

## Contributing

Pull requests and advice are welcomed. Please feel free to raise issues and PRs.

## License

[MIT License](https://choosealicense.com/licenses/mit/)