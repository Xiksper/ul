import os
import json

def generate():
    supported = ('.jpg', '.jpeg', '.png', '.bmp')
    # Собираем все картинки из текущей папки
    files = [f for f in os.listdir('.') if f.lower().endswith(supported) and os.path.isfile(f)]
    
    # Сохраняем в manifest.json
    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(files, f, ensure_ascii=False, indent=4)
        
    print(f"Успешно! Записано {len(files)} картинок в manifest.json")

if __name__ == '__main__':
    generate()