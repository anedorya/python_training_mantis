from model.project import Project
import random


def test_delete_project(app, db):
        app.session.login("administrator", "root")
        if len(db.get_project_list()) == 0:
            app.project.add_new_project(Project(name="test"))
        old_projects = db.get_project_list()
        project = random.choice(old_projects)
        app.project.delete_project(project.name)
        new_projects = db.get_project_list()
        old_projects.remove(project)
        assert old_projects == new_projects
