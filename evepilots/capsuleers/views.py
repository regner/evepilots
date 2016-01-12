

import eveimageserver

from flask import Blueprint, render_template
from flask.views import MethodView

from evepilots.capsuleers.services import capsuleers, capsuleer_corp_history

blueprint = Blueprint('capsuleers', __name__, static_folder='../static', url_prefix='/capsuleers')


class CapsuleerView(MethodView):
    """
        View for getting the details of an individual capsuleer.
    """
    
    def get(self, capsuleer_id):
        capsuleers_details = capsuleers.get_or_404(capsuleer_id)
        
        context = {
            'name': capsuleers_details.name,
            'security_status': capsuleers_details.security_status,
            'imageserver': eveimageserver.get_image_server_link(capsuleer_id, 'char', 128),
            'birthday': capsuleer_corp_history.get_birthday_from_id(capsuleer_id).start_time,
        }
        
        return render_template('capsuleers/details.html', context=context)

blueprint.add_url_rule('/<int:capsuleer_id>', view_func=CapsuleerView.as_view('details'))
