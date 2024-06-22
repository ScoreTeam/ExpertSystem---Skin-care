from experta import *
from typing import Union
class Answer(Fact):
    ident=Field(str)
    text=Field(str)
    cf=Field(float,mandatory=False,default=1.0)
class Question(Fact):
    qid=Field(str)
    ident = Field(str)
    questionType = Field(str)
    valid = Field(list or int or str)
    text = Field(str)
    cfq=Field(str,mandatory=True,default="What is your cf?")
class Ask(Fact):
    questionIdent=Field(str)
    cf=Field(float,mandatory=False,default=1.0)
class User(Fact):
    skintype = Field(str)
    skintypeconf = Field(float)
    skintone = Field(str)
    skintoneconf = Field(float)
    season = Field(str)
    seasonconf = Field(float)
    routinetype = Field(str)
    routinetypeconf = Field(float)
    # sensitivity = Field(str)
    # sensitivityconf = Field(float)
    sensitivitydetails = Field(str)
    sensitivitydetailsconf = Field(float)
    have_acne = Field(str)
    have_acneconf = Field(float)
    # noore's notess: i think we should delete acne dets
    # new noore's note : based on nour's feedback the ance details will server as cf
    acnedetails = Field(str)
    acnedetailsconf = Field(float)
    skindeffects = Field(str)
    skindeffectsconf = Field(float)
    skincondition = Field(str)
    skinconditionconf = Field(float)
    age = Field(str)
    ageconf = Field(float)
    gender = Field(str)
    genderconf = Field(float)
    pregnancy = Field(str)
    pregnancyconf = Field(float)
    breastfeeding = Field(str)
    breastfeedingconf = Field(float)

class Recommendations(Fact):
     product = Field(str)
     ingredients = Field(list)
     reason = Field(str)
     avoidance = Field(list),
     conf=Field(float)
    #  def __init__(self, product, ingredients, reason, avoidance, conf):
    #     self.product = product
    #     self.ingredients = ingredients
    #     self.reason = reason
    #     self.avoidance = avoidance
    #     self.conf = conf

    #  def __str__(self):
    #     return (f"Recommendations(product='{self.product}', "
    #             f"ingredients={self.ingredients}, reason='{self.reason}', "
    #             f"avoidance={self.avoidance}, conf={self.conf})")


