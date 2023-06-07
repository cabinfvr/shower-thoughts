from flask import Flask, render_template
import grab_posts
app = Flask('app')

@app.route('/')
def index():
  return render_template('template.html', shower_thought=grab_posts.get_post().lower())

@app.route('/api')
def api():
  return grab_posts.get_post()

@app.route('/json')
def json():
  return {
    "thought": grab_posts.get_post()
  }

app.run(host='0.0.0.0', port=8080)
