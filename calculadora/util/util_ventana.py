def centrar_ventana(ventana,aplicaciona_ancho,aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int ((pantall_ancho/2) - (aplicaciona_ancho/2))
    y = int ((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicaciona_ancho}x{aplicacion_largo}+{x}+{y}")