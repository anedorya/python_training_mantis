
import random
import string


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_manage_projects_page(self):
        wd = self.app.wd
        # if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def open_add_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.open_add_project_page()
        self.fill_info(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_manage_projects_page()
        self.project_cache = None


    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()



    def fill_info(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_project(self, name):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//a[contains(text(), '%s')]" % name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None


