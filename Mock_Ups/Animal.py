#!/usr/bin/python36

import os, sys, getopt

try:
    import numpy
except ImportWarning:
    "It is recommended to have 'numpy' installed for 'python3.6'."
    pass

class Animal:
    """\
    This is a class object representing a real world 'Animal'.
    
    Note: This does not include "citizen" implementations such as...
            - Jobs, Housing, Social Security Number...etc
    
    :args: Each attribute provided during class' __init__
    - name______________Animal's name. 'None' if Feral.
    - species___________Animal's generalized species, such as "cat".
    - kingdom___________Animal's generalized kingdom, such as 'feline'.
    - age_______________Animal's uptime since birth, or to general knowledge.
    - gender____________Animal's gender of birth.
    - birth_defects_____Animal's list of known medical birth defects.
    - health____________Animal's general medical health as a percentage.
    - height____________Animal's height in feet, and inches. such as [2,6] [ft,inches].
    - weight____________Animal's weight in American pounds (lbs.).
    - IsFeral___________<Bool> Is the animal feral?
    - IsOwned___________<Bool> Is the animal owned?
    - IsTrained_________<Bool> Is the animal trained?
    - IsInHeat__________<Bool> Is the animal in heat? (mating season)
    - IsPregnant________<Bool> Is the animal pregnant?
    - IsColorblind______<Bool> Is the animal colorblind? (generally determined by species.)
    - IsVaccinated______<Bool> Is the animal vaccinated as per standard practice?
    """
    # TBA: Please only add to these if you also have a functional purpose in mind for it.
    # TBA: The act of assigning a value to a container/variable is the act of using up
    # TBA: private memory. Literally. Let's not waste it.
    def __init__(self,name,species,kingdom,age,gender,birth_defects,
                 health,IsTrained,IsOwned,IsFeral,height,weight,
                 IsPregnant,IsInHeat,IsColorblind,IsVaccinated):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.age = age
        self.gender = gender
        self.birth_defects = birth_defects
        self.health = health
        self.height = height
        self.weight = weight
        self.IsFeral = IsFeral
        self.IsOwned = IsOwned
        self.IsTrained = IsTrained
        self.IsInHeat = IsInHeat
        self.IsPregnant = IsPregnant
        self.IsColorblind = IsColorblind
        self.IsVaccinated = IsVaccinated

        self.dictAttributes = {'name':self.name, 'species':self.species,
                               'kingdom':self.kingdom, 'age':self.age,
                               'gender':self.gender, 'birth_defects':self.birth_defects[0:],
                               'health':self.health, 'height':self.height[0:], 'weight':self.weight,
                               'isferal':self.IsFeral, 'isowned':self.IsOwned,
                               'istrained':self.IsTrained, 'isinheat':self.IsInHeat,
                               'ispregnant':self.IsPregnant, 'iscolorblind':self.IsColorblind,
                               'isvaccinated':self.IsVaccinated}

        pass

    def PrettyPrint(self):
        print("""\n\
              Name:   {}
           Species:   {}
           Kingdom:   {}
               Age:   {} Years Old
            Gender:   {}
     Birth Defects:   {}
            Health:   {}
            Height:   {}
            Weight:   {}
          Is Feral:   {}
          Is Owned:   {}
        Is Trained:   {}
        Is In Heat:   {}
       Is Pregnant:   {}
     Is Colorblind:   {}
     Is Vaccinated:   {}
        """.format(self.name,self.species,self.kingdom,self.age,
                   self.gender,self.birth_defects,self.health,
                   self.height[0:],self.weight,self.IsFeral,self.IsOwned,
                   self.IsTrained,self.IsInHeat,self.IsPregnant,
                   self.IsColorblind,self.IsVaccinated))
        pass

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
                        #TBA: ERROR. THIS IS UNALIGNED. (IN PERSON.PY ASWELL!!)
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
                    print("Animal's {} was changed to '{}' successfully"
                          .format(str(i[0]), str(i[1])))
                    continue
                except IndexError:
                    print("""\n\
                    Error. Set is used like this:
                       > Animal.set([attributeName,valueToSet])
                       real EG:
                       > myanimal.set(['isvaccinated', True])\n
                    """)
                    break
                pass
            else:
                print("""\n\
                Error. Set is used like this:
                       > Animal.set([attributeName,valueToSet])
                       real EG:
                       > myanimal.set(['isvaccinated', True])\n
                    """)
                break
            pass
        pass


#### END OF CLASS ####



#### TESTS GO HERE ####

myanimal = Animal("Annabelle","Cat","Feline", 5, 'Female',
                  ['Blind in Left Eye'], '65%', True, True,
                  False, [2,6], 34, False, True, False, True)
myanimal.PrettyPrint()
print(myanimal.get('name','height','height','isvaccinated'))
myanimal.set(['name','Vivian'],['height',[4,2]])
print(myanimal.get('height'))
myanimal.PrettyPrint()
print(myanimal.get('name','height','height','isvaccinated'))
myanimal.PrettyPrint()
#### END TESTS ####
