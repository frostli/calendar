from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from calendarlulz.models import Post, Comment

home = Blueprint('home', __name__, template_folder='templates')


class IndexView(MethodView):
  def get(self):
    return 'hi'

class ListView(MethodView):
	def get(self):
		posts = Post.objects.all()
		return render_template('posts/list.html', posts=posts)


class DetailView(MethodView):
	def get(self, slug):
		post = Post.objects.get_or_404(slug=slug)
		return render_template('posts/detail.html', post=post)


# Register the urls
home.add_url_rule('/', view_func=IndexView.as_view('index'))
