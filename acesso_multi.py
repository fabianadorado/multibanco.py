from multibanco import multibanco

if __name__ == "__main__": 
    app = multibanco()
    if app.logar():
        app.menu() 
        
    else:
        print("Encerrando Sistema.")
    