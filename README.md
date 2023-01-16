# Ask-Filius

A command-line tool for searching Linux commands

## Description

Sometimes, we forget the command we planned to use if we haven't used it in a while. For new command line users, this happens more often, as they just started learning and aren't familiar with the commands. This is where this tool, Ask-Filius, comes in handy. It allows users to search for the command by describing what the command should do, then it will recommend several candidates the user is likely looking for.

Ask-Filius relies on information on the internet. Descriptions of commands are scraped down and analyzed using TF-IDF and apriori method. The recommendation is then made according to the analysis result.

The current challenge of this project is that it lacks accuracy. This is probably because of the defective collection of data I use to analyze. Also, I wonder if there is a better way to implement this idea. If you have a better solution in mind, please feel free to raise an issue.
