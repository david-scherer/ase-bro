from flask import Flask, request, Response, jsonify
import psycopg2

app = Flask(__name__)

# GET return a list of all planets [{'id': 1, 'name': 'plan1'}, {'id': 2, 'name': 'plan2'}, {'id': 3, 'name': 'somevalue'}]
# POST insert planet and return inserted planet {'id': 1, 'name': 'plan1'}
# id has to be null
@app.route('/planets', methods=['GET', 'POST'])
def planets():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456",
        port=5432
    )
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM planet")
        rows = cur.fetchall()
        res = []
        for row in rows:
            res.append(dict(id=row[0], name=row[1] ))
        return Response(str(res), status=200, mimetype='application/json')
    else:
        data = request.json
        try:
            hasKeys = 'id' in data and 'name' in data and data['id'] == None
            checkFields = type(data['name']) == str and len(data['name']) > 0
            if hasKeys and checkFields:
                cur = conn.cursor()
                cur.execute("INSERT INTO planet(name) values('{name}') RETURNING id".format(name=data['name']))
                conn.commit()
                new_row_id = cur.fetchone()[0]
                res = dict(id=new_row_id, name=data["name"])
                cur.close()
                return Response(str(res), status=200, mimetype='application/json')
            else:
                return Response("errr", status=422, mimetype='application/json')

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
            return Response("errr", status=422, mimetype='application/json')
        finally:
            if conn is not None:
                conn.close()

# GET return a list of all connections [{'id': 1, 'from_planet_id': 1, 'to_planet_id': 2, 'price': 4}, {'id': 2, 'from_planet_id': 1, 'to_planet_id': 1, 'price': 42}]
# POST insert planet and return inserted connection {'id': 1, 'from_planet_id': 1, 'to_planet_id': 2, 'price': 4}
# id has to be null, price > 0, if planet ids not in db, then return 404
@app.route('/connections', methods=['GET', 'POST'])
def connections():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456",
        port=5432
    )
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM connection")
        rows = cur.fetchall()
        res = []
        for row in rows:
            res.append(dict(id=row[0], from_planet_id=row[1], to_planet_id=row[2], price=row[3]))
        if conn is not None:
                conn.close()
        return Response(str(res), status=200, mimetype='application/json')
    else:
        data = request.json
        try:
            hasKeys = 'id' in data and 'from_planet_id' in data and 'to_planet_id' in data and 'price' in data and data['id'] == None 
            checkFields = type(data['from_planet_id']) == int and type(data['to_planet_id']) == int and type(data['price']) == int and data['price'] > 0
            if hasKeys and checkFields:
                cur = conn.cursor()
                cur.execute("INSERT INTO connection(from_planet_id,to_planet_id,price) values('{fp}','{tp}','{pr}') RETURNING id"
                            .format(fp=data['from_planet_id'], tp=data['to_planet_id'], pr=data['price']))
                conn.commit()
                new_row_id = cur.fetchone()[0]
                res = dict(id=new_row_id, fp=data['from_planet_id'], to=data['to_planet_id'], pr=data['price'])
                cur.close()
                return Response(str(res), status=200, mimetype='application/json')
            else:
                print(hasKeys)
                print(checkFields)
                return Response("errr", status=422, mimetype='application/json')

        except psycopg2.DatabaseError as e:
            print("db-err")
            print(e)
            return Response("errr", status=404, mimetype='application/json')
        except Exception as e:
            print(e)
            print("idk-err")
            return Response("errr", status=422, mimetype='application/json')
        finally:
            if conn is not None:
                conn.close()
                

# find the cheapest path, return if its reachable, return price and connections used
@app.route('/booking/<int:from_planet_id>/<int:to_planet_id>') 
def algoTask(from_planet_id, to_planet_id):
    return 'Hello ' + from_planet_id + ' ' + to_planet_id 

if __name__ == '__main__':
    app.run(debug=True)

