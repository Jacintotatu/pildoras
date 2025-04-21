def validacionUsuario(usuario):
    if len(usuario) < 5:
        return "El usuario no puede tener menos de 5 caracteres."
    elif len(usuario) > 15:
        return "El usuario no puede tener mas de 15 caracteres."
    elif not usuario.isalnum():
        return "El usuario solo puede contener letras y numeros."
    else:
        return True

def validacionContraseña(contraseña):
    if len(contraseña) <= 10:
        return "La contraseña debe tener mas de 10 caracteres."
    
    elif  not any(not letra.isalnum() for letra in contraseña):
        return "La contraseña debe contener un caracter que no sea ni letras y numeros."

    elif not any(letra.isupper() for letra in contraseña) or not any(letra.islower() for letra in contraseña):
        return "La contraseña no es segura."
    
    elif any(letra.isspace() for letra in contraseña):
        return "La contraseña no puede contener espacios en blanco."
    
    else:
        return True
    

    
    