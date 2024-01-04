import os
import cv2
import detect
from flask import Flask, url_for, render_template, request, session, json, send_from_directory, current_app, g,make_response, jsonify
from config.config import *
from base.sqlhelper import SqlHelper
from tqdm import tqdm
import time
from multiprocessing import pool
a=detect.detectapi(weights='./pt/yolov5s.pt')  #yolov5s.pt






app = Flask(__name__)
app.config['SECRET_KEY'] = 'video-cms'

pbar=None
@app.route('/GETVIDEOSTUAS', methods=['POST'])
def get_stuas():
	response = make_response(jsonify(dict(n=pbar.n, total=pbar.total)))
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', '*')
	response.headers.add('Access-Control-Allow-Methods', '*')
	return response




def gen_video(video_name):
	videoWriter = None
	fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
	cap = cv2.VideoCapture(r'upload/video/'+video_name)
	fps = int(cap.get(5)) #5帧率 7总帧数
	num = int(cap.get(7))
	global pbar
	pbar = tqdm(total=num, desc="Count", unit="it")
	while cap.isOpened():
		rec, img = cap.read()
		if not rec:
			break
		img1 = cv2.resize(img, (800, 640))
		result, names, dian = a.detect([img1])
		img = result[0][0]  # 第一张图片的处理结果图片
		if videoWriter is None:
			newname=video_name.split('.')[0]
			cv2.imwrite("upload/img/" + newname+".jpg",
						img1)
			cv2.imwrite("upload/img/" + "xin_"+newname + ".jpg",
						img)
			videoWriter = cv2.VideoWriter(
			r'upload/chuli_video/' +"xin_"+video_name, fourcc, fps, (img.shape[1], img.shape[0]))
		videoWriter.write(img)
		pbar.update(1)  # 进度条更新

	print('video done!')
	cap.release()
	videoWriter.release()
	cv2.destroyAllWindows()
	pbar.close()  # 关闭资源
	response = make_response(jsonify(dict(n=pbar.n, total=pbar.total)))
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', '*')
	response.headers.add('Access-Control-Allow-Methods', '*')
	return response


def init():
	g.website_name = website_name
	g.username = session.get('username')
	if g.username is not None:
		helper = SqlHelper()
		sql = "select * from category"
		g.categories = helper.fetchall(sql)






@app.route('/')
@app.route('/index')
@app.route('/index/<int:category_id>')
def index(category_id = None):
	init()
	if g.username == None:
		return render_template('login.html')
	else:
		g.category_id = category_id
		helper = SqlHelper()
		if category_id is None:
			sql = "select * from video"
			g.videos = helper.fetchall(sql)
		else:
			sql = "select * from video where category_id=%s"
			g.videos = helper.fetchall(sql, (category_id,))

		return render_template('index.html')

@app.route('/login', methods = [ 'GET', 'POST' ])
def login():
	init()
	if request.method == 'POST':
		username = request.values.get('username')
		password = request.values.get('password')
		helper = SqlHelper()
		sql = 'select * from user where username=%s and password=%s'
		result = helper.fetchone(sql, (username, password));
		if result is None:
			return json.dumps({
				'success': 'false',
				'msg': 'Username or password is wrong!'
				})
		else:
			session['username'] = result['username']
			return json.dumps({
				'success': 'true',
				'msg': 'Login success!'
				})
	else:
		return render_template('login.html')

@app.route('/logout', methods = [ 'GET', 'POST' ])
def logout():
	session.clear()
	return json.dumps({
		'success': 'true',
		'msg': 'Logout success!'
		})

@app.route('/video/<int:id>')
def video(id):
	init()
	helper = SqlHelper()
	sql = "select * from video where id=%s"
	g.video = helper.fetchone(sql, (id,))
	return render_template('video.html')

@app.route('/manage/category')
def category_manage():
	init()
	g.pageSize = request.values.get('pageSize')
	g.pageNum = request.values.get('pageNum')

	if g.pageSize is None:
		g.pageSize = 10
	if g.pageNum is None:
		g.pageNum = 1

	g.pageNum = int(g.pageNum)
	g.pageSize = int(g.pageSize)
	
	helper = SqlHelper()
	sql = "select count(1) total from category"
	g.total = helper.fetchone(sql)['total']
	g.totalPage = int(g.total / g.pageSize) if g.total % g.pageSize == 0 else g.total // g.pageSize + 1

	sql = "select * from category order by id desc limit %s,%s "
	g.rows = helper.fetchall(sql, (g.pageSize * (g.pageNum - 1), g.pageSize))
	
	g.category_id = 'system'
	return render_template('manage/category.html');

@app.route('/manage/category/edit', methods = [ 'GET','POST' ])
def category_edit():
	init()
	id = request.values.get('id')
	id = 0 if id is None else int(id)
	helper = SqlHelper()
	if request.method == 'POST':
		name = request.values.get('name')
		if id == 0:
			sql = "insert into category (name) values (%s)"
			helper.execute(sql, (name,))
		else:
			sql = "update category set name=%s where id=%s"
			helper.execute(sql, (name, id))
		return json.dumps({
			'success': 'true',
			'msg': 'Save success!'
			})
	else:
		g.id = id
		g.name = ''
		if g.id > 0:
			sql = "select name from category where id=%s"
			category = helper.fetchone(sql, (id,))
			g.name = category['name']
		g.category_id = 'system'
		return render_template('manage/category_edit.html');

@app.route('/manage/category/delete/<int:id>', methods = ['POST'])
def category_delete(id):
	init()
	helper = SqlHelper()
	sql = "delete from category where id=%s"
	helper.execute(sql, (id,))
	return json.dumps({
		'success': 'true',
		'msg': 'Delete success!'
		})

@app.route('/manage/video')
def video_manage():
	init()
	g.pageSize = request.values.get('pageSize')
	g.pageNum = request.values.get('pageNum')

	if g.pageSize is None:
		g.pageSize = 10
	if g.pageNum is None:
		g.pageNum = 1

	g.pageNum = int(g.pageNum)
	g.pageSize = int(g.pageSize)
	
	helper = SqlHelper()
	sql = "select count(1) total from video"
	g.total = helper.fetchone(sql)['total']
	g.totalPage = int(g.total / g.pageSize) if g.total % g.pageSize == 0 else g.total // g.pageSize + 1

	sql = """select video.id,video.category_id,category.name category_name,video.name,video.path from video 
	    left join category on video.category_id=category.id order by id desc limit %s,%s """
	g.rows = helper.fetchall(sql, (g.pageSize * (g.pageNum - 1), g.pageSize))
	
	g.category_id = 'system'
	return render_template('manage/video.html');

@app.route('/manage/video/edit', methods = [ 'GET','POST' ])
def video_edit():
	init()
	id = request.values.get('id')
	id = 0 if id is None else int(id)
	helper = SqlHelper()
	if request.method == 'POST':
		category_id = request.values.get('category_id')
		name = request.values.get('name')
		path = request.values.get('path')
		picture = request.values.get('picture')
		if id == 0:
			sql = "insert into video (category_id,name,path,picture) values (%s,%s,%s,%s)"
			helper.execute(sql, (category_id, name, path, picture))
		else:
			sql = "update video set category_id=%s,name=%s,path=%s,picture=%s where id=%s"
			helper.execute(sql, (category_id, name, path, picture, id))
		return json.dumps({
			'success': 'true',
			'msg': 'Save success!'
			})
	else:
		g.id = id
		g.video_category_id = 0
		g.name = ''
		g.path = ''
		g.picture = ''
		if g.id > 0:
			sql = "select category_id,name,path,picture from video where id=%s"
			video = helper.fetchone(sql, (id,))
			g.video_category_id = video['category_id']
			g.name = video['name']
			g.path = video['path']
			g.picture = video['picture']
		g.category_id = 'system'
		return render_template('manage/video_edit.html');

@app.route('/manage/video/delete/<int:id>', methods = ['POST'])
def video_delete(id):
	init()

	helper = SqlHelper()
	sql1 = "select * from video where id=%s"
	all = helper.fetchone(sql1, (id,))
	name = all['name']
	category_id = all['category_id']
	sql = "delete from video where id=%s"
	helper.execute(sql, (id,))

	img_name = name.split(".")[0]
	if category_id ==1:
		os.remove("./upload/video/" + name)
	else:
		os.remove("./upload/chuli_video/"+name)
	os.remove("./upload/img/"+img_name+".jpg")
	return json.dumps({
		'success': 'true',
		'msg': 'Delete success!'
		})

@app.route('/manage/user')
def user_manage():
	init()
	g.pageSize = request.values.get('pageSize')
	g.pageNum = request.values.get('pageNum')

	if g.pageSize is None:
		g.pageSize = 10
	if g.pageNum is None:
		g.pageNum = 1

	g.pageNum = int(g.pageNum)
	g.pageSize = int(g.pageSize)
	
	helper = SqlHelper()
	sql = "select count(1) total from user"
	g.total = helper.fetchone(sql)['total']
	g.totalPage = int(g.total / g.pageSize) if g.total % g.pageSize == 0 else g.total // g.pageSize + 1

	sql = "select * from user order by id desc limit %s,%s "
	g.rows = helper.fetchall(sql, (g.pageSize * (g.pageNum - 1), g.pageSize))
	
	g.category_id = 'system'
	return render_template('manage/user.html');

@app.route('/manage/user/edit', methods = [ 'GET','POST' ])
def user_edit():
	init()
	id = request.values.get('id')
	id = 0 if id is None else int(id)
	helper = SqlHelper()
	if request.method == 'POST':
		username = request.values.get('username')
		password = request.values.get('password')
		name = request.values.get('name')
		if id == 0:
			sql = "insert into user (username,password,name) values (%s,%s,%s)"
			helper.execute(sql, (username,password,name))
		else:
			sql = "update user set username=%s,password=%s,name=%s where id=%s"
			helper.execute(sql, (username, password, name, id))
		return json.dumps({
			'success': 'true',
			'msg': 'Save success!'
			})
	else:
		g.id = id
		g.username = ''
		g.password = ''
		g.name = ''
		if g.id > 0:
			sql = "select username,password,name from user where id=%s"
			category = helper.fetchone(sql, (id,))
			g.username = category['username']
			g.password = category['password']
			g.name = category['name']
		g.category_id = 'system'
		return render_template('manage/user_edit.html');

@app.route('/manage/user/delete/<int:id>', methods = ['POST'])
def user_delete(id):
	init()
	helper = SqlHelper()
	sql = "delete from user where id=%s"
	helper.execute(sql, (id,))
	return json.dumps({
		'success': 'true',
		'msg': 'Delete success!'
		})

@app.route('/upload/<path:path>')
def send_upload(path):
	return send_from_directory('upload', path)

@app.route('/video', methods=['POST'])
def upload():
		f = request.files['file']
		basepath = os.path.dirname(__file__)  # 当前文件所在路径
		upload_path = './upload/video'
		# if not os.path.exists(upload_path):
		#     os.mkdir(upload_path)
		upload_file_path = os.path.join(basepath, upload_path, (f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
		f.save(upload_file_path)

		helper = SqlHelper()
		jpgname=f.filename.split('.')[0]
		sql = "insert into video (category_id,name,path,picture) values (%s,%s,%s,%s)"
		helper.execute(sql, (1,f.filename, '/upload/video/'+f.filename, '/upload/img/'+jpgname+'.jpg'))
		gen_video(f.filename)
		global pbar
		pbar =None
		sql = "insert into video (category_id,name,path,picture) values (%s,%s,%s,%s)"
		helper.execute(sql, (2, "xin_"+f.filename, '/upload/chuli_video/' +"xin_"+f.filename, '/upload/img/xin_'+jpgname+'.jpg'))





		return video_manage();







if __name__ == '__main__':
    app.run(host=ip, threaded=True, debug=False, port=web_port)
