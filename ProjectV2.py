import json
import os
from experta import *
from typing import Union
from FactClasses import *
class SkinCareExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        # this is for the tree @nour we can still do it if we have time ✌
        # self.graph = graphviz.Digraph(comment='Skin Care Expert System')
        self.recommendations = []
        self.valid_cf_values=[-1.0,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8, 1]
        # keep it just in case:
        # ----
        # self.CleanserRecommendations = []
        # self.MoisturizerRecommendations = []
        # self.SunscreenRecommendations = []
        # self.GenderRec = []
        # self.SenRec = []
        # self.pregrec = []
        # ----
        
        

    
        
#   User info 
#   using the rules we can assign the user details (it better approach and give us better and cleaner code)
#   also it can help us when it comes to expanding 
    def Userinfo(self,genderr,acne,skintype,skintone,age,pregnancyr,acnedets,skindefs,sdd,sensitvityd,sensitvitys,seasons,skinconditionb,routines,cf1,cf2,cf3,cf4,cf5,cf6,cf7,cf8,cf9,cf10,cf11,cf12,cf13,cf14): 
        self.declare( User(gender=genderr,genderconf=cf1
                           ,skintype=skintype,
                        skintypeconf=cf4,
                    skintone=skintone,skintoneconf=cf5,season=seasons,seasonconf=cf13,
                    routinetype=routines,routinetypeconf=cf12,
                    sensitivity=sensitvitys,sensitivityconf=cf11,
                    sensitivitydetails=sensitvityd,sensitivitydetailsconf=cf10,
                    have_acne=acne,have_acneconf=cf3,
                    acnedetails=acnedets,acnedetailsconf=cf7,
                    skindeffects=skindefs,skindeffectsconf=cf8,
                    skincondition=skinconditionb,skinconditionconf=cf14,
                    deffectsdetails=sdd,deffectsdetailsconf=cf9,
                    age=age,ageconf=cf6,
                    pregnancy=pregnancyr,pregnancyconf=cf2,
                    # breastfeeding=cf15
                    ))
    @Rule( Answer(ident=L("Gender"),text=MATCH.genderr,cf=MATCH.cf1),
          Answer(ident=L("pregnancy"),text=MATCH.pregnancyr,cf=MATCH.cf2),
          Answer(ident=L("Acne"),text=MATCH.acne,cf=MATCH.cf3),
          Answer(ident=L("Skin Type"),text=MATCH.skintype,cf=MATCH.cf4),
          Answer(ident=L("SkinTone"),text=MATCH.skintone,cf=MATCH.cf5),
          Answer(ident=L("Age"),text=MATCH.age,cf=MATCH.cf6),
          Answer(ident=L("acne details"),text=MATCH.acnedets,cf=MATCH.cf7),
          Answer(ident=L("skin defects"),text=MATCH.skindefs,cf=MATCH.cf8),
          Answer(ident=L("skin defects details"),text=MATCH.sdd,cf=MATCH.cf9),
          Answer(ident=L("sensitvity details"),text=MATCH.sensitvityd,cf=MATCH.cf10),
          Answer(ident=L("sensitvity"),text=MATCH.sensitvitys,cf=MATCH.cf11),
          Answer(ident=L("routine"),text=MATCH.routines,cf=MATCH.cf12),
          Answer(ident=L("season"),text=MATCH.seasons,cf=MATCH.cf13),
          Answer(ident=L("skin condition"),text=MATCH.skinconditionb,cf=MATCH.cf14)
          
          )

    # def Userinfo(self,genderr,acne,skintype,skintone,age,pregnancyr,acnedets,skindefs,sdd,sensitvityd,sensitvitys,seasons,skinconditionb):
    def Userinfo(self,genderr,acne,skintype,skintone,age,pregnancyr,acnedets,skindefs,sdd,sensitvityd,sensitvitys,seasons,skinconditionb,routines,cf1,cf2,cf3,cf4,cf5,cf6,cf7,cf8,cf9,cf10,cf11,cf12,cf13,cf14): 
        

        print("yoink3")
        self.declare( User(gender=genderr,genderconf=cf1
                           ,skintype=skintype,
                        skintypeconf=cf4,
                    skintone=skintone,skintoneconf=cf5,season=seasons,seasonconf=cf13,
                    routinetype=routines,routinetypeconf=cf12,
                    sensitivity=sensitvitys,sensitivityconf=cf11,
                    sensitivitydetails=sensitvityd,sensitivitydetailsconf=cf10,
                    have_acne=acne,have_acneconf=cf3,
                    acnedetails=acnedets,acnedetailsconf=cf7,
                    skindeffects=skindefs,skindeffectsconf=cf8,
                    skincondition=skinconditionb,skinconditionconf=cf14,
                    deffectsdetails=sdd,deffectsdetailsconf=cf9,
                    age=age,ageconf=cf6,
                    pregnancy=pregnancyr,pregnancyconf=cf2,
                    # breastfeeding=cf15
                    ))
        
            

        
    
# --------------------------------------------------------------------------------------------------------
# Products assignment
# in here we can set the products depending on the user info
# we will add more products and examples in the future 
    # cleansers
    # based on skin type + skin condtion and sensitivity
    @Rule(User(skintype=L("oily"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2))
    def Oilycleanser5(self,cf1,cf2):
        cleanser_reason = 'A good cleanser is essential for removing dirt, oil,     and impurities from the skin, helping to unclog pores and prevent   breakouts.'
        cleanser_reason += ' Look for products containing Salicylic Acid or     Glycolic Acid, which can help control oil production and exfoliate the  skin.'
        cleanser_ingredients = ['Salicylic Acid', 'Glycolic Acid']
        cleanser_avoidance = ['Harsh Surfactants', 'Artificial Fragrances']
        cf = 0.9 *min(cf1,cf2)

        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",    ingredients=cleanser_ingredients, reason=cleanser_reason,  avoidance=cleanser_avoidance, conf=cf))
    
    @Rule(User(skintype=L("oily"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),skinconditionconf=MATCH.cf1,sensitivityconf=MATCH.cf2))
    def Oilycleanser1(self,cf1,cf2):
        cleanser_reason = "Rosacea is a chronic inflammatory skin condition. Harsh cleansers can irritate and inflame the skin, worsening rosacea symptoms. A gentle cleanser helps remove excess oil, dirt, and makeup without stripping the skin's natural moisture barrier. Oily skin with rosacea can be a tricky combination. You want to remove excess oil to prevent breakouts, but you also don't want to over-strip the skin,"
        cleanser_ingredients = ['chamomile', 'green tea','licorice root extract']
        cleanser_avoidance = ['Harsh Sulfates', 'Alcohol', 'Fragrance','Exfoliating Scrubs']
        cf = 0.9 *min(cf1,cf2)

        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("oily"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),skinconditionconf=MATCH.cf1,sensitivityconf=MATCH.cf2))
    def Oilycleanser2(self,cf1,cf2):
        cleanser_reason = "Support Skin Barrier: Eczema disrupts the skin's natural barrier, making it susceptible to irritation and dryness. Gentle cleansers help remove dirt and irritants without further damaging the barrier. Reduce Inflammation: Eczema involves inflammation in the skin. Using a gentle cleanser helps avoid unnecessary aggravation."
        cleanser_ingredients = ['Hydrating Ingredients ', 'Fatty Acids','Soothing Ingredients']
        cleanser_avoidance = ['Fragrance', 'Alcohol', 'Soap','Exfoliating Scrubs','Harsh Sulfates']
        cf = 0.9 *min(cf1,cf2)

        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("oily"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Oilycleanser3(self,cf1,cf2):

        cleanser_reason = 'Fragrance allergy. Find fragrance-free cleansers containing Salicylic or Glycolic Acid.'
        cleanser_ingredients = ['Salicylic Acid', 'Glycolic Acid']  
        cleanser_avoidance = ['Artificial Fragrances']
        cf = 0.9 *min(cf1,cf2)

        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("oily"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Oilycleanser4(self,cf1,cf2):
        cleanser_reason = 'hile salicylic acid is a common ingredient for pore cleansing, there are alternatives for those with allergies. A gentle cleanser helps keep pores clear and prevent breakouts without irritation.'
        cleanser_avoidance = ['Salicylic Acid (Obviously!)','Harsh Sulfates','Alcohol','Heavy Oils']
        cleanser_ingredients = ['Gentle Exfoliants', 'Soothing Ingredients','Hydrating Ingredients','Clay Masks (Optional)'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("oily"),skincondition=L("Rosacea"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Oilycleanser6(self,cf1,cf2):
        cleanser_reason = 'For oily skin with Rosacea and sensitivity, finding a cleanser requires a delicate balance, gentle cleansers are the better option'
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils']
        cleanser_ingredients = ['Gentle Exfoliants', 'Sulfates (SLS/SLES) - Limited (if tolerated)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients (for Rosacea):Green Tea Extract-Colloidal Oatmeal,','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("oily"),skincondition=L("Eczema"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Oilycleanser7(self,cf1,cf2):
        cleanser_reason = '''This needs a very gentle cleanser that offers:
Effective Cleansing: Removes excess oil and dirt without stripping the skin's natural oils.
Soothing Relief: Calms irritation and itching associated with Eczema.
Hydration: Provides moisture without clogging pores.
Skin Barrier Repair: Supports the skin's natural barrier function, crucial for Eczema.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils']
        cleanser_ingredients = ['Gentle Exfoliants', 'Sulfates (SLS/SLES) - Limited (if tolerated)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients:Oat Milk','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))

    # test
    @Rule(User(skintype=L("dry"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def Drycleanser1(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing:  A gentle cleanser removes dirt, impurities, and makeup without stripping away the already-limited moisture in dry skin. Maintain Moisture Barrier: Dry,  A gentle cleanser helps prevent further dryness and irritation."
        cleanser_ingredients = ['Hydrating Ingredients :Hyaluronic acid, ceramides', 'Soothing Ingredients :Chamomile,Creamy Cleansers:','Gentle Cleansers:']
        cleanser_avoidance = ['Harsh Sulfates', 'Alcohol','Fragrance']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def Drycleanser2(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing:  Rosacea is hypersensitive to harsh ingredients. A gentle cleanser removes dirt, impurities, and makeup without stripping away the already-limited moisture in dry skin. Maintain Moisture Barrier: Dry, rosacea-prone skin has a compromised moisture barrier. A gentle cleanser helps prevent further dryness and irritation."
        cleanser_ingredients = ['Hydrating Ingredients :Hyaluronic acid, ceramides', 'Soothing Ingredients :Chamomile,Creamy Cleansers:','Gentle Cleansers:']
        cleanser_avoidance = ['Harsh Sulfates', 'Alcohol','Fragrance']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def Drycleanser3(self,cf1,cf2):
        cleanser_reason = "Support Skin Barrier: Eczema disrupts the skin's natural barrier, making it dry, itchy, and prone to irritation. A gentle cleanser removes dirt and irritants without further damaging the barrier, allowing it to retain moisture. Minimize Irritation: Dry, eczema-prone skin is already sensitive. A gentle cleanser avoids unnecessary aggravation and helps soothe existing irritation."
        cleanser_ingredients = ["Ultra-Hydrating Ingredients: Hyaluronic acid, ceramides,", "Emollients: Ingredients like shea butter, cocoa butter",'Fragrance-Free']
        cleanser_avoidance = ['Harsh Sulfates', 'Alcohol','Soap']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def Drycleanser4(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing: Dry skin already lacks moisture, and harsh cleansers can further strip it away, worsening dryness and irritation. A gentle cleanser effectively removes dirt and impurities without disrupting the skin's delicate balance. Minimize Irritation: Fragrance is a common skin irritant, especially for those with sensitive skin. A fragrance-free cleanser avoids unnecessary aggravation and helps soothe existing dryness."
        cleanser_ingredients = ['Hydrating Ingredients: Hyaluronic acid', 'Fragrance-Free','Creamy or Ointment Cleansers']
        cleanser_avoidance = ['Fragrance (Obviously!)', 'Alcohol','Essential Oils']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def Drycleanser5(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing: Dry skin lacks moisture, and harsh cleansers can further strip it away, worsening dryness and irritation. A gentle cleanser effectively removes dirt and impurities without disrupting the skin's delicate balance. Minimize Irritation:  Since you're allergic to salicylic acid, a gentle cleanser avoids unnecessary aggravation and helps soothe existing dryness."
        cleanser_ingredients = ['Hydrating Ingredients: Hyaluronic acid', 'Emollients: Ingredients like shea butter, cocoa butter,','Gentle Cleansers:','Soothing Ingredients: Chamomile, calendula']
        cleanser_avoidance = ['Salicylic Acid (Obviously!)', 'Alcohol','Fragrance']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Rosacea"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Drycleanser6(self,cf1,cf2):
        cleanser_reason = '''This needs a very gentle cleanser that offers:
Mild Cleansing: Removes impurities without stripping away the skin's natural oils, which can worsen dryness.
Soothing Relief: Calms redness and irritation associated with Rosacea.
Hydration: Provides moisture to replenish dry skin.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils']
        cleanser_ingredients = ['Gentle Exfoliants', 'Sulfates (SLS/SLES) - Limited (if tolerated)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin - Hyaluronic Acid - Creamy Cleansers)','Soothing Ingredients (for Rosacea):Green Tea Extract-Licorice Root Extract,','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("dry"),skincondition=L("Eczema"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def Drycleanser7(self,cf1,cf2):
        cleanser_reason = '''This needs a very gentle cleanser that offers:
Ultra-Gentle Cleansing: Removes impurities without stripping away the skin's already compromised moisture barrier.
Soothing Relief: Calms irritation and itching associated with Eczema.
Hydration and Skin Barrier Repair: Provides moisture to replenish dry skin and supports the skin's natural barrier function, crucial for Eczema.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils','Sulfates (SLS/SLES)','Soap']
        cleanser_ingredients = ['Gentle Exfoliants','Micellar Water (Fragrance-Free)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients:Oat Milk','Non-comedogenic:','Lotion or Cream Cleansers'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    # test
    @Rule(User(skintype=L("combination"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def combinationcleanser1(self,cf1,cf2):
        cleanser_reason = 'A good cleanser is essential for removing dirt, oil, and impurities from the skin, helping to unclog pores and prevent breakouts.'
        cleanser_reason += ' Choose a gentle cleanser suitable for all skin types, and pay attention to oily areas without over-drying the dry parts.'
        cleanser_ingredients = ['Gentle Cleansing Agents', 'Botanical Extracts']
        cleanser_avoidance = ['Harsh Exfoliants', 'Heavy Oils']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def combinationcleanser2(self,cf1,cf2):
        cleanser_reason = "Balance Oil Control and Hydration: Combination skin has areas that are oily (often the T-zone: forehead, nose, chin) and areas that are dry or normal. A gentle cleanser removes excess oil from oily areas without stripping moisture from drier areas, maintaining a healthy balance. Minimize Rosacea Irritation: Harsh cleansers can irritate rosacea-prone skin, worsening redness and inflammation. A gentle cleanser cleanses effectively without triggering flare-ups."
        cleanser_ingredients = ['Balancing Ingredients: Niacinamide', 'Hydrating Ingredients: Hyaluronic acid or glycerin','Gentle Cleansers']
        cleanser_avoidance = ['Harsh Exfoliants', 'Heavy Oils','Harsh Sulfates','Alcohol','Fragrance']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def combinationcleanser3(self,cf1,cf2):
        cleanser_reason = "Balance Oil Control and Barrier Repair: Combination skin has areas that are oily (often the T-zone: forehead, nose, chin) and areas that are dry or eczema-prone. A gentle cleanser removes excess oil from oily areas without stripping moisture from drier, eczema-prone areas, while also supporting the skin's barrier function. Minimize Eczema Irritation: Harsh cleansers can irritate eczema, worsening redness, itching, and dryness. A gentle cleanser cleanses effectively without triggering flare-ups."
        cleanser_ingredients = ['Balancing Ingredients: Niacinamide', 'Barrier Repair Ingredients: Ceramides and hyaluronic acid','Soothing Ingredients: Chamomile, calendula','Gentle Cleansers']
        cleanser_avoidance = ['Harsh Exfoliants','Harsh Sulfates','Alcohol','Fragrance']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def combinationcleanser4(self,cf1,cf2):
        cleanser_reason = "Balance Oil Control: Combination skin has areas that are oily (often the T-zone) and areas that are normal or dry. A gentle cleanser removes excess oil from oily areas without stripping moisture from drier areas, maintaining a healthy balance. Minimize Irritation: Fragrance can irritate sensitive skin, especially for those with fragrance allergies. A fragrance-free cleanser avoids unnecessary aggravation and helps maintain a calm complexion."
        cleanser_ingredients = ['Balancing Ingredients: Niacinamide', 'Hydrating Ingredients: Hyaluronic acid or glycerin','Gentle Cleansers']
        cleanser_avoidance = ['Fragrance (Obviously!)','Harsh Sulfates','Alcohol']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def combinationcleanser5(self,cf1,cf2):
        cleanser_reason = "Balance Oil Control:  Combination skin has areas that are oily (often the T-zone) and areas that are normal or dry. A gentle cleanser removes excess oil from oily areas without stripping moisture from drier areas, maintaining a healthy balance. Minimize Irritation (No Salicylic Acid): Since you're allergic to salicylic acid, a gentle cleanser avoids any potential irritation and helps manage oil without triggering flare-ups."
        cleanser_ingredients = ['Balancing Ingredients: Niacinamide','Gentle Cleansers']
        cleanser_avoidance = ['Fragrance (Obviously!)','Harsh Sulfates','Alcohol']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Rosacea"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def combinationcleanser6(self,cf1,cf2):
        cleanser_reason = '''Finding a cleanser for combination skin with Rosacea and sensitivity requires addressing both dryness and oiliness while prioritizing gentleness.This needs a very gentle cleanser that offers:
Balanced Cleansing: Removes excess oil from the T-zone (forehead, nose, chin) without stripping moisture from drier cheeks.
Soothing Relief: Calms redness and irritation associated with Rosacea.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils']
        cleanser_ingredients = ['Gentle Exfoliants','Micellar Water (Oil-Free, Fragrance-Free) ','Low-Foaming Cream Cleansers', 'Sulfates (SLS/SLES) - Limited (if tolerated)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients (for Rosacea):Green Tea Extract-Licorice Root Extract,','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("combination"),skincondition=L("Eczema"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def combinationcleanser7(self,cf1,cf2):
        cleanser_reason = '''combination skin with Eczema requires a gentle cleanser that addresses both dryness and oiliness while prioritizing soothing properties.This needs a very gentle cleanser that offers:
Balanced Cleansing: Removes excess oil without stripping moisture from drier areas.
Soothing Relief: Calms irritation and itching associated with Eczema.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils','Sulfates (SLS/SLES)']
        cleanser_ingredients = ['Gentle Exfoliants','Micellar Water (Oil-Free, Fragrance-Free)','Lotion or Cream Cleansers','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients:Oat Milk','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    # test
    # @noores'note : make one for normal with Rosacea
    @Rule(User(skintype=L("normal"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def NormalCleanser1(self,cf1,cf2):
        cleanser_reason = "Maintain Balance:  Normal skin is the holy grail - not too oily, not too dry. A gentle cleanser effectively removes dirt, impurities, and makeup without disrupting the skin's natural balance and healthy moisture barrier. Support Overall Health:  A good cleanser helps maintain the clarity and radiance of healthy normal skin."
        cleanser_ingredients = ['Balancing Ingredients: Niacinamide',"Hydrating Ingredients (Optional)",'Gentle Cleansers']
        cleanser_avoidance = ['Fragrance ','Harsh Sulfates','Alcohol']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def NormalCleanser2(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing:  Even though your overall skin type is normal, eczema disrupts the skin's natural barrier, making it prone to dryness and irritation. A gentle cleanser removes dirt, impurities, and makeup without stripping away moisture or further damaging the barrier. Minimize Eczema Irritation:  Normal skin can tolerate more, but eczema patches are sensitive and easily irritated. A gentle cleanser avoids unnecessary aggravation and helps soothe existing irritation."
        cleanser_ingredients = ['Barrier Repair Ingredients: Ceramides and hyaluronic acid',"Soothing Ingredients: Chamomile, calendula",'Gentle Cleansers']
        cleanser_avoidance = ['Fragrance ','Harsh Sulfates','Alcohol','Exfoliating Scrubs']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def NormalCleanser3(self,cf1,cf2):
        cleanser_reason = "Gentle Cleansing:  Even though your overall skin type is normal,A gentle cleanser avoids unnecessary aggravation and helps soothe existing irritation."
        cleanser_ingredients = ['Barrier Repair Ingredients: Ceramides and hyaluronic acid',"Soothing Ingredients: Chamomile, calendula",'Gentle Cleansers']
        cleanser_avoidance = ['Fragrance ','Harsh Sulfates','Alcohol','Exfoliating Scrubs']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def NormalCleanser4(self,cf1,cf2):
        cleanser_reason = "Normal skin generally has a good balance of oil and moisture, so the cleanser's main purpose is to remove dirt, impurities, and makeup without disrupting this balance. Since you have a fragrance allergy, fragrance-free is the priority."
        cleanser_ingredients = ["Hydrating Ingredients (Optional)",'Gentle Cleansers']
        cleanser_avoidance = ['Fragrance (Obviously!) ','Harsh Sulfates','Alcohol']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def NormalCleanser5(self,cf1,cf2):
        cleanser_reason = "Normal skin generally has a good balance of oil and moisture. The cleanser's main purpose is to remove dirt, impurities, and makeup without disrupting this balance. Since you're allergic to salicylic acid, you'll need a cleanser that avoids it."
        cleanser_ingredients = ["Hydration Boost (Optional)",'Gentle Cleansers']
        cleanser_avoidance = ['Salicylic Acid','Harsh Sulfates','Alcohol']
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
        'product': 'Cleanser',
        'ingredients': cleanser_ingredients,
        'reason': cleanser_reason,
        'avoidance': cleanser_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser",ingredients=cleanser_ingredients,reason=cleanser_reason,avoidance=cleanser_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Rosacea"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def NormalCleanser6(self,cf1,cf2):
        cleanser_reason = '''Normal skin with Rosacea requires a gentle cleanser that removes impurities without disrupting the skin's natural balance.This needs a very gentle cleanser that offers:
Effective Cleansing: Removes dirt and makeup without stripping natural oils.
Soothing Relief: Calms redness and irritation associated with Rosacea.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils']
        cleanser_ingredients = ['Gentle Exfoliants','Micellar Water (Oil-Free, Fragrance-Free) ','Low-Foaming Cream Cleansers', 'Sulfates (SLS/SLES) - Limited (if tolerated)','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients (for Rosacea):Green Tea Extract-Licorice Root Extract,','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    @Rule(User(skintype=L("normal"),skincondition=L("Eczema"),sensitivitydetails=~L("Not any"),skinconditionconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2))
    def NormalCleanser7(self,cf1,cf2):
        cleanser_reason = '''Normal skin with Eczema requires a gentle cleanser that focuses on soothing irritation and supporting the skin barrier function. This needs a very gentle cleanser that offers:
Mild Cleansing: Removes impurities without stripping natural oils.
Soothing Relief: Calms irritation and itching associated with Eczema.
Hydration and Skin Barrier Repair: Supports the skin's natural barrier function, crucial for Eczema.'''
        cleanser_avoidance = ['Fragrance','Harsh Sulfates','Alcohol','Comedogenic Oils','Sulfates (SLS/SLES)']
        cleanser_ingredients = ['Gentle Exfoliants','Micellar Water (Oil-Free, Fragrance-Free)','Lotion or Cream Cleansers','HBetaine (Coco-Betaine, etc.)','Hydrating Ingredients(Glycerin)','Soothing Ingredients:Oat Milk','Non-comedogenic:'] 
        cf = 0.9 *min(cf1,cf2)
        self.recommendations.append({
            'product': 'Cleanser',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': cf,
        })
        self.declare(Recommendations(product="Cleanser", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=cf))
    # test
    # Moisturizer
    # based on skin type/acne/sensetivites/skin conditions
    @Rule(User(skintype=L("oily"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer1(self,cf1,cf2,cf3):
        moisturizer_reason = "Oily skin can be deceptive. While it produces excess oil, it still needs proper hydration to maintain a healthy barrier function. Using a moisturizer specifically formulated for oily skin helps: Balance hydration without clogging pores. Potentially reduce oil production over time. Improve overall skin health."
        moisturizer_ingredients = ['Niacinamide', 'Hyaluronic Acid']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer2(self,cf1,cf2,cf3):
        moisturizer_reason = "Oily, acne-prone skin needs a balancing act. It craves hydration to maintain a healthy barrier, but excess oil can lead to breakouts. A moisturizer formulated for oily skin with acne can help: Hydrate without clogging pores (non-comedogenic). Control excess oil production. Potentially reduce acne breakouts with specific ingredients."
        moisturizer_ingredients = ['Niacinamide', 'Acne-Fighting Ingredients(Salicylic Acid-Benzoyl Peroxide)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer3(self,cf1,cf2,cf3):
        moisturizer_reason = "Sensitive, oily skin presents a unique challenge. While it produces excess oil, harsh ingredients can easily trigger irritation. A gentle, oil-free moisturizer can help: Balance hydration without clogging pores (non-comedogenic). Soothe and calm sensitive skin. Maintain a healthy skin barrier"
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers', 'Soothing Ingredients(Centella Asiatica (CICA)-Allantoin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer4(self,cf1,cf2,cf3):
        moisturizer_reason = "oily skin can still have specific skin conditions that require tailored care. A moisturizer formulated for oily skin with a skin condition can help: Balance hydration without clogging pores (non-comedogenic). Address the specific concerns of your skin condition. Maintain a healthy skin barrier."
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers','fragrance-free']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer5(self,cf1,cf2,cf3):
        moisturizer_reason = "This combination requires a delicate balancing act. Oily skin needs hydration, but harsh ingredients can trigger irritation in sensitive skin, and the specific skin condition has its own needs. A gentle, oil-free moisturizer formulated for sensitive skin can help: Balance hydration without clogging pores (non-comedogenic). Soothe and calm sensitive skin. Maintain a healthy skin barrier, addressing the specific concerns of your skin condition."
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers','fragrance-free','Soothing Ingredients(Centella Asiatica (CICA)-Allantoin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer6(self,cf1,cf2,cf3):
        moisturizer_reason = "This combination requires a delicate balancing act. Oily skin needs hydration, but harsh ingredients can trigger irritation in sensitive skin, and the specific skin condition has its own needs. A gentle, oil-free moisturizer formulated for sensitive skin can help: Balance hydration without clogging pores (non-comedogenic). Soothe and calm sensitive skin. Maintain a healthy skin barrier, addressing the specific concerns of your skin condition. Additionally, some ingredients can help manage acne."
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers','fragrance-free','Soothing Ingredients(Centella Asiatica (CICA)-Allantoin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("oily"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer7(self,cf1,cf2,cf3):
        moisturizer_reason = "This combination requires a delicate balancing act. Oily skin needs hydration, and the specific skin condition has its own needs. A gentle, oil-free moisturizer formulated for sensitive skin can help: Balance hydration without clogging pores (non-comedogenic). Maintain a healthy skin barrier, addressing the specific concerns of your skin condition. Additionally, some ingredients can help manage acne."
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers','fragrance-free','Soothing Ingredients(Centella Asiatica (CICA)-Allantoin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
        
    @Rule(User(skintype=L("oily"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer8(self,cf1,cf2,cf3):
        moisturizer_reason = "This combination requires a delicate balancing act. Oily skin needs hydration, A gentle, oil-free moisturizer formulated for sensitive skin can help: Balance hydration without clogging pores (non-comedogenic). Additionally, some ingredients can help manage acne."
        moisturizer_ingredients = ['Oil-Free Lotions or Gel Moisturizers','fragrance-free','Soothing Ingredients(Centella Asiatica (CICA)-Allantoin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    # dry skin moistuizer
    @Rule(User(skintype=L("dry"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer1d(self,cf1,cf2,cf3):
        moisturizer_reason = 'Moisturizers help maintain the skin\'s hydration levels and protect the skin barrier.'
        moisturizer_reason += ' Choose rich, emollient moisturizers with ingredients like Hyaluronic Acid or Ceramides to replenish moisture and soothe dryness.'
        moisturizer_ingredients = ['Hyaluronic Acid', 'Ceramides']
        moisturizer_avoidance = ['Artificial Fragrances', 'Alcohol']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer2d(self,cf1,cf2,cf3):
        moisturizer_reason = '''Dry skin with acne can be a tricky combination. While acne-prone skin might benefit from some oil control, it also needs proper hydration to function optimally. The right moisturizer can:
Provide hydration without clogging pores (non-comedogenic).
Help manage acne breakouts.'''
        moisturizer_ingredients = ['non-comedogenic formulas', 'Acne-Fighting Ingredients(Salicylic Acid-Benzoyl Peroxide)','Hydrating Ingredients(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance','Heavy Creams or Ointments','Alcohol']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        
        
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer3d(self,cf1,cf2,cf3):
        moisturizer_reason = '''Dry, sensitive skin needs a gentle approach. Harsh ingredients can trigger irritation, so a fragrance-free, calming moisturizer is key to provide:
Deep hydration without clogging pores (non-comedogenic)
Soothing relief for sensitive skin'''
        moisturizer_ingredients = ['Creams or Ointments', 'Emollients(Ceramides-Shea Butter)','Humectants(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer4d(self,cf1,cf2,cf3):
        moisturizer_reason = '''Dry skin with a specific skin condition requires a targeted approach. A moisturizer can help with:
Deep hydration without clogging pores (non-comedogenic).
Addressing the specific concerns of your skin condition.'''
        moisturizer_ingredients = ['Creams or Ointments','fragrance-free moisturizers(ceramides-colloidal oatmeal)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer5d(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario requires a multi-pronged approach to address dry skin, sensitive skin, and a specific skin condition. This requires a gentle, yet effective moisturizer that provides deep hydration without clogging pores (non-comedogenic) while calming sensitivity and addressing your specific skin condition.'''
        moisturizer_ingredients = ['Creams or Ointments','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Emollients(Ceramides-Shea Butter)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer6d(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario requires a very careful approach due to the combination of dry skin, sensitive skin, acne, and a specific skin condition. Finding the right moisturizer is crucial. It needs to:
Provide deep hydration without clogging pores (non-comedogenic).
Soothe sensitivity and address your specific skin condition.
Potentially manage acne breakouts (gently, considering sensitivities).'''
        moisturizer_ingredients = ['Creams or Ointments','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments','Soothing ingredients (Niacinamide -Centella Asiatica (CICA))']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("dry"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer7d(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario allows for a more targeted approach to address dry skin, acne, and a specific skin condition, without the added concern of fragrance or ingredient sensitivity.Dry skin with acne needs a moisturizer that provides hydration without clogging pores (non-comedogenic) while also managing breakouts. Knowing your specific skin condition allows for further targeted benefits.'''
        moisturizer_ingredients = ['Creams (non-comedogenic)','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
        
    @Rule(User(skintype=L("dry"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer8d(self,cf1,cf2,cf3):
        moisturizer_reason = '''Here's a breakdown for a moisturizer suitable for dry, sensitive skin with acne, but without any specific skin conditions.This combination requires a delicate balance. Dry skin needs hydration, but harsh ingredients can trigger irritation in sensitive skin, and acne needs management. A gentle, non-comedogenic moisturizer can:
Provide deep hydration without clogging pores.
Soothe sensitivity.
Potentially help manage acne breakouts (gently, considering sensitivities).'''
        moisturizer_ingredients = ['Creams(fragrance-free" and "gentle)','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Avoid Harsh Acne Treatments(Salicylic Acid and Benzoyl Peroxide)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    
    # combination skin
    @Rule(User(skintype=L("combination"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer1c(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario allows for a more straightforward approach to address combination skin, which can have oily areas (typically T-zone: forehead, nose, chin) and drier areas (typically cheeks).Your goal is to find a moisturizer that provides:
Hydration for the drier areas without clogging pores (non-comedogenic) in the oilier areas.
A lightweight, comfortable feel for all-day wear.'''
        moisturizer_ingredients = ['Lotions or Gel-Creams', 'Humectants(Hyaluronic Acid-Glycerin)','Emollients (optional):Ceramides-Dimethicone']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer2c(self,cf1,cf2,cf3):
        moisturizer_reason = '''a moisturizer suitable for combination skin with acne, but without sensitive skin or other skin conditions : Combination skin with acne needs a moisturizer that addresses both concerns:
Provides hydration for drier areas without clogging pores (non-comedogenic) in the oilier T-zone.
Helps manage acne breakouts.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams', 'Acne-Fighting Ingredients(Salicylic Acid-Benzoyl Peroxide)','Hydrating Ingredients(Hyaluronic Acid-Glycerin)','Humectants(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer3c(self,cf1,cf2,cf3):
        moisturizer_reason = '''a moisturizer suitable for combination skin with sensitive skin, but without acne or other skin conditions:Sensitive skin with combination needs a gentle approach. Harsh ingredients can trigger irritation, so a fragrance-free, calming moisturizer is key to:
Provide targeted hydration for drier and oilier areas without clogging pores (non-comedogenic).
Soothe and protect sensitive skin.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams', 'Emollients(Ceramides-Shea Butter)','Humectants(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance',]
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer4c(self,cf1,cf2,cf3):
        moisturizer_reason ='''a moisturizer suitable for combination skin with a specific skin condition, but without acne or sensitive skin:Combination skin with a specific skin condition requires a targeted approach. A moisturizer can help with:
Hydration for drier areas without clogging pores (non-comedogenic) in the oilier T-zone.
Addressing the specific concerns of your skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(non-comedogenic)','fragrance-free moisturizers(ceramides-colloidal oatmeal)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer5c(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario requires a multi-pronged approach to address combination skin, sensitive skin, and a specific skin condition, all without worrying about acne.This requires a gentle, yet effective moisturizer that:
Provides targeted hydration for drier and oilier areas without clogging pores (non-comedogenic).
Soothes sensitivity.
Addresses the specific concerns of your specific skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Emollients(Ceramides-Shea Butter)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer6c(self,cf1,cf2,cf3):
        moisturizer_reason ='''This scenario requires the most delicate balancing act. Here's how to navigate finding a moisturizer for combination skin with acne, sensitive skin, and a specific skin condition:This needs a gentle moisturizer that offers:
Targeted hydration for drier and oilier areas without clogging pores (non-comedogenic).
Soothing relief for sensitive skin.
Some level of acne management (considering sensitivities).
Addressing the specific concerns of your skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments','Soothing ingredients (Niacinamide -Centella Asiatica (CICA))']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("combination"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer7c(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario allows for a more targeted approach to address acne and a specific skin condition within the context of combination skin, without worrying about fragrance or ingredient sensitivity.Combination skin with acne and a skin condition needs a moisturizer that offers:
Targeted hydration for drier and oilier areas without clogging pores (non-comedogenic).
Management of acne breakouts.
Addressing the specific concerns of your skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams (non-comedogenic)','fragrance-free ','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
        
    @Rule(User(skintype=L("combination"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer8c(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario requires a delicate balance between managing acne and soothing sensitive skin.This needs a gentle moisturizer that offers:
Targeted hydration for drier and oilier areas without clogging pores (non-comedogenic).
Management of acne breakouts (considering sensitivities).'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Avoid Harsh Acne Treatments(Salicylic Acid and Benzoyl Peroxide)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    
    # normal skin
    @Rule(User(skintype=L("normal"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer1n(self,cf1,cf2,cf3):
        moisturizer_reason ='''Normal skin needs a basic moisturizer that provides:
Hydration to maintain the skin's natural balance.
Protection from environmental factors.'''
        moisturizer_ingredients = ['Lotions or Creams', 'Humectants(Hyaluronic Acid-Glycerin)','Emollients (optional):Ceramides-Dimethicone']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer2n(self,cf1,cf2,cf3):
        moisturizer_reason = '''Normal skin with acne needs a moisturizer that addresses both concerns: 
Provides hydration without clogging pores (non-comedogenic).
Helps manage acne breakouts.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams', 'Acne-Fighting Ingredients(Salicylic Acid-Benzoyl Peroxide)','Hydrating Ingredients(Hyaluronic Acid-Glycerin)','Humectants(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer3n(self,cf1,cf2,cf3):
        moisturizer_reason = '''Normal skin provides a good base, but sensitivity requires a gentle approach. This moisturizer should:
Provide hydration without disrupting the sensitive skin barrier.
Soothe and protect sensitive skin.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams', 'Emollients(Ceramides-Shea Butter)','Humectants(Hyaluronic Acid-Glycerin)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance',]
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("no"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer4n(self,cf1,cf2,cf3):
        moisturizer_reason ='''Normal skin provides a good base, but the specific skin condition requires targeted ingredients. This moisturizer should:
Provide hydration without disrupting the skin barrier.
Address the concerns of his specific skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(non-comedogenic)','fragrance-free moisturizers(ceramides-colloidal oatmeal)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("no"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer5n(self,cf1,cf2,cf3):
        moisturizer_reason = '''This scenario requires a multi-pronged approach to address normal skin, sensitive skin, and a specific skin condition:This needs a very gentle moisturizer that offers:
Hydration without disrupting the sensitive skin barrier.
Soothing properties to calm irritation.
Targeted ingredients for his specific skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Emollients(Ceramides-Shea Butter)']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments','Alcohol']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer6n(self,cf1,cf2,cf3):
        moisturizer_reason ='''This scenario requires the most delicate balancing act. Here's how to navigate finding a moisturizer for normal skin with acne, sensitive skin, and a specific skin condition:This needs a very gentle moisturizer that offers:
Hydration without clogging pores (non-comedogenic).
Soothing relief for sensitive skin.
Limited acne management (considering sensitivities).
Addressing the specific concerns of his skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','fragrance-free','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)', 'Fragrance (if applicable)','Heavy Creams or Ointments','Soothing ingredients (Niacinamide -Centella Asiatica (CICA))']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    @Rule(User(skintype=L("normal"),have_acne=L("yes"),sensitivitydetails=L("Not any"),skincondition=~L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer7n(self,cf1,cf2,cf3):
        moisturizer_reason = '''a moisturizer suitable for normal skin with acne and a specific skin condition, without sensitive skinThis needs a moisturizer that offers:
Hydration without clogging pores (non-comedogenic).
Management of acne breakouts.
Addressing the concerns of his specific skin condition.'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams (non-comedogenic)','fragrance-free ','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Ingredients that Clog Pores (Comedogenic)']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
        
    @Rule(User(skintype=L("normal"),have_acne=L("yes"),sensitivitydetails=~L("Not any"),skincondition=L("Not any"),have_acneconf=MATCH.cf1,sensitivitydetailsconf=MATCH.cf2,skinconditionconf=MATCH.cf3),)
    def RecommededMoisturizer8n(self,cf1,cf2,cf3):
        moisturizer_reason ='''This scenario requires a delicate balance between managing acne and soothing sensitive skin. This needs a very gentle moisturizer that offers:
Hydration without clogging pores (non-comedogenic).
Management of acne breakouts (considering sensitivities).'''
        moisturizer_ingredients = ['Lotions or Lightweight Creams(fragrance-free and gentle)','Humectants(Hyaluronic Acid-Glycerin)','Acne-Fighting Ingredients(Salicylic Acid (if not sensitive)-Niacinamide )']
        moisturizer_avoidance = ['Avoid Harsh Acne Treatments(Salicylic Acid and Benzoyl Peroxide)', 'Fragrance (if applicable)','Heavy Creams or Ointments']
        cf = 0.9 *min(cf1,cf2,cf3)
        self.recommendations.append({
        'product': 'Moisturizer',
        'ingredients': moisturizer_ingredients,
        'reason': moisturizer_reason,
        'avoidance': moisturizer_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Moisturizer",ingredients=moisturizer_ingredients,reason=moisturizer_reason,avoidance=moisturizer_avoidance,conf=cf))
    # test
    # sunscreen
    # based on routine and season and Skin Condition,Skin Sensitivity,
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2))
    def RecommededSunScreen1(self,cf1,cf2):
        sunscreen_reason = "Protects skin from harmful UVA and UVB rays, especially important during summer when the sun's rays are strongest. Helps prevent premature aging and sun damage, including sunburn"
        sunscreen_ingredients = ['Zinc Oxide', 'Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters', 'Oxybenzone']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Not any"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen2(self,cf1,cf2):
        sunscreen_reason = 'Sunscreen is crucial for protecting the skin from harmful UV rays and preventing premature aging and sun damage.'
        sunscreen_reason += ' Even in colder months, UV rays can still penetrate through clouds and windows, so daily sunscreen application is essential.'
        sunscreen_ingredients = ['Zinc Oxide', 'Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters', 'Oxybenzone']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen3(self,cf1,cf2):
        sunscreen_reason = 'Essential for protecting eczema-prone skin from UV rays, which can worsen flare-ups and irritation.'
        sunscreen_reason += ' Even in colder months, UV rays can still penetrate through clouds and windows, so daily sunscreen application is essential.'
        sunscreen_ingredients = ['Zinc Oxide', 'Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen4(self,cf1,cf2):
        sunscreen_reason = 'Crucial for protecting rosacea-prone skin from UV rays, a major trigger for flare-ups.'
        sunscreen_reason += ' Even in colder months, UV rays can still penetrate through clouds and windows, so daily sunscreen application is essential.'
        sunscreen_ingredients = ['Zinc Oxide', 'Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance ']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Eczema"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen5(self,cf1,cf2):
        sunscreen_reason = "While the sun's rays are weaker in winter, UV exposure can still damage eczema-prone skin.  Sunscreen helps protect against:Premature aging and wrinkles (caused by UVA rays).Sunburn (caused by UVB rays, even on cloudy days)."
        # sunscreen_reason += ' Even in colder months, UV rays can still penetrate through clouds and windows, so daily sunscreen application is essential.'
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)', 'Chemical UV Filters']
        sunscreen_avoidance = ['Harsh chemicals','fragrance']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Rosacea"),sensitivitydetails=L("Not any"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen6(self,cf1,cf2):
        sunscreen_reason = "Important for protecting rosacea-prone skin from UV rays, a trigger for flare-ups, even in winter."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)']
        sunscreen_avoidance = ['Chemical UV Filters','fragrance']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen7(self,cf1,cf2):
        sunscreen_reason = "Essential for protecting your skin from UV rays, especially important in summer when the sun's strongest. Sunscreen helps prevent premature aging and sun damage, including sunburn"
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen8(self,cf1,cf2):
        sunscreen_reason = "Essential for protecting your skin from UV rays, especially important in summer when the sun's strongest. Sunscreen helps prevent premature aging and sun damage, including sunburn., ook for fragrance-free and non-comedogenic formulas."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Not any"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen9(self,cf1,cf2):
        sunscreen_reason = "While the sun's rays are weaker in winter, UV exposure can still damage your skin. Sunscreen helps protect against:Premature aging and wrinkles (caused by UVA rays).Sunburn (caused by UVB rays, even on cloudy days)."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Not any"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen10(self,cf1,cf2):
        sunscreen_reason = "While the sun's rays are weaker in winter, UV exposure can still damage your skin. Sunscreen helps protect against:Premature aging and wrinkles (caused by UVA rays).Sunburn (caused by UVB rays, even on cloudy days)."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
        # sunscreen comb
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Eczema"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen11(self,cf1,cf2):
        sunscreen_reason = "Although the winter sun is weaker, UV exposure can still irritate eczema-prone skin. Sunscreen helps protect against Premature aging (UVA rays)Sunburn (UVB rays)"
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Eczema"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen12(self,cf1,cf2):
        sunscreen_reason = "Important for protecting eczema-prone skin from UV rays, even in winter."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Rosacea"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen13(self,cf1,cf2):
        sunscreen_reason = "Although the winter sun is weaker, UV exposure can still irritate eczema-prone skin. Sunscreen helps protect against Premature aging (UVA rays)Sunburn (UVB rays)"
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("winter"),skincondition=L("Rosacea"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen14(self,cf1,cf2):
        sunscreen_reason = "Crucial for protecting rosacea-prone skin from UV rays, a major trigger for flare-ups, even in winter."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Eczema"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen15(self,cf1,cf2):
        sunscreen_reason = "Essential for protecting eczema-prone skin from UV rays, especially crucial in summer when the sun's strongest. Sunscreen helps prevent premature aging and sun damage, including sunburn, which can worsen eczema."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Eczema"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen16(self,cf1,cf2):
        sunscreen_reason = "Crucial for protecting eczema-prone skin from UV rays, especially in summer."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Rosacea"),sensitivitydetails=L("allergy to salicylic acid"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen17(self,cf1,cf2):
        sunscreen_reason = "Critical for protecting rosacea-prone skin from UV rays, a major trigger for flare-ups, even in summer."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Salicylic Acid (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    @Rule(User(routinetype=L("morning"),season=L("summer"),skincondition=L("Rosacea"),sensitivitydetails=L("Fragrance Allergy"),sensitivityconf=MATCH.cf1,skinconditionconf=MATCH.cf2),)
    def RecommededSunScreen18(self,cf1,cf2):
        sunscreen_reason = "Crucial for protecting rosacea-prone skin from UV rays, a major trigger for flare-ups, even in summer."
        sunscreen_ingredients = ['Mineral UV Filters (physical blockers)','Zinc Oxide','Titanium Dioxide']
        sunscreen_avoidance = ['Chemical UV Filters','Fragrance (obviously!)']
        cf=0.9*min(cf1,cf2)
        self.recommendations.append({
        'product': 'Sun screen',
        'ingredients': sunscreen_ingredients,
        'reason': sunscreen_reason,
        'avoidance': sunscreen_avoidance,
        'confidence': cf,
        })
        self.declare(Recommendations(product="Sun screen",ingredients=sunscreen_ingredients,reason=sunscreen_reason,avoidance=sunscreen_avoidance,conf=cf))
    
        
    # Serum 
    # based on the routine type and age 
    @Rule(OR(User(routinetype=L("night"),age=L("mature")),User(routinetype=L("both"),age=L("mature"))))
    def Recommededserum1(self):
        serum_reason = 'Serums are concentrated formulas designed to target specific skincare concerns, such as fine lines, wrinkles, and loss of firmness.'
        serum_ingredients = ['Retinol', 'Peptides']
        serum_avoidance = ['Artificial Colors', 'Parabens']
        self.recommendations.append({
        'product': 'Anti-Aging Serum',
        'ingredients': serum_ingredients,
        'reason': serum_reason,
        'avoidance': serum_avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(product="Anti-Aging Serum",ingredients=serum_ingredients,reason=serum_reason,avoidance=serum_avoidance,conf=1.0))
    @Rule(User(skincondition=L("hyperpigmentation")))
    def Recommededserum2(self):
        serum_reason = 'Brightening serums help to fade dark spots, even out skin tone, and restore radiance to the complexion.'
        serum_ingredients = ['Vitamin C', 'Niacinamide']
        serum_avoidance = ['Fragrance', 'Essential Oils']
        self.recommendations.append({
            'product': 'Brightening Serum',
            'ingredients': serum_ingredients,
            'reason': serum_reason,
            'avoidance': serum_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="Brightening Serum",ingredients=serum_ingredients,reason=serum_reason,avoidance=serum_avoidance,conf=1.0))
        
    
    
    # special cases:
    
    # Sensitive Skin
    @Rule(User(skintype=W(), sensitivity=L("yes")))
    def RefineForSensitiveOilySkin(self,):
        sensitive_reason = 'Gentle, soothing products are essential for sensitive skin to minimize irritation and maintain a healthy skin barrier.'
        sensitive_ingredients = ['Aloe Vera', 'Colloidal Oatmeal']
        sensitive_avoidance = ['Alcohol', 'Synthetic Dyes']
        self.recommendations.append({
            'product': 'Soothing Cream',
            'ingredients': sensitive_ingredients,
            'reason': sensitive_reason,
            'avoidance': sensitive_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="Soothing Cream",ingredients=sensitive_ingredients,reason=sensitive_reason,avoidance=sensitive_avoidance,conf=1.0))
        
    # Gender-specific recommendations
        
    @Rule(User(gender=L("female")))
    def GenderSpeRec1(self):
        feminine_hygiene_reason = 'Feminine hygiene products should be gentle and pH-balanced to maintain intimate area health and prevent irritation.'
        feminine_hygiene_ingredients = ['Hypoallergenic', 'Fragrance-Free']
        feminine_hygiene_avoidance = ['Artificial Dyes', 'Harsh Surfactants']
        self.recommendations.append({
        'product': 'Feminine Hygiene Products',
        'ingredients': feminine_hygiene_ingredients,
        'reason': feminine_hygiene_reason,
        'avoidance': feminine_hygiene_avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(product="Feminine Hygiene Products",ingredients=feminine_hygiene_ingredients,reason=feminine_hygiene_reason,avoidance=feminine_hygiene_avoidance,conf=1.0))
    @Rule(User(gender=L("male")))
    def GenderSpeRec2(self):
        shaving_gel_reason = 'Using a shaving gel with soothing ingredients can help minimize irritation and razor burn during shaving.'
        shaving_gel_ingredients = ['Aloe Vera', 'Vitamin E']
        shaving_gel_avoidance = ['Alcohol', 'Menthol']
        self.recommendations.append({
        'product': 'Shaving Gel',
        'ingredients': shaving_gel_ingredients,
        'reason': shaving_gel_reason,
        'avoidance': shaving_gel_avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(product="Shaving Gel",ingredients=shaving_gel_ingredients,reason=shaving_gel_reason,avoidance=shaving_gel_avoidance))
    
    # Pregnancy and breastfeeding considerations
    @Rule(User(pregnancy=L("yes"),gender=L('female')))
    def PregORBFRec(self):
        pregnancy_safe_reason = 'Opt for pregnancy-safe skincare products with minimal use of active ingredients that may be harmful during pregnancy or breastfeeding.'
        pregnancy_safe_ingredients = ['Glycolic Acid (in low concentrations)', 'Hyaluronic Acid', 'Vitamin C (in stable form)']
        pregnancy_safe_avoidance = ['Retinoids', 'Salicylic Acid (in high concentrations)']
        self.recommendations.append({
            'product': 'Pregnancy-Safe Skincare',
            'ingredients': pregnancy_safe_ingredients,
            'reason': pregnancy_safe_reason,
            'avoidance': pregnancy_safe_avoidance,
            'confidence': 1.0,
            
        })
        self.declare(Recommendations(product="Pregnancy-Safe Skincare",ingredients=pregnancy_safe_ingredients,reason=pregnancy_safe_reason,avoidance=pregnancy_safe_avoidance,conf=1.0))
        
    # Skin Tone Specific Recommendations
    @Rule(User(skintone=L("fair")))
    def Skintone1(self):
        fair_skin_reason = 'For fair skin tones, focus on products that offer gentle care and protection against UV damage.'
        fair_skin_ingredients = ['Gentle Exfoliants', 'SPF Moisturizers']
        fair_skin_avoidance = ['Heavy Fragrances', 'Chemical Peels']
        self.recommendations.append({
            'product': 'Fair Skin Care',
            'ingredients': fair_skin_ingredients,
            'reason': fair_skin_reason,
            'avoidance': fair_skin_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="Fair Skin Care",ingredients=fair_skin_ingredients,reason=fair_skin_reason,avoidance=fair_skin_avoidance,conf=1.0))
    @Rule(User(skintone=L("medium")))
    def Skintone2(self):
        medium_skin_reason = 'Medium skin tones can benefit from products that maintain moisture and even out complexion.'
        medium_skin_ingredients = ['Hydrating Serums', 'Tinted Moisturizers']
        medium_skin_avoidance = ['Drying Alcohols', 'Harsh Scrubs']
        self.recommendations.append({
            'product': 'Medium Skin Care',
            'ingredients': medium_skin_ingredients,
            'reason': medium_skin_reason,
            'avoidance': medium_skin_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="Medium Skin Care",ingredients=medium_skin_ingredients,reason=medium_skin_reason,avoidance=medium_skin_avoidance,conf=1.0))
    @Rule(User(skintone=L("dark")))
    def Skintone3(self):
        dark_skin_reason = 'Dark skin tones require products that prevent hyperpigmentation and provide adequate moisture.'
        dark_skin_ingredients = ['Dark Spot Correctors', 'Rich Body Butters']
        dark_skin_avoidance = ['Bleaching Agents', 'Heavy Fragrances']
        self.recommendations.append({
            'product': 'Dark Skin Care',
            'ingredients': dark_skin_ingredients,
            'reason': dark_skin_reason,
            'avoidance': dark_skin_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="Dark Skin Care",ingredients=dark_skin_ingredients,reason=dark_skin_reason,avoidance=dark_skin_avoidance,conf=1.0))
    #test
    @Rule(User(skincondition=L("Eczema")),)
    def KnowledgeinfoEczema(self):
        explaination = 'the disease is due to inheritance of a faulty gene in your skin called Filaggrin or flare with a particular food. Histamine is not the only cause of the itch of eczema so anti-histamines may not control the symptoms.'
        ingredients = ['Colloidal Oatmeal ', 'Ceramides', 'Extra Soothing','Barrier Repair']
        avoidance = ['Stress', 'Skin Dryness', 'Allergens', 'Harsh Soaps']
        self.recommendations.append({
        'product': 'INFO:',
        'ingredients': ingredients,
        'explaination': explaination,
        'avoidance': avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(info="INFO",ingredients=ingredients,explaination=explaination,avoidance=avoidance,conf=1.0))
    @Rule(User(sensitivitydetails=L("Food")),)
    def KnowledgeinfoFood(self):
        explaination = 'Check product labels for potential allergens. Use products clearly labeled as free from specific allergens'
        ingredients = ['Nut Oils-Free', 'Diary-Free', 'Gluten-Free', 'Soy-Free', 'Cirtus-Free']
        avoidance = ['Lactose', 'Casein', 'Nuts Oil', 'Almond Oil', 'Peanuts', 'Wheat', 'Barley', 'Rye', 'Soybean', 'Soy Lecithin', 'Citrus Oils']
        self.recommendations.append({
        'product': 'INFO:',
        'ingredients': ingredients,
        'explaination': explaination,
        'avoidance': avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(info="INFO",ingredients=ingredients,explaination=explaination,avoidance=avoidance,conf=1.0))
    @Rule(User(sensitivitydetails=L("Chemicals")),)
    def KnowledgeinfoChemical(self):
        explaination = 'for products labeled as -free of harsh chemicals-, -hypoallergenic- and -non-comedogeni'
        ingredients = ['sulfate-free', 'paraben-free', 'formaldehyde-free', 'phthalate-free', 'phenoxyethanol-free', 'alcohol-free']
        avoidance = ['Sodium Lauryl Sulfates (SLS)', 'Sodium Laureth Sulfates (SLS)', 'Methylparaben', 'Propylparaben' 'Quaternium-15', 'DMDM Hydantoin', 'Imidazolidinyl Urea', 'Fragrances', 'Undisclosed Chemicals', 'SD Alcohol']
        self.recommendations.append({
        'product': 'INFO:',
        'ingredients': ingredients,
        'explaination': explaination,
        'avoidance': avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(info="INFO",ingredients=ingredients,explaination=explaination,avoidance=avoidance,conf=1.0))
    @Rule(User(sensitivitydetails=L("Preservative")),)
    def KnowledgeinfoChemicalPreservative(self):
        explaination = 'for products labeled as -free of harsh chemicals-, -hypoallergenic- and -non-comedogenic'
        ingredients = ['grapefruit seed extract', 'natural preservatives', 'preservative-free']
        avoidance = ['Parabens', 'formaldehyde-releasing agents', 'DMDM hydantoin', 'methylisothiazolinone (MIT)', 'methylchloroisothiazolinone (CMIT)']
        self.recommendations.append({
        'product': 'INFO:',
        'ingredients': ingredients,
        'explaination': explaination,
        'avoidance': avoidance,
        'confidence': 1.0,
        })
        self.declare(Recommendations(info="INFO",ingredients=ingredients,explaination=explaination,avoidance=avoidance,conf=1.0))
    @Rule(User(skintype=L("oily")))
    def USA(self):
        cleanser_reason = '''The US wants to give you freedom'''
        cleanser_avoidance = ['Dictatorship','socialism']
        cleanser_ingredients = ['Oil','Democracy'] 
        self.recommendations.append({
            'product': 'USA',
            'ingredients': cleanser_ingredients,
            'reason': cleanser_reason,
            'avoidance': cleanser_avoidance,
            'confidence': 1.0,
        })
        self.declare(Recommendations(product="USA", ingredients=cleanser_ingredients, reason=cleanser_reason, avoidance=cleanser_avoidance, conf=1.0))
    @Rule(User(skintype=~L("default")),salience=-1)
    def Default(self):
        # with open('recommendations.json', 'a') as json_file:
        #     json.dump(self.recommendations, json_file)
        #     json_file.write('\n')
        # print("Facts have been successfully written to facts.json")
        if os.path.exists('recommendations.json'):
            with open('recommendations.json', 'w') as json_file:
                json.dump(self.recommendations, json_file)
                json_file.write('\n')
            print("File already existed. Updated the recommendations.")
        else:
            with open('recommendations.json', 'a') as json_file:
                json.dump(self.recommendations, json_file)
                json_file.write('\n')
            print("Facts have been successfully written to recommendations.json")
    
        
# engine = SkinCareExpertSystem()
# engine.reset()
# engine.run()
# print(engine.facts)
