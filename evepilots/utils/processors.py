

from evepilots.capsuleers.services import capsuleers

def inject_counters():
    """
        Adds the total counts seen in the header of all pages.
    """
    
    return dict(
        total_capsuleers=capsuleers.count(),
    )


def configure_processors(app):
    """
        Adds all the context processors to the application.
    """
    
    app.context_processor(inject_counters)
