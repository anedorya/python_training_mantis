from model.project import Project
import random
import string


def test_add_project(app):
        app.session.login("administrator", "root")
        username = "administrator"
        password = "root"
        old_projects = sorted(app.soap.get_list_of_projects(username, password), key=Project.id_or_max)
        project = Project(name=random_string("name", 10), description=random_string("description", 20))
        app.project.add_new_project(project)
        new_projects = sorted(app.soap.get_list_of_projects(username, password), key=Project.id_or_max)
        old_projects.append(project)
        assert len(new_projects) == len(old_projects)
        n = 0
        for x in sorted(old_projects, key=Project.id_or_max):
            assert x.name == new_projects[n].name
            assert x.description == new_projects[n].description
            n = n + 1



def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])