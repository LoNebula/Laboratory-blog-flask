# reset_database.py

from app import app, db
import os
import shutil

# データベースのリセット
with app.app_context():
    db.drop_all()
    db.create_all()

# アップロードファイルの削除
upload_folder = 'static/uploads'
if os.path.exists(upload_folder):
    shutil.rmtree(upload_folder)
    os.makedirs(upload_folder)

print("Reset complete")
