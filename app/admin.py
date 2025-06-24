from django.contrib import admin
from django.utils.html import format_html
from .models import Trabajo, ImagenTrabajoExtra, Product, ImagenExtra, Visita


# ---------- INLINE IMAGEN EXTRA PARA PRODUCTOS ----------
class ImagenExtraInline(admin.TabularInline):
    model = ImagenExtra
    extra = 1
    verbose_name = "Imagen adicional"
    verbose_name_plural = "Imágenes adicionales"


# ---------- ADMIN PRODUCT ----------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'descuento', 'thumbnail')
    search_fields = ('title',)
    inlines = [ImagenExtraInline]

    def thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.imagen.url)
        return "Sin imagen"

    thumbnail.short_description = "Vista previa"


# ---------- INLINE IMAGEN EXTRA PARA TRABAJOS ----------
class ImagenTrabajoExtraInline(admin.TabularInline):
    model = ImagenTrabajoExtra
    extra = 1
    verbose_name = "Imagen adicional"
    verbose_name_plural = "Imágenes adicionales"


# ---------- ADMIN TRABAJO ----------
@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'creado', 'thumbnail')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('creado',)
    inlines = [ImagenTrabajoExtraInline]

    def thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.imagen.url)
        return "Sin imagen"

    thumbnail.short_description = "Vista previa"


# ---------- ADMIN VISITAS ----------
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'url', 'ip')
    list_filter = ('fecha',)
