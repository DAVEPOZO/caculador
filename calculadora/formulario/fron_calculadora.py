import tkinter as tk
from tkinter import font 
from  config import constante as cons 
import util.util_ventana as util_ventana

class formulariocalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()
        self.construir_widget_toggle()

    def construir_widget_toggle(self):
         # iniciar con el tema ocuro 
        self.dark_theme = True
        # configurar la fuente FontAwesome
        font_awesomw = font.Font(family='FontAwesome', size=12)
        # boton `para cambiar de tema 
        self.theme_button = tk.Button(self, text="Modo oscuro \uf186",width=13, font=font_awesomw, bd=0,borderwidth=0,
                                      highlightthickness=0, relief=tk.FLAT, command=self.toggle_theme, bg=cons.colores_botones_especilaes_light)
        self.theme_button.grid(row=0, column=0, columnspan=2,
                               pady=0, padx=0, sticky="nw")#añadido padx y sticky
        
    def toggle_theme(self):
         # cambiar entre temas oscuro y claro 
         if self.dark_theme:
              self.configure(bg=cons.colores_de_fondo_light)
              self.entry.config(fg=cons.colores_de_texto_light,
                                bg=cons.color_caja_de_texto_light)
              self.operation_label.config(
                  fg=cons.colores_de_texto_light, bg=cons.colores_de_fondo_light)
              self.theme_button.configure(
                  text="\f185 Modo claro", relief=tk.SUNKEN, bg=cons.colores_botones_especilaes_light)
         else:
              self.configure(bg=cons.color_de_fondo_dark)
              self.entry.config(fg=cons.color_de_texto_dark,
                                bg=cons.color_caja_de_texto_dark)
              self.operation_label.config(
                  fg=cons.color_de_texto_dark, bg=cons.color_de_fondo_dark)
              self.theme_button.configure(
                  text="Modo oscuro \uf186", relief=tk.RAISED, bg=cons.colores_botones_especilaes_light)
              
          #invertir el tema 
         self.dark_theme = not self.dark_theme

         
    def config_window(self):
        #configuracion inicial de la ventana 
        self.title('Python GUI Calculadora')
        #configuracion el color de fondo y hacer transparente la ventana 
        self.configure(bg=cons.color_de_fondo_dark)
        self.attributes('-alpha', 0.96)
        w, h = 370, 570
        util_ventana.centrar_ventana(self, w, h)

    def construir_widget(self):
          # etiqueta para mostrar la operacion solicitada
          self.operation_label = tk.Label(self,text="", font=(
              'Arial', 16), fg=cons.color_de_texto_dark, bg=cons.color_de_fondo_dark, justify='right')
          self.operation_label.grid(
            row=0, column=3, padx=10, pady=10) # añadido columnspan
          
          # pantalla de operacion 
          self.entry = tk.Entry(self, width=12, font=(
              'Arial', 40), bd=0, fg=cons.color_de_texto_dark, bg=cons.color_de_fondo_dark, justify='right')
          self.entry.grid(row=1, column=0, columnspan=4,
                          padx=10, pady=10) # añadido padding
          
          #lista de botones 
          buttons = [
               'C', '%', '<', '/',
               '7', '8', '9', '*',
               '4', '5', '6', '-',
               '1', '2', '3', '+',
               '0', '.', '=',
            ]

          row_val = 2 # ajustara para dejar espacio para la etiqueta de la opetacion 
          col_val = 0 

          # configurara la tipografia "Roboto" para botones 
          roboto_font = font.Font(family="Roboto", size=16)

          for button  in buttons:
            
               # establecer el color de fondo  de los botones especiales
               if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                    color_fondo = cons.color_botones_especiales_dark
                    # ajustar el tamaño de la fuente solo para estos botones 
                    button_font = font.Font(size=16, weight='bold')
               else:
                    color_fondo = cons.color_botones_dark
                    button_font = roboto_font 

               tk.Button(self, text=button, width=5, height=2,command=lambda b=button: self.on_button_click(b),
                           bg=color_fondo, fg=cons.color_de_texto_dark, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                           overrelief='flat').grid(row=row_val, column=col_val, pady=5) # añadido padding
               col_val += 1

             

               if col_val > 3:
                  col_val = 0
                  row_val += 1   
  
    def on_button_click(self, value):
         if value == '=':           
             try:
                  expression = self.entry.get().replace('%', '/100')
                  result =  eval(expression)
                  self.entry.delete(0, tk.END)
                  self.entry.insert(tk.END, str(result))
                  operation = expression +  " " + value
                  self.operation_label.config(text=operation)
                  
             except Exception as  e :
                  self.entry.delete(0, tk.END)
                  self.entry.insert(tk.END, "Error")
                  self.operation_label.config(text="")
         elif value == 'c':
              self.entry.delete(0, tk.END)
              self.operation_label.config(text="")
         elif value == '<':
              current_text = self.entry.get()
              if current_text:
                   new_text = current_text[:-1] # eliminar el ultimo caracter 
                   self.entry.delete(0, tk.END)
                   self.entry.insert(tk.END, new_text)
                   # actualizar la etiqueta de la operacion 
                   self.operation_label.config(text=new_text + " ")
         else:
              current_text = self.entry.get()
              self.entry.delete(0, tk.END)
              self.entry.insert(tk.END, current_text + value)
              if value == '=':
                   self.operation_label.config(text="")


   


                  