if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/mastermindmayankofficial/Mastermind-Mayank-Movies.git /Mastermind-Mayank-Movies
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Mastermind-Mayank-Movies
fi
cd /Mastermind-Mayank-Movies
pip3 install -U -r requirements.txt
echo "Starting Mastermind-Mayank-Movies...."
python3 bot.py
