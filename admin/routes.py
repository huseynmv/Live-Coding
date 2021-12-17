from run import app,db
from flask import render_template, redirect, request

@app.route("/adminhome", methods = ["GET","POST"])
def admin():
    from models import Service
    services = Service.query.all()
    if request.method == 'POST':
        service = Service(
            service_title = request.form["service_title"],
            service_description = request.form["service_description"]
        )
        db.session.add(service)
        db.session.commit()
        return redirect("/adminhome")
    return render_template("admin/service.html", services=services)
    
@app.route("/adminhome/delete/<int:id>",methods=["GET","POST"])
def service_delete(id):
    from models import Service
    service = Service.query.filter_by(id=id).first()
    db.session.delete(service)
    db.session.commit()
    return redirect("/adminhome")

@app.route("/adminhome/update/<int:id>", methods= ["GET","POST"])
def service_update(id):
    from models import Service
    service = Service.query.filter_by(id=id).first()
    if request.method == 'POST':
        service = Service.query.filter_by(id=id).first()
        service.service_title = request.form["service_title"]
        service.service_description = request.form["service_description"]
        db.session.commit()
        return redirect("/adminhome")
    return render_template("admin/service-update.html", service=service)


@app.route("/adminhome/works", methods = ["GET","POST"])
def admin_works():
    from models import Work
    import os
    works = Work.query.all()
    if request.method == 'POST':
        file = request.files['work_img']
        filename = file.filename
        file.save(os.path.join("static/uploads/",filename))
        work = Work(
            work_title = request.form["work_title"],
            work_client_name = request.form["work_client_name"],
            work_img =filename,
            work_url = request.form["work_url"]
        )
        db.session.add(work)
        db.session.commit()
        return redirect("/adminhome/works")
    return render_template("admin/works.html", works=works)


@app.route("/adminhome/works/delete/<int:id>")
def works_delete(id):
    from models import Work
    work = Work.query.filter_by(id=id).first()
    db.session.delete(work)
    db.session.commit()
    return redirect("/adminhome/works")

@app.route("/adminhome/works/update/<int:id>", methods= ["GET","POST"])
def works_update(id):
    from models import Work
    works = Work.query.filter_by(id=id).first()
    if request.method == 'POST':
        work = Work.query.filter_by(id=id).first()
        work.work_title = request.form["work_title"]
        work.work_url = request.form["work_url"]
        work.work_client_name = request.form["work_client_name"]
        db.session.commit()
        return redirect("/adminhome/works")
    return render_template("admin/works-update.html", works=works)


@app.route('/adminhome/timeline', methods= ["GET","POST"])
def timeline():
    from models import TimeLine
    timelines = TimeLine.query.all()
    if request.method == 'POST':
        timeline = TimeLine(
            timeline_year=request.form['timeline_year'],
            timeline_description=request.form['timeline_description'],
            timeline_number=request.form['timeline_number']
        )
        db.session.add(timeline)
        db.session.commit()
        return redirect('/adminhome/timeline')
    return render_template('admin/timeline.html', timelines=timelines)

@app.route("/adminhome/timeline/delete/<int:id>")
def delete_timeline(id):
    from models import TimeLine
    timeline = TimeLine.query.filter_by(id=id).first()
    db.session.delete(timeline)
    db.session.commit()
    return redirect("/adminhome/timeline")

@app.route("/adminhome/timeline/update/<int:id>", methods= ["GET","POST"])
def timeline_update(id):
    from models import TimeLine
    timelines = TimeLine.query.filter_by(id=id).first()
    if request.method == 'POST':
        timeline = TimeLine.query.filter_by(id=id).first()
        timeline.timeline_year = request.form["timeline_year"]
        timeline.timeline_description = request.form["timeline_description"]
        timeline.timeline_number = request.form["timeline_number"]
        db.session.commit()
        return redirect("/adminhome/timeline")
    return render_template("admin/timeline_update.html", timelines=timelines)



@app.route("/adminhome/blog", methods = ["GET","POST"])
def admin_blog():
    from models import Blog
    import os
    blogs = Blog.query.all()
    if request.method == 'POST':
        file = request.files['blog_img']
        filename = file.filename
        file.save(os.path.join("static/uploads/",filename))
        blog = Blog(
            blog_title = request.form["blog_title"],
            blog_description = request.form["blog_description"],
            blog_img =filename,
            blog_url = request.form["blog_url"]
        )
        db.session.add(blog)
        db.session.commit()
        return redirect("/adminhome/blog")
    return render_template("admin/blog.html", blogs=blogs)

@app.route("/adminhome/blog/delete/<int:id>")
def delete_blog(id):
    from models import Blog
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect("/adminhome/blog")

@app.route("/adminhome/blog/update/<int:id>", methods= ["GET","POST"])
def blog_update(id):
    from models import Blog
    blogs = Blog.query.filter_by(id=id).first()
    if request.method == 'POST':
        blog = Blog.query.filter_by(id=id).first()
        blog.blog_title = request.form["blog_title"]
        blog.blog_description = request.form["blog_description"]
        blog.blog_url = request.form["blog_url"]
        db.session.commit()
        return redirect("/adminhome/blog")
    return render_template("admin/update_blog.html", blogs=blogs)