#!/bin/bash
# This script will query covid data and display it for lab 2


POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].posi         tive')
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].nega         tive')
DEAD=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].pending'         )
HOSPITAL=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hosp         italizedCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative t         ests, $DEAD deaths, and $HOSPITAL hospitalized."
