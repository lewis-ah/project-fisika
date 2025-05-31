from flask import Blueprint, render_template, request
from app.models.materi_model import Materi

materi_bp = Blueprint('materi', __name__)

rumus_fisika = [
    {"nama": "Kecepatan", "rumus": "v = s / t"},
    {"nama": "Percepatan", "rumus": "a = Δv / Δt"},
    {"nama": "Gaya", "rumus": "F = m * a"},
    {"nama": "Usaha", "rumus": "W = F * s"},
    {"nama": "Daya", "rumus": "P = W / t"},
    {"nama": "Tekanan", "rumus": "P = F / A"},
    {"nama": "Energi Kinetik", "rumus": "EK = 1/2 * m * v^2"},
    {"nama": "Energi Potensial", "rumus": "EP = m * g * h"},
    {"nama": "Hukum Newton 2", "rumus": "F = m * a"},
    {"nama": "Momentum", "rumus": "p = m * v"},
    {"nama": "Gaya Sentripetal", "rumus": "Fs = m * v^2 / r"},
    {"nama": "Muatan Listrik", "rumus": "Q = I * t"},
    {"nama": "Tegangan Listrik", "rumus": "V = I * R"},
    {"nama": "Energi Listrik", "rumus": "W = V * I * t"},
    {"nama": "Induksi Magnetik", "rumus": "B = μ * I / (2 * π * r)"},
    {"nama": "Frekuensi", "rumus": "f = 1 / T"},
    {"nama": "Cepat Rambat Gelombang", "rumus": "v = λ * f"},
    {"nama": "Refleksi Cahaya", "rumus": "i = r"},
    {"nama": "Pembiasan Cahaya", "rumus": "n1 * sin(i) = n2 * sin(r)"},
    {"nama": "Lensa Cembung", "rumus": "1/f = 1/s + 1/s'"},
    {"nama": "Kuat Lensa", "rumus": "P = 100 / f"},
]


@materi_bp.route('/')
def home():
    return render_template('home.html')

@materi_bp.route('/materi')
def list_materi():
    semua_materi = Materi.query.all()
    query = request.args.get('query', '').lower()
    hasil_rumus = []

    if query:
        hasil_rumus = [r for r in rumus_fisika if query in r['nama'].lower() or query in r['rumus'].lower()]

    return render_template('list_materi.html', materi=semua_materi, results=hasil_rumus)

@materi_bp.route('/materi/<int:id>')
def detail_materi(id):
    data = Materi.query.get_or_404(id)
    query = request.args.get('query', '').lower()
    hasil_rumus = []

    if query:
        hasil_rumus = [r for r in rumus_fisika if query in r['nama'].lower() or query in r['rumus'].lower()]

    return render_template('detail_materi.html', materi=data, results=hasil_rumus)
