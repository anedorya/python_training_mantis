from model.project import Project


def test_add_project(app, db):
        app.session.login("administrator", "root")
        old_projects = db.get_project_list()
        project = Project(name="rrr604ed5", description="wwwwwww")
        app.project.add_new_project(project)
        new_projects = db.get_project_list()
        old_projects.append(project)
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
