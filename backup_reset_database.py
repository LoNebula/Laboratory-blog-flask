# reset_database.py

from app import app, db
import os
import shutil
from datetime import datetime

# バックアップフォルダーのパス
backup_folder = 'backup'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
db_backup_path = os.path.join(backup_folder, f'db_backup_{timestamp}.db')
uploads_backup_path = os.path.join(backup_folder, f'uploads_backup_{timestamp}')

# バックアップフォルダーの作成
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# データベースのバックアップ
with app.app_context():
    # データベースファイルのパスを取得（例: 'app.db'）
    db_path = 'your_database_path_here'  # 実際のデータベースのファイルパスに置き換えてください
    if os.path.exists(db_path):
        shutil.copy(db_path, db_backup_path)

# アップロードファイルのバックアップ
upload_folder = 'static/uploads'
if os.path.exists(upload_folder):
    shutil.copytree(upload_folder, uploads_backup_path)

# データベースとアップロードフォルダーのリセット
with app.app_context():
    db.drop_all()
    db.create_all()

# アップロードフォルダーの削除
if os.path.exists(upload_folder):
    shutil.rmtree(upload_folder)
os.makedirs(upload_folder)

print("Backup and reset complete")
