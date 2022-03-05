from input_values import *

def compose_query_CB_get(request):
  v_req_keys = [i for i in request.args.keys()]

  query = 'SELECT * FROM cocktailbar'
  v_q = []
  for rk in v_req_keys:
    if rk not in v_possible_keys_CB_GET:
      continue
    value = request.args.get(rk)
    if type(value) == str:
      v_q.append(rk + " = '" + request.args.get(rk) + "'")
    else:
      v_q.append(rk + " = " + request.args.get(rk))
  
  for i, q in enumerate(v_q):
    if i == 0:
      query += ' WHERE'
    else:
      query += ' AND'
    query += ' ' + q
  
  query += ' ORDER BY name ASC'
  return query
