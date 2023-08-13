# Prediction tumor nature based on its characteristics (sklearn)

This code allows to perform a multiple sequence alignment (MSA) using biopython and clustalW.

## Usage

First we need to download clustalw from http://www.clustal.org/download/current/

Then:
 - Load some data downloaded from UCI and preprocess it.
 - Split the data and train the models.
 - Use different classifiers to find the accuracy of the model and save them using pickle.
 - Test the model using different parameters to see if it classifies the tumours correctly.


## Output

The output will be the model that can classify these tumours.


