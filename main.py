import keyboard

# Dicionário para armazenar o estado das teclas
keys_state = {}

def on_press(key_event):
    key = key_event.name
    keys_state[key] = 'pressed'
    
    # Priorizar a última tecla pressionada
    for k, state in keys_state.items():
        if k != key and state == 'pressed':
            keyboard.release(k)
            keys_state[k] = 'released'

def on_release(key_event):
    key = key_event.name
    keys_state[key] = 'released'

# Registrando os eventos
keyboard.on_press(on_press)
keyboard.on_release(on_release)

# Loop principal
keyboard.wait('esc')  # O programa continua rodando até a tecla 'esc' ser pressionada
