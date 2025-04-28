from flask_frozen import Freezer
from app import app, pages

freezer = Freezer(app)

@freezer.register_generator
def project_url_generator():
    for page in pages:
        if page.path.startswith('projects/'):
            yield {'path': page.path.replace('projects/', '')}

@freezer.register_generator
def page_url_generator():
    for page in pages:
        if page.path.startswith('pages/'):
            yield {'path': page.path.replace('pages/', '')}

if __name__ == '__main__':
    # Set to False to get more detailed error messages
    freezer.freeze()