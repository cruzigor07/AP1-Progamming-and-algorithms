def interpretar(comando):
    match comando:
        case ['login', usuario]:
            return f"Autenticando {usuario}"
        case ['buscar', termo]:
            return f"Buscando {termo}"
        case ['sair']:
            return "Sessão encerrada"
        case _:
            return "Comando inválido"


print(interpretar(['buscar', 'python'])) 
print(interpretar(['sair']))            
print(interpretar(['ajuda']))           