from models import Model


# 继承自 Model 的 Todo 类
class Todo(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        self.title = form.get('title', '')
        self.user_id = int(form.get('user_id', -1))
        self.created_time=form.get('created_time',None)
        self.updated_time=form.get('updated_time',None)
        # 还应该增加 时间 等数据
