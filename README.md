
# Team Nivaaran Backend Documentation

![alt text](https://github.com/diffrxction/nivaaran-api/blob/dev/media/github/banners/banner.png?raw=true)

## Description :computer:

Django files for Nivaaran app APIs with Django Rest Framework. :rocket:
<br><br>
### Before Updating or Pushing the repo :fire:

<br>Add protected files to `.gitignore` as and when needed, then perform a manual addition of libraries to `requirements.txt`
<br>

Followed by 

```
git add .
git commit -m "Message"
git push origin dev
```

## Project Setup :mechanic:
<br>

### Installing torch, torchvision and torchaudio depending on the OS used.

<br>

[Official PyTorch installation commands](https://pytorch.org/get-started/locally/)
<br>

Run the system specific command and then follow up with 

```bash
pip install -r requirements.txt
```
## Run Project :rocket:
<br>

**Remember to configure settings.py for the database accordingly if running on localhost.**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
