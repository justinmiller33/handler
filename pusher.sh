#Bash scrip to commit and push to github
# Get name of repository
echo Repository Name:
read FILENAME

echo Commiting and Pushing  $FILENAME

# Moving to repository
cd ~/devel/$FILENAME

# Loop through files in repository fixing path
for F in $(find -name *.py)

do
# Return to handler
cd ~/handler

# Run PathSwap for the file
python3 pathSwapBack.py $FILENAME/${F:2}
echo Processed $FILENAME/${F:2}

done

# Return to repository
cd ~/devel/$FILENAME

# Prompt commit message
echo Commit Message?
read MSG

# Commit
git commit -a -m "$MSG"
echo Commited

# Push
git push
echo Pushed
