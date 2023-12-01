from flask import Flask, url_for, redirect, render_template, request
import smtplib
import os

smtp_server = "smtp.gmail.com"
email = os.environ['EMAIL']
password = os.environ['PASSWORD']

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html', hightlight='Home')


@app.route('/about')
def about():
  return render_template('about.html', highlight='About')


@app.route('/contact')
def contact():
  return render_template('contact.html', hightlight='contact')


@app.route('/resume', methods=["GET", "POST"])
def resume():

  if request.method == "POST":
    user_name = request.form.get('name')
    user_phone = request.form.get('phone')
    user_email = request.form.get('email')
    user_location = request.form.get('location')
    user_sec_edu = request.form.get('secondary_edu')
    user_sr_edu = request.form.get('senior_secondary_edu')
    user_languages = request.form.get('languages').split(', ')
    user_profile = request.form.get('profile')
    user_achievements = request.form.get('achievements').split(', ')
    user_skills = request.form.get('prof_skills').split(', ')
    user_knowledge = request.form.get('prof_knowledge').split(', ')
    user_hobbies = request.form.get('hobbies').split(', ')
    user_linkedin = request.form.get('linkedin')
    picture = request.form.get('picture')

    lang_name = [i for i in user_languages[:7:2]]
    lang_val = [i for i in user_languages[1:8:2]]
    skill_name = [i for i in user_skills[:7:2]]
    skill_val = [i for i in user_skills[1:8:2]]
    achi_val = [i for i in user_achievements[:7:2]]
    achi_txt = [i for i in user_achievements[1:8:2]]

    def to_dict(key, val):
      return key, val

    lang = dict(map(to_dict, lang_name, lang_val))
    skill = dict(map(to_dict, skill_name, skill_val))
    achi = dict(map(to_dict, achi_val, achi_txt))

    with smtplib.SMTP(smtp_server) as connection:
      connection.starttls()
      connection.login(email, password)
      connection.sendmail(
          email, user_email,
          f"Subject:Work in progress\n\nDear, {user_name} sorry for the inconvenience we are still working on the site\n\nSite: https://fee.maniklakhanpal.repl.co"
      )

    # return f"{user_name}, {user_phone}, {user_email}, {user_location}, {user_sec_edu}, {user_sr_edu}, {user_languages}, {user_profile}, {user_achievements}, {user_skills}, {user_knowledge}, {user_hobbies}"
    return render_template(
        'resume.html',
        name=user_name,  #done
        phone=user_phone,  #done
        email=user_email,  #done
        location=user_location,  #done
        sec=user_sec_edu,  #done
        sr=user_sr_edu,  #done
        language=lang,  #done
        profile=user_profile,  #done
        achievements=achi,  #done
        skills=skill,  #done
        linkedin=user_linkedin,  #done
        knowledge=user_knowledge,  #done
        picture=picture,  #done
        hobbies=user_hobbies)  #done
  else:
    return render_template('form.html', hightlight='Resume')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5004, debug=True)
