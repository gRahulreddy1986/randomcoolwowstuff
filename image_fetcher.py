from flask import Flask, render_template, g,jsonify
import datetime
import sqlite3

app = Flask(__name__)
DATABASE = 'path_to_your_database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')

def index(): 
    

    return render_template('index.html')

@app.route('/refresh_image')
def refresh_image():
    db = get_db()
    cur = db.execute('SELECT id, path FROM images ORDER BY RANDOM() LIMIT 1')
    image = cur.fetchone()
    image_id, image_path = image[0], image[1]
    
    # Update or insert view count 
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("SELECT view_count FROM image_stats WHERE image_id = ?", (image_id,))
    result = cur.fetchone()
    if result:
        view_count = result[0] + 1
        cur.execute("UPDATE image_stats SET view_count = ?, last_viewed = ? WHERE image_id = ?", (view_count, current_time, image_id))
    else:
        view_count = 1
        cur.execute("INSERT INTO image_stats (image_id, view_count, last_viewed) VALUES (?, ?, ?)", (image_id, view_count, current_time))

    db.commit()

    return jsonify({'image_url': 'static/' + image_path, 'view_count': view_count})

@app.route('/reset_count', methods=['GET', 'POST'])
def reset_count():
    db = get_db()
    cur = db.execute("UPDATE image_stats SET view_count = 0, last_viewed = NULL")
    db.commit()
    return jsonify({'message': 'View counts reset successfully', 'status': 'success'})


if __name__ == "__main__":
    app.run(host='192.168.1.37', port=5000, debug=True)