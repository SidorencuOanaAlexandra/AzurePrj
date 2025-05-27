from functools import wraps
from flask import session, redirect, url_for

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('templates.login'))
        return view_func(*args, **kwargs)
    return wrapped_view