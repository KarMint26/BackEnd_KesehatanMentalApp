from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Data Artikel Kesehatan Mental
articles = [
    {
        'id': 1,
        'title': 'Mengelola Stres Secara Efektif',
        'content': 'Artikel tentang strategi mengelola stres dalam kehidupan sehari-hari.',
        'category': 'Stres',
        'link': 'Show Link'
    },
    {
        'id': 2,
        'title': 'Menjaga Kesehatan Mental di Tempat Kerja',
        'content': 'Panduan praktis untuk menjaga kesehatan mental saat bekerja.',
        'category': 'Kesejahteraan di Tempat Kerja',
        'link': 'Show Link'
    },
    {
        'id': 3,
        'title': 'Mengatasi Kecemasan Sosial',
        'content': 'Tips untuk mengatasi kecemasan sosial dan meningkatkan kenyamanan dalam berinteraksi dengan orang lain.',
        'category': 'Kecemasan',
        'link': 'Show Link'
    }
]

# Endpoint untuk mendapatkan semua artikel
@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(articles)

# Endpoint untuk mendapatkan artikel berdasarkan ID
@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = next((article for article in articles if article['id'] == article_id), None)
    if article:
        return jsonify(article)
    return jsonify({'message': 'Artikel tidak ditemukan'}), 404

# Endpoint untuk tampilan HTML
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
