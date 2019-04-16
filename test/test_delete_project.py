from model.project import Project
import random


def test_delete_project(app):
        app.session.login("administrator", "root")
        username = "administrator"
        password = "root"
        if len(app.soap.get_list_of_projects(username, password)) == 0:
            app.project.add_new_project(Project(name="test"))
        old_projects = sorted(app.soap.get_list_of_projects(username, password), key=Project.id_or_max)
        project = random.choice(old_projects)
        app.project.delete_project(project.name)
        new_projects = sorted(app.soap.get_list_of_projects(username, password), key=Project.id_or_max)
        old_projects.remove(project)
        assert len(new_projects) == len(old_projects)
        n = 0
        for x in sorted(old_projects, key=Project.id_or_max):
            assert x.name == new_projects[n].name
            assert x.description == new_projects[n].description
            n = n + 1


