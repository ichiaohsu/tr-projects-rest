from eve import Eve
from flask import redirect, request
import json

app = Eve()

@app.route("/tag/<name>", methods=['GET'])
def tagSearch(name):
  return redirect('/article/?where={"tags":{"$in":["%s"]}}' % name, code=302)

@app.route("/tags/", methods=['POST'])
def tagBulkSearch():
  data = json.loads(request.data)
  results = []
  tc = app.test_client()
  for tag in data['tags']:
    resp = tc.get('article/?where={"tags":{"$in":["%s"]}}' % tag)
    results.append(json.loads(resp.data))
  return json.dumps({'results':results})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
