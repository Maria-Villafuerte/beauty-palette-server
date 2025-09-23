# 🎨 Beauty Palette MCP Server

Servidor MCP especializado en generación de paletas de colores y sistema de belleza.

## 🚀 URL del Servidor

**Producción**: https://beauty-pallet-server.railway.app

## ✨ Funcionalidades

### 🎨 Generación de Paletas
- **Paletas de Ropa**: Combinaciones para diferentes eventos
- **Paletas de Maquillaje**: Colores según características físicas
- **Paletas de Accesorios**: Coordinación de joyería y complementos

### 🔬 Análisis Avanzado
- **Análisis de Armonía**: Evaluación científica de combinaciones de colores
- **Recomendaciones Personalizadas**: Basadas en tono de piel y subtono
- **Teoría del Color**: Algoritmos avanzados de colorimetría

### 💬 Contenido Inspiracional
- **Citas de Belleza**: Base de datos curada de frases inspiracionales
- **Consejos de Estilo**: Recomendaciones contextuales

## 📡 Endpoints

### Estado del Servidor
```
GET /health
```
Verificar si el servidor está funcionando.

### Generar Paleta
```
POST /api/generate-palette
Content-Type: application/json

{
  "profile": {
    "user_id": "maria_123",
    "skin_tone": "media",
    "undertone": "calido",
    "eye_color": "cafe",
    "hair_color": "castano",
    "style_preference": "moderno"
  },
  "palette_type": "ropa",
  "event_type": "trabajo",
  "preferences": {
    "season": "verano"
  }
}
```

### Obtener Cita Inspiracional
```
GET /api/quote?category=confianza
```

### Analizar Armonía de Colores
```
POST /api/analyze-harmony
Content-Type: application/json

{
  "colors": ["#FF6347", "#4169E1", "#32CD32"]
}
```

### Recomendaciones Personalizadas
```
GET /api/recommendations/media/calido
```

## 🔧 Uso con Clientes MCP

### Configuración del Cliente
```python
# En tu cliente MCP
server_url = "https://beauty-pallet-server.railway.app"

# Ejemplo de conexión
async def connect_to_beauty_server():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{server_url}/health")
        return response.json()
```

### Ejemplo de Generación de Paleta
```python
import httpx

async def generate_palette():
    payload = {
        "profile": {
            "user_id": "usuario_123",
            "skin_tone": "media",
            "undertone": "calido",
            "eye_color": "cafe"
        },
        "palette_type": "ropa",
        "event_type": "fiesta"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://beauty-pallet-server.railway.app/api/generate-palette",
            json=payload
        )
        return response.json()
```

## 📚 Documentación Interactiva

- **Swagger UI**: https://beauty-pallet-server.railway.app/docs
- **ReDoc**: https://beauty-pallet-server.railway.app/redoc

## 🎯 Tipos de Paleta Soportados

- `ropa`: Combinaciones de vestimenta
- `maquillaje`: Colores para maquillaje
- `accesorios`: Coordinación de complementos

## 🎭 Eventos Soportados

- `trabajo`: Ambientes profesionales
- `casual`: Uso diario relajado
- `fiesta`: Eventos sociales
- `formal`: Ocasiones elegantes
- `cita`: Encuentros románticos

## 🌈 Características Físicas

### Tonos de Piel
- `clara`: Piel pálida/clara
- `media`: Piel media/morena
- `oscura`: Piel oscura/negra

### Subtonos
- `frio`: Venas azules, mejor en plateados
- `calido`: Venas verdes, mejor en dorados
- `neutro`: Puede usar ambos metales

## 🔍 Análisis de Armonía

El servidor analiza:
- **Diferencias de matiz**: Relaciones entre colores
- **Saturación**: Intensidad de los colores
- **Luminosidad**: Brillo de los colores
- **Tipo de armonía**: Análoga, complementaria, triádica, etc.

## 💡 Ejemplo de Respuesta

```json
{
  "success": true,
  "data": {
    "palette_id": "beauty_ropa_20241215_143022",
    "palette_type": "ropa",
    "event_type": "trabajo",
    "colors": [
      {
        "hex": "#1E40AF",
        "name": "Blusa Principal",
        "category": "superior",
        "usage": "Ideal para superior en trabajo"
      }
    ],
    "recommendations": {
      "styling_tips": [
        "Mantén un look profesional con colores neutros como base"
      ]
    },
    "harmony_analysis": {
      "harmony_score": 85,
      "harmony_type": "Análoga"
    }
  }
}
```

## 🛠️ Para Desarrolladores

### Desplegar tu Propia Instancia

1. Fork este repositorio
2. Conecta con Railway/Render
3. Despliega automáticamente
4. Configura tu URL personalizada

### Contribuir

1. Agregar nuevas categorías de colores
2. Mejorar algoritmos de armonía
3. Expandir base de datos de citas
4. Optimizar recomendaciones

## 📊 Estado del Servidor

Monitorea el estado en: https://beauty-pallet-server.railway.app/health

## 🔒 Seguridad

- CORS habilitado para todas las conexiones
- Validación de parámetros
- Manejo robusto de errores
- Rate limiting disponible

## 📞 Soporte

Para soporte técnico o preguntas sobre integración, consulta la documentación interactiva en `/docs`.

---

**Beauty Palette MCP Server v2.0** - Donde la ciencia del color se encuentra con la belleza personal.