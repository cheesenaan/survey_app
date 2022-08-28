# survey_app


follow the following commands to push code to github

            create a new repository on the command line:
echo "# survey_app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/cheesenaan/survey_app.git
git push -u origin main


            …or push an existing repository from the command line
git remote add origin https://github.com/cheesenaan/survey_app.git
git branch -M main
git push -u origin main


             Uploading your code to PythonAnywhere
git clone https://github.com/cheesenaan/survey_app.git

virtualenv env

source env/bin/activate

pip install django

Warning: Django may take a long time to install. PythonAnywhere has very fast internet, but the filesystem access can be slow, and Django creates a lot of small files during its installation. Thankfully you only have to do it once!

add venv to 
