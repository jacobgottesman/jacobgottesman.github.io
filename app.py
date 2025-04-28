from flask import Flask, render_template, abort
from flask_flatpages import FlatPages
import config
from datetime import datetime

# Create Flask app
app = Flask(__name__)
app.config.from_object(config)

# Initialize FlatPages
pages = FlatPages(app)

# Add current year to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Add custom Jinja filters
@app.template_filter('format_date')
def format_date(date, format='%B %d, %Y'):
    if isinstance(date, str):
        try:
            return datetime.strptime(date, '%Y-%m-%d').strftime(format)
        except ValueError:
            return date
    elif hasattr(date, 'strftime'):
        return date.strftime(format)
    return date

@app.route('/')
def index():
    """Homepage with featured projects"""
    # Get all projects
    projects = [p for p in pages if p.path.startswith('projects/')]
    
    # Sort by order first (if available), then by date
    def get_sort_key(p):
        # If order is specified, use it as primary sort key
        if 'order' in p.meta:
            try:
                return (int(p.meta.get('order', 999)), '')  # Lower order = higher priority
            except (ValueError, TypeError):
                pass
                
        # Otherwise, sort by date
        date = p.meta.get('date')
        if isinstance(date, str):
            # Try to parse the string date
            try:
                return (999, datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'))
            except ValueError:
                return (999, '0000-00-00')
        # If it's already a date object, convert to string
        elif hasattr(date, 'strftime'):
            return (999, date.strftime('%Y-%m-%d'))
        else:
            return (999, '0000-00-00')
    
    projects.sort(key=get_sort_key)
    return render_template('index.html', projects=projects)

@app.route('/projects/<path:path>/')
def project(path):
    """Individual project page"""
    project = pages.get_or_404(f'projects/{path}')
    return render_template('project.html', project=project)

@app.route('/<path:path>/')
def page(path):
    """Generic page route for about, resume, etc."""
    page = pages.get_or_404(f'pages/{path}')
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host='0.0.0.0', port=8000)