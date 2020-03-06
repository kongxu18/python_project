"""
天龙八部设计
    封装：将每种影响效果单独做成类
    继承：将各种影响效果抽象 SkillImpactEffect
        隔离技能释放器于各种影响效果的变化
    多态：各种影响效果在重写抽象 SkillImpactEffect中的方法
        释放器调用 父类 执行各种效果

    六大原则：
        开闭：增加新 技能 新影响效果，不修改释放器 客户端代码
        单一职责：每个类有且只有一个改变的原因
            SkillImpactEffect 负责隔离变化
            DamageEffect 负责定义具体效果
        依赖倒置：释放器 没有调用具体影响效果，而是调用抽象父类SkillImpactEffect
            抽象的不依赖于具体的 eval 执行字符串。
            要创建一个子对象，使用依赖注入，读取配置文件，使释放器不依赖具体影响效果
        组合复用：释放器与影响效果使组合关系，可以灵活的选择各种影响效果
        里氏替换：父出现的地方可以被子类替换掉
            释放器存储影响效果列表，实际可以将各类子类存进去
            父类方法 super 扩展重写
        迪米特法制：低耦合。
"""


# 技能影响效果
class SkillImpactEffect:
    def impact(self):
        raise NotImplementedError


class DamageEffect(SkillImpactEffect):
    """
    伤害生命
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print('扣除血量', self.value)


class LowerDeffenseEffect(SkillImpactEffect):
    """
    降低防御
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print('降低防御', self.value, self.time)


class DizzinessEffect(SkillImpactEffect):
    """
    眩晕
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print('眩晕', self.time)


class SkillDeployer:
    """
    技能释放器
        1，加载配置文件
        2。创建效果对象
        3。生成技能，执行效果
    """

    def __init__(self, name):
        self.name = name
        self.__dict_skill_config = self.__load_config_file()
        self.__effect_objects = self.__create_effect_objects()

    @staticmethod
    def __load_config_file():
        return {
            '降龙十八掌': ['DamageEffect(200)', 'LowerDeffenseEffect(-20,5)'],
            '六脉神剑': ['DamageEffect(200)', 'DizzinessEffect(6)']
        }

    def __create_effect_objects(self):
        # 根据name 创建相应的技能对象
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            list_effect_object.append(eval(item))
        return list_effect_object

    def generate_skill(self):
        print(self.name, '释放')
        for item in self.__effect_objects:
            item.impact()


xlsbz = SkillDeployer('降龙十八掌')
xlsbz.generate_skill()
