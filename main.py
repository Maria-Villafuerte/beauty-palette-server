#!/usr/bin/env python3
"""
Beauty Palette MCP Server
Servidor para generación de paletas de colores y sistema de belleza
URL: https://beauty-pallet-server.railway.app
"""

import json
import os
import colorsys
import random
from typing import Dict, List, Any, Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

# Configuración del servidor
app = FastAPI(
    title="Beauty Palette MCP Server",
    description="Servidor MCP especializado en paletas de colores y sistema de belleza",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir conexiones desde cualquier cliente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BeautyPaletteMCPServer:
    def __init__(self):
        """Inicializar servidor MCP de paletas de belleza"""
        self.server_name = "Beauty Palette MCP Server"
        self.version = "2.0.0"
        self.color_database = self._load_color_database()
        self.quotes_database = self._load_beauty_quotes()
        self.harmony_rules = self._load_harmony_rules()
        
    def _load_color_database(self) -> Dict[str, Any]:
        """Base de datos completa de colores para belleza"""
        return {
            "skin_tones": {
                "clara": {
                    "base_colors": ["#F5E6D3", "#E8D4C2", "#F2E7D5", "#FDF2E9"],
                    "best_colors": ["#FFB6C1", "#87CEEB", "#DDA0DD", "#F0E68C", "#98FB98"],
                    "avoid_colors": ["#000000", "#8B0000", "#2F4F4F", "#4B0082"],
                    "recommendations": [
                        "Los pasteles y tonos suaves realzan tu piel clara",
                        "Evita colores muy oscuros o intensos",
                        "Los colores fríos como azules y rosas te favorecen"
                    ]
                },
                "media": {
                    "base_colors": ["#D4B896", "#C1A882", "#B8956A", "#DEB887"],
                    "best_colors": ["#FF6347", "#32CD32", "#4169E1", "#DAA520", "#FF69B4"],
                    "avoid_colors": ["#FFFF00", "#00FF00", "#FF00FF", "#00FFFF"],
                    "recommendations": [
                        "Tienes la versatilidad de usar muchos colores",
                        "Los tonos tierra y cálidos te sientan especialmente bien",
                        "Puedes experimentar con colores vibrantes"
                    ]
                },
                "oscura": {
                    "base_colors": ["#8B5A3C", "#6B4423", "#4A2C17", "#5D4037"],
                    "best_colors": ["#FF4500", "#9400D3", "#FFD700", "#DC143C", "#00CED1"],
                    "avoid_colors": ["#FFFFE0", "#F0F8FF", "#FFFAF0", "#F5F5DC"],
                    "recommendations": [
                        "Los colores ricos y vibrantes realzan tu belleza",
                        "Evita colores muy pálidos que pueden lavarte",
                        "Los metálicos como oro y cobre son perfectos"
                    ]
                }
            },
            "undertones": {
                "frio": {
                    "colors": ["#4169E1", "#9370DB", "#C71585", "#00CED1", "#4682B4"],
                    "metals": ["plata", "platino", "oro_blanco", "acero"],
                    "description": "Venas azules, mejor en tonos fríos y metales plateados"
                },
                "calido": {
                    "colors": ["#FF6347", "#DAA520", "#D2691E", "#CD853F", "#B22222"],
                    "metals": ["oro", "cobre", "bronce", "oro_rosa"],
                    "description": "Venas verdes, mejor en tonos cálidos y metales dorados"
                },
                "neutro": {
                    "colors": ["#708090", "#BC8F8F", "#F0E68C", "#DEB887", "#D2B48C"],
                    "metals": ["oro_rosa", "acero_inoxidable", "oro_amarillo", "plata_oxidada"],
                    "description": "Puedes usar tanto metales dorados como plateados"
                }
            },
            "event_palettes": {
                "trabajo": {
                    "primary": ["#1E40AF", "#374151", "#6B7280", "#1F2937"],
                    "secondary": ["#F8FAFC", "#F1F5F9", "#E2E8F0", "#CBD5E1"],
                    "accent": ["#3B82F6", "#6366F1", "#8B5CF6"],
                    "description": "Colores profesionales que inspiran confianza"
                },
                "casual": {
                    "primary": ["#3B82F6", "#10B981", "#F59E0B", "#EF4444"],
                    "secondary": ["#DBEAFE", "#D1FAE5", "#FEF3C7", "#FEE2E2"],
                    "accent": ["#1D4ED8", "#059669", "#D97706", "#DC2626"],
                    "description": "Colores relajados y versátiles para el día a día"
                },
                "fiesta": {
                    "primary": ["#EC4899", "#8B5CF6", "#06B6D4", "#F59E0B"],
                    "secondary": ["#F9A8D4", "#C4B5FD", "#67E8F9", "#FCD34D"],
                    "accent": ["#FFD700", "#C0C0C0", "#B87333"],
                    "metallic": ["#FFD700", "#C0C0C0", "#CD7F32", "#E6E6FA"],
                    "description": "Colores vibrantes y llamativos para destacar"
                },
                "formal": {
                    "primary": ["#1F2937", "#374151", "#6B7280", "#111827"],
                    "secondary": ["#9CA3AF", "#D1D5DB", "#F3F4F6", "#F9FAFB"],
                    "accent": ["#1E40AF", "#7C2D12", "#064E3B", "#92400E"],
                    "description": "Elegancia clásica para eventos importantes"
                },
                "cita": {
                    "primary": ["#EC4899", "#F59E0B", "#8B5CF6", "#EF4444"],
                    "secondary": ["#F9A8D4", "#FCD34D", "#C4B5FD", "#FCA5A5"],
                    "accent": ["#BE185D", "#D97706", "#6D28D9", "#B91C1C"],
                    "description": "Colores románticos y favorecedores"
                }
            },
            "seasonal_adjustments": {
                "primavera": {
                    "colors": ["#98FB98", "#FFB6C1", "#F0E68C", "#DDA0DD"],
                    "mood": "Fresco y renovador"
                },
                "verano": {
                    "colors": ["#87CEEB", "#F0E68C", "#98FB98", "#FFB6C1"],
                    "mood": "Brillante y luminoso"
                },
                "otono": {
                    "colors": ["#D2691E", "#CD853F", "#DAA520", "#B22222"],
                    "mood": "Cálido y acogedor"
                },
                "invierno": {
                    "colors": ["#4169E1", "#9370DB", "#C71585", "#2F4F4F"],
                    "mood": "Profundo e intenso"
                }
            }
        }
    
    def _load_beauty_quotes(self) -> List[Dict[str, str]]:
        """Base de datos de citas inspiracionales de belleza"""
        return [
            {
                "quote": "La belleza comienza en el momento en que decides ser tú misma",
                "author": "Coco Chanel",
                "category": "confianza"
            },
            {
                "quote": "El estilo es una manera de decir quién eres sin tener que hablar",
                "author": "Rachel Zoe",
                "category": "estilo"
            },
            {
                "quote": "La elegancia es la única belleza que nunca se desvanece",
                "author": "Audrey Hepburn",
                "category": "elegancia"
            },
            {
                "quote": "La confianza es el mejor accesorio que puedes usar",
                "author": "Anónimo",
                "category": "confianza"
            },
            {
                "quote": "La moda se desvanece, pero el estilo es eterno",
                "author": "Yves Saint Laurent",
                "category": "estilo"
            },
            {
                "quote": "Invierte en tu piel, es donde vas a vivir para siempre",
                "author": "Warren Buffett",
                "category": "cuidado"
            },
            {
                "quote": "La belleza real está en ser auténtica contigo misma",
                "author": "Lupita Nyong'o",
                "category": "autenticidad"
            },
            {
                "quote": "El maquillaje no es una máscara que cubre tu belleza; es un arte que celebra tu unicidad",
                "author": "Kevyn Aucoin",
                "category": "maquillaje"
            }
        ]
    
    def _load_harmony_rules(self) -> Dict[str, Any]:
        """Reglas de armonía de colores"""
        return {
            "complementary": {"angle": 180, "description": "Colores opuestos que crean contraste vibrante"},
            "analogous": {"angle": 30, "description": "Colores adyacentes que crean armonía suave"},
            "triadic": {"angle": 120, "description": "Tres colores espaciados uniformemente"},
            "split_complementary": {"angles": [150, 210], "description": "Una variación más suave de los complementarios"},
            "tetradic": {"angles": [60, 180, 240], "description": "Cuatro colores en esquema rectangular"}
        }
    
    def generate_advanced_palette(self, profile: Dict[str, str], palette_type: str, 
                                 event_type: str, preferences: Dict = None) -> Dict[str, Any]:
        """Generar paleta avanzada personalizada"""
        try:
            # Validar parámetros
            if palette_type not in ["ropa", "maquillaje", "accesorios"]:
                raise ValueError("Tipo de paleta debe ser: ropa, maquillaje, o accesorios")
            
            if event_type not in self.color_database["event_palettes"]:
                event_type = "casual"  # Valor por defecto
            
            # Obtener colores base según perfil
            skin_tone = profile.get('skin_tone', 'media')
            undertone = profile.get('undertone', 'neutro')
            eye_color = profile.get('eye_color', 'cafe')
            
            # Generar paleta específica
            if palette_type == "ropa":
                colors = self._generate_clothing_palette(skin_tone, undertone, event_type, preferences)
            elif palette_type == "maquillaje":
                colors = self._generate_makeup_palette(skin_tone, undertone, eye_color, event_type, preferences)
            else:  # accesorios
                colors = self._generate_accessories_palette(skin_tone, undertone, event_type, preferences)
            
            # Generar recomendaciones
            recommendations = self._generate_advanced_recommendations(profile, palette_type, event_type, colors)
            
            return {
                "palette_id": f"beauty_{palette_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "user_profile": profile.get('user_id', 'anonymous'),
                "palette_type": palette_type,
                "event_type": event_type,
                "season": preferences.get('season', 'verano') if preferences else 'verano',
                "colors": colors,
                "recommendations": recommendations,
                "harmony_analysis": self.analyze_color_harmony([c["hex"] for c in colors]),
                "created_at": datetime.now().isoformat(),
                "server_info": {
                    "name": self.server_name,
                    "version": self.version,
                    "url": "https://beauty-pallet-server.railway.app"
                }
            }
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generando paleta: {str(e)}")
    
    def _generate_clothing_palette(self, skin_tone: str, undertone: str, 
                                  event_type: str, preferences: Dict = None) -> List[Dict[str, str]]:
        """Generar paleta específica para ropa"""
        colors = []
        
        # Colores base del evento
        event_colors = self.color_database["event_palettes"][event_type]["primary"]
        
        # Colores según tono de piel
        skin_colors = self.color_database["skin_tones"].get(skin_tone, {}).get("best_colors", [])
        
        # Combinar y seleccionar
        all_colors = event_colors + skin_colors[:3]
        
        categories = ["superior", "inferior", "superior", "acento", "neutro", "complemento"]
        names = ["Blusa Principal", "Pantalón Base", "Chaqueta", "Accesorio Vibrante", "Neutro Elegante", "Complemento"]
        
        for i, color_hex in enumerate(all_colors[:6]):
            colors.append({
                "hex": color_hex,
                "name": names[i],
                "category": categories[i],
                "usage": f"Ideal para {categories[i]} en {event_type}"
            })
        
        return colors
    
    def _generate_makeup_palette(self, skin_tone: str, undertone: str, 
                                eye_color: str, event_type: str, preferences: Dict = None) -> List[Dict[str, str]]:
        """Generar paleta específica para maquillaje"""
        colors = []
        
        # Colores para ojos según su color
        eye_colors = {
            "azul": ["#D2691E", "#CD853F", "#B8860B"],
            "verde": ["#8B0000", "#9370DB", "#B22222"],
            "cafe": ["#4682B4", "#8B4513", "#DAA520"],
            "gris": ["#4B0082", "#FF6347", "#20B2AA"],
            "negro": ["#B8860B", "#8B4513", "#CD853F"]
        }
        
        eye_palette = eye_colors.get(eye_color, eye_colors["cafe"])
        
        # Colores para labios según tono de piel
        lip_colors = {
            "clara": ["#FF69B4", "#DC143C", "#CD5C5C"],
            "media": ["#B22222", "#FF4500", "#D2691E"],
            "oscura": ["#8B0000", "#FF6347", "#DC143C"]
        }
        
        lip_palette = lip_colors.get(skin_tone, lip_colors["media"])
        
        # Construir paleta completa
        makeup_items = [
            {"colors": eye_palette, "names": ["Sombra Principal", "Sombra Complemento", "Delineador"], "category": "ojos"},
            {"colors": lip_palette, "names": ["Labial Principal", "Labial Día", "Labial Noche"], "category": "labios"},
            {"colors": ["#F08080", "#E9967A"], "names": ["Rubor Natural", "Bronceador"], "category": "mejillas"}
        ]
        
        for item_group in makeup_items:
            for i, color_hex in enumerate(item_group["colors"]):
                if i < len(item_group["names"]):
                    colors.append({
                        "hex": color_hex,
                        "name": item_group["names"][i],
                        "category": item_group["category"],
                        "usage": f"Perfecto para {item_group['category']} en {event_type}"
                    })
        
        return colors[:8]  # Limitar a 8 colores
    
    def _generate_accessories_palette(self, skin_tone: str, undertone: str, 
                                     event_type: str, preferences: Dict = None) -> List[Dict[str, str]]:
        """Generar paleta específica para accesorios"""
        colors = []
        
        # Metales según subtono
        metal_colors = self.color_database["undertones"][undertone]["colors"][:3]
        
        # Colores complementarios
        complement_colors = self.color_database["event_palettes"][event_type]["primary"][:3]
        
        accessory_types = [
            "Joyería Principal", "Bolso Coordinado", "Calzado Elegante",
            "Metal Complementario", "Textura Especial", "Acento Final"
        ]
        
        categories = ["joyeria", "bolsos", "calzado", "metales", "textiles", "varios"]
        
        all_colors = metal_colors + complement_colors
        
        for i, color_hex in enumerate(all_colors[:6]):
            colors.append({
                "hex": color_hex,
                "name": accessory_types[i],
                "category": categories[i],
                "usage": f"Ideal para {categories[i]} en eventos {event_type}"
            })
        
        return colors
    
    def _generate_advanced_recommendations(self, profile: Dict[str, str], 
                                          palette_type: str, event_type: str, 
                                          colors: List[Dict]) -> Dict[str, Any]:
        """Generar recomendaciones avanzadas"""
        skin_tone = profile.get('skin_tone', 'media')
        
        recommendations = {
            "styling_tips": [],
            "color_combinations": [],
            "seasonal_notes": [],
            "personalized_advice": []
        }
        
        # Tips específicos del evento
        event_tips = {
            "trabajo": [
                "Mantén un look profesional con colores neutros como base",
                "Agrega un toque de color en accesorios para personalidad",
                "Evita colores demasiado vibrantes para el ambiente laboral"
            ],
            "fiesta": [
                "¡Es momento de brillar! Usa colores intensos y metálicos",
                "Combina texturas diferentes para crear interés visual",
                "Los acentos dorados o plateados añaden glamour"
            ],
            "casual": [
                "Juega con colores y experimenta combinaciones divertidas",
                "Los denim y neutros son perfectos como base",
                "Añade color con accesorios según tu estado de ánimo"
            ]
        }
        
        recommendations["styling_tips"] = event_tips.get(event_type, [])
        
        # Consejos según tono de piel
        skin_advice = self.color_database["skin_tones"].get(skin_tone, {}).get("recommendations", [])
        recommendations["personalized_advice"] = skin_advice
        
        # Combinaciones de colores
        if len(colors) >= 3:
            recommendations["color_combinations"] = [
                f"Combina {colors[0]['name']} con {colors[1]['name']} para un look equilibrado",
                f"{colors[2]['name']} funciona perfecto como acento",
                f"Para mayor impacto, usa {colors[0]['name']} como color dominante"
            ]
        
        return recommendations
    
    def analyze_color_harmony(self, colors: List[str]) -> Dict[str, Any]:
        """Análizar armonía avanzada de colores"""
        if len(colors) < 2:
            return {"harmony_score": 0, "analysis": "Se necesitan al menos 2 colores para análisis"}
        
        try:
            # Convertir a HSL para análisis
            hsl_colors = []
            for color_hex in colors:
                hex_clean = color_hex.lstrip('#')
                if len(hex_clean) == 6:
                    rgb = tuple(int(hex_clean[i:i+2], 16) / 255.0 for i in (0, 2, 4))
                    hsl = colorsys.rgb_to_hls(*rgb)
                    hsl_colors.append(hsl)
            
            if len(hsl_colors) < 2:
                return {"harmony_score": 0, "analysis": "Colores no válidos para análisis"}
            
            # Calcular diferencias de matiz
            hue_differences = []
            for i in range(len(hsl_colors) - 1):
                h1, h2 = hsl_colors[i][0], hsl_colors[i + 1][0]
                diff = abs(h1 - h2) * 360
                hue_differences.append(diff)
            
            avg_diff = sum(hue_differences) / len(hue_differences)
            
            # Analizar saturación y luminosidad
            saturations = [hsl[1] for hsl in hsl_colors]
            lightnesses = [hsl[2] for hsl in hsl_colors]
            
            sat_variance = max(saturations) - min(saturations)
            light_variance = max(lightnesses) - min(lightnesses)
            
            # Determinar tipo y puntuación
            harmony_analysis = self._determine_harmony_type(avg_diff, sat_variance, light_variance)
            
            return harmony_analysis
            
        except Exception as e:
            return {"harmony_score": 50, "analysis": f"Error en análisis: {str(e)}"}
    
    def _determine_harmony_type(self, avg_diff: float, sat_var: float, light_var: float) -> Dict[str, Any]:
        """Determinar tipo de armonía y puntuación"""
        if avg_diff < 60:
            harmony_type = "Análoga"
            base_score = 85
            description = "Colores vecinos que crean tranquilidad y cohesión"
        elif 150 < avg_diff < 210:
            harmony_type = "Complementaria"
            base_score = 90
            description = "Colores opuestos que crean contraste dinámico y energía"
        elif 90 < avg_diff < 150:
            harmony_type = "Triádica"
            base_score = 80
            description = "Tres colores balanceados que ofrecen vitalidad con armonía"
        else:
            harmony_type = "Compleja"
            base_score = 70
            description = "Paleta diversa que requiere habilidad para equilibrar"
        
        # Ajustar score según variación
        if sat_var < 0.3 and light_var < 0.3:
            score_adj = 10  # Bonus por consistencia
        elif sat_var > 0.7 or light_var > 0.7:
            score_adj = -15  # Penalización por inconsistencia
        else:
            score_adj = 0
        
        final_score = min(100, max(0, base_score + score_adj))
        
        return {
            "harmony_score": final_score,
            "harmony_type": harmony_type,
            "analysis": description,
            "technical_details": {
                "average_hue_difference": round(avg_diff, 2),
                "saturation_variance": round(sat_var, 3),
                "lightness_variance": round(light_var, 3)
            },
            "recommendations": self._get_harmony_recommendations(harmony_type, final_score)
        }
    
    def _get_harmony_recommendations(self, harmony_type: str, score: int) -> List[str]:
        """Recomendaciones basadas en armonía"""
        base_recs = {
            "Análoga": [
                "Perfecta para looks relajados y sofisticados",
                "Ideal para uso diario y ambientes profesionales",
                "Combina bien con texturas naturales"
            ],
            "Complementaria": [
                "Excelente para ocasiones donde quieres destacar",
                "Usa un color como dominante y el otro como acento",
                "Perfecto para crear puntos focales en tu look"
            ],
            "Triádica": [
                "Balanceo perfecto entre armonía y contraste",
                "Versátil para múltiples ocasiones",
                "Permite creatividad manteniendo cohesión"
            ],
            "Compleja": [
                "Requiere más cuidado en la aplicación",
                "Considera usar neutrales para equilibrar",
                "Experimenta con diferentes proporciones"
            ]
        }
        
        recs = base_recs.get(harmony_type, [])
        
        if score >= 85:
            recs.append("¡Excelente combinación! Úsala con confianza")
        elif score >= 70:
            recs.append("Buena armonía, funciona bien en la mayoría de situaciones")
        else:
            recs.append("Considera ajustar proporciones o añadir un neutro")
        
        return recs
    
    def get_inspirational_quote(self, category: str = None) -> Dict[str, str]:
        """Obtener cita inspiracional filtrada"""
        quotes = self.quotes_database
        
        if category:
            filtered_quotes = [q for q in quotes if q.get('category', '').lower() == category.lower()]
            quotes = filtered_quotes if filtered_quotes else quotes
        
        if not quotes:
            return {
                "quote": "La belleza está en los ojos del que mira",
                "author": "Platón",
                "category": "filosofia"
            }
        
        selected_quote = random.choice(quotes)
        selected_quote["timestamp"] = datetime.now().isoformat()
        
        return selected_quote

# Instancia global del servidor
beauty_server = BeautyPaletteMCPServer()

# === ENDPOINTS DE LA API ===

@app.get("/", response_class=HTMLResponse)
async def root():
    """Página de inicio con información del servidor"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Beauty Palette MCP Server</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; }}
            .endpoint {{ background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .method {{ font-weight: bold; color: #28a745; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🎨 Beauty Palette MCP Server</h1>
            <p>Servidor especializado en paletas de colores y sistema de belleza</p>
            <p><strong>Versión:</strong> {beauty_server.version}</p>
            <p><strong>Estado:</strong> ✅ Activo</p>
        </div>
        
        <h2>📋 Endpoints Disponibles</h2>
        
        <div class="endpoint">
            <div class="method">GET /health</div>
            <p>Verificar estado del servidor</p>
        </div>
        
        <div class="endpoint">
            <div class="method">POST /api/generate-palette</div>
            <p>Generar paleta de colores personalizada</p>
        </div>
        
        <div class="endpoint">
            <div class="method">GET /api/quote</div>
            <p>Obtener cita inspiracional de belleza</p>
        </div>
        
        <div class="endpoint">
            <div class="method">POST /api/analyze-harmony</div>
            <p>Analizar armonía entre colores</p>
        </div>
        
        <div class="endpoint">
            <div class="method">GET /api/recommendations/{{skin_tone}}/{{undertone}}</div>
            <p>Obtener recomendaciones personalizadas</p>
        </div>
        
        <h2>📚 Documentación</h2>
        <p><a href="/docs">📖 Swagger UI</a> | <a href="/redoc">📘 ReDoc</a></p>
        
        <h2>🔗 Conexión</h2>
        <p>URL del servidor: <strong>https://beauty-pallet-server.railway.app</strong></p>
        <p>Para conectar tu cliente, usa esta URL en la configuración.</p>
    </body>
    </html>
    """
    return html_content

@app.get("/health")
async def health_check():
    """Endpoint de salud del servidor"""
    return {
        "status": "healthy",
        "server_name": beauty_server.server_name,
        "version": beauty_server.version,
        "timestamp": datetime.now().isoformat(),
        "endpoints": 5,
        "uptime": "Running"
    }

@app.post("/api/generate-palette")
async def generate_palette_endpoint(request: Dict[str, Any]):
    """Generar paleta de colores personalizada"""
    try:
        profile = request.get("profile", {})
        palette_type = request.get("palette_type", "ropa")
        event_type = request.get("event_type", "casual")
        preferences = request.get("preferences", {})
        
        if not profile:
            raise HTTPException(status_code=400, detail="Perfil de usuario requerido")
        
        palette = beauty_server.generate_advanced_palette(profile, palette_type, event_type, preferences)
        
        return {
            "success": True,
            "data": palette,
            "message": f"Paleta de {palette_type} generada exitosamente para {event_type}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/quote")
async def get_quote_endpoint(category: str = None):
    """Obtener cita inspiracional"""
    try:
        quote = beauty_server.get_inspirational_quote(category)
        return {
            "success": True,
            "data": quote,
            "server_info": beauty_server.server_name
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze-harmony")
async def analyze_harmony_endpoint(request: Dict[str, Any]):
    """Analizar armonía de colores"""
    try:
        colors = request.get("colors", [])
        
        if not colors or len(colors) < 2:
            raise HTTPException(status_code=400, detail="Se requieren al menos 2 colores")
        
        analysis = beauty_server.analyze_color_harmony(colors)
        
        return {
            "success": True,
            "data": analysis,
            "colors_analyzed": len(colors)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/recommendations/{skin_tone}/{undertone}")
async def get_recommendations_endpoint(skin_tone: str, undertone: str):
    """Obtener recomendaciones por características físicas"""
    try:
        recommendations = {}
        
        # Validar parámetros
        valid_skin_tones = ["clara", "media", "oscura"]
        valid_undertones = ["frio", "calido", "neutro"]
        
        if skin_tone not in valid_skin_tones:
            raise HTTPException(status_code=400, detail=f"Tono de piel debe ser: {', '.join(valid_skin_tones)}")
        
        if undertone not in valid_undertones:
            raise HTTPException(status_code=400, detail=f"Subtono debe ser: {', '.join(valid_undertones)}")
        
        # Obtener recomendaciones
        if skin_tone in beauty_server.color_database['skin_tones']:
            skin_data = beauty_server.color_database['skin_tones'][skin_tone]
            recommendations.update({
                "best_colors": skin_data['best_colors'],
                "avoid_colors": skin_data['avoid_colors'],
                "skin_recommendations": skin_data['recommendations']
            })
        
        if undertone in beauty_server.color_database['undertones']:
            undertone_data = beauty_server.color_database['undertones'][undertone]
            recommendations.update({
                "undertone_colors": undertone_data['colors'],
                "best_metals": undertone_data['metals'],
                "undertone_description": undertone_data['description']
            })
        
        return {
            "success": True,
            "data": recommendations,
            "profile": {"skin_tone": skin_tone, "undertone": undertone}
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/mcp")
async def mcp_endpoint(request: Dict[str, Any]):
    """Endpoint MCP estándar para compatibilidad con protocolo"""
    try:
        method = request.get("method")
        params = request.get("params", {})
        
        if method == "generate_palette":
            result = beauty_server.generate_advanced_palette(
                params.get("profile", {}),
                params.get("palette_type", "ropa"),
                params.get("event_type", "casual"),
                params.get("preferences", {})
            )
        elif method == "get_quote":
            result = beauty_server.get_inspirational_quote(params.get("category"))
        elif method == "analyze_harmony":
            result = beauty_server.analyze_color_harmony(params.get("colors", []))
        else:
            raise HTTPException(status_code=400, detail=f"Método MCP no soportado: {method}")
        
        return {
            "success": True,
            "result": result,
            "method": method,
            "server": beauty_server.server_name
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Configuración del servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    print("🚀 Iniciando Beauty Palette MCP Server...")
    print(f"📍 Servidor disponible en puerto: {port}")
    print("🌐 URL pública: https://beauty-pallet-server.railway.app")
    print("📚 Documentación: https://beauty-pallet-server.railway.app/docs")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )