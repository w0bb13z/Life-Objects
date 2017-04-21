#!/usr/bin/python36

import os, sys, getopt

try:
    import numpy
except ImportWarning:
    "It is recommended to have 'numpy' installed for 'python3.6'."
    pass


class Person:
    """\
    This is a class object representing a real world 'Person'.
    
    Note: This does not include "citizen" implementations such as...
            - Jobs, Housing, Social Security Number...etc
    
    :args: Each attribute provided during class' __init__
    - gender______________Person's identified gender.
    - first_name__________Person's legal first name.
    - last_name___________Person's legal last name.
    - age_________________Person's uptime since birth.
    - birthday____________Person's DD/MM/YYYY of birth.
    - hair_type___________Person's Hair type such as ['Long','Wavy'].
    - hair_color__________Person's Hair color such as "brown"
    - eye_color___________Person's eye color such as 'green'
    - ethnicity___________Person's primary ethnic heritage such as 'Caucasian'.
    - height______________Person's physical height measured in feet & inches (f' i").
    - weigth______________Person's physical weight measured in pounds (lbs.).
    - sexuality___________Person's identified sexuality / sexual preferences.
    - bloodtype___________Person's medically documented blood type identifier.
    - health______________Person's overall medically diagnosed health as a percentage.
    - favorite_color______Person's personally assigned favorite color.
    - favorite_music______Person's personally assigned favorite music genre
    - lucky_number________Person's personally assigned lucky/favorite number.
    - talents_____________Person's personally undertaken talents.
    - handicaps___________Person's medically diagnosed handicaps.
    - common_mood_________Person's general outward appearence/energy.
    - medical_diagnoses___Person's medically diagnosed health complications.
    - allergies___________Person's medically diagnosed allergies.
    """
    # TBA: Please only add to these if you also have a functional purpose in mind for it.
    # TBA: The act of assigning a value to a container/variable is the act of using up
    # TBA: private memory. Literally. Let's not waste it.
    def __init__(self, gender, first_name, last_name, age,
                 birthday, hair_type, hair_color, eye_color,
                 ethnicity, height, weight, sexuality,
                 bloodtype, health, favorite_color, lucky_number,
                 favorite_music, talents, handicaps,
                 common_mood, medical_diagnoses, allergies):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.hair_type = hair_type
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.ethnicity = ethnicity
        self.height = height
        self.weight = weight
        self.sexuality = sexuality
        self.bloodtype = bloodtype
        self.health = health
        self.favorite_color = favorite_color
        self.favorite_music = favorite_music
        self.lucky_number = lucky_number
        self.talents = talents
        self.handicaps = handicaps
        self.common_mood = common_mood
        self.medical_diagnoses = medical_diagnoses
        self.allergies = allergies

        # Defined Dictionaries
        self.dictAttributes = {'gender': self.gender,
                               'firstname': self.first_name, 'fname': self.first_name,
                               'lastname': self.last_name, 'lname': self.last_name,
                               'age': self.age, 'birthday': self.birthday[0:],
                               'hairtype': self.hair_type, 'htype': self.hair_type,
                               'eyecolor': self.eye_color, 'ecolor': self.eye_color,
                               'ethnicity': self.ethnicity, 'race': self.ethnicity,
                               'height': self.height[0:], 'weight': self.weight,
                               'sexuality': self.sexuality,
                               'bloodtype': self.bloodtype, 'btype': self.bloodtype,
                               'favoritemusic': self.favorite_music, 'fmusic': self.favorite_music,
                               'favoritecolor': self.favorite_color, 'fcolor': self.favorite_color,
                               'luckynumber': self.lucky_number, 'luckynum': self.lucky_number,
                               'talents': self.talents[0:],
                               'handicaps': self.handicaps[0:], 'disabilities': self.handicaps[0:],
                               'commonmood': self.common_mood, 'cmood': self.common_mood,
                               'medicaldiagnoses': self.medical_diagnoses[0:],
                               'mdiagnoses': self.medical_diagnoses[0:], 'health': self.health,
                               'allergies': self.allergies[0:]}
        pass

    def PrettyPrint(self):
        print("""\n\
               First Name:   {}
                Last Name:   {}
                   Gender:   {}
                      Age:   {}
                 Birthday:   {}
                Hair Type:   {}
               Hair Color:   {}
                Eye Color:   {}
                Ethnicity:   {}
                   Height:   {}
                   Weight:   {}
                Sexuality:   {}
                BloodType:   {}
                   Health:   {}
           Favorite Color:   {}
           Favorite Music:   {}
             Lucky Number:   {}
                  Talents:   {}
                Handicaps:   {}
              Common Mood:   {}
        Medical Diagnoses:   {}
                Allergies:   {}
        """.format(self.first_name, self.last_name, self.gender, self.age, self.birthday[0:],
                   self.hair_type, self.hair_color, self.eye_color, self.ethnicity, self.height[0:],
                   self.weight, self.sexuality, self.bloodtype, self.health, self.favorite_color,
                   self.favorite_music, self.lucky_number, self.talents[0:], self.handicaps[0:],
                   self.common_mood, self.medical_diagnoses[0:], self.allergies[0:]))

    def get(self, *args):
        """\
        This function returns a list of values in the same corresponding order
        that the user provides the arguments in.
        
        :return: PassedArgs[] => dictAttributes[str(PassedArgs[])]
        """
        toReturn = []
        for i in args:
            if str(i) in self.dictAttributes:
                toReturn.append(self.dictAttributes[str(i)])
            else:
                pass
            pass
        return toReturn

    def set(self, *args):
        """\
        This function allows the modification of core attribute values.
        Such as in the wake of a "life changing" event or the acquisition of
        behavior changing knowledge or even personal choices such as changing
        their own name.
        """
        for i in args:
            if len(i) > 1:
                if self.dictAttributes[i[0]] is list:
                    try:
                        cntr = 0
                        # TBA: ERROR. THIS IS UNALIGNED. (IN ANIMAL.PY ASWELL!!)
                        for iA in i:
                            cntr += 1
                            if cntr is 2:
                                cntr = 0
                                self.dictAttributes[i[0]][1] = i[0][1]
                            else:
                                self.dictAttributes[i[0]][0] = i[0][0]
                                pass
                            pass
                        pass
                    except IndexError:
                        print("Error ID: 0x002 [Array Append]")
                        sys.exit(0x002)
                try:
                    self.dictAttributes[i[0]] = i[1]
                    print("Person's {} was changed to '{}' successfully"
                          .format(str(i[0]), str(i[1])))
                    continue
                except IndexError:
                    print("""\n\
                    Error. Set is used like this:
                       > Person.set([attributeName,valueToSet])
                       real EG:
                       > myperson.set(['ethnicity','african american'])\n
                    """)
                    break
                pass
            else:
                print("""\n\
                Error. Set is used like this:
                       > Person.set([attributeName,valueToSet])
                       real EG:
                       > myperson.set(['ethnicity','african american'])\n
                    """)
                break
            pass
        pass


#### END CLASS ####



#### TESTS GO HERE ####

myperson = Person('Male', "Jimmy", "Johnster", 24, [2, 26, 1993], 'Long Wavy', "Black", 'blue',
                  'caucasian', [5, 11], 132, "Heterosexual", "AB+", '75%', "Purple", 14, "Rap",
                  ["has no friends", "lol talents"], [], "Chill", ["ADHD", "Bipolar"], ['Peanuts'])
print(myperson.get('medicaldiagnoses', 'weight', 'age'))
myperson.set(['weight', 111], ['age', 42])
print(myperson.get('weight', 'age', 'height'))
myperson.set(['height', [5, 2]])
print(myperson.get('height'))

myperson.PrettyPrint()

#### END TESTS ####
