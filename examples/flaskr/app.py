from flask import Flask, request, jsonify
from dev.sorm import Model, StrField, IntField, TimeField


class Student(Model):
    name = StrField()
    gender = IntField()
    major = StrField()
    stu_num = StrField(maxlen=25)
    class_num = StrField(maxlen=25)
    mz = StrField(maxlen=10)
    birthdate = TimeField()


app = Flask(__name__)


# 若按学号查询
@app.route('/search', methods=['GET'])
def search_student():
    num = request.args.get('num')
    return jsonify(Student.where(stu_num=num).select())


"""
如此的简单粗暴
写成一行也没人阻止你 233
"""


if __name__ == '__main__':
    app.run()
