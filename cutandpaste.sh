git clone https://github.com/bibbox/sys-idmapping.git

git pull

git add .
git commit -m "update from development server"
git push -u origin master

git remote add origin https://github.com/bibbox/sys-activities.git 

sudo /etc/init.d/apache2 reload