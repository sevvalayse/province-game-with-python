import turtle
from PIL import Image
from tkinter import messagebox

img = Image.open('./unnamed.gif')


class Province:
    data =[
        {
            'name': 'Adana',
            'x': img.width * 0.498,
            'y': img.height * 0.667,
            'entered': 0
        },
        {
            'name': 'Adıyaman',
            'x': img.width * 0.621,
            'y': img.height * 0.625,
            'entered': 0
        },
        {
            'name': 'Afyon',
            'x': img.width * 0.275,
            'y': img.height * 0.507,
            'entered': 0
        },
        {
            'name': 'Ağrı',
            'x': img.width * 0.849,
            'y': img.height * 0.403,
            'entered': 0
        },
        {
           'name': 'Aksaray',
            'x': img.width * 0.421,
            'y': img.height * 0.556,
            'entered': 0 
        },
        {
            'name': 'Amasya',
            'x': img.width * 0.498,
            'y': img.height * 0.305,
            'entered': 0
        },
        {
            'name': 'Ankara',
            'x': img.width * 0.342,
            'y': img.height * 0.377,
            'entered': 0
        },
        {
            'name': 'Antalya',
            'x':img.width*0.275,
            'y':img.height*0.7,
            'entered': 0
        },
        {
            'name': 'Artvin',
            'x':img.width*0.808,
            'y':img.height*0.233,
            'entered': 0
        },
        {
            'name': 'Aydın',
            'x': img.width * 0.124,
            'y': img.height * 0.608,
            'entered': 0
        },
        {
            'name': 'Balıkesir',
            'x':img.width*0.119,
            'y':img.height*0.394,
            'entered': 0
        },
        {
            'name': 'Bilecik',
            'x':img.width*0.237,
            'y':img.height*0.363,
            'entered': 0
        },
        {
            'name': 'Bingöl',
            'x':img.width*0.75,
            'y':img.height*0.478,
            'entered': 0
        },
        {   'name': 'Bitlis',
            'x':img.width*0.824,
            'y':img.height*0.536,
            'entered': 0
        },
        {
            'name': 'Bolu',
            'x':img.width*0.322,
            'y':img.height*0.314,
            'entered': 0
        },
        {
            'name': 'Burdur',
            'x':img.width*0.229,
            'y':img.height*0.648,
            'entered': 0
        },
        {
            'name': 'Bursa',
            'x':img.width*0.18,
            'y':img.height*0.357,
            'entered': 0
        },
        {
            'name': 'Çanakkale',
            'x':img.width*0.072,
            'y':img.height*0.348,
            'entered': 0
        },
        {
            'name': 'Çankırı',
            'x':img.width*0.409,
            'y':img.height*0.311,
            'entered': 0
        },
        {
            'name': 'Çorum',
            'x':img.width*0.46,
            'y':img.height*0.325,
            'entered': 0
        },
        {
            'name': 'Denizli',
            'x':img.width*0.186,
            'y':img.height*0.619,
            'entered': 0
        },
        {
            'name': 'Diyarbakır',
            'x':img.width*0.729,
            'y':img.height*0.573,
            'entered': 0
        },
        {
            'name': 'Edirne',
            'x':img.width * 0.08,
            'y':img.height * 0.25,
            'entered': 0
        },
        {
            'name': 'Elazığ',
            'x':img.width*0.681,
            'y':img.height*0.533,
            'entered': 0
        },
        {
            'name': 'Erzincan',
            'x':img.width*0.678,
            'y':img.height*0.406,
            'entered': 0
        },
        {
            'name': 'Erzurum',
            'x':img.width*0.778,
            'y':img.height*0.36,
            'entered': 0
        },
        {
            'name': 'Eskişehir',
            'x':img.width*0.275,
            'y':img.height*0.417,
            'entered': 0
        },
                {
            'name': 'Gaziantep',
            'x':img.width*0.573,
            'y':img.height*0.703,
            'entered': 0
        },
        {
            'name': 'Giresun',
            'x':img.width*0.632,
            'y':img.height*0.302,
            'entered': 0
        },
        {
            'name': 'Gümüşhane',
            'x':img.width*0.67,
            'y':img.height*0.334,
            'entered': 0
        },
        {
            'name': 'Hakkari',
            'x':img.width*0.914,
            'y':img.height*0.625,
            'entered': 0
        },
        {
            'name': 'Hatay',
            'x':img.width*0.532,
            'y':img.height*0.795,
            'entered': 0
        },
        {
            'name': 'Isparta',
            'x':img.width*0.265,
            'y':img.height*0.599,
            'entered': 0
        },
        {
            'name': 'Mersin',
            'x':img.width*0.418,
            'y':img.height*0.752,
            'entered': 0
        },
        {
            'name': 'Istanbul',
            'x':img.width*0.165,
            'y':img.height*0.23,
            'entered': 0
        },
        {
            'name': 'Izmir',
            'x':img.width*0.086,
            'y':img.height*0.544,
            'entered': 0
        },
        {
            'name': 'Kars',
            'x':img.width*0.855,
            'y':img.height*0.314,
            'entered': 0
        },
        {
            'name': 'Kastamonu',
            'x':img.width*0.406,
            'y':img.height*0.219,
            'entered': 0
        },
        {
            'name': 'Kayseri',
            'x':img.width*0.513,
            'y':img.height*0.524,
            'entered': 0
        },
        {
            'name': 'Kırklareli',
            'x':img.width*0.114,
            'y':img.height*0.164,
            'entered': 0
        },
        {
            'name': 'Kırşehir',
            'x':img.width*0.434,
            'y':img.height*0.461,
            'entered': 0
        },
        {
            'name': 'Kocaeli',
            'x':img.width*0.224,
            'y':img.height*0.282,
            'entered': 0
        },
        {
            'name': 'Konya',
            'x':img.width*0.349,
            'y':img.height*0.599,
            'entered': 0
        },
        {
            'name': 'Kütahya',
            'x':img.width*0.203,
            'y':img.height*0.449,
            'entered': 0
        },
        {
            'name': 'Malatya',
            'x':img.width*0.606,
            'y':img.height*0.538,
            'entered': 0
        },
        {
            'name': 'Manisa',
            'x': img.width * 0.13,
            'y': img.height * 0.495,
            'entered': 0
        },
        {
            'name': 'Kahramanmaraş',
            'x':img.width*0.555,
            'y':img.height*0.593,
            'entered': 0
        },
        {
            'name': 'Mardin',
            'x':img.width*0.752,
            'y':img.height*0.665,
            'entered': 0
        },
        {
            'name': 'Muğla',
            'x':img.width*0.126,
            'y':img.height*0.657,
            'entered': 0
        },
        {
            'name': 'Muş',
            'x':img.width*0.8,
            'y':img.height*0.469,
            'entered': 0
        },
        {
            'name': 'Nevşehir',
            'x':img.width*0.459,
            'y':img.height*0.521,
            'entered': 0
        },
        {
            'name': 'Niğde',
            'x':img.width*0.462,
            'y':img.height*0.602,
            'entered': 0
        },
        {
            'name': 'Ordu',
            'x':img.width*0.59,
            'y':img.height*0.288,
            'entered': 0
        },
        {
            'name': 'Rize',
            'x':img.width*0.742,
            'y':img.height*0.27,
            'entered': 0
        },
        {
            'name': 'Sakarya',
            'x':img.width*0.256,
            'y':img.height*0.308,
            'entered': 0
        },
        {
            'name': 'Samsun',
            'x':img.width*0.518,
            'y':img.height*0.253,
            'entered': 0
        },
        {
            'name': 'Siirt',
            'x':img.width*0.822,
            'y':img.height*0.59,
            'entered': 0
        },
        {
            'name': 'Sinop',
            'x':img.width*0.477,
            'y':img.height*0.207,
            'entered': 0
        },
        {
            'name': 'Sivas',
            'x':img.width*0.58,
            'y':img.height*0.428,
            'entered': 0
        },
        {
            'name': 'Tekirdağ',
            'x':img.width*0.108,
            'y':img.height*0.253,
            'entered': 0
        },
        {
            'name': 'Tokat',
            'x':img.width*0.549,
            'y':img.height*0.34,
            'entered': 0
        },
        {
            'name': 'Trabzon',
            'x':img.width*0.696,
            'y':img.height*0.288,
            'entered': 0
        },
        {
            'name': 'Tunceli',
            'x':img.width*0.68,
            'y':img.height*0.463,
            'entered': 0
        },
        {
            'name': 'Şanlıurfa',
            'x':img.width*0.66,
            'y':img.height*0.694,
            'entered': 0
        },
          {
            'name': 'Uşak',
            'x':img.width*0.19,
            'y':img.height*0.521,
            'entered': 0
        },
        {
            'name': 'Van',
            'x':img.width*0.9,
            'y':img.height*0.512,
            'entered': 0
        },
        {
            'name': 'Yozgat',
            'x':img.width*0.48,
            'y':img.height*0.409,
            'entered': 0
        },
        {
            'name': 'Zonguldak',
            'x':img.width*0.318,
            'y':img.height*0.227,
            'entered': 0
        },
        {
            'name': 'Bayburt',
            'x':img.width*0.708,
            'y':img.height*0.354,
            'entered': 0
        },
        {
            'name': 'Karaman',
            'x':img.width*0.381,
            'y':img.height*0.694,
            'entered': 0
        },
        {
            'name': 'Kırıkkale',
            'x':img.width*0.404,
            'y':img.height*0.403,
            'entered': 0
        },
        {
            'name': 'Batman',
            'x':img.width*0.778,
            'y':img.height*0.608,
            'entered': 0
        },
        {
            'name': 'Şırnak',
            'x':img.width*0.832,
            'y':img.height*0.645,
            'entered': 0
        },
        {
            'name': 'Bartın',
            'x':img.width*0.36,
            'y':img.height*0.195,
            'entered': 0
        },
        {
            'name': 'Ardahan',
            'x':img.width*0.84,
            'y':img.height*0.239,
            'entered': 0
        },
        {
            'name': 'Iğdır',
            'x':img.width*0.901,
            'y':img.height*0.357,
            'entered': 0
        },
        {
            'name': 'Yalova',
            'x':img.width*0.185,
            'y':img.height*0.293,
            'entered': 0
        },
        {
            'name': 'Karabük',
            'x':img.width*0.355,
            'y':img.height*0.256,
            'entered': 0
        },
        {
            'name': 'Kilis',
            'x':img.width*0.568,
            'y':img.height*0.734,
            'entered': 0
        },
        {
            'name': 'Osmaniye',
            'x':img.width*0.527,
            'y':img.height*0.682,
            'entered': 0
        },
        {
            'name': 'Düzce',
            'x':img.width*0.295,
            'y':img.height*0.276,
            'entered': 0
        }
    ]

    def get(self, name):
        for item in self.data:
            if item.get('name') == name:
                return item
        return None
    
    def get_remains(self):
        count = 0
        for item in self.data:
            if item.get('entered') == 0:
                count += 1
        return count

class Game:
    username = None
    image = './unnamed.gif'
    score = 0
    screen = None
    width = img.width
    height = img.height
    data = Province()
    entry = 5
    update = None

    def setup(self):
        self.screen = turtle.Screen()
        self.screen.bgpic(picname=self.image)
        self.screen.setup(width=self.width, height=self.height, startx=None, starty=None)
        turtle.hideturtle()

    def __init__(self):
        self.setup()

    def get_name(self):
        while self.username is None or self.username == '':
            self.username = turtle.textinput('Welcome to Province Game!', 'Please, enter your name')

    def prompt(self):
        for _ in range(1, 85):
            if self.entry == 0:
                messagebox.showinfo('Game over!', str(self.username) + ' Your score is ' + str(self.score))
                exit()
            name = turtle.textinput('Province', 'Enter province name\nexit for ending game')
            if name is None:
                continue
            if name == 'exit':
                exit()
            name = name.lower().capitalize()
            self.draw_province(name)
            

    def run(self):
        self.get_name()
        self.prompt()
        turtle.mainloop()
    
    def erasable_write(self, tortoise, name, font):
        eraser = turtle.Turtle()
        eraser.hideturtle()
        eraser.up()
        eraser.setposition(tortoise.position())
        eraser.write(name, font=font)
        return eraser

    def write(self, x, y, name):
        turtle.penup()
        x1 = x - self.width / 2
        y1 = self.height / 2 - y
        turtle.setpos(x1, y1)

        turtle.write(name, move=False, font=('Calibri', 8,'bold'))
    
    def update_info(self):
        trt = turtle.Turtle()
        trt.penup()
        trt.hideturtle()
        trt.setpos(self.width / 2 - 150, (-1) * self.height / 2 + 150)
        if (self.update is not None):
            self.update.clear()
        self.update = self.erasable_write(trt, 'Remains: ' + str(self.data.get_remains()), font=('Calibri', 12,'bold'))
       

    def draw_province(self, name):
        province = self.data.get(name)
        if province is not None:
            if province['entered'] == 0:
                self.write(province['x'], province['y'], province['name'])
                province['entered'] = 1
                self.score += 5
                self.update_info()
            else:
                self.entry -= 1
                messagebox.showwarning("Alert", "You already entered this province\nEntries left %s" % self.entry)
        else:
            self.entry -= 1
            messagebox.showwarning("Oops", "Your answer is wrong!\nEntries left %s" % self.entry)


game = Game()
game.run()
