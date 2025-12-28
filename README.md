Enfoque Refinado del Proyecto

Título del Proyecto : Mabel (Modular Automation Builder Enhanced with Learning)

Género : Ingeniería de Software / Automatización / IA aplicada al desarrollo

Lenguaje implementado: Python

Lenguaje Resultante : PHP 8.2+

Tema Central: Diseñar y desarrollar un sistema de agentes de inteligencia artificial capaz de analizar requerimientos, diseñar y generar recursos para sistemas de automatización de procesos, basándose en contratos declarativos (YAML).

Público Objetivo : 	
Desarrolladores backend PHP
Arquitectos de software
Equipos que necesitan acelerar el desarrollo de módulos repetitivos
Personas interesadas en automatizar procesos mediante APIs modulares

Propósito del Sistema : Proveer una plataforma asistida por IA que permita crear, mantener y escalar módulos de software de forma consistente, segura y estructurada, reduciendo drásticamente el tiempo de desarrollo sin sacrificar calidad ni estándares.

Objetivo General : Desarrollar una interfaz conversacional y declarativa que permita a un usuario definir requerimientos funcionales y técnicos, y que un sistema de agentes IA especializados genere automáticamente uno o varios módulos backend listos para integrarse en un sistema existente.

Objetivos Específicos : 

Implementar un sistema de agentes basado en Microsoft Agent Framework.
Generar código PHP compatible con Zend/Laminas Framework.
Utilizar Eloquent ORM exclusivamente en la capa de infraestructura.
Respetar:
PSR-12
Arquitectura limpia (Clean Architecture / Hexagonal)
Separación estricta de responsabilidades
Permitir configuración total del módulo mediante archivos YAML.
Facilitar la integración del código generado en proyectos existentes.
Preparar el sistema para futuras extensiones (tests, eventos, colas, microservicios).


Arquitectura de Agentes IA

Agente Analista de Requerimientos
Responsabilidad:
Interpretar lenguaje natural
Convertirlo en una estructura YAML válida
Validar ambigüedades
Solicitar información faltante

Agente Diseñador de Módulos
Responsabilidad:
Analizar el YAML
Definir:
Capas necesarias
Dependencias
Estructura del módulo
Validar consistencia arquitectónica

Agente Generador de Código
Responsabilidad:
Generar código PHP por capas:
Domain
Application
Infrastructure
Implementar:
Entities
Repositories
Mappers
UseCases
Services
Aplicar estándares de calidad

Agente Validador y Refactor
Responsabilidad:
Revisar el código generado
Detectar:
Errores lógicos
Violaciones de arquitectura
Inconsistencias de naming
Proponer o aplicar mejoras


Arquitectura del Código Generado

Module/
 ├── Domain/
 │   ├── Entity/
 │   ├── Repository/
 │   └── ValueObject/
 ├── Application/
 │   ├── UseCase/
 │   ├── Service/
 │   └── DTO/
 ├── Infrastructure/
 │   ├── Persistence/
 │   │   ├── Eloquent/
 │   │   └── Mapper/
 │   ├── Controller/
 │   └── Config/
 └── Tests/




Configuración Declarativa (YAML)

El archivo YAML actúa como contrato, no como sugerencia.

Ejemplo Base

module:
  name: User
  namespace: App\Module\User
  framework: zend

database:
  driver: mysql
  orm: eloquent
  table: users

entities:
  User:
    id: int
    name: string
    email: string
    created_at: datetime

use_cases:
  - CreateUser
  - UpdateUser
  - DeleteUser
  - GetUser

services:
  - UserService

Interfaz de Usuario

Chat IA (Opcional pero estratégico)
Entrada de requerimientos
Validación interactiva
Visualización del YAML
Confirmación antes de generar código
⚠️ El chat no controla la lógica, solo la orquesta.

Integración con Zend / Laminas
Controladores HTTP generados opcionalmente
Configuración de rutas
Inyección de dependencias
Adaptación al ServiceManager de Zend

Principios Clave del Proyecto
Declarativo sobre imperativo
Contrato antes que código
Dominio independiente del framework
IA como asistente, no como improvisador
Código generado ≠ código intocable

Escalabilidad Futura
Generación automática de:
Tests unitarios
OpenAPI / Swagger
Eventos de dominio
Soporte para:
Otros ORMs
Otros frameworks
CLI y pipelines CI/CD

Conclusión

Mabel deja de ser “una IA que genera código” y se convierte en un motor de construcción de módulos gobernado por contratos, con agentes especializados y arquitectura limpia.

Próximo paso (MVP)

El MVP técnico está documentado en `MVP.md` y se incluye un contrato de ejemplo en `contracts/UserMVP.yaml`.

Pasos propuestos:
- Revisa `MVP.md` para criterios de aceptación y sprints.
- Ejecuta `python -m pytest` para verificar que los generadores y validaciones pasan.
- Indica si quieres que implemente ahora el `ContractValidator` (recomendado).

Dime cómo quieres que proceda y lo automatizo.

