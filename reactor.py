import re

class Molecule:
    regex = '[A-Z]([a-z])*(_[1-9]([0-9])*)*' # molecular abbrevations
    elements = {}
    # {'H': 2, 'O': 1}
    # input syntax: H_2O
    def __init__(self, abbrevation):

        return
    def calculate_molar_mass(self):
        return

class Element:
  def __init__(self, abbrevation, molar_mass):
    self.abbrevation = abbrevation
    self.molar_mass = molar_mass

class Elements:
    elements = []

    def add_elements(self,element):
        self.elements.append(element)

    def get_molar_mass(self,abbrevation):
        for element in self.elements:
            if element.abbrevation == abbrevation:
                return element.molar_mass

molecules = ['H_2O','NH_3','C_6H_6','NaCl','NH_4NCS','C_6H_20','C_1H_3']

for molecule in molecules:
    match = re.finditer('[A-Z]([a-z])*(_[1-9]([0-9])*)*',molecule)
    for mtc in match:
        print(mtc)

elements = Elements()
elements.add_elements(Element("H",1.0079))
elements.add_elements(Element("He",4.0026))
elements.add_elements(Element("Li",6.941))
elements.add_elements(Element("Be",9.0122))
elements.add_elements(Element("B",10.811))
elements.add_elements(Element("C",12.0107))
elements.add_elements(Element("N",14.0067))
elements.add_elements(Element("O",15.9994))
elements.add_elements(Element("F",18.9984))
elements.add_elements(Element("Ne",20.1797))
elements.add_elements(Element("Na",22.9897))
elements.add_elements(Element("Mg",24.305))
elements.add_elements(Element("Al",26.9815))
elements.add_elements(Element("Si",28.0855))
elements.add_elements(Element("P",30.9738))
elements.add_elements(Element("S",32.065))
elements.add_elements(Element("Cl",35.453))
elements.add_elements(Element("K",39.0983))
elements.add_elements(Element("Ar",39.948))
elements.add_elements(Element("Ca",40.078))
elements.add_elements(Element("Sc",44.9559))
elements.add_elements(Element("Ti",47.867))
elements.add_elements(Element("V",50.9415))
elements.add_elements(Element("Cr",51.9961))
elements.add_elements(Element("Mn",54.938))
elements.add_elements(Element("Fe",55.845))
elements.add_elements(Element("Ni",58.6934))
elements.add_elements(Element("Co",58.9332))
elements.add_elements(Element("Cu",63.546))
elements.add_elements(Element("Zn",65.39))
elements.add_elements(Element("Ga",69.723))
elements.add_elements(Element("Ge",72.64))
elements.add_elements(Element("As",74.9216))
elements.add_elements(Element("Se",78.96))
elements.add_elements(Element("Br",79.904))
elements.add_elements(Element("Kr",83.8))
elements.add_elements(Element("Rb",85.4678))
elements.add_elements(Element("Sr",87.62))
elements.add_elements(Element("Y",88.9059))
elements.add_elements(Element("Zr",91.224))
elements.add_elements(Element("Nb",92.9064))
elements.add_elements(Element("Mo",95.94))
elements.add_elements(Element("Tc",98.9063))
elements.add_elements(Element("Ru",101.07))
elements.add_elements(Element("Rh",102.9055))
elements.add_elements(Element("Pd",106.42))
elements.add_elements(Element("Ag",107.8682))
elements.add_elements(Element("Cd",112.411))
elements.add_elements(Element("In",114.818))
elements.add_elements(Element("Sn",118.71))
elements.add_elements(Element("Sb",121.76))
elements.add_elements(Element("I",126.9045))
elements.add_elements(Element("Te",127.6))
elements.add_elements(Element("Xe",131.293))
elements.add_elements(Element("Cs",132.9055))
elements.add_elements(Element("Ba",137.327))
elements.add_elements(Element("La",138.9055))
elements.add_elements(Element("Ce",140.116))
elements.add_elements(Element("Pr",140.9077))
elements.add_elements(Element("Nd",144.24))
elements.add_elements(Element("Pm",145))
elements.add_elements(Element("Sm",150.36))
elements.add_elements(Element("Eu",151.964))
elements.add_elements(Element("Gd",157.25))
elements.add_elements(Element("Tb",158.9253))
elements.add_elements(Element("Dy",162.5))
elements.add_elements(Element("Ho",164.9303))
elements.add_elements(Element("Er",167.259))
elements.add_elements(Element("Tm",168.9342))
elements.add_elements(Element("Yb",173.04))
elements.add_elements(Element("Lu",174.967))
elements.add_elements(Element("Hf",178.49))
elements.add_elements(Element("Ta",180.9479))
elements.add_elements(Element("W",183.84))
elements.add_elements(Element("Re",186.207))
elements.add_elements(Element("Os",190.23))
elements.add_elements(Element("Ir",192.217))
elements.add_elements(Element("Pt",195.078))
elements.add_elements(Element("Au",196.9665))
elements.add_elements(Element("Hg",200.59))
elements.add_elements(Element("Tl",204.3833))
elements.add_elements(Element("Pb",207.2))
elements.add_elements(Element("Bi",208.9804))
elements.add_elements(Element("Po",209))
elements.add_elements(Element("At",210))
elements.add_elements(Element("Rn",222))
elements.add_elements(Element("Fr",223))
elements.add_elements(Element("Ra",226))
elements.add_elements(Element("Ac",227))
elements.add_elements(Element("Pa",231.0359))
elements.add_elements(Element("Th",232.0381))
elements.add_elements(Element("Np",237))
elements.add_elements(Element("U",238.0289))
elements.add_elements(Element("Am",243))
elements.add_elements(Element("Pu",244))
elements.add_elements(Element("Cm",247))
elements.add_elements(Element("Bk",247))
elements.add_elements(Element("Cf",251))
elements.add_elements(Element("Es",252))
elements.add_elements(Element("Fm",257))
elements.add_elements(Element("Md",258))
elements.add_elements(Element("No",259))
elements.add_elements(Element("Rf",261))
elements.add_elements(Element("Lr",262))
elements.add_elements(Element("Db",262))
elements.add_elements(Element("Bh",264))
elements.add_elements(Element("Sg",266))
elements.add_elements(Element("Mt",268))
elements.add_elements(Element("Rg",272))
elements.add_elements(Element("Hs",277))

print("*************************************************************************")
print("Welcome to Reactor >.<")
print("please enter a reaction equation")
print("Example: N_2 + H_2 -> NH_3")
reaction_equation = input("Please enter the reaction equation: ")
print("Example: N_2 + H_2 -> NH_3")
reaction_equation = reaction_equation.strip()
print("Example: N_2+H_2->NH_3")
reaction_equation = reaction_equation.split("->")
reaction_equation_left = reaction_equation[0]
reaction_equation_right = reaction_equation[1]
reaction_equation_left = reaction_equation_left.split("+")
reaction_equation_right = reaction_equation_right.split("+")
print("*************************************************************************")




