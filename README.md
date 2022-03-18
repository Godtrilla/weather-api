# weather-api
Weather API


Execute script from command line with two arguments: api key, and output csv filepath

The script when called from command line should:

    1) Get current weather for Boston, San Francisco, and London

    2) Append to existing CSV, or create new if one doesn't exist the following:

*         1 Row per city

*         Units should be in imperial (fahrenheit, feet etc)

*         Columns should be: City Name | Date (human readable) | Temp | Weather Description (e.g. "Few clouds") | Pressure | Humidity

*

*Use Open Weather API* (Onecall) API: https://openweathermap.org/api/one-call-api

(A Free account must be created in order to get an API key)

 

In its finished form, the deliverable should be a repository, or zip file containing:

- python file which can be called from commandline with arguments, e.g. python3 myfile <api_key> <csv filepath>

- the output csv artifact from a successful run

 

Projects will be evaluated on:

1) Script executes acceptance criteria and produces desired outcome csv file

2) Code is readable and contains docstrings / comments when appropriate.

3) Script is well structured and "pythonic"  (e.g. appropriate use of classes, functions, data structures, __main__ block where necessary).  Script's logical tasks are modular and isolated for maintainability, rather than one long function which performs all tasks and cannot be decoupled.

 

Extra credit idea:

# Commit your script to a github repo.

# Create a github action workflow which:

* Executes the script on a schedule

* Commits the updated CSV artifact to the repository