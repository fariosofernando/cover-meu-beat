print(

)

# /import Modul stage
# Modulo responsavel por import de tudo material python3 e kivy2,kivymd dev
from config import imports

# /Update Grapic stage
# Nossa parte gráfica. 90% da representação do applicativo é feito nesse arquivo ('kivy_file')
imports.Builder.load_file('config/kivy_file.kv')
imports.version()

# /Logic stage
# Nossas funções logícas, a parte responsavél pelo comportamento do applicativo é feita neste arquivo 'main'.
class ManagerScreen(imports.ScreenManager):
    def __init__(
        self, **kw
    ):
        super(
            ManagerScreen, self
        ).__init__(**kw)
    
    def my_callback(
        self
    ):
        print('Ops! Happy precioned!')

    def animation_1(
        self, widget
    ):
        animation = imports.Animation (height = 200)
        animation(widget)

class My_Beat(imports.MDApp):
    imports.Window.size = (298, 615)
    def pri(
        self
    ):
        print(imports.Window.size)
    def build(
        self
    ):
        self.icon = ''
        
        # Nosso root
        return ManagerScreen()


if __name__ == '__main__':
    My_Beat().run()

print(
    None
)