from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Upload configuration
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    "txt", "rtf", "md", "docs", "py", "java", "js", "c", "cpp", "php",
    "ini", "json", "xml", "log", "csv", "tsv", "mp4", "avi", "mov", "wmv",
    "mkv", "webm", "flv", "3gp", "jpg", "jpeg", "png", "gif", "bmp", "cr2",
    "nef", "arw", "xlsx", "xls", "db", "sql", "pptx", "ppt", "odp", "mp3",
    "wav", "ogg", "aac", "flac", "fbx", "obj", "stl", "blend", "max", "dae",
    "svg", "ai", "epub", "mobi", "pdf", "zip", "rar", "7z", "tar", "gz",
    "key", "ods", "mdb", "ttf", "otf", "doc", "docx", "xls", "xlsx", "csv", "xls", "xlsx", "ppt", "pptx"
}


# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Database models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    files = db.Column(db.Text)  # Stores filenames as a comma-separated string

    def __repr__(self):
        return f'<Post {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()
    
def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return filename
    return None

# Create the database tables and initialize users
def init_db():
    db.create_all()
    
    # Check if users already exist
    if User.query.first() is None:
        users = {
            "user1": "password",
            "user2": "password",
            "user3": "password",
            "user4": "password",
            "user5": "password",
            "user6": "password"
        }
        for username, password in users.items():
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
        
        db.session.commit()
        print("Users initialized")

with app.app_context():
    init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        flash('Please log in to access this page', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        files = request.files.getlist('files')

        uploaded_files = []
        for file in files:
            filename = save_file(file)
            if filename:
                uploaded_files.append(filename)
        
        post = Post(
            username=session['username'],
            title=title,
            content=content,
            files=','.join(uploaded_files)
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('dashboard.html')


@app.route('/user/<username>')
def user_posts(username):
    if 'username' not in session:
        return redirect(url_for('login'))
    user_posts = Post.query.filter_by(username=username).all()
    return render_template('user_posts.html', posts=user_posts, username=username)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = Post.query.get_or_404(post_id)
    print(f"Files: {post.files}")  # デバッグ用にファイル名を出力
    return render_template('post.html', post=post)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
