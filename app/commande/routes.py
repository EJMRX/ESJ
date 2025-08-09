from flask import Blueprint, render_template

bp = Blueprint('commande', __name__, url_prefix='/commande', template_folder='templates')

@bp.route('/')
def index():
    # بيانات وهمية (Dummy Data) لبطاقات الإحصاء (KPIs)
    kpi_stats = {
        'total': , 
        'abandoned': , 
        'pending': , 
        'confirmed': , 
        'ready': ,
        'return_not_received': , 
        'shipped': , 
        'delivered': , 
        'cancelled': 
    }
    
    # بيانات وهمية لجدول الطلبات
    dummy_orders = [
        {'client': 'EMNA MANAI', 'reference': '48583', 'etat': 'En attente', 'status_class': 'status-pending', 'gouvernorat': 'Tunis', 'total': '40,500 TND', 'articles': 1, 'cree_par': 'Esprit Jeune', 'tel': '21 040 204'},
        {'client': 'INÈS BARGUI', 'reference': '48582', 'etat': 'Retour', 'status_class': 'status-returned', 'gouvernorat': 'Nabeul', 'total': '158,000 TND', 'articles': 3, 'cree_par': 'Esprit Jeune', 'tel': '27 818 485'},
        {'client': 'SAIDA', 'reference': '48581', 'etat': 'Confirmée', 'status_class': 'status-confirmed', 'gouvernorat': 'Ben Arous', 'total': '17,500 TND', 'articles': 1, 'cree_par': 'Esprit Jeune', 'tel': '55 545 490'},
        {'client': 'RETOUR SAIDA', 'reference': '48580', 'etat': 'Annulée', 'status_class': 'status-cancelled', 'gouvernorat': 'Ben Arous', 'total': '23,000 TND', 'articles': 1, 'cree_par': 'Esprit Jeune', 'tel': '27 818 485'},
        {'client': 'SALMA', 'reference': '48579', 'etat': 'Expédiée', 'status_class': 'status-shipped', 'gouvernorat': 'Sousse', 'total': '228,000 TND', 'articles': 1, 'cree_par': 'Esprit Jeune', 'tel': '58 934 133'},
    ]

    # تمرير المتغيرات إلى القالب
    return render_template('commande/index.html', orders=dummy_orders, kpi=kpi_stats)
