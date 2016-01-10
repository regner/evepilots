

from flask import Blueprint, render_template
from flask.views import MethodView

from evepilots.capsuleers.services import capsuleers

blueprint = Blueprint('public', __name__, static_folder='../static')


class HomeView(MethodView):
    """
        View for the home page of EVE Pilots.
    """
    
    def get(self):
        new_capsuleers = capsuleers.get_newest_updates(7)
        
        context = {
            'new_capsuleers': new_capsuleers,
        }
        
        return render_template('public/home.html', context=context)

blueprint.add_url_rule('/', view_func=HomeView.as_view('home'))
