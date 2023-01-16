# Ask-Filius

A command-line tool for searching Linux commands

## Description

Sometimes, we forget the command we planned to use if we haven't used it in a while. For new command line users, this happens more often, as they just started learning and aren't familiar with the commands. This is where this tool, Ask-Filius, comes in handy. It allows users to search for the command by describing what the command should do, then it will recommend several candidates the user is likely looking for.

Ask-Filius relies on information on the internet. Descriptions of commands are scraped down and analyzed using TF-IDF and apriori method. The recommendation is then made according to the analysis result.

The current challenge of this project is that it lacks accuracy. This is probably because of the defective collection of data I use to analyze. Also, I wonder if there is a better way to implement this idea. If you have a better solution in mind, please feel free to raise an issue.

## Installation

### Install from archive

1. Download archive from the [Release page](https://github.com/leafoliage/ask-filius/releases)
2. Extract the tool

```
tar -xzf ask_filius_0.1.0_linux.tar.gz -C /usr/local/bin
```

### Build from source

1. Download source code from the [Release page](https://github.com/leafoliage/ask-filius/releases)
2. If you haven't installed pyinstaller, install it

```
pip install pyinstaller
```

3. Build with pyinstaller

```
pyinstaller main.py --name ask --add-data tfidf.csv:./ --add-data rules.csv:./ --add-data commands.csv:./
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