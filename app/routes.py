from run import app
from flask import redirect, render_template, request

@app.route("/")
def app_index():
    from models import Service
    from models import Work
    from models import TimeLine
    from models import Blog
    
    timeline=TimeLine.query.all()
    blogs = Blog.query.all()
    service = Service.query.all()
    works = Work.query.all()
    return render_template("app/index.html", service=service, works=works, timeline=timeline, blogs=blogs)