from flask_frozen import Freezer
from app import app, pages
import os

freezer = Freezer(app)

@freezer.register_generator
def project():
    for page in pages:
        if page.path.startswith('projects/'):
            yield {'path': page.path.replace('projects/', '')}

@freezer.register_generator
def page():
    for page in pages:
        if page.path.startswith('pages/'):
            yield {'path': page.path.replace('pages/', '')}

if __name__ == '__main__':
    # Create the build directory if it doesn't exist
    if not os.path.exists('build'):
        os.makedirs('build')
    
    # Create a .nojekyll file to disable Jekyll processing
    with open(os.path.join(freezer.root, '.nojekyll'), 'w') as f:
        pass
    
    freezer.freeze()