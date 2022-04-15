from flask import Flask
from json import load

with open("candidates.json", encoding="utf-8") as f:
    names = load(f)

app = Flask(__name__)

@app.route("/")
def page_index():
    """Главная страница с выводом всех кондидатов"""
    show = ""
    for i in names:
        show +=  f"\nИмя - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}\n\n"
    return f"<pre >{show}<pre>"
    
   
@app.route("/candidates/<x>")
def page_candidates(x):
    """Дочерняя страница с выводом кандидата по id"""
    x = int(x)
    pic = ""
    info = ""
    for i in names:
        if x == i["id"]:
            pic += i["picture"]
            info += f"\nИмя - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}\n\n"
            
    return f"<img src = {pic}>\n<pre >{info}<pre>"
            

@app.route("/skills/<y>")
def page_skills(y):
    """Дочерняя страница с выводом кондидатов по навыку"""
    y = str(y)
    by_skill = ""
    for i in names:
        if y in i["skills"].split(","):
            by_skill += f"\nИмя - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}\n\n"
        if y.title() in i["skills"].split(","):
            by_skill += f"\nИмя - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}\n\n"
        
    return f"<pre >{by_skill}<pre>"

app.run()
