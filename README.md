## Train indonesian POS-tagger for Stanford CoreNLP

 - 1. Download Stanford CoreNLP 3.8.0 from https://stanfordnlp.github.io/CoreNLP/index.html#download
 - 2. Download trainin data for Indonesian Part of Speech from http://universaldependencies.org
 - 3. Run the script ```clean_conllu.py``` to remove all comments from the conllu file. Make sure to edit the filename for your .conllu file here before running. 
 - 4. Update the indonesian.props file with appropriate settings (trainFile and model most importantly)
 - 5. Run the train.sh script (or copy paste the one liner from the script to the terminal.) Make sure your path to the downloaded CoreNLP package is correct before you run the script. 


 The props file might not be the best one. From the sample.props files (generated using the MaxEntTagger in Stanford CoreNLP --genprops flag):

 "This is really the tag set which is used for the list of open-class tags, and perhaps deterministic  tag
expansion). Currently we have 'english', 'arabic', 'german', 'chinese' or 'polish' predefined. For your own language, you can specify the same information via openClassTags or closedClassTags below (only ONE of these three options may be specified). 'english' means UPenn English treebank tags. 'german' is STTS 'chinese' is CTB, and Arabic is an expanded Bies mapping from the ATB 'polish' means some tags that some guy on the internet once used. 
See the TTags class for more information."

Meaning if you want a proper model you should probably try this. The model is not evaluated either but it should be fairly easy to do.
