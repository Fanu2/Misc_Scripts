import os
import shutil


def create_directory_structure(base_path):
    categories = ['Web Development', 'Data Science', 'Automation', 'Miscellaneous']

    for category in categories:
        category_path = os.path.join(base_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)


def move_project(project_name, base_path, category):
    project_path = os.path.join(base_path, project_name)
    category_path = os.path.join(base_path, category, project_name)

    if os.path.exists(project_path):
        if not os.path.exists(category_path):
            shutil.move(project_path, category_path)
            print(f"Moved '{project_name}' to '{category}'.")
        else:
            print(f"'{project_name}' already exists in '{category}'.")
    else:
        print(f"'{project_name}' does not exist in the base directory.")


def organize_projects(base_path):
    create_directory_structure(base_path)

    # Example projects and categories
    projects_and_categories = {
        'my_web_app': 'Web Development',
        'data_analysis': 'Data Science',
        'automation_scripts': 'Automation',
        'random_project': 'Miscellaneous'
    }

    for project, category in projects_and_categories.items():
        move_project(project, base_path, category)


if __name__ == "__main__":
    base_path = '/home/jasvir/PycharmProjects'  # Update this path to your base directory
    organize_projects(base_path)
