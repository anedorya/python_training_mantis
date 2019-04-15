from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app


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
        # self.project_cache = None

    # def select_first_group(self):
    #     wd = self.app.wd
    #     wd.find_element_by_name("selected[]").click()
    #
    #
    # def select_group_by_index(self, index):
    #     wd = self.app.wd
    #     wd.find_elements_by_name("selected[]")[index].click()
    #
    # def select_group_by_id(self, id):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("input[value='%s']" % id).click()
    #
    # def modify_first_group(self):
    #     self.modify_group_by_index(0)
    #
    # def modify_group_by_index(self, index, group_changes):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     # open modification form
    #     wd.find_element_by_name("edit").click()
    #     # edit group form
    #     self.fill_info(group_changes)
    #     # confirm changes
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def modify_group_by_id(self, id, group_changes):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     # open modification form
    #     wd.find_element_by_name("edit").click()
    #     # edit group form
    #     self.fill_info(group_changes)
    #     # confirm changes
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    def fill_info(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
    #
    # def delete_first_group(self):
    #     self.delete_group_by_index(0)
    #
    # def delete_group_by_index(self, index):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     # submit group deletion
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def delete_group_by_id(self, id):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     # submit group deletion
    #     wd.find_element_by_name("delete").click()
    #     self.return_to_groups_page()
    #     self.group_cache = None
    #
    # def return_to_groups_page(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("group page").click()
    #
    # def count(self):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     return len(wd.find_elements_by_name("selected[]"))
    #
    # group_cache = None
    #
    #
    # def get_group_list(self):
    #     if self.group_cache is None:
    #         wd = self.app.wd
    #         self.open_groups_page()
    #         self.group_cache = []
    #         for element in wd.find_elements_by_css_selector("span.group"):
    #             text = element.text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.group_cache.append(Group(groupname=text, id=id))
    #     return list(self.group_cache)
    #
    #
