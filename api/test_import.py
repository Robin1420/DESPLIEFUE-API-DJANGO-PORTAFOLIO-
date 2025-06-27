import os
import sys
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiportafolio.settings')
django.setup()

try:
    from portafolio import models
    print("¡Importación exitosa! El módulo 'models' se importó correctamente.")
    print(f"Modelos disponibles: {[m for m in dir(models) if not m.startswith('_')]}")
    
    # Verificar algunos modelos
    print("\nAlgunos modelos encontrados:")
    for model_name in ['Certificados', 'DatosPersonales', 'Experiencias', 'Proyectos']:
        if hasattr(models, model_name):
            print(f"- {model_name} encontrado")
        else:
            print(f"- {model_name} NO encontrado")
            
except Exception as e:
    import traceback
    print(f"Error al importar el módulo 'models': {e}")
    print("\nDetalles del error:")
    traceback.print_exc()
