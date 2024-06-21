# -*- coding: utf-8 -*-
from experta import Fact, Field

# Fact classes with associated fields
class Answer(Fact):
    ident = Field(str)
    text = Field(str)
    cf = Field(float, mandatory=False, default=1.0)

class Question(Fact):
    ident = Field(str)
    questionType = Field(str)
    valid = Field(list or int or str)
    text = Field(str)
    cfq = Field(str, mandatory=True, default="What is your cf?")

class Ask(Fact):
    questionIdent = Field(str)
    cf = Field(float, mandatory=False, default=1.0)

class User(Fact):
    skintype = Field(str)
    skintypeconf = Field(float)
    skintone = Field(str)
    skintoneconf = Field(float)
    season = Field(str)
    seasonconf = Field(float)
    routinetype = Field(str)
    routinetypeconf = Field(float)
    sensitivity = Field(str)
    sensitivityconf = Field(float)
    sensitivitydetails = Field(str)
    sensitivitydetailsconf = Field(float)
    have_acne = Field(str)
    have_acneconf = Field(float)
    # noore's notes: I think we should delete acne dets
    acnedetails = Field(str)
    acnedetailsconf = Field(float)
    skindeffects = Field(str)
    skindeffectsconf = Field(float)
    skincondition = Field(str)
    skinconditionconf = Field(float)
    deffectsdetails = Field(str)
    deffectsdetailsconf = Field(float)
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
    avoidance = Field(list)
    conf = Field(float)
