#Bash scrip to commit and push to github
# Get name of repository
echo Repository Name:
read FILENAME

echo Pulling and Personalizing  $FILENAME

# Moving to repository
cd ~/devel/$FILENAME

# Pull Files
git pull

# Loop Through .py Files in Repository
for F in $(find -name *.py)

do
# Return to handler
cd ~/handler

# Run PathSwap for the file
python3 pathSwap.py $FILENAME/${F:2}

echo Processed $FILENAME/${F:2}
done
